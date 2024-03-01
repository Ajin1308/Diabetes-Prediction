import os
from hopsworks_connect import FeatureStoreManager
from dotenv import load_dotenv
import pandas as pd


load_dotenv()

hopsworks_api_key_value: str = os.environ.get("HOPSWORKS_API_KEY_VALUE")

manager = FeatureStoreManager(hopsworks_api_key_value)

data = pd.read_csv(r"C:\Users\user\Diabetes-Prediction\expirements\Diabetes_prediction.csv")

users_fg = manager.get_or_create_feature_group(
    feature_group_name="diabetecs_data",
    version=1,
    description="diabetic dataset",
    primary_key=["Age"]
)

write_options = {"wait_for_job": True}

manager.insert_data_into_feature_group(feature_group=users_fg, data_frame=data, write_options=write_options)

# users_fg.insert(
#     users,
#     write_options={"wait_for_job": True},
# )

feature_descriptions = [
    {"name": "Pregnancies", "description": "how many pregnancies"},
    {"name": "Age", "description": "age"},
    {"name": "Glucose", "description": "glucose"},
    {"name": "BloodPressure", "description": "blood pressure"},
    {"name": "SkinThickness", "description": "skin thickness"},
    {"name": "Insulin", "description": "insulin"},
    {"name": "BMI", "description": "bmi value"},
    {"name": "DiabetesPedigreeFunction", "description": "diabetes pedigree function"},
    {"name": "Diagnosis", "description": "diabetic or not"},
]

for desc in feature_descriptions:
    users_fg.update_feature_description(desc["name"], desc["description"])