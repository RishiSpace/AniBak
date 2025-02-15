import requests
import json

# Firebase Realtime Database URL
database_url = "https://anime-back-default-rtdb.firebaseio.com/users/creds.json"

# Your Firebase API key (from the credentials you provided earlier)
api_key = "AIzaSyCHaosG3iAmABaLPdtZpxk2thX8nmMEwCs"

# Login credentials to push
login_creds = {
    'email': 'anibak@rishi.com',
    'password': 'LinuxIsGod'
}

# Add the API key to the database URL for authentication
database_url_with_api_key = f"{database_url}?auth={api_key}"

# Make a PUT request to Firebase Realtime Database to store the login credentials
response = requests.put(database_url_with_api_key, json=login_creds)

# Check if the request was successful
if response.status_code == 200:
    print("Login credentials uploaded successfully!")
else:
    print(f"Failed to upload credentials: {response.status_code}, {response.text}")
