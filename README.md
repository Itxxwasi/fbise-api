# 📘 Gazette API – SSC-II Result Lookup

A simple **Flask-based API** to fetch student results from the **FBISE Gazette** by Roll Number.  
Perfect for **bots, integrations, and third-party apps**.

---

## ✅ Features
- Search **student result by Roll Number**
- Returns **JSON response** (easy for API use)
- Lightweight & fast
- **Ready for Heroku deployment**

---



---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/Itxxwasi/fbise-api
cd fbise-api

pip install -r requirements.txt

RollNo,Name,Status,Marks,Grade,SchoolName,SchoolCode


{
  "status": "success",
  "data": {
    "RollNo": "1234567",
    "Name": "Ali Khan",
    "Status": "PASS",
    "Marks": 678,
    "Grade": "A",
    "SchoolName": "F.G. School Wah Cantt"
  }
}
