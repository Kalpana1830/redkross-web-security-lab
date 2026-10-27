\# Web Application Security Test Checklist



Project: RedKross Web Security Lab



\## 1. Basic application

\- \[x] Homepage returns HTTP 200.

\- \[x] Homepage contains the expected heading.



\## 2. SQL injection

\- \[ ] Demonstrate SQL injection against a deliberately vulnerable local test endpoint.

\- \[ ] Fix database queries using parameterized SQL.

\- \[ ] Verify malicious input cannot bypass the query's intended behavior.



\## 3. Cross-site scripting (XSS)

\- \[ ] Test how the application handles untrusted text.

\- \[ ] Escape untrusted content before rendering HTML.

\- \[ ] Verify script-like input is displayed as text, not executed.



\## 4. Authentication

\- \[ ] Verify passwords are not stored as plaintext.

\- \[ ] Test valid and invalid login attempts.

\- \[ ] Check that unauthenticated users cannot access protected routes.



\## 5. Access control

\- \[ ] Test that users cannot access another user's private records.

\- \[ ] Enforce authorization on the server.

\- \[ ] Add regression tests for denied access.



\## 6. Final verification

\- \[ ] Run the complete automated test suite.

\- \[ ] Record actual results and any failures.

\- \[ ] Document remediation and regression evidence.



Note: Only test this deliberately created local lab or systems for which explicit authorization has been provided. Checklist items remain incomplete until tested and evidenced.

