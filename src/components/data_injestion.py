#Target guided label encoding we are dependenet of dependent features
import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation

#Initialize the Data Ingestion Configuration

@dataclass
class DataInjestionconfig:
    #here we don't need to create __init__ function ,because we don't have need  to make any function inside the class
    train_data_path:str = os.path.join('artifacts','train2.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','raw.csv')

# Create a class for Data Ingestion
class DataInjestion:
    def __init__(self):
        self.Ingestion_config = DataInjestionconfig()
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion methods starts')
        try:
            df = pd.read_csv(os.path.join('notebooks','train.csv'))
            logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.Ingestion_config.raw_data_path),exist_ok = True)
            df.to_csv(self.Ingestion_config.raw_data_path,index=False)
            logging.info('TRain test Split')
            train_set , test_set = train_test_split(df,test_size=0.30,random_state = 42)
            

            train_set.to_csv(self.Ingestion_config.train_data_path,index=False, header = True)
            test_set.to_csv(self.Ingestion_config.test_data_path,index = False,header = True)

            logging.info('Ingestion of Data is Completed')

            return(
                self.Ingestion_config.train_data_path,
                self.Ingestion_config.test_data_path
            )
        except Exception as e:
            logging.info('Exception Occured at Data Ingestion stage')
            raise CustomException(e,sys)

# run data injestion
''''
if __name__ == '__main__':
    obj = DataInjestion()
    train_data , test_data = obj.initiate_data_ingestion()
'''
'''
# run Data injestion

if __name__=='__main__':
    obj= DataInjestion()
    train_data_path,test_data_path = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr, processor_file_path = data_transformation.initiate_data_transformation(train_data_path,test_data_path)
'''