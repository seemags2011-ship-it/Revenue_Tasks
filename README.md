# 💼 Revenue Automation Demo

This project demonstrates **GUI** and **API automation** for sample tasks based on *Revenue NSW* use cases using **Python (Behave BDD)**.  
It showcases automation design, test execution, HTML reporting, and CI/CD integration following real-world QA best practices.

---

## 🧰 Tools & Frameworks

| Purpose | Tool/Library |
|----------|---------------|
| **BDD Framework** | Behave |
| **GUI Automation** | Playwright |
| **API Testing** | Requests |
| **HTML Reporting** | Behave HTML Formatter |
| **Environment Management** | Python Virtual Environment |
| **CI/CD** | GitHub Actions |

---

## ▶️ How to Run the Tests

### **1️⃣ Activate the Virtual Environment**
```bash
.\.venv\Scripts\activate
2️⃣ Run GUI Tests
bash
Copy code
.\run_gui_tests.bat
➡ Generates: GUI_Automation/reports/report.html

3️⃣ Run API Tests
bash
Copy code
.\run_api_tests.bat
➡ Generates: API_Automation/reports/report.html

4️⃣ Run All Tests Together
bash
Copy code
.\run_all_tests.bat
➡ Executes both GUI and API tests and generates individual reports.

📊 Reports
Each execution generates an HTML test report viewable in any browser.

Suite	Report Path
GUI Tests	GUI_Automation/reports/report.html
API Tests	API_Automation/reports/report.html

Screenshots (for GUI) are automatically captured only on failure and stored in the same folder.

🔄 CI/CD Integration (GitHub Actions)
The project includes a fully automated pipeline:

Creates and activates a Python virtual environment

Installs dependencies for both GUI & API test suites

Runs both test suites in sequence

Generates HTML reports

Uploads reports as downloadable artifacts

Workflow File: .github/workflows/automation.yml

You can view the pipeline under the Actions tab in this repository.

✅ Folder Structure
bash
Copy code
Revenue_Tasks/
│
├── GUI_Automation/
│   ├── features/
│   ├── page_objects/
│   ├── utils/
│   ├── reports/
│   ├── behave.ini
│   ├── requirements.txt
│   └── run_gui_tests.bat
│
├── API_Automation/
│   ├── features/
│   │   └── author/
│   │       ├── author_api.feature
│   │       └── steps/
│   │           └── author_steps.py
│   ├── api_objects/
│   ├── utils/
│   ├── reports/
│   ├── behave.ini
│   ├── requirements.txt
│   └── run_api_tests.bat
│
├── .github/workflows/automation.yml
├── README.md
└── run_all_tests.bat

👤 Author
Seema GS