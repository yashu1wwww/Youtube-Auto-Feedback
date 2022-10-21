import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

email = 'mail23\n'               #change to your mail
password = 'pass23@\n'           #change to your pass  

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver,20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
time.sleep(1)
wait.until(EC.visibility_of_element_located((By.NAME,'Passwd'))).send_keys(password)
time.sleep(20)
driver.find_element_by_id("avatar-btn").click()
time.sleep(10)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[5]/div[2]/ytd-compact-link-renderer[2]/a/tp-yt-paper-item').click()
time.sleep(3)
driver.find_element_by_css_selector('body > div:nth-child(3) > div > div > uf-describe-page > form > div:nth-child(2) > textarea').send_keys("hey youtube") #change to your feedback text
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/uf-describe-page/form/footer/uf-material-button[1]/label/button').click()
time.sleep(30)
