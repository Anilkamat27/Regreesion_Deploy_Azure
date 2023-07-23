import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd


from src.components.data_injestion import DataInjestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


## run Data Ingestion 
if __name__=='__main__':
    obj= DataInjestion()
    train_data_path,test_data_path = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr, processor_file_path = data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(train_arr, test_arr)