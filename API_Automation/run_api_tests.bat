@echo off
echo Running API automation tests...
behave API_Automation/features -f behave_html_formatter:HTMLFormatter -o API_Automation/reports/report.html
echo Report generated at API_Automation\reports\report.html
pause