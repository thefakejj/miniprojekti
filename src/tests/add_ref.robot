*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page


*** Test Cases ***
Add Book With Valid Inputs
    Click Link  Lisää kirjaviite
    Fill Book Form  ${username}  ${author}  ${title}  ${year}  ${publisher}
    Submit Form
    Home Page Should Be Open

Book List Should Show
    Click Link  Lisää kirjaviite
    Fill Book Form  ${username}  ${author}  ${title}  ${year}  ${publisher}
    Submit Form
    Adding Book Should Succeed  ${author}  ${title}  ${year}  ${publisher}

Add Book With Invalid Inputs
    Click Link  Lisää kirjaviite
    Fill Book Form  ${username}  ${author}  ${title}  4444  ${publisher}
    Submit Form
    Adding Should Fail With Message  Vuosi väärin!

Add Masterthesis With Valid Inputs
    Click Link  Lisää graduviite
    Fill Masterthesis Form  ${username}  ${author}  ${title}  ${school}  ${year}
    Submit Form
    Home Page Should Be Open

Masterthesis List Should Show
    Click Link  Lisää graduviite
    Fill Masterthesis Form  ${username}  ${author}  ${title}  ${school}  ${year}
    Submit Form
    Adding Masterthesis Should Succeed  ${author}  ${title}  ${school}  ${year}

Add Masterthesis With Invalid Inputs
    Click Link  Lisää graduviite
    Fill Masterthesis Form  ${username}  ${author}  ${title}  ${school}  4444
    Submit Form
    Adding Should Fail With Message  Vuosi väärin!

Add Phdthesis With Valid Inputs
    Click Link  Lisää väitöskirjaviite
    Fill Phdthesis Form  ${username}  ${author}  ${title}  ${school}  ${year}
    Submit Form
    Home Page Should Be Open

Phdthesis List Should Show
    Click Link  Lisää väitöskirjaviite
    Fill Phdthesis Form  ${username}  ${author}  ${title}  ${school}  ${year}
    Submit Form
    Adding Phdthesis Should Succeed  ${author}  ${title}  ${school}  ${year}

Add Phdthesis With Invalid Inputs
    Click Link  Lisää väitöskirjaviite
    Fill Phdthesis Form  ${username}  ${author}  ${title}  ${school}  4444
    Submit Form
    Adding Should Fail With Message  Vuosi väärin!

Add Article With Valid Inputs
    Click Link  Lisää artikkeliviite
    Fill Article Form  ${username}  ${author}  ${title}  ${journal}  ${year}
    Submit Form
    Home Page Should Be Open

Article List Should Show
    Click Link  Lisää artikkeliviite
    Fill Article Form  ${username}  ${author}  ${title}  ${journal}  ${year}
    Submit Form
    Adding Article Should Succeed  ${author}  ${title}  ${school}  ${year}

Add Article With Invalid Inputs
    Click Link  Lisää artikkeliviite
    Fill Article Form  ${username}  ${author}  ${title}  ${journal}  4444
    Submit Form
    Adding Should Fail With Message  Vuosi väärin!

*** Keywords ***
Adding Book Should Succeed
    [Arguments]  ${author}  ${title}  ${year}  ${publisher}
    Page Should Contain  key
    Page Should Contain  reftype
    Page Should Contain  book
    Page Should Contain  ${author}
    Page Should Contain  author
    Page Should Contain  ${title}
    Page Should Contain  title
    Page Should Contain  ${year}
    Page Should Contain  year
    Page Should Contain  ${publisher}
    Page Should Contain  publisher
    Page Should Contain  Muokkaa
    Page Should Contain  Poista

Adding Masterthesis Should Succeed
    [Arguments]  ${author}  ${title}  ${school}  ${year}
    Page Should Contain  key
    Page Should Contain  reftype
    Page Should Contain  masterthesis
    Page Should Contain  ${author}
    Page Should Contain  author
    Page Should Contain  ${title}
    Page Should Contain  title
    Page Should Contain  ${school}
    Page Should Contain  school
    Page Should Contain  ${year}
    Page Should Contain  year
    Page Should Contain  Muokkaa
    Page Should Contain  Poista

Adding Phdthesis Should Succeed
    [Arguments]  ${author}  ${title}  ${school}  ${year}
    Page Should Contain  key
    Page Should Contain  reftype
    Page Should Contain  phdthesis
    Page Should Contain  ${author}
    Page Should Contain  author
    Page Should Contain  ${title}
    Page Should Contain  title
    Page Should Contain  ${school}
    Page Should Contain  school
    Page Should Contain  ${year}
    Page Should Contain  year
    Page Should Contain  Muokkaa
    Page Should Contain  Poista

Adding Article Should Succeed
    [Arguments]  ${author}  ${title}  ${journal}  ${year}
    Page Should Contain  key
    Page Should Contain  reftype
    Page Should Contain  article
    Page Should Contain  ${author}
    Page Should Contain  author
    Page Should Contain  ${title}
    Page Should Contain  title
    Page Should Contain  ${journal}
    Page Should Contain  journal
    Page Should Contain  ${year}
    Page Should Contain  year
    Page Should Contain  Muokkaa
    Page Should Contain  Poista

Adding Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}