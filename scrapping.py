import time
import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


website = "https://www.adamchoi.co.uk/teamgoals/detailed"

driver = webdriver.Chrome()
driver.get(website)

wait = WebDriverWait(driver, 10)

allMatches = wait.until(EC.element_to_be_clickable((By.XPATH,'//label[@analytics-event="All matches"]')))
allMatches.click()

time.sleep(1)

selectCountry = wait.until(EC.element_to_be_clickable((By.ID, 'country')))
select = Select(selectCountry)

select.select_by_visible_text("Italy")


matches = wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'tr')))


matchesAll = []

for match in matches:
    matchesAll.append(match.text)

dataFrame = pandas.DataFrame({'Matches': matchesAll})
print(dataFrame)
dataFrame.to_csv('reports/resultMatches.csv', index=False)