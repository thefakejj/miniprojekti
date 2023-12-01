*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0 seconds
${HOME_URL}  http://${SERVER}
${POSTBOOK_URL}  http://${SERVER}/postbook
${POSTMASTER_URL}  http://${SERVER}/postmaster
${username}  Test_tunnus
${author}  Test_author
${title}  Test_title
${year}  1999
${publisher}  Test_Publisher
${school}  Test_School

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

Set Kayttajatunnus
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Key
    [Arguments]  ${key}
    Input Text  key  ${key}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Set School
    [Arguments]  ${school}
    Input Text  school  ${school}

Fill Book Form
    [Arguments]  ${username}  ${author}  ${title}  ${year}  ${publisher}
    Set Kayttajatunnus  ${username}
    Set Author  ${author}
    Set Title  ${title}
    Set Year  ${year}
    Set Publisher  ${publisher}

Fill Master Form
    [Arguments]  ${username}  ${author}  ${title}  ${school}  ${year}
    Set Kayttajatunnus  ${username}
    Set Author  ${author}
    Set Title  ${title}
    Set School  ${school}
    Set Year  ${year}