import os
import sys
from dotenv import load_dotenv
from logger.logging import logging
from exception.exception import customexception
from hopsworks_connect import FeatureStoreManager
load_dotenv()

def retrive_data_from_hopsworks(feature_group_name):
    try:
        hopsworks_api_key_value: str = os.environ.get("HOPSWORKS_API_KEY_VALUE")
        manager = FeatureStoreManager(hopsworks_api_key_value)
        users_fg = manager.get_feature_group(feature_group_name, version=1)
        query = users_fg.select_all()
        df = query.read()
        logging.info("Data Retrieved as dataframe from hopsworks")
        return df
    except Exception as e:
        logging.info("Exception happend at retrieve_data")
        raise customexception(e,sys)