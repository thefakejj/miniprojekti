*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0 seconds
${HOME_URL}  http://${SERVER}
${POSTBOOK_URL}  http://${SERVER}/postbook
${POSTMASTER_URL}  http://${SERVER}/postmaster

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Home Page Should Be Open
    Title Should Be  APPI

Go To Home Page
    Go To  ${HOME_URL}

Go To Postbook Page
    Go To  ${POSTBOOK_URL}

Go To Postmaster Page
    Go To  ${POSTMASTER_URL}
