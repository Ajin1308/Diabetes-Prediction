import sys
from dotenv import load_dotenv
from retrive_data import retrive_data_from_hopsworks
from sklearn.pipeline import Pipeline
from joblib import dump
from sklearn.model_selection import train_test_split
from processing.data_manager import save_pipeline
from src.logger.logging import logging
from src.exception.exception import customexception
from src.components.pipeline import diab_pipe
from hopsworks_connect import FeatureStoreManager


def run_training_pipeline():

    try:
        df = retrive_data_from_hopsworks("diabetics_data")
        logging.info("retrieved data from hopsworks")
        X = df.drop(columns=['diagnosis'])
        y = df['diagnosis']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        logging.info("Splitted the data!")
    except Exception as e:
        logging.info("Exception occured while splitting at training_pipeline")
        raise customexception(e,sys)

    diab_pipe.fit(X_train,y_train)
    logging.info("Pipline Trained")
    save_pipeline(pipeline_to_persist = diab_pipe)

if __name__ == "__main__":
    run_training_pipeline()