import os
import sys
from src.exception import customexception
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', "train_csv")
    test_data_path: str=os.path.join('artifacts', "test_csv")
    raw_data_path: str=os.path.join('artifacts', "raw_csv")
    
class DataIngestion:
    def __init__(self):
            self.ingestion_config=DataIngestionConfig()
            
            
    def initiate_data_ingestion(self):
        logging.info("Enterees the data ingestion method or component")
        try:
            df=pd.read_csv(r"C:\Users\HARMEET SINGH\Downloads\mlproject-main\mlproject-main\notebook\data\stud.csv")
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise customexception(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

