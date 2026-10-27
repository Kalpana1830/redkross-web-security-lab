\# RedKross Web Security Lab — Test Results



\*\*Date:\*\* 27 October 2026



\## Test run 1: Homepage and SQL injection prevention



\*\*Command:\*\* `python -m pytest -v`



\*\*Result:\*\* 4 tests passed, 0 failed.



\### Tests executed

1\. `test\_home\_page\_returns\_success` — homepage returns HTTP 200 and the expected heading.

2\. `test\_existing\_user\_is\_found` — existing user is found.

3\. `test\_unknown\_user\_is\_not\_found` — unknown user returns no results.

4\. `test\_sql\_injection\_input\_does\_not\_return\_all\_users` — SQL injection test input is treated as data.



\*\*Remediation implemented:\*\* Parameterized SQL query using a `?` placeholder.



\*\*Limitations:\*\* These are initial local regression tests. They do not establish that the entire application is secure.





