<h2 align="center"> Vehichle Insurance</h2>
<h1 align="center">
  🚧 This project is under 
  <img src="https://img.shields.io/badge/CONSTRUCTION-red?style=for-the-badge" alt="CONSTRUCTION" height="34" align="absmiddle" /> 
  🏗️
</h1>

## Insights: 
- Heavy MLOps, not Data Science
- Strong Exposure to SDE
- An End to End project
- Expert difficulties expected
- Follow industry grade project template

## Tools:
- **MongoDB:** For data management
- **Robust Pipeline:** Robust pipeline for
    - Training
    - Predicting
- **FastAPI:** Server is based on FstAPI
- **CI/CD:** Performed via *Github Actions*
- **AWS:** *IAM*, *ECR*, *EC2*
- No conventional MLOps tools used

# 🚗 Vehicle Project Flow Tracker

**How to use:** For each step, mark your choice by changing `⬜` to `☑️` in exactly one of the three columns (✅ Done, ⏳ Pending, ⏭️ Skip). By default, everything starts as **Pending**.

| Symbol | Meaning |
|:------:|---------|
| ✅ | Done |
| ⏳ | Pending |
| ⏭️ | Skip |

---

## 1. Project Setup

| # | Task | ✅ Done | ⏳ Pending | ⏭️ Skip |
|:-:|------|:------:|:---------:|:------:|
| 1 | Create project template by executing `template.py` | ☑️ | ⬜ | ⬜ |
| 2 | Write code in `setup.py` and `pyproject.toml` to import local packages<br>↳ See `crashcourse.txt` for more details | ☑️ | ⬜ | ⬜ |
| 3 | Create a virtual env, activate it and install requirements<br>↳ `conda create -n vehicle python=3.10 -y`<br>↳ `conda activate vehicle`<br>↳ Add required modules to `requirements.txt`<br>↳ `pip install -r requirements.txt` | ☑️ | ⬜ | ⬜ |
| 4 | Run `pip list` in terminal to confirm local packages are installed | ☑️ | ⬜ | ⬜ |

---

## 2. MongoDB Setup

| # | Task | ✅ Done | ⏳ Pending | ⏭️ Skip |
|:-:|------|:------:|:---------:|:------:|
| 5 | Sign up to MongoDB Atlas and create a new project (give it a name, then next, next, create) | ☑️ | ⬜ | ⬜ |
| 6 | On "Create a cluster" screen, hit **Create**, select **M0** (keep other defaults), hit **Create deployment** | ☑️ | ⬜ | ⬜ |
| 7 | Set up username and password, then create the DB user | ☑️ | ⬜ | ⬜ |
| 8 | Go to **Network Access** and add IP address `0.0.0.0/0` (access from anywhere) | ☑️ | ⬜ | ⬜ |
| 9 | Project → **Get Connection String** → **Drivers** → Driver: Python, Version: 3.6 or later<br>↳ Copy and save the connection string (replace the password) | ☑️ | ⬜ | ⬜ |
| 10 | Create folder `notebook` → complete step 11 → create `mongoDB_demo.ipynb` → select kernel → Python → `vehicle` | ☑️ | ⬜ | ⬜ |
| 11 | Add the dataset to the `notebook` folder | ☑️ | ⬜ | ⬜ |
| 12 | Push your data to the MongoDB database from the Python notebook | ☑️ | ⬜ | ⬜ |
| 13 | MongoDB Atlas → Database → Browse Collection → verify data in key-value format | ☑️ | ⬜ | ⬜ |

---

## 3. Logging, Exception and Notebooks

| # | Task | ✅ Done | ⏳ Pending | ⏭️ Skip |
|:-:|------|:------:|:---------:|:------:|
| 14 | Write the logger file and test it in `demo.py` | ☑️ | ⬜ | ⬜ |
| 15 | Write the exception file and test it in `demo.py` | ☑️ | ⬜ | ⬜ |
| 16 | Add EDA and Feature Engineering notebook | ☑️ | ⬜ | ⬜ |

---

## 4. Data Ingestion

