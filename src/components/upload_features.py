import os
import sys
from hopsworks_connect import FeatureStoreManager
from dotenv import load_dotenv
import pandas as pd
from src.logger.logging import logging
from src.exception.exception import customexception

def upload_features_to_hopsworks(data,feature_descriptions):

    try:
        load_dotenv()
        hopsworks_api_key_value: str = os.environ.get("HOPSWORKS_API_KEY_VALUE")
        manager = FeatureStoreManager(hopsworks_api_key_value)

        users_fg = manager.get_or_create_feature_group(
            feature_group_name="diabetics_data",
            version=1,
            description="diabetic historic dataset",
            primary_key=["Age"]
        )

        write_options = {"wait_for_job": True}

        manager.insert_data_into_feature_group(feature_group=users_fg, data_frame=data, write_options=write_options)

        # users_fg.insert(
        #     users,
        #     write_options={"wait_for_job": True},
        # )

        for desc in feature_descriptions:
            users_fg.update_feature_description(desc["name"], desc["description"])
        logging.info("features uploaded!")
    except Exception as e:
        logging.info('Exception occured at upload_features')
        raise customexception(e,sys)

if __name__ == "__main__":
    data = pd.read_csv(r"C:\Users\user\Diabetes-Prediction\expirements\Diabetes_prediction.csv")
    feature_descriptions = [
            {"name": "pregnancies", "description": "how many pregnancies"},
            {"name": "age", "description": "age"},
            {"name": "glucose", "description": "glucose"},
            {"name": "bloodpressure", "description": "blood pressure"},
            {"name": "skinthickness", "description": "skin thickness"},
            {"name": "insulin", "description": "insulin"},
            {"name": "bmi", "description": "bmi value"},
            {"name": "diabetespedigreefunction", "description": "diabetes pedigree function"},
            {"name": "diagnosis", "description": "diabetic or not"},
        ]

    up = upload_features_to_hopsworks(data,feature_descriptions)
