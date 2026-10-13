from networksecurity.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException 
from networksecurity.logging.logger import logging 
from networksecurity.constants.training_pipeline import SCHEMA_FILE_PATH
from scipy.stats import ks_2samp
import pandas as pd
import os,sys
from networksecurity.utils.main_utils.utils import read_yaml_file, write_yaml_file

class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,
                 data_validation_config:DataValidationConfig):
        
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def validate_number_of_columns(self,dataframe:pd.DataFrame)->bool:
        try:
            number_of_columns=len(self._schema_config["columns"])
            logging.info(f"Required number of columns:{number_of_columns}")
            logging.info(f"Data frame has columns:{len(dataframe.columns)}")
            return len(dataframe.columns)==number_of_columns
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def detect_dataset_drift(self,base_df,current_df,threshold=0.05)->bool:
        """Returns True when no column has drifted."""
        try:
            status=True
            report={}
            for column in base_df.columns:
                d1=base_df[column]
                d2=current_df[column]
                is_same_dist=ks_2samp(d1,d2)
                if threshold<=is_same_dist.pvalue: # type: ignore
                    is_found=False
                else:
                    is_found=True
                    status=False
                report.update({column:{
                    "p_value":float(is_same_dist.pvalue), # type: ignore
                    "drift_status":is_found
                    
                    }})
            drift_report_file_path = self.data_validation_config.drift_report_file_path

            #Create directory
            dir_path = os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path,exist_ok=True)
            write_yaml_file(file_path=drift_report_file_path,content=report)
            return status

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    
    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            train_file_path=self.data_ingestion_artifact.trained_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

            ## read the data from train and test
            train_dataframe=DataValidation.read_data(train_file_path)
            test_dataframe=DataValidation.read_data(test_file_path)
            
            ## validate number of columns
            status=True
            if not self.validate_number_of_columns(dataframe=train_dataframe):
                logging.error("Train dataframe does not contain all columns.")
                status=False
            if not self.validate_number_of_columns(dataframe=test_dataframe):
                logging.error("Test dataframe does not contain all columns.")
                status=False

            ## lets check datadrift (only meaningful when the columns match)
            if status:
                status=self.detect_dataset_drift(base_df=train_dataframe,current_df=test_dataframe)

            config=self.data_validation_config
            train_out=config.valid_train_file_path if status else config.invalid_train_file_path
            test_out=config.valid_test_file_path if status else config.invalid_test_file_path
            os.makedirs(os.path.dirname(train_out),exist_ok=True)

            train_dataframe.to_csv(train_out, index=False, header=True)
            test_dataframe.to_csv(test_out, index=False, header=True)
            
            data_validation_artifact = DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=train_out if status else None, # type: ignore
                valid_test_file_path=test_out if status else None, # type: ignore
                invalid_train_file_path=None if status else train_out, # type: ignore
                invalid_test_file_path=None if status else test_out, # type: ignore
                drift_report_file_path=config.drift_report_file_path,
            )
            return data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
