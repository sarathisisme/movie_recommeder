# Streamlit

**Streamlit** is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps. It is a Python-based library specifically designed for machine learning engineers.

This repository shows, with the example of a **movie-recommender app**, how the frontend of an app could be developed with Streamlit, and how it could then be deployed on Streamlit Community Cloud.


## Environment

Use the requirements file to create a new environment for this task. 

```Bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### **`WindowsOS`** requires the following commands:

For `PowerShell` CLI :
```PowerShell
pyenv local 3.11.3
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

For `Git-Bash` CLI :
```
pyenv local 3.11.3
python -m venv .venv
source .venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Running Locally

In your terminal, go to the project folder and run the command: 
```
streamlit run app.py
```

## Deployment

- In the [Streamlit Community Cloud](https://share.streamlit.io/), sign in with your github account
- Click on `Create app`, and then on `Deploy a public app from GitHub`
- Give the correct repo, branch and main-file names, along with a suitable url, for your app
- In `Advanced settings`, choose `3.11` as *Python version*, and `save`
- Click on `Deploy`