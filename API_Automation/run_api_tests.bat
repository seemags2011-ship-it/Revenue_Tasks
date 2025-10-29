@echo off
echo =============================================
echo Running API Automation Tests
echo =============================================

pushd %~dp0

if exist ..\.venv\Scripts\activate (
    call ..\.venv\Scripts\activate
)

if not exist reports mkdir reports

echo Running tests...
python -m behave features -f behave_html_formatter:HTMLFormatter -o reports/report.html

echo =============================================
echo Test Execution Complete
echo Report saved in reports\report.html
echo =============================================

start reports\report.html
pause
