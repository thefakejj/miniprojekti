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
${key_to_delete}  AB12
${deleted_author}  Deleted_Author
${deleted_title}  Deleted_Title
${deleted_year}  2025
${deleted_publisher}  Deleted_Publisher
${deleted_school}  Deleted_School

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
<<<<<<< HEAD
    Set Kayttajatunnus  ${username}
    Set Key  ${key}
    Set Author  ${author}
    Set Title  ${title}
    Set Year  ${year}
    Set Publisher  ${publisher}
=======
    Set Kayttajatunnus  Test_tunnus
    Set Author  Test_author
    Set Title  Test_title
    Set Year  Test_year
    Set Publisher  Test_Publisher
>>>>>>> main
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

Add Reference For Deletion
    Click Link  Lisää kirjaviite
    Set Key  ${key_to_delete}
    Set Kayttajatunnus  ${username}
    Set Author  ${deleted_author}
    Set Title  ${deleted_title}
    Set Year  ${deleted_year}
    Set Publisher  ${deleted_publisher}
    Click Button  Lisää
    Home Page Should Be Open
    Adding Should Succeed  ${deleted_author}  ${deleted_title}  ${deleted_year}  ${deleted_publisher}

Delete Reference
    Click Link  Keylist
    Click Link  ${key_to_delete}
    Page Should Contain Element  xpath://li[contains(., "${deleted_author}")]
    Page Should Contain Element  xpath://li[contains(., "${deleted_title}")]
    Page Should Contain Element  xpath://li[contains(., "${deleted_year}")]
    Page Should Contain Element  xpath://li[contains(., "${deleted_publisher}")]
    Click Button  Poista!

Keylist Should Not Contain Deleted Reference
    Click Link  Keylist
    Page Should Not Contain Element  xpath://li[contains(., "${deleted_author}")]
    Page Should Not Contain Element  xpath://li[contains(., "${deleted_title}")]
    Page Should Not Contain Element  xpath://li[contains(., "${deleted_year}")]
    Page Should Not Contain Element  xpath://li[contains(., "${deleted_publisher}")]


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