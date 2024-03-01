import hopsworks
import pandas as pd

class FeatureStoreManager:
    def __init__(self, api_key_value):
        self.project = hopsworks.login(api_key_value=api_key_value)
        self.fs = self.project.get_feature_store()
        self.mr = self.project.get_model_registry()

    def get_feature_group(self, feature_group_name, version=1):
        return self.fs.get_feature_group(feature_group_name, version=version)

    def get_or_create_feature_group(self, feature_group_name, version=1, description=None, primary_key=None):
        return self.fs.get_or_create_feature_group(name=feature_group_name, version=version, description=description, primary_key=primary_key)

    def insert_data_into_feature_group(self, feature_group, data_frame, write_options=None):
        feature_group.insert(data_frame, write_options=write_options)
        print('Insert Done')
        
    def get_feature_view(self, feature_view_name, version=1):
        return self.fs.get_feature_view(feature_view_name, version=version)

    
    # def get_feature_group_data(self, feature_group_name, version=1):
    #     # Get the feature group object
    #     feature_group = self.get_feature_group(feature_group_name, version=version)
        
    #     # Retrieve the data from the feature group and return as a Pandas DataFrame
    #     query_result = feature_group.select()
        
    #     # Convert the query result to a Pandas DataFrame
    #     # Assuming query_result is an iterable containing the data
    #     data = [row.values() for row in query_result]
    #     df = pd.DataFrame(data, columns=query_result.column_names())
        
    #     return df
