import os
from dotenv import load_dotenv
from hopsworks_connect import FeatureStoreManager
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from joblib import dump

load_dotenv()

hopsworks_api_key_value: str = os.environ.get("HOPSWORKS_API_KEY_VALUE")

manager = FeatureStoreManager(hopsworks_api_key_value)

users_fg = manager.get_feature_group("diabetecs_data", version=1)

query = users_fg.select_all()

df = query.read()
