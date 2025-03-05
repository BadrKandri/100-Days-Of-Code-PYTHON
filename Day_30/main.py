from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from config import get_per_info

mail,mdp,phone_number=get_per_info()
url='https://www.linkedin.com/jobs/search/?currentJobId=4150269747&f_AL=true&keywords=Engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")  # Only show fatal errors, hide warnings and info
chrome_options.add_experimental_option("detach", True)  # Keep the browser open after execution

def abort_application():
    # Click Close Button
    close_button = driver.find_element(By.CLASS_NAME, "artdeco-button__icon")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
    discard_button.click()
    
# Initialize the driver
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

time.sleep(2)
click_signIn=driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
click_signIn.click()

print_mail=driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_key"]')
print_mail.send_keys(mail)

print_mdp=driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]')
print_mdp.send_keys(mdp)

signIn=driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
signIn.click()


# Get Listings
time.sleep(5)
all_listings = driver.find_elements(By.CSS_SELECTOR, '[id^="ember"] span > strong')
for job in all_listings:
    job.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)
        phone = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4150269747-9-phoneNumber-nationalNumber"]')
        if phone.text == "":
            phone.send_keys(phone_number)
            
        # Check the Submit Button
        submit_button = driver.find_element(By.XPATH, '//*[@id="ember311"]/span')
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            ActionChains(driver).move_to_element(submit_button).click().perform()
        time.sleep(2)
        
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-button__icon")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
