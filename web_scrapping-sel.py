from selenium import webdriver   
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


driver = webdriver.Chrome()
url = "https://www.satellite-calculations.com/11parameter/ephemeris/separationlist.php?53.3772668N/2.8813544W/0.19589988708496092/59987/171/60/-1.0E-8?0/0/59915#google_vignette"

driver.get(url)
driver.refresh()
time.sleep(40)


rows = []
col = []


for i in [1, 25, 49, 73, 97, 121, 145, 169]:
    xpath = "/html/body/div[2]/center/table/tbody/tr[" + str(i) + "]/td[2]/p/font"
    date_element = driver.find_element(By.XPATH, xpath)
    dates_txt = date_element.text.strip()
    rows.append(dates_txt)

    xpath_2 = "/html/body/div[2]/center/table/tbody/tr[" + str(i) + "]/td[4]/p/font"
    col_2_element = driver.find_element(By.XPATH, xpath_2)
    col_2_txt = col_2_element.text.strip()
    col.append(col_2_txt)
    
    
heads = []

for j in [2,4]:
    x_path_heads = "/html/body/div[2]/center/table/thead/tr/th[" + str(j) + "]/p/font/b/span"
    headers = driver.find_element(By.XPATH, x_path_heads)
    headers_txt= headers.text.strip()
    heads.append(headers_txt)
    

    
data = list(zip(rows, col))



df = pd.DataFrame(data, columns = heads)

df.to_excel('python_b4s.xlsx', index=False)

