## Web Application Penetration Testing

## Introduction

This project is designed for performing basic web application penetration testing. It includes functionalities for detecting common vulnerabilities such as SQL Injection, Cross-Site Scripting (XSS), and insecure authentication mechanisms. The script also integrates `mitmproxy` to assist with Man-in-the-Middle (MITM) attacks.

## Prerequisites

Before running this script, ensure you have the following installed on your system:

- Python 3.x
- `requests` library
- `mitmproxy`

To install the `requests` library, use the following command:
```sh
pip install requests
```

To install `mitmproxy`, follow the instructions on the [official website](https://mitmproxy.org/).

## Installation

1. Clone the repository or download the script file.
2. Ensure all prerequisites are installed.
3. Place the script in your desired directory.

## Usage

### 1. Starting MITMProxy

`mitmproxy` is used to capture and analyze traffic. The script includes a function to start `mitmproxy` on port 8080.

### 2. Running the Script

Run the script using the following command:
```sh
python3 script_name.py
```

### 3. Input Parameters

The script will prompt for the following inputs:
- **Website URL**: The URL of the web application you want to test.
- **Username**: The username for authentication testing.
- **Password**: The password for authentication testing.

### 4. Testing for Vulnerabilities

The script performs the following tests:

#### a. SQL Injection

To test for SQL Injection vulnerabilities, the script appends a payload to a specified parameter in the URL and checks for error messages indicating a potential vulnerability.

#### b. Cross-Site Scripting (XSS)

The script tests for XSS vulnerabilities by injecting a payload into a specified parameter and checking if it is reflected in the response.

#### c. Insecure Authentication Mechanism

The script attempts to log in with the provided credentials and checks for messages indicating insecure authentication practices.

### 5. Example

Here is an example of how to use the script:

```sh
python3 script_name.py
```

When prompted, enter the following:
```
Enter the website URL: http://example.com
Enter the username: test_user
Enter the password: test_pass
```

Replace `script_name.py` with the actual name of your script file.

## Functions

### 1. `sql_injection(url, param, payload)`

- **Description**: Tests for SQL Injection vulnerabilities.
- **Parameters**:
  - `url`: The target URL.
  - `param`: The parameter to test.
  - `payload`: The SQL payload to inject.

### 2. `xss(url, param, payload)`

- **Description**: Tests for XSS vulnerabilities.
- **Parameters**:
  - `url`: The target URL.
  - `param`: The parameter to test.
  - `payload`: The XSS payload to inject.

### 3. `insecure_auth(url, username_param, password_param, username, password)`

- **Description**: Checks for insecure authentication mechanisms.
- **Parameters**:
  - `url`: The login URL.
  - `username_param`: The parameter name for the username.
  - `password_param`: The parameter name for the password.
  - `username`: The username to test.
  - `password`: The password to test.

### 4. `start_mitmproxy()`

- **Description**: Starts `mitmproxy` on port 8080.

### 5. `main()`

- **Description**: The main function that orchestrates the testing process.

## Notes

- **Ethical Considerations**: Ensure you have permission to test the target web application. Unauthorized testing is illegal and unethical.
- **Customization**: Modify the `param` and `payload` variables in the `sql_injection` and `xss` functions to suit your testing needs.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Disclaimer

This tool is intended for educational purposes and authorized testing only. Unauthorized testing of web applications without proper consent is illegal and unethical.
