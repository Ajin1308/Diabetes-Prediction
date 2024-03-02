import os
import sys
from dotenv import load_dotenv
from retrive_data import retrive_data_from_hopsworks
from sklearn.pipeline import Pipeline
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from src.logger.logging import logging
from src.exception.exception import customexception
from hopsworks_connect import FeatureStoreManager

df = retrive_data_from_hopsworks("diabetics_data")

try:
    X = df.drop(columns=['diagnosis'])
    y = df['diagnosis']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    logging.info("Splitted the data!")
except Exception as e:
    logging.info("Exception occured while splitting at training_pipeline")
    raise customexception(e,sys)

diab_pipe = Pipeline([
    ("mean_imputation", SimpleImputer(strategy='mean', missing_values=pd.NA, 
                                      add_indicator=False, fill_value=None, copy=True)),
    
    ('scalar', MinMaxScaler()),

    ('Logistic_Regression',LogisticRegression(random_state=42))
])
