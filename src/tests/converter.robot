*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Variables ***
${username}  Test_tunnus
${key}  Test_key
${author}  Test_author
${title}  Test_title
${year}  Test_year
${publisher}  Test_Publisher

*** Test Cases ***
Add Book With Valid Inputs
    Click Link  Lisää kirjaviite
    Set Kayttajatunnus  ${username}
    Set Key  ${key}
    Set Author  ${author}
    Set Title  ${title}
    Set Year  ${year}
    Set Publisher  ${publisher}
    Click Button  Lisää
    Home Page Should Be Open

Book list Should Contain Book
    Click Link  Lisää kirjaviite
    Set Kayttajatunnus  Test_tunnus
    Set Key  Test_key
    Set Author  Test_author
    Set Title  Test_title
    Set Year  Test_year
    Set Publisher  Test_Publisher
    Click Button  Lisää
    Home Page Should Be Open
    Adding Should Succeed  ${key}  ${author}  ${title}  ${year}  ${publisher}

*** Keywords ***
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


Adding Should Succeed
    [Arguments]  ${key}  ${author}  ${title}  ${year}  ${publisher}
    Page Should Contain  ${key}
    Page Should Contain  ${author}
    Page Should Contain  ${title}
    Page Should Contain  ${year}
    Page Should Contain  ${publisher}