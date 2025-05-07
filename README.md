# Full-Web-Application-Deployment-on-AWS-EC2-RDS-S3-
# Jamshiddin's Social Media Tracker Web App

S3 site is: https://jamshiddin-webapp.s3.ap-northeast-2.amazonaws.com/index_jamshiddin.html

EC2 Flask app is hosted at: http://3.38.212.216:5000/socialmedia

RDS PostgreSQL database name is: db_jamshiddin

The table is: tbl_jamshiddin_socialmedia

This project demonstrates a full web application deployment on AWS using the following services:
- **Amazon EC2** for backend Flask API
- **Amazon RDS (PostgreSQL)** for data storage
- **Amazon S3** for static HTML frontend hosting

---

## 🚀 Project Overview

The application tracks global social media usage and presents the data through a web-based dashboard.

### Features:
- Displays real social media data from a Kaggle dataset (imported into RDS).
- HTML/CSS frontend hosted on S3.
- Flask backend deployed on EC2 and connected to RDS.
- All components are live and integrated end-to-end.

---

## 🧩 Technologies Used

| Layer          | Technology |
|----------------|------------|
| Frontend       | HTML + JavaScript |
| Backend        | Python + Flask |
| Database       | PostgreSQL (via Amazon RDS) |
| Hosting (UI)   | Amazon S3 (Static Website) |
| Hosting (API)  | Amazon EC2 (Ubuntu) |

---

## 🌐 Live Deployed Resources

- **Frontend (S3):**  
  [https://jamshiddin-webapp.s3.ap-northeast-2.amazonaws.com/index_jamshiddin.html](https://jamshiddin-webapp.s3.ap-northeast-2.amazonaws.com/index_jamshiddin.html)

- **Backend API (Flask on EC2):**  
  [http://3.38.212.216:5000/socialmedia](http://3.38.212.216:5000/socialmedia)

- **Database (Amazon RDS):**  
  PostgreSQL instance hosted in `ap-northeast-2` region  
  - DB Name: `postgres`  
  - Table Name: `tbl_jamshiddin_socialmedia`

---

## 🛠️ How to Run the Application (Locally or on EC2)

### 1. Launch EC2 and install dependencies:

sudo apt update
sudo apt install python3-pip
pip install flask flask-cors psycopg2-binary

### 2. Clone this repository:

git clone <your-github-repo-url>
cd <your-project-folder>

### 3. Run app.py:

python app.py 
OR
python3 app.py

## Project Structure
webapp_jamshiddin/
│
├── app.py                    # Flask backend
├── index_jamshiddin.html     # S3-hosted frontend
├── socialmedia.csv           # Original Kaggle dataset (optional)
├── README.md                 # This file

## Example of Response
GET http://3.38.212.216:5000/socialmedia

json 
[
  {
    "platform": "Instagram",
    "owner": "Meta",
    "country": "Timor-Leste",
    "Primary Usage": "Photo and video sharing",
    "Daily Time Spent (min)": 295.43,
    "Verified Account": "Yes",
    "Date Joined": "2019-04-21"
  },
  ...
]

## ✅ Status
-S3 frontend is live
-EC2 backend is responding to /socialmedia
-RDS is connected and serving data
-All components are integrated and working


## 📘 Full Setup Instructions
🔧 Part 1: Set Up Amazon RDS (PostgreSQL)
Go to AWS RDS Console

Click "Create database"

Engine: PostgreSQL

DB instance identifier: postgres

Master username: postgres

Master password: postgres

Under Connectivity:

Make the DB publicly accessible

Allow inbound traffic on port 5432

Launch the instance.

After creation, copy the Endpoint (e.g., db-jamshiddin.xxxx.rds.amazonaws.com)

Use DBeaver or psql to connect and run:
CREATE TABLE tbl_jamshiddin_socialmedia (
    platform VARCHAR(100),
    owner VARCHAR(100),
    country VARCHAR(100),
    "Primary Usage" VARCHAR(100),
    "Daily Time Spent (min)" FLOAT,
    "Verified Account" VARCHAR(10),
    "Date Joined" DATE
);

Import the dataset (socialmedia.csv) into this table using DBeaver or SQL import.

## 🧰 Part 2: Launch EC2 and Deploy Flask Backend
Go to AWS EC2 Console

Launch a new Ubuntu 20.04 instance.

Allow HTTP, HTTPS, and port 5000 in the security group.

SSH into your EC2:

bash
ssh -i your-key.pem ubuntu@<your-ec2-public-ip>


