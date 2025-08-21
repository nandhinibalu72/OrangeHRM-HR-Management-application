# OrangeHRM Automated Testing Project

## Objective
Automate the testing of https://opensource-demo.orangehrmlive.com focusing on:
- Login & logout
- Menu accessibility
- User management
- Leave & claim requests

## Architecture
- `pages/` - Page Objects
- `tests/` - Test Cases
- `data/` - Test data (e.g., `login_data.csv`)
- `utils/` - Helpers, logger
- `reports/` - Allure results
- `pytest.ini` - Test settings
- `.gitignore` - Excludes venv, temp files

## Features
- Page Object Model
- Parameterized test data
- Explicit waits & error handling
- Allure test reports
- Scripts for test execution
- Supports multiple browsers

## Quick Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/nandhinibalu72/OrangeHRM-HR-Management-application.git
   cd orangehrm_automation
