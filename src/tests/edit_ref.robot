*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Variables ***
${edited_author}  Edited_Author
${edited_title}  Edited_Title
${edited_year}  2000

*** Test Cases ***
Edit Book Reference With Valid Inputs
    Click Link  Lisää kirjaviite
    Fill Book Form  ${username}  ${author}  ${title}  ${year}  ${publisher}
    Submit Form
    Click Muokkaa
    Edit Filled Values  ${edited_author}  ${edited_title}  ${edited_year}
    Submit Form
    Editing Masterthesis Should succeed  ${edited_author}  ${edited_title}  ${edited_year}  ${publisher} 
    Delete Edited Reference


Edit Masterthesis Reference With Valid Inputs
    Click Link  Lisää graduviite
    Fill Masterthesis Form  ${username}  ${author}  ${title}  ${school}  ${year}
    Submit Form
    Click Muokkaa
    Edit Filled Values  ${edited_author}  ${edited_title}  ${edited_year}
    Submit Form
    Editing Masterthesis Should Succeed  ${edited_author}  ${edited_title}  ${school}  ${edited_year}
    Delete Edited Reference

Edit Phdthesis Reference With Valid Inputs
    Click Link  Lisää väitöskirjaviite
    Fill Phdthesis Form  ${username}  ${author}  ${title}  ${school}  ${year}
    Submit Form
    Click Muokkaa
    Edit Filled Values  ${edited_author}  ${edited_title}  ${edited_year}
    Submit Form
    Editing Phdthesis Should Succeed  ${edited_author}  ${edited_title}  ${school}  ${edited_year}
    Delete Edited Reference

Edit Article Reference With Valid Inputs
    Click Link  Lisää artikkeliviite
    Fill Article Form  ${username}  ${author}  ${title}  ${journal}  ${year}
    Submit Form
    Click Muokkaa
    Edit Filled Values  ${edited_author}  ${edited_title}  ${edited_year}
    Submit Form
    Editing Article Should Succeed  ${edited_author}  ${edited_title}  ${journal}  ${edited_year}
    Delete Edited Reference


*** Keywords ***
Click Muokkaa
    Set Focus to Element  xpath://a[text()='Muokkaa']
    Press Keys  None  ENTER

Click Poista    
    Set Focus to Element  xpath://a[text()='Poista']
    Press Keys  None  ENTER

Delete Edited Reference
    Click Poista
    Submit Form


Edit Filled Values
    [Arguments]  ${edited_author}  ${edited_title}  ${edited_year}
    Set Author  ${edited_author}
    Set Title  ${edited_title}
    Set Year  ${edited_year}

Editing Book Should Succeed
    [Arguments]  ${edited_author}  ${edited_title}  ${edited_year}  ${publisher} 
    Page Should Contain  ${edited_author}
    Page Should Contain  ${edited_title}
    Page Should Contain  ${edited_year}
    Page Should Contain  ${publisher} 

Editing Masterthesis Should Succeed
    [Arguments]  ${edited_author}  ${edited_title}  ${school}  ${edited_year}
    Page Should Contain  ${edited_author}
    Page Should Contain  ${edited_title}
    Page Should Contain  ${school}
    Page Should Contain  ${edited_year}

Editing Phdthesis Should Succeed
    [Arguments]  ${edited_author}  ${edited_title}  ${school}  ${edited_year}
    Page Should Contain  ${edited_author}
    Page Should Contain  ${edited_title}
    Page Should Contain  ${school}
    Page Should Contain  ${edited_year}

Editing Article Should Succeed
    [Arguments]  ${edited_author}  ${edited_title}  ${school}  ${edited_year}
    Page Should Contain  ${edited_author}
    Page Should Contain  ${edited_title}
    Page Should Contain  ${school}
    Page Should Contain  ${edited_year}
