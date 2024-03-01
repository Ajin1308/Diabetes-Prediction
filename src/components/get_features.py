import pandas as pd
import hsfs
import hopsworks
from hopsworks_connect import FeatureStoreManager
from dotenv import load_dotenv
import os

hopsworks_api_key_value: str = os.environ.get("HOPSWORKS_API_KEY_VALUE")

# connection = hsfs.connection()
# fs = connection.get_feature_store(name='ajinravi_featurestore')
# fg = fs.get_feature_group('diabetecs_data', version=1)
# fg.info()
# print("done")

manager = FeatureStoreManager(hopsworks_api_key_value)
df = manager.get_feature_view('diabetecs_data', version=1)
# query = "SELECT * FROM diabetecs_data"
# result = df.query(query)
# df = pd.DataFrame(df)
# print(df.info())
# print("done")
print(df.info())