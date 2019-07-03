
import os
from dotenv import load_dotenv

import base64
from email.mime.text import MIMEText

#from oauth2client.service_account import ServiceAccountCredentials
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


load_dotenv()

MY_EMAIL_ADDRESS = os.getenv("MY_EMAIL_ADDRESS")
#CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "credentials.json")
CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "web_creds.json")
AUTH_SCOPES = [
    #"https://www.googleapis.com/auth/userinfo.email",
    #"https://www.googleapis.com/auth/userinfo.profile",
    "https://www.googleapis.com/auth/gmail.send" # Send messages only. No read or modify privileges on mailbox.
]

print("------------------------")
print("READING CREDENTIALS...")
print(os.path.isfile(CREDENTIALS_FILEPATH))
#credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPES)
#print(type(credentials), credentials) #> <class 'oauth2client.service_account.ServiceAccountCredentials'>









# create the credential the first time and save it in token.pickle
creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILEPATH, AUTH_SCOPES)
        creds = flow.run_local_server()
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

#create the service
service = build('gmail', 'v1', credentials=creds)







breakpoint()


print("------------------------")
print("INITIALIZING THE API CLIENT...")
#service = build("gmail", "v1", credentials=creds)
print(type(service)) #> <class 'googleapiclient.discovery.Resource'>
print(type(service.users())) #> <googleapiclient.discovery.Resource object at ____>
print(type(service.users().messages())) #> <googleapiclient.discovery.Resource object at ____>

#try:
#    print("------------------------")
#    print("GETTING MY PROFILE...")
#    profile_request = client.users().getProfile(userId="me")
#    profile_response = profile_request.execute() #> googleapiclient.errors.HttpError: <HttpError 403 when requesting https://www.googleapis.com/gmail/v1/users/me/profile?alt=json returned "Insufficient Permission">
#    #print("RESPONSE:", type(response))
#except HttpError as e:
#    print("OOPS, SOMETHING WENT WRONG", e)


print("------------------------")
print("INITIALIZING THE MESSAGE...")
message_text = "Grade Details Report\n\n\n..."
message = MIMEText(message_text)
message["to"] = MY_EMAIL_ADDRESS # TODO: student address
message["from"] = MY_EMAIL_ADDRESS
message["subject"] = "Grade Report - 'Shopping Cart' Project"
print(message.as_string())

try:
    print("------------------------")
    print("SENDING THE MESSAGE...")
    #encoded_message = {"raw": base64.urlsafe_b64encode(message.as_string())} #> TypeError: a bytes-like object is required, not 'str'
    #encoded_message = {"raw": message.as_string()}
    encoded_message = {"raw": base64.urlsafe_b64encode(message.as_string().encode()).decode()} # h/t: https://stackoverflow.com/a/45306759/670433
    message_request = service.users().messages().send(userId="me", body=encoded_message)
    print("REQUEST", type(message_request)) #> <class 'googleapiclient.http.HttpRequest'>
    message_response = message_request.execute() #> googleapiclient.errors.HttpError: <HttpError 400 when requesting https://www.googleapis.com/gmail/v1/users/me/messages/send?alt=json returned "Invalid value for ByteString: Content-Type: text/plain; charset="us-ascii"
    print("RESPONSE:", type(message_response)) #> __________
except HttpError as e:
    print("OOPS, SOMETHING WENT WRONG", e)
