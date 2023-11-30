![CI_workflow](https://github.com/thefakejj/miniprojekti/workflows/CI/badge.svg) [![codecov](https://codecov.io/gh/thefakejj/miniprojekti/graph/badge.svg?token=P4OWZDSB9C)](https://codecov.io/gh/thefakejj/miniprojekti)
# miniprojekti
This is **Nelosen oppilaat** group's repository for Ohjelmistotuotanto course

[**Project backlog**](https://docs.google.com/spreadsheets/d/1rMa7GUguUNTL2GxiPYZAxfzeGfuaFnNYY5xCVqZGXGg/edit?usp=sharing)

[**Arvosteluperusteet**](https://ohjelmistotuotanto-hy.github.io/miniprojektin_arvosteluperusteet/)

[**Aiheen kuvaus**](https://ohjelmistotuotanto-hy.github.io/speksi/)

## Use Case Overview
![UML_UseCase](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/thefakejj/miniprojekti/master/doc/use_case.puml&Refresh)

## Architecture Overview
![UML_Architecture](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/thefakejj/miniprojekti/master/doc/architecture.puml&Refresh)

## Weekly Schedule
* **Monday**
  * 15:30 Retrospective
  * 16:00 Demo A319, Exactum
  * 16:30 Sprint planning
* **Wednesday**
  * 12-14 Development meeting
* **Thursday**
  * 10-12 Development meeting    

## Role Descriptions
* **Product Owner**
  * Maintains product backlog
  * Sets up sprint backlog
  * Ensures that the development team focuses on:
    * Story implementation in the prioritization order
    * Sprint grading criteria
  * Implements non-development sprint grading criteria
* **Developer**
  * Designs and implements the necessary solutions to meet the story acceptance criteria
  * Install and configures the developemnt tools and frameworks

## Definition of Done
* All tasks required for implementing the user story have been finished
* Automated test implemented for the feature

# Installation
* [Install python 3.8+](https://www.python.org/about/gettingstarted/)
* [Install poetry 1.7.0+](https://python-poetry.org/docs/#installation)
```
git clone git@github.com:thefakejj/miniprojekti.git
```
```
poetry install
```
```
poetry run flask run
```

# User Guide
After starting the application open the following url with a browser: http://127.0.0.1:5000

* _Lisää kirjaviite_ link allows adding book references into database.
  * Input book reference details into corresponding form fields and click _Lisää_
* _Lisää graduviite_ link allows adding master thesis references into database.
  * Input master thesis reference details into corresponding form fields and click _Lisää_
* Existing book references are displayed on the bottom of the page in Bibtex format
  * _Poista_ link opens a confirmation screen for deleting the reference
    * Clicking _Takaising_ returns to previous screen.
    * Clicking _Poista!_ deletes the reference. The operation is undoable.
  * _Muokkaa_ link opens a screen for editing the reference details
    * Clicking _Takaising_ returns to previous screen.
    * Clicking _Tallenna muutokset_ saves the changes.
