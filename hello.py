import requests
from requests.auth import HTTPBasicAuth

# GitHub API base URL
api_url = 'https://api.github.com'

# Your GitHub credentials
username = 'YOUR_USERNAME'
token = 'YOUR_TOKEN'

# Repository information
repo_owner = 'REPO_OWNER'
repo_name = 'REPO_NAME'

# New file information
new_file_path = 'NEW_FILE_PATH'
new_file_content = 'NEW_FILE_CONTENT'
commit_message = 'COMMIT_MESSAGE'

# API endpoint for creating a new file
endpoint = f'/repos/{repo_owner}/{repo_name}/contents/{new_file_path}'

# API URL
url = api_url + endpoint

# File content in base64 encoding
content_base64 = b64encode(new_file_content.encode()).decode('utf-8')

# Request payload
payload = {
    "message": commit_message,
    "content": content_base64
}

# Request headers
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Make the request to create a new file
response = requests.put(url, json=payload, headers=headers)

# Check the response
if response.status_code == 201:
    print(f"File '{new_file_path}' created successfully!")
else:
    print(f"Failed to create file. Status code: {response.status_code}")
    print(response.json())
