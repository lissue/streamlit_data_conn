# Streamlit Data Connection for DataRobot

[DataRobot](www.datarobot.com) is an enterprise AI/ML platform. From data to model in production,
the end-to-end platform accelerates the time to value with AI while maintaining high quality and
standardization.

This repo demonstrates a Streamlit data connection that uses the
[DataRobot API](https://docs.datarobot.com/en/api) to retrieve various assets such as
[datasets](https://datarobot-public-api-client.readthedocs-hosted.com/en/latest-release/autodoc/api_reference.html#datasets),
[projects](https://datarobot-public-api-client.readthedocs-hosted.com/en/latest-release/autodoc/api_reference.html#project), and
[deployments](https://datarobot-public-api-client.readthedocs-hosted.com/en/latest-release/autodoc/api_reference.html#deployment).
The Streamlit app then uses `data_editor` to allow the users customize the way of organizing
the assets, with filters and locally stored labels. All without requiring the users' familiarity
with the DataRobot API.
