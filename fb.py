



import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()



driver.get("fb.url")

comments_section = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='UFI2CommentsList/root_depth_0']"))
)
driver.execute_script("arguments[0].scrollIntoView();", comments_section)
comments = comments_section.find_elements(By.CSS_SELECTOR, "[data-testid='UFI2Comment/root_depth_0']")
for comment in comments:
    author = comment.find_element(By.CSS_SELECTOR, "[data-testid='UFI2Comment/actor_name']").text
    content = comment.find_element(By.CSS_SELECTOR, "[data-testid='UFI2Comment/body']").text
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{timestamp}.txt"
    file_path = os.path.join("comment_files", filename)
    os.makedirs("fb_comments", exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Author: {author}\n")
        file.write(f"Comment: {content}\n")

        
        
#time.sleep(2)
driver.quit()





