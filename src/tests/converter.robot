*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Add Book With Valid Inputs
    Click Link  Lisää kirjaviite
    Set Kayttajatunnus  Test_tunnus
    Set Key  Test_key
    Set Author  Test_author
    Set Title  Test_title
    Set Year  Test_year
    Set Publisher  Test_Publisher
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
    Adding Should Succeed  Test_key

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

Set Book
    @{book_inputs}=  ${key}  ${author}  ${title}  ${year}  ${publisher}

Adding Should Succeed
    [Arguments]  @{book_inputs}
    FOR  ${arg}  IN  @{book_inputs}
        Page Should Contain  ${arg}
    END