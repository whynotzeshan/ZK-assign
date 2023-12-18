import re
import requests

pattern = r'\b\d{3}-\d{2}-\d{4}\b'  # Example: Social Security Number pattern
text = "John's SSN is 123-45-6789."
match = re.search(pattern, text)

if match:
    print("SSN found:", match.group())
else:
    print("SSN not found.")
url = 'https://api.example.com/data'
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Convert JSON response to Python data structure
    print("API Data:", data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
api_key = 'your_api_key'
headers = {'Authorization': f'Bearer {api_key}'}
response = requests.get(url, headers=headers)
# Example: Extract email addresses from an API response
api_url = 'https://api.example.com/users'
response = requests.get(api_url)

if response.status_code == 200:
    user_data = response.json()
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', str(user_data))
    print("Emails:", emails)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
