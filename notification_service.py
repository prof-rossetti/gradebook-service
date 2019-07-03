
import os

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "credentials.json")
AUTH_SCOPE = ["https://www.googleapis.com/auth/gmail.send"] # Send messages only. No read or modify privileges on mailbox.

print("------------------------")
print("READING CREDENTIALS...")
print(os.path.isfile(CREDENTIALS_FILEPATH))
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
print(type(credentials), credentials) #> <class 'oauth2client.service_account.ServiceAccountCredentials'>

print("------------------------")
print("INITIALIZING THE API CLIENT...")
client = build("gmail", "v1", credentials=credentials)
print(type(client)) #> <class 'googleapiclient.discovery.Resource'>

breakpoint()








#print("SENDING AN EMAIL HERE....")
