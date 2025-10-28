@echo off
echo Running GUI automation...
behave GUI_Automation/features -f behave_html_formatter:HTMLFormatter -o GUI_Automation/reports/report.html

echo Running API automation...
behave API_Automation/features -f behave_html_formatter:HTMLFormatter -o API_Automation/reports/report.html

echo All tests executed successfully.
pause
