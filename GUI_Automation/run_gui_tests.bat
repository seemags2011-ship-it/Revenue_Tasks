@echo off
echo Running GUI automation tests...
behave GUI_Automation/features -f behave_html_formatter:HTMLFormatter -o GUI_Automation/reports/report.html
echo Report generated at GUI_Automation\reports\report.html
pause
