# *** Settings ***
# Resource  resource.robot
# Library  OperatingSystem
# Suite Setup  Open And Configure Browser
# Suite Teardown  Close Browser
# Test Setup  Go To Home Page

# *** Variables ***
# ${downloads_path}  ~/Downloads/references.bib

# *** Test Cases ***
# Download book
#     Click Link  Lisää kirjaviite
#     Fill Book Form  ${username}  ${author}  ${title}  ${year}  ${publisher}
#     Submit Form
#     Home Page Should Be Open
#     Click Button  Lataa bibtex-tiedosto
#     Sleep  2s
#     File Should Exist  ${downloads_path}