*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Variables ***
${sort_by_author}  author
${sort_by_year}  1997 

*** Test Cases ***

Sort References By Author With Valid Inputs
    Click Link  Lisää kirjaviite
    Fill Book Form  ${username}  ${author}  ${title}  ${year}  ${publisher}
    Submit Form
    Click Link  Lisää graduviite
    Fill Master Form  ${username}  ${sort_by_author}  ${title}  ${school}  ${year}
    Submit Form    
    Click Element  id=sort_by
    Click Element  //select[@id='sort_by']/option[text()='Author']


Sort References By Year With Valid Inputs
    Click Link  Lisää kirjaviite
    Fill Book Form  ${username}  ${author}  ${title}  ${year}  ${publisher}
    Submit Form
    Click Link  Lisää graduviite
    Fill Master Form  ${username}  ${sort_by_author}  ${title}  ${school}  ${sort_by_year}
    Submit Form    
    Click Element  id=sort_by
    Click Element  //select[@id='sort_by']/option[text()='Year']
        

