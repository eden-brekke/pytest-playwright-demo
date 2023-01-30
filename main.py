from playwright.sync_api import sync_playwright

URL = 'https://phptravels.net/login'
DASHBOARD_URL = 'https://phptravels.net/account/dashboard'


EMAILIDTEXTBOX = "//input[@placeholder='Email']" # if you control f on the console and search for this xpath on the webpage it will highlight the element which is being targetted.
# alternatively if you are having trouble writing an xpath to target the element you want correctly and uniquely then you can rightclick the element in the console and copy>copy xpath. It spits out an xpath thats specific to that element.
EMAILID = "user@phptravels.com"
PASSWORDTEXTBOX = "//input[@placeholder='Password']"
PASSWORD = "demouser"
SUBMIT_BUTTON = "//button[@type='submit']"

# https://phptravels.net/
# = "//[='']"

MY_BOOKINGS_BUTTON = "//a[@class=' waves-effect' and @href='https://phptravels.net/account/bookings']"
MY_BOOKINGS_VERIFY = "//h3[text()='My Bookings']"
ADD_FUNDS_BUTTON = "//a[@class=' waves-effect' and @href='https://phptravels.net/account/add_funds']"
ADD_FUNDS_VERIFY = "//h3[text()='Add Funds']"
PROFILE_BUTTON = "//a[@class=' waves-effect' and @href='https://phptravels.net/account/profile']"
PROFILE_VERIFY = "//h3[text()='Profile Information']"
LOGOUT_BUTTON = "//a[@class=' waves-effect' and @href='https://phptravels.net/account/logout']"

# with is context management, we use this keyword so python automatically starts and closes the playwright context which is created when we call the sync_playwright.start() method.
with sync_playwright() as p:
  
  # open the browser and page
  browser = p.chromium.launch(headless=False, slow_mo=2*1000)
  # initialize a new browser instance, each page makes a new instance and it is stored in the page variable.
  page = browser.new_page()
  
  # open the site
  page.goto(URL)
  
  # enter the email
  page.fill(EMAILIDTEXTBOX, EMAILID)
  
  # enter the password
  page.fill(PASSWORDTEXTBOX, PASSWORD)
  
  # click the submit button
  page.click(SUBMIT_BUTTON)
  
  # wait until the dashboard loads
  page.wait_for_url(DASHBOARD_URL)
  
  # click on the my bookings button
  page.click(MY_BOOKINGS_BUTTON)
  
  # wait for the page to load 
  page.wait_for_selector(MY_BOOKINGS_VERIFY)

  page.click(ADD_FUNDS_BUTTON)
  
  page.wait_for_selector(ADD_FUNDS_VERIFY)
  
  page.click(PROFILE_BUTTON)
  
  page.wait_for_selector(PROFILE_VERIFY)

  # click the logout button
  page.click(LOGOUT_BUTTON)
  
  # verify logout by checking for the email id text box
  page.wait_for_selector(EMAILIDTEXTBOX)
  
  # make sure to close the page and browser when tests complete
  page.close()
  browser.close()