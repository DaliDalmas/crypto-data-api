# crypto-data-api
This product scrapes the web for the value of crypto currencies then serves the data through an api. This is a project which I did for the purpose of showing my youtube community <a href='https://www.youtube.com/channel/UCzSlSeJ4XH4bWH79DKmIxjg'>here on dalicodes<a> how to use beautifulsoup, airflow and fastapi in building a data engineering system that fetches data from the web then serves the cleaner version of the data through an api. Here is the video tutorial on how I build this project <a href='https://www.youtube.com/channel/UCzSlSeJ4XH4bWH79DKmIxjg'>here on dalicodes<a>

# Installation
1. Clone or fork the repo and cd into the main repo.
2. Switch the local version of python to 3.10.0 using `pyenv local 3.10.0`.
3. Create the virtual environment using `python -m venv venv`.
4. Activate the virtual environment using `source venv/bin/activate` for the case of mac.
5. Install all the requirements of the project using `pip install -r requirements.txt`.


# Execution
## Starting airflow
1. Open a terminal and cd to the root folder of the project.
2. Activate the virtual environment using `source venv/bin/activate`
3. run `export AIRFLOW_HOME=\`pwd\``
4. run `airflow webserver`
5. Open a new terminal in the root directory of the project and activate the virtual environment using step 2
6. run `export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES`
7. run `export AIRFLOW_HOME=`\`pwd`
8. run `airflow scheduler`
9. you can access airflow on your web browser on ``

## Starting fastapi
1. Open a new terminal
2. cd into the root directory of the project and activate the virtual environment using `source venv/bin/activate`
3. cd into the api folder and run `uvicorn main:app --reload`
2. you can access the api on your web browser on ``
