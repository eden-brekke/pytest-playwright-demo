# Pytest Playwright Demo

Playwright is a test framework which gives the developers a way to control the browser's behaviour, you can use playwright in a variety of languages, but this demo is for pytest-playwright in the python language.

## Resources

For this demo I am using [Php Travels Demo Testing Site](https://phptravels.com/demo) which is a free platform in which you can use to learn front end testing methods.

And I'm using [Pytest Playwright](https://playwright.dev/python/docs/intro)

### Install from Repo

Steps to run this repo and these tests:

git clone the repo down to your local machine, and then create your virtual environment for python. I am on windows and I use venv, so the commands are:

```cli
py -m venv .venv
.\.venv\Scripts\activate
```

Then install the requirements and run the script:

```cli
pip install -r requirements.txt
python main.py
```

This will open the playwright browser and I have a 2 second slowmo so that you can see the tests working, otherwise it moves too fast for most human eyes to comprehend.

### Install from Scratch

Steps for installation from scratch:

create your virtual environment for python. I am on windows and I use venv, so the commands are:

```cli
py -m venv .venv
.\.venv\Scripts\activate
```

Then you'll need to install pytest-playwright and the playwright browser with these commands:

```cli
pip install pytest-playwright
playwright install
```

From there it's your playground!

## Additional notes on Xpaths

We use xpath's to talk to the browser
The syntax for an xpath is:

```py
VARIABLE_NAME = "//attribute[@identifier='Text within what we're trying to target']"
```

A more specified example from the code within:

```py
URL = 'https://phptravels.net/login'

EMAILIDTEXTBOX = "//input[@placeholder='Email']" 
EMAILID = "user@phptravels.com"
```

We then use playwright commands such as:

```py
with sync_playwright() as p:
  browser = p.chromium.launch(headless=False, slow_mo=2*1000)
  page = browser.new_page()
  page.goto(URL)
  page.fill(EMAILIDTEXTBOX, EMAILID)
```

Where browers is specifying the browser to launch, and slow_mo is just slowing down the process we can see it.  
Page is creating a new page instance each time we call it and storing it in memory.  

The URL specifies the URL in which we first visit, so we 'page.goto(URL)'

Then the EMAILIDTEXTBOX variable is targeting the textbox associated with logging in using your email.  
If you go to the URL and open the console, hit control f and paste the xpath ```(//input[@placeholder='Email'])``` you will see the email text area highlighted.

Once that's been selected, the EMAILID variable is input to that text box. These two variables are the arguments for the fill() method that playwright uses.

There are a bunch of different ways to target html elements with xpaths and a good resource for the syntax is [here](https://devhints.io/xpath)

### Final notes

Finally, there are a lot of different ways to write tests in playwright, so definitely go exploring [Playwright for Python Docs](https://playwright.dev/python/)