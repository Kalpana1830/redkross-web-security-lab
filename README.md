\# RedKross Web Security Lab



\## Overview



A beginner-friendly, local web application security lab created for the RedKross Ethical Hacking \& Web Application Security assignment.



The project demonstrates security testing, remediation examples, and automated regression tests in a controlled environment.



\## Technologies



\- Python 3.14.3

\- Flask 3.1.3

\- Werkzeug 3.1.9

\- pytest 9.1.1

\- SQLite



\## Current Features



\- Flask homepage

\- In-memory SQLite user database

\- Parameterized SQL query example

\- XSS output-escaping test fixture

\- Password-hashing tests using Werkzeug

\- Access-control test fixture

\- Automated regression tests using pytest



\## Setup on Windows



1\. Install Python.

2\. Open Command Prompt in the project directory.

3\. Create a virtual environment:



&#x20;  `python -m venv .venv`



4\. Activate it:



&#x20;  `.venv\\Scripts\\activate`



5\. Install dependencies:



&#x20;  `python -m pip install Flask pytest`



6\. Run the tests:



&#x20;  `python -m pytest -v`



\## Run the Application



Activate the virtual environment and run:



`python app.py`



Open `http://127.0.0.1:5000` in your browser.



Keep the application bound to localhost during development.



\## Testing



The test suite covers the homepage, parameterized SQL queries, HTML output escaping, password hashing, and a demonstration of access-control decisions.



Record the actual test results in `evidence/test-results.md`.



\## Limitations



The current project is an educational prototype. The XSS and access-control checks use separate test applications, and the authentication tests verify password hashing rather than a complete login workflow.



These tests do not constitute a comprehensive security audit.



\## Safety



Use this lab only on your own machine. Do not test systems without explicit authorization.



\## Project Status



Initial automated tests have been reported passing. Further work is needed on integrated authentication, authorization, regression coverage, and submission evidence.