| # | Task | ✅ Done | ⏳ Pending | ⏭️ Skip |
|:-:|------|:------:|:---------:|:------:|
| 17 | Build the Data Ingestion component:<br>↳ Declare variables in `constants/__init__.py`<br>↳ Add code to `configuration/mongo_db_connections.py` (MongoDB connection function)<br>↳ In `data_access` folder, add code to `proj1_data` (use `mongo_db_connections.py` to connect to DB, fetch key-value data, convert to DataFrame)<br>↳ Add code to `entity/config_entity.py` up to `DataIngestionConfig`<br>↳ Add code to `entity/artifact_entity.py` up to `DataIngestionArtifact`<br>↳ Add code to `components/data_ingestion.py`<br>↳ Add code to training pipeline<br>↳ Run `demo.py` (set MongoDB URL first, see step 18) |☑️ |    ⬜gi    | ⬜ |
| 18 | Set up the MongoDB connection URL as an environment variable<br>**Bash:** `export MONGODB_URL="mongodb+srv://<username>:<password>......"` → check: `echo $MONGODB_URL`<br>**PowerShell:** `$env:MONGODB_URL = "mongodb+srv://<username>:<password>......"` → check: `echo $env:MONGODB_URL`<br>**Windows:** open Environment Variables settings → add Name: `MONGODB_URL`, Value: `<url>`<br>↳ Also add the `artifact` dir to `.gitignore` | ☑️ |     ⬜     | ⬜ |

---

## 5. Data Validation, Data Transformation & Model Trainer

| # | Task | ✅ Done | ⏳ Pending | ⏭️ Skip |
|:-:|------|:------:|:---------:|:------:|
| 19 | Complete `utils/main_utils.py` and `config/schema.yaml` (add entire dataset info for validation) | ⬜ | ☑️ | ⬜ |
| 20 | Work on the **Data Validation** component (same approach as step 17) | ⬜ | ☑️ | ⬜ |
| 21 | Work on the **Data Transformation** component (same approach; add `estimator.py` to the `entity` folder) | ⬜ | ☑️ | ⬜ |
| 22 | Work on the **Model Trainer** component (same approach; add class to `estimator.py` in `entity` folder) | ⬜ | ☑️ | ⬜ |

---

## 6. AWS Setup (before Model Evaluation)

| # | Task | ✅ Done | ⏳ Pending | ⏭️ Skip |
|:-:|------|:------:|:---------:|:------:|
| 23.1 | Log in to AWS console, keep region as `us-east-1` | ⬜ | ☑️ | ⬜ |
| 23.2 | IAM → Create new user (name: `firstproj`) | ⬜ | ☑️ | ⬜ |
| 23.3 | Attach policy → `AdministratorAccess` → next → create user | ⬜ | ☑️ | ⬜ |
| 23.4 | User → Security Credentials → Access Keys → Create access key → select **CLI** → agree → next → create → download CSV | ⬜ | ☑️ | ⬜ |
| 23.5 | Set AWS env variables from the CSV values<br>**Bash:** `export AWS_ACCESS_KEY_ID="..."` and `export AWS_SECRET_ACCESS_KEY="..."` → check with `echo $AWS_ACCESS_KEY_ID`<br>**PowerShell:** `$env:AWS_ACCESS_KEY_ID="..."` and `$env:AWS_SECRET_ACCESS_KEY="..."` → check with `echo $env:AWS_ACCESS_KEY_ID` | ⬜ | ☑️ | ⬜ |
| 23.6 | Add access key, secret key and region name to `constants/__init__.py` | ⬜ | ☑️ | ⬜ |
| 23.7 | Add code to `src/configuration/aws_connection.py` (to work with S3) | ⬜ | ☑️ | ⬜ |
| 23.8 | Ensure these are in `constants/__init__.py`:<br>↳ `MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02`<br>↳ `MODEL_BUCKET_NAME = "my-model-mlopsproj"`<br>↳ `MODEL_PUSHER_S3_KEY = "model-registry"` | ⬜ | ☑️ | ⬜ |
| 23.9 | S3 → Create bucket → Region: `us-east-1` → General purpose → Name: `my-model-mlopsproj` → uncheck "Block all public access" and acknowledge → Create bucket | ⬜ | ☑️ | ⬜ |
| 23.10 | In `src/aws_storage`, add code for configs to pull/push model from the S3 bucket | ⬜ | ☑️ | ⬜ |
| 23.11 | In `entity` dir, add `s3_estimator.py` with functions to pull/push data from S3 | ⬜ | ☑️ | ⬜ |

---

## 7. Evaluation, Pusher & Prediction

