from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from processing.data_manager import save_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer


diab_pipe = Pipeline([
    ("mean_imputation", SimpleImputer(strategy='mean', missing_values=pd.NA, 
                                      add_indicator=False, fill_value=None, copy=True)),
    
    ('scalar', MinMaxScaler()),

    ('Logistic_Regression',LogisticRegression(random_state=42))
])




