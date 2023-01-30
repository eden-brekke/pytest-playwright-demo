from playwright.sync_api import sync_playwright

URL = 'https://phptravels.net/login'
DASHBOARD_URL = 'https://phptravels.net/account/dashboard'


EMAILIDTEXTBOX = "//input[@placeholder='Email']" # if you control f on the console and search for this xpath on the webpage it will highlight the element which is being targetted.
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


