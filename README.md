📊 Outsourcing Analysis
This project is an end-to-end automated ETL pipeline for analyzing open job positions across multiple outsourcing companies. The stack includes Python, GitHub Actions, Tableau, and Google Sheets.

🚀 Project Overview
This automated ETL pipeline performs the following:

Scrapes job postings from various company websites.

Cleans and transforms the data.

Stores the results in a CSV file.

Syncs the data with a Google Sheet.

Visualizes job location insights on a Tableau map chart.

Runs automatically every 12 hours using GitHub Actions.

⚙️ ETL Pipeline Details
1. Data Scraping
A Python script (Pytest.py) launches a local server and sends multiple requests to each company's job listing URLs.

The script parses HTML elements to extract relevant job posting information.

2. ETL Process (Pytest.py)
Extract: Data is collected into a dictionary.

Transform: The transform_data() function (from ETL_functions.py) cleans whitespace and standardizes the location column into a country column.

Load: The cleaned data is saved into jobs_posting.csv using save_to_csv().

🤖 Automation with GitHub Actions
A GitHub Actions workflow is scheduled to run every 12 hours using the following cron expression:

yaml
Copy
Edit
schedule:
  - cron: '0 */12 * * *'
The workflow is deployed on a free Ubuntu GitHub runner.

It executes Pytest.py, updates the CSV file, and triggers the data sync with Google Sheets.

🔗 Google Sheets Integration
A Google Sheet is linked using the =IMPORTDATA() formula, which fetches live data from the jobs_posting.csv file in the repository.

The sheet is updated automatically every time the GitHub Action runs and the CSV file is refreshed.

📍 Tableau Data Visualization
A map chart was created in Tableau Public.

It connects directly to the Google Sheet for real-time updates.

The map displays job location data (by country) and updates automatically with each GitHub Action run.

🌐 Project Links
🔎 Frontend Job Dashboard: https://datapipelinejobs.rosystems.net/

🗺️ Tableau Map Chart: Tableau Public Link
