🧾 Revenue Automation Demo

This project demonstrates GUI and API automation for Revenue NSW sample tasks using Python (Behave BDD).
It showcases automation design, test execution, and reporting aligned with real-world QA practices.

🧰 Tools & Frameworks
Behave (BDD) – For readable, business-style test cases
Playwright – GUI browser automation
Requests – API testing
Behave HTML Formatter – For visual HTML reports
Python Virtual Environment – For isolated dependencies

▶️ How to Run the Tests

Activate Environment
.\.venv\Scripts\activate


Run GUI Tests
.\run_gui_tests.bat


➡ Generates GUI_Automation/reports/report.html

Run API Tests
.\run_api_tests.bat


➡ Generates API_Automation/reports/report.html
Run All Tests
.\run_all_tests.bat


➡ Executes both GUI & API tests together

📊 Reports
Each test run produces an HTML report viewable in any browser
Reports are located under:
GUI_Automation/reports/
API_Automation/reports/

🔄 CI/CD (Optional Demo)
When integrated into a pipeline (GitHub Actions):
Install dependencies
Run both .bat test suites
Generate HTML reports
Upload reports as artifacts for review

👤 Author
Seema Suresh