import pandas as pd
import streamlit as st
import datarobot as dr
from streamlit.runtime.caching import cache_data
from streamlit.connections import ExperimentalBaseConnection

class DataRobotConnection(ExperimentalBaseConnection[dr.Client]):
    def _connect(self, **kwargs) -> dr.Client:
        if 'DATAROBOT_API_KEY' in kwargs:
            DATAROBOT_API_KEY = kwargs.pop('DATAROBOT_API_KEY')
            DATAROBOT_ENDPOINT = kwargs.pop('DATAROBOT_ENDPOINT')
        else:
            DATAROBOT_API_KEY = self._secrets['DATAROBOT_API_KEY']
            DATAROBOT_ENDPOINT = self._secrets['DATAROBOT_ENDPOINT']
        return dr.Client(token=DATAROBOT_API_KEY, endpoint=DATAROBOT_ENDPOINT)

    def query(self, query:str, ttl:int=3600, **kwargs) -> pd.DataFrame:
        @cache_data(ttl=ttl)
        def _query(query:str, **kwargs) -> pd.DataFrame:
            if query == 'datasets':
                datasets = dr.Dataset.list()
                dataset_name = [d.name for d in datasets]
                dataset_id = [d.id for d in datasets]
                dataset_categories = [d.categories for d in datasets]
                dataset_created_at = [d.created_at for d in datasets]
                res = pd.DataFrame(
                    {
                        'Name': dataset_name,
                        'Category': dataset_categories,
                        'Creation Date': dataset_created_at,
                        'ID': dataset_id,
                    }
                )
            elif query == 'projects':
                projects = dr.Project.list()
                project_name = [p.project_name for p in projects]
                project_id = [p.id for p in projects]
                res = pd.DataFrame(
                    {
                        'Name': project_name,
                        'ID': project_id,
                    }
                )
            elif query == 'deployments':
                deployments = dr.Deployment.list()
                deployment_name = [d.label for d in deployments]
                deployment_id = [d.id for d in deployments]
                res = pd.DataFrame(
                    {
                        'Name': deployment_name,
                        'ID': deployment_id,
                    }
                )
            return res
        return _query(query, **kwargs)
