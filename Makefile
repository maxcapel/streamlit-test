init:
	poetry config virtualenvs.in-project true
	poetry install

local:
	streamlit run emd_streamlit/app.py

reqm:
	poetry export -f requirements.txt --output ./emd_streamlit/requirements.txt.

configure:
	rsconnect add --server $SERVER_URL --name rcondev --api-key $RSC_STREAMLIT_API_KEY

deploy:
	rsconnect deploy streamlit -n rcondev -p .venv/Scripts/python.exe -v emd_streamlit