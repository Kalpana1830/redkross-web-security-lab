# RedKross Web Security Lab

## Overview

A beginner-friendly, local web application security lab created for the RedKross Ethical Hacking & Web Application Security assignment.

The project demonstrates security testing, remediation examples, and automated regression tests in a controlled environment.

## Technologies

- Python 3.14.3
- Flask 3.1.3
- Werkzeug 3.1.9
- pytest 9.1.1
- SQLite

## Current Features

- Flask homepage
- In-memory SQLite user database
- Parameterized SQL query example
- XSS output-escaping test fixture
- Password-hashing tests using Werkzeug
- Access-control test fixture
- Automated regression tests using pytest

## Setup on Windows

1. Install Python.
2. Open Command Prompt in the project directory.
3. Create a virtual environment:

   ```bat
   python -m venv .venv
   ```

4. Activate the virtual environment:

   ```bat
   .venv\Scripts\activate
   ```

5. Install the project dependencies:

   ```bat
   python -m pip install -r requirements.txt
   ```

6. Run the automated tests:

   ```bat
   python -m pytest -v
   ```

## Run the Application

Activate the virtual environment and run:

```bat
python app.py
```

Open this address in your browser:

http://127.0.0.1:5000

Keep the application bound to localhost during development.

## Testing

The test suite covers:

- Homepage response
- Parameterized SQL query behavior
- HTML output escaping
- Password hashing and verification
- Demonstration access-control decisions

Run the tests with `python -m pytest -v`.

Record the actual test command, date, results, and any failures in `evidence/test-results.md`. Only report results that you have verified by running the tests.

## Limitations

This project is an educational prototype, not a production-ready application.

- The XSS and access-control checks use separate test applications.
- The authentication tests verify password hashing rather than a complete login workflow.
- The tests cover selected scenarios and do not establish that the entire application is secure.
- Additional integration tests, authorization checks, and security validation are needed before considering the application suitable for real users.

## Safety

Use this lab only on your own machine or in an environment for which you have explicit authorization. Do not test systems without permission.

## Project Status

The initial automated test suite has been reported passing locally. Further work is needed on integrated authentication, authorization, expanded regression coverage, and submission evidence.
