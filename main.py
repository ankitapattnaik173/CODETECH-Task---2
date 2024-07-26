import requests
import subprocess

# Function to perform SQL Injection
def sql_injection(url, param, payload):
    test_url = f"{url}?{param}={payload}"
    response = requests.get(test_url)
    
    if "syntax error" in response.text or "mysql" in response.text or "sql" in response.text:
        print(f"SQL Injection vulnerability found at {test_url}")
    else:
        print(f"No SQL Injection vulnerability found at {test_url}")

# Function to perform XSS
def xss(url, param, payload):
    test_url = f"{url}?{param}={payload}"
    response = requests.get(test_url)
    if payload in response.text:
        print(f"XSS vulnerability found at {test_url}")
    else:
        print(f"No XSS vulnerability found at {test_url}")

# Function to check for insecure authentication mechanism
def insecure_auth(url, username_param, password_param, username, password):
    login_data = {username_param: username, password_param: password}
    response = requests.post(url, data=login_data)
    if "invalid credentials" not in response.text.lower():
        print("Insecure authentication mechanism found")
    else:
        print("No insecure authentication mechanism found")

# Function to start mitmproxy
def start_mitmproxy():
    subprocess.run(["mitmproxy", "-p", "8080"])

# Main function
def main():
    url = input("Enter the website URL: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    print("Starting MITMProxy...")
    start_mitmproxy()
    
    print("Testing for SQL Injection...")
    sql_injection(url, "param", "payload")  # Replace "param" and "payload" with actual test parameters

    print("Testing for XSS...")
    xss(url, "param", "payload")  # Replace "param" and "payload" with actual test parameters

    print("Testing for insecure authentication mechanism...")
    insecure_auth(url, username, password)

if __name__ == "__main__":
    main()
