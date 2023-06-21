




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get("https://www.facebook.com/SBS8news/posts/pfbid02oQytvxBitx8VZT5G5yE4aMrkaWcUw3KzSWEVgjbo7aZVEHGd82nxeFqxUhJyPaXwl")

element = driver.find_element_by_xpath("//span[contains(@class, 'x193iq5w')]")
element.click()
element = driver.find_element_by_class_name("x193iq5w")
element.click()
driver.execute_script("arguments[0].scrollIntoView();", comments_section)
comments = comments_section.find_elements(By.CSS_SELECTOR, "[data-testid='UFI2Comment/root_depth_0']")
for comment in comments:
    author = comment.find_element(By.CSS_SELECTOR, "[data-testid='UFI2Comment/actor_name']").text
    content = comment.find_element(By.CSS_SELECTOR, "[data-testid='UFI2Comment/body']").text
    #print(comment)


#sleep
driver.quit()





