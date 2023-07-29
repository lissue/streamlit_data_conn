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
                res = datasets
            elif query == 'projects':
                projects = dr.Project.list()
                res = projects
            elif query == 'deployments':
                deployments = dr.Deployment.list()
                res = deployments
            df = pd.DataFrame({query: res})
            return df
        return _query(query, **kwargs)
