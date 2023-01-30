from playwright.sync_api import sync_playwright

url = 'https://phptravels.net/login'
dashboard_url = 'https://phptravels.net/account/dashboard'


email_id_textbox = "//input[@placeholder='Email']" # if you control f on the console and search for this xpath on the webpage it will highlight the element which is being targetted.
# alternatively if you are having trouble writing an xpath to target the element you want correctly and uniquely then you can rightclick the element in the console and copy>copy xpath. It spits out an xpath thats specific to that element.
email_id = "user@phptravels.com"
password_text_box = "//input[@placeholder='Password']"
password = "demouser"
submit_button = "//button[@type='submit']"

# https://phptravels.net/
# = "//[='']"

my_bookings_button = "//a[@class=' waves-effect' and @href='https://phptravels.net/account/bookings']"
my_bookings_verify = "//h3[text()='My Bookings']"
add_funds_button = "//a[@class=' waves-effect' and @href='https://phptravels.net/account/add_funds']"
add_funds_verify = "//h3[text()='Add Funds']"
profile_button = "//a[@class=' waves-effect' and @href='https://phptravels.net/account/profile']"
profile_verify = "//h3[text()='Profile Information']"
logout_button = "//a[@class=' waves-effect' and @href='https://phptravels.net/account/logout']"

# with is context management, we use this keyword so python automatically starts and closes the playwright context which is created when we call the sync_playwright.start() method.
with sync_playwright() as p:
  
  # open the browser and page
  browser = p.chromium.launch(headless=False, slow_mo=2*1000)
  # initialize a new browser instance, each page makes a new instance and it is stored in the page variable.
  page = browser.new_page()
  
  # open the site
  page.goto(url)
  
  # enter the email
  page.fill(email_id_textbox, email_id)
  
  # enter the password
  page.fill(password_text_box, password)
  
  # click the submit button
  page.click(submit_button)
  
  # wait until the dashboard loads
  page.wait_for_url(dashboard_url)
  
  # click on the my bookings button
  page.click(my_bookings_button)
  
  # wait for the page to load 
  page.wait_for_selector(my_bookings_verify)

  page.click(add_funds_button)
  
  page.wait_for_selector(add_funds_verify)
  
  page.click(profile_button)
  
  page.wait_for_selector(profile_verify)

  # click the logout button
  page.click(logout_button)
  
  # verify logout by checking for the email id text box
  page.wait_for_selector(email_id_textbox)
  
  # make sure to close the page and browser when tests complete
  page.close()
  browser.close()