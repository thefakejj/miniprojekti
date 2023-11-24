*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Variables ***
${username}  Test_tunnus
${author}  Test_author
${title}  Test_title
${year}  Test_year
${publisher}  Test_Publisher
${school}  Test_School

*** Test Cases ***
Add Book With Valid Inputs
    Click Link  Lisää kirjaviite
    Set Kayttajatunnus  ${username}
    Set Author  ${author}
    Set Title  ${title}
    Set Year  ${year}
    Set Publisher  ${publisher}
    Click Button  Lisää
    Home Page Should Be Open

Add Master With Valid Inputs
    Click Link  Lisää graduviite
    Set Kayttajatunnus  ${username}
    Set Author  ${author}
    Set Title  ${title}
    Set School  ${school}
    Set Year  ${year}
    Click Button  Lisää
    Home Page Should Be Open

Book list Should Contain Book
    Click Link  Lisää kirjaviite
    Set Kayttajatunnus  Test_tunnus
    Set Author  Test_author
    Set Title  Test_title
    Set Year  Test_year
    Set Publisher  Test_Publisher
    Click Button  Lisää
    Home Page Should Be Open
    Adding Should Succeed  ${author}  ${title}  ${year}  ${publisher}

Master list Should Contain Master
    Click Link  Lisää graduviite
    Set Kayttajatunnus  Test_tunnus
    Set Author  Test_author
    Set Title  Test_title
    Set School  Test_School
    Set Year  Test_year
    Click Button  Lisää
    Home Page Should Be Open
    Adding Master Should Succeed  ${author}  ${title}  ${year}  ${publisher}


*** Keywords ***
Set Kayttajatunnus
    [Arguments]  ${username}
    Input Text  username  ${username}

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

Adding Should Succeed
    [Arguments]  ${author}  ${title}  ${year}  ${publisher}
    Page Should Contain  ${author}
    Page Should Contain  ${title}
    Page Should Contain  ${year}
    Page Should Contain  ${publisher}

Adding Master Should Succeed
    [Arguments]  ${author}  ${title}  ${school}  ${year}
    Page Should Contain  ${author}
    Page Should Contain  ${title}
    Page Should Contain  ${school}
    Page Should Contain  ${year}