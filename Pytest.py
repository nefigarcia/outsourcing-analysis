from ETL_functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


element_list = []

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (optional)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())

print("Starting job search scraping...")
T0 = time.time()


for page in range(1, 5):
    # Initialize driver properly
    driver = webdriver.Chrome(service=service, options=options)

    # Load the URL
    url = f"https://www.ibm.com/careers/search?field_keyword_18%5B0%5D=Entry%20Level"
    driver.get(url)
    time.sleep(4)  # Optional wait to ensure page loads

    # Extract product details
    #titles = driver.find_elements(By.CLASS_NAME, "bx--card__eyebrow")
    role = driver.find_elements(By.CLASS_NAME, "bx--card__heading")
    pais = driver.find_elements(By.CLASS_NAME, "ibm--card__copy__inner")

    # Store results in a list
    for i in range(len(role)):
        element_list.append([
            'IBM',
            #titles[i].text,
            role[i].text,
            pais[i].text
        ])

    driver.quit()
# Continue with Accenture job search scraping
for page in (range(1, 2)):
    driver = webdriver.Chrome(service=service, options=options)
    url = "https://www.accenture.com/us-en/careers/jobsearch"
    driver.get(url)
    time.sleep(4)

    roles = driver.find_elements(By.CLASS_NAME, "rad-filters-vertical__job-card-title")
    locations = driver.find_elements(By.CLASS_NAME, "rad-filters-vertical__job-card-details-location")
    levels = driver.find_elements(By.CLASS_NAME, "rad-filters-vertical__job-card-details-type")  # Same as 'pais'

    for i in range(len(roles)):
        element_list.append([
            'Accenture',
            roles[i].text,
            locations[i].text,
            levels[i].text
        ])

    driver.quit()    

T1 = time.time()
print(f"Scraping completed in {T1 - T0:.2f} seconds.")
# Display extracted data

# transform data
T0 = time.time()
print("Transforming data...")
result = transform_data(element_list)
for row in result:
    print(row)
T1 = time.time()
print(f"Data transformation completed in {T1 - T0:.2f} seconds.")
total = len(result)
print(f"Total number of job postings: {total}")

# Save to CSV file

T0 = time.time()
print("Saving data to CSV file...")
save_to_csv(result)
T1 = time.time()
print(f"Data saved in csv file in {T1 - T0:.2f} seconds.")
print("Job search scraping and data transformation completed successfully.")
# End of the script
# Note: Ensure that the ETL_functions module is available in the same directory or in the