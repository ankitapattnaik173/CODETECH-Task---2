Name: ANKITA PATTNAIK Company: CODETECH IT SOLUTIONS ID: CT8CSEH1196 Domain: "CYBER SECURITY&ETHICAL HACKING" Duration: JUNE 20th to AUGUST 20th,2024. Mentor:

Web Application Penetration Testing Tool

Overview

This script is designed to perform basic penetration testing on web applications to identify common security vulnerabilities such as SQL Injection, Cross-Site Scripting (XSS), and insecure authentication mechanisms. Additionally, it includes a function to start mitmproxy for man-in-the-middle attacks.

Features

SQL Injection Detection: Tests for SQL injection vulnerabilities by injecting payloads into URL parameters.
XSS Detection: Tests for Cross-Site Scripting vulnerabilities by injecting payloads into URL parameters.
Insecure Authentication Detection: Tests for weak or insecure authentication mechanisms.
MITMProxy Integration: Starts mitmproxy to capture and inspect HTTP traffic.
Prerequisites
Python 3.x
requests library
mitmproxy
Installing Dependencies
Use the following commands to install the necessary dependencies:

bash
Copy code
pip install requests
To install mitmproxy, follow the instructions on the official mitmproxy installation page.

Usage
Clone the Repository

Clone the repository to your local machine.

bash
Copy code
git clone https://github.com/yourusername/web-app-pen-test.git
cd web-app-pen-test
Update the Script

Update the script with actual test parameters for SQL Injection and XSS testing:

python
Copy code
# Replace "param" and "payload" with actual test parameters
sql_injection(url, "param", "payload")
xss(url, "param", "payload")
Run the Script

Execute the script using Python:

bash
Copy code
python web_app_pen_test.py
Follow the Prompts

Enter the website URL.
Enter the username and password for authentication testing.
The script will start mitmproxy and test for SQL Injection, XSS, and insecure authentication mechanisms.
Example
Here’s an example of running the script:

bash
Copy code
python web_app_pen_test.py
rust
Copy code
Enter the website URL: http://example.com
Enter the username: admin
Enter the password: admin

Starting MITMProxy...
Testing for SQL Injection...
No SQL Injection vulnerability found at http://example.com?param=payload
Testing for XSS...
No XSS vulnerability found at http://example.com?param=payload
Testing for insecure authentication mechanism...
Insecure authentication mechanism found
Functions
sql_injection(url, param, payload)
Performs SQL Injection testing on the given URL with the specified parameter and payload.

Parameters:
url (str): The target URL.
param (str): The parameter to test.
payload (str): The SQL Injection payload.
xss(url, param, payload)
Performs XSS testing on the given URL with the specified parameter and payload.

Parameters:
url (str): The target URL.
param (str): The parameter to test.
payload (str): The XSS payload.
insecure_auth(url, username_param, password_param, username, password)
Tests for insecure authentication mechanisms by attempting to log in with the provided credentials.

Parameters:
url (str): The login URL.
username_param (str): The username parameter name.
password_param (str): The password parameter name.
username (str): The username.
password (str): The password.
start_mitmproxy()
Starts mitmproxy on port 8080 to capture and inspect HTTP traffic.

Disclaimer
This tool is intended for educational purposes and authorized testing only. Unauthorized testing of web applications without proper consent is illegal and unethical.
