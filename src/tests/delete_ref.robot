*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Variables ***
${username}  Test_tunnus
${key_to_delete}  De25
${deleted_author}  Deleted_Author
${deleted_title}  Deleted_Title
${deleted_year}  2025
${deleted_publisher}  Deleted_Publisher
${deleted_school}  Deleted_School

*** Test Cases ***
Add Reference For Deletion
    Click Link  Lisää kirjaviite
    Set Kayttajatunnus  ${username}
    Set Author  ${deleted_author}
    Set Title  ${deleted_title}
    Set Year  ${deleted_year}
    Set Publisher  ${deleted_publisher}
    Submit Form
    Wait Until Page Contains  APPI
    Home Page Should Be Open
    Adding Book Should Succeed  ${deleted_author}  ${deleted_title}  ${deleted_year}  ${deleted_publisher}

Delete Reference
    Set Focus To Element  xpath://a[@href='/confirmdelete/${key_to_delete}'] 
    Press Keys  None  ENTER
    Wait Until Page Contains Element  xpath://input[@value='Poista!']
    Page Should Contain Element  xpath://li[contains(., "${deleted_author}")]
    Page Should Contain Element  xpath://li[contains(., "${deleted_title}")]
    Page Should Contain Element  xpath://li[contains(., "${deleted_year}")]
    Page Should Contain Element  xpath://li[contains(., "${deleted_publisher}")]
    #Click Element  xpath://input[@value='Poista!']
    #Scroll Element Into View  xpath://input[@value='Poista!']
    Submit Form
    #Click Button  xpath://input[@value='Poista!']

Keylist Should Not Contain Deleted Reference
    Page Should Not Contain Element  xpath://li[contains(., "${key_to_delete}")]

*** Keywords ***
Adding Book Should Succeed
    [Arguments]  ${author}  ${title}  ${year}  ${publisher}
    Page Should Contain  ${author}
    Page Should Contain  ${title}
    Page Should Contain  ${year}
    Page Should Contain  ${publisher}