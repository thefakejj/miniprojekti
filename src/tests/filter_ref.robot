*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Variables ***
${search_query}  book

*** Test Cases ***

Filter References By Search Query
    Click Link  Lisää kirjaviite
    Fill Book Form  ${username}  ${author}  ${title}  ${year}  ${publisher}
    Submit Form
    Click Link  Lisää graduviite
    Fill Masterthesis Form  ${username}  ${author}  ${title}  ${school}  ${year}
    Submit Form
    Input Search Query  ${search_query}
    Submit Search Form
    Search Should Succeed

*** Keywords ***
Input Search Query
    [Arguments]  ${query}
    Input Text  id=query  ${query}

Submit Search Form
    Click Button  //input[@type='submit']

Search Should Succeed
    Page Should Contain  book