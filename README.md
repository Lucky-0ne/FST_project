# FST_project
This is a project for the "Fortgeschrittene Softwaretechnik" (FS or FST) course. An alternate Atari Breakout video game.

required packages:
`pip install -r requirements.txt`

## 1. Git
Used Git for synchronizing project related files between my home PC and Uni Laptop.

(and because it was mandatory for the final submission of the "Fortgeschrittene Softwaretechnik" course)

## 2. UML 
There were three UML diagramms created for this project. Each of them shall be able to be pumped up artificially as intended in the Domain-Driven Design (DDD).

- [activity diagramm](https://github.com/Lucky-0ne/FST_project/blob/main/images/uml/Activity_Diagramm.png)
- [use case diagramm](https://github.com/Lucky-0ne/FST_project/blob/main/images/uml/Use_Case_Diagramm.png)
- [component diagramm](https://github.com/Lucky-0ne/FST_project/blob/main/images/uml/Component_Diagramm.png)

## 3. DDD
&rarr; [Event-Storming and Core Domain Chart](https://github.com/Lucky-0ne/FST_project/blob/main/images/ddd/event_storming_ddd.jpg)

## 4. Metrics
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Lucky-0ne_FST_project&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Lucky-0ne_FST_project)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Lucky-0ne_FST_project&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Lucky-0ne_FST_project)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Lucky-0ne_FST_project&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Lucky-0ne_FST_project)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Lucky-0ne_FST_project&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Lucky-0ne_FST_project)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Lucky-0ne_FST_project&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Lucky-0ne_FST_project)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Lucky-0ne_FST_project&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=Lucky-0ne_FST_project)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Lucky-0ne_FST_project&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Lucky-0ne_FST_project)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Lucky-0ne_FST_project&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=Lucky-0ne_FST_project)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Lucky-0ne_FST_project&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Lucky-0ne_FST_project)

## 5. Clean Code Development
For this project I tried to follow the Style Guide (PEP 8) for Python Code, written by Guido van Rossum, Barry Warsaw and Nick Coghlan.

### A)
  - [Indentation:](https://github.com/Lucky-0ne/FST_project/blob/main/python/main/brickbreaker_main.py#L9-11) Use either 4 spaces per indentation level or 1 tab BUT be consistent with whatever you choose. I prefer tabs even if spaces is the official recommended style.
  - [Documentation Strings:](https://github.com/Lucky-0ne/FST_project/blob/main/python/main/imports/brickbreaker_methods.py#L7) (a.k.a. "docstrings") For describing functions inlcuding their in- and outputs.
  - [Self explanatory variable names:](https://github.com/Lucky-0ne/FST_project/blob/main/python/main/imports/brickbreaker_classes.py#L7) The variable name itself helps in understanding the code.
  - [Constants:](https://github.com/Lucky-0ne/FST_project/blob/main/python/main/imports/brickbreaker_init.py#L9) All constants are written in capital letters with underscores seperating words.
  - [D.R.Y.:](https://github.com/Lucky-0ne/FST_project/blob/main/python/main/imports/brickbreaker_classes.py#L30) Try to keep your code "dry" (Don't Repeat Yourself!).

### B)

## 6. Build Management
TBD

## 7. Unit-Tests
TBD

## 8. Continuous Delivery
TBD

## 9. IDE

I use **Visual Studio Code** as my IDE. It was the first IDE I got introduced to and since then there was never a big enough reason to switch to another IDE. I like the look and feel to it and especially it's easy to use interactive window. Plus it has a lot of useful preinstalled features and installing new ones isn't that hard either. Debugging is easy too!

#### *personal shortcuts*:

- ```numpad /``` &rarr; open new interactive window

#### *regular shortcuts*:

- ```shift + enter```               &rarr; run line in interactive window (has to be enabled in settings first)
- ```alt + left mouse button```     &rarr; multi cursor selection
- ```shift + alt + up/down```       &rarr; duplicate line or block of code
- ```alt + up/down```               &rarr; move line or block of code up and down
- ```f3``` or ```strg + f```        &rarr; search in code + option to replace by text
- ```strg + z```                    &rarr; undo
- ```strg + y```                    &rarr; redo

## 10. DSL
TBD

## 11. Functional Programming
TBD
