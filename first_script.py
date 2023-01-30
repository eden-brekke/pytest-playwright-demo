from playwright.sync_api import sync_playwright

URL = 'https://phptravels.net/login'
DASHBOARD_URL = 'https://phptravels.net/account/dashboard'


EMAILIDTEXTBOX = "//input[@placeholder='Email']" # if you control f on the console and search for this xpath on the webpage it will highlight the element which is being targetted.
EMAILID = "user@phptravels.com"
PASSWORDTEXTBOX = "//input[@placeholder='Password']"
PASSWORD = "demouser"
SUBMIT_BUTTON = "//button[@type='submit']"

