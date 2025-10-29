@echo off
echo =============================================
echo Running GUI Automation Tests with Behave
echo =============================================

rem Set the working directory to the script's location
pushd %~dp0

rem Ensure we're using the venv's Python
call ..\.venv\Scripts\activate
if not exist reports mkdir reports

rem Run behave with HTML formatting
python -m behave --format behave_html_formatter:HTMLFormatter --outfile reports/report.html

echo =============================================
echo Test Execution Complete
echo Report saved in reports\report.html
echo =============================================

start reports\report.html
pause
