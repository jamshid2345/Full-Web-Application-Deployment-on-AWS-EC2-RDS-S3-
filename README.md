# Full-Web-Application-Deployment-on-AWS-EC2-RDS-S3-
# Jamshiddin's Social Media Tracker Web App

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