| # | Task | ✅ Done | ⏳ Pending | ⏭️ Skip |
|:-:|------|:------:|:---------:|:------:|
| 24 | Work on **Model Evaluation** and **Model Pusher** components | ⬜ | ☑️ | ⬜ |
| 25 | Create the code structure of **Prediction Pipeline** and set up `app.py` | ⬜ | ☑️ | ⬜ |
| 26 | Add `static` and `template` dirs to the project | ⬜ | ☑️ | ⬜ |

---

## 8. CI/CD Setup

| # | Task | ✅ Done | ⏳ Pending | ⏭️ Skip |
|:-:|------|:------:|:---------:|:------:|
| 27.1 | Set up `Dockerfile` and `.dockerignore` | ⬜ | ☑️ | ⬜ |
| 27.2 | Set up `.github/workflows` dir with `aws.yaml` inside | ⬜ | ☑️ | ⬜ |
| 27.3 | Create a new IAM user the same way as before (name: `usvisa-user`) → Security Credentials → Access Keys → CLI → agree → create → download CSV | ⬜ | ☑️ | ⬜ |
| 27.4 | Create an ECR repo: AWS console → ECR → Region: `us-east-1` → Create repository → name: `vehicleproj` → create → **copy and keep the URI** | ⬜ | ☑️ | ⬜ |
| 27.5 | Create EC2 Ubuntu server: EC2 → Launch Instance<br>↳ Name: `vehicledata-machine`<br>↳ Image: Ubuntu, AMI: Ubuntu Server 24.04 (free tier)<br>↳ Instance: T2 Medium (chargeable, ~3.5 Rs/hr)<br>↳ Create new key pair (name: `proj1key`)<br>↳ Allow HTTPS and HTTP traffic<br>↳ Storage: 30 GB → Launch<br>↳ Instance → Connect → EC2 Instance Connect → Connect (terminal launches) | ⬜ | ☑️ | ⬜ |

---

## 9. EC2 and GitHub Runner

| # | Task | ✅ Done | ⏳ Pending | ⏭️ Skip |
|:-:|------|:------:|:---------:|:------:|
| 28 | Install Docker on the EC2 machine<br>↳ *Optional:* `sudo apt-get update -y` and `sudo apt-get upgrade`<br>↳ *Required* (Docker isn't preinstalled, check with `docker --version`):<br>`curl -fsSL https://get.docker.com -o get-docker.sh`<br>`sudo sh get-docker.sh`<br>`sudo usermod -aG docker ubuntu`<br>`newgrp docker` | ⬜ | ☑️ | ⬜ |
| 29 | Connect GitHub with EC2 (self-hosted runner)<br>↳ GitHub project → Settings → Actions → Runner → New self-hosted runner → OS: Linux<br>↳ Run all **Download** commands step by step on the EC2 server<br>↳ Run the first **Configure** command (hit enter for runner group; runner name: `self-hosted`)<br>↳ Additional label: hit enter to skip; work folder: hit enter<br>↳ Run the second **Configure** command (`./run.sh`) → runner connects to GitHub<br>↳ Verify on GitHub → Runner shows state **idle**<br>↳ If you press Ctrl+C on EC2 the runner shuts down; restart with `./run.sh` | ⬜ | ☑️ | ⬜ |
| 30 | Set GitHub secrets (Project → Settings → Secrets and variables → Actions → New repository secret):<br>↳ `AWS_ACCESS_KEY_ID`<br>↳ `AWS_SECRET_ACCESS_KEY`<br>↳ `AWS_DEFAULT_REGION`<br>↳ `ECR_REPO` | ⬜ | ☑️ | ⬜ |
| 31 | CI/CD pipeline triggers on the next commit and push | ⬜ | ☑️ | ⬜ |

---

## 10. Deployment

| # | Task | ✅ Done | ⏳ Pending | ⏭️ Skip |
|:-:|------|:------:|:---------:|:------:|
| 32 | Open the app port on EC2: Instance → Security → Security Groups → Edit inbound rules → Add rule<br>↳ Type: Custom TCP, Port range: `5080`, Source: `0.0.0.0/0` → Save rules | ⬜ | ☑️ | ⬜ |
| 33 | Paste the EC2 public IP in the browser address bar followed by `:5080` to launch the app | ⬜ | ☑️ | ⬜ |
| 34 | Run model training from the `/training` route | ⬜ | ☑️ | ⬜ |

---

> 💡 **Tip:** Your original notes say port `5000` in step 32 but use `5080` in the rule and URL. Make sure it matches the port your `app.py` and `Dockerfile` actually use.
