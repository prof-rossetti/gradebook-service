
import os
from dotenv import load_dotenv

from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText
import base64

load_dotenv()

MY_EMAIL_ADDRESS = os.getenv("MY_EMAIL_ADDRESS")
CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "credentials.json")
AUTH_SCOPE = ["https://www.googleapis.com/auth/gmail.send"] # Send messages only. No read or modify privileges on mailbox.

print("------------------------")
print("READING CREDENTIALS...")
print(os.path.isfile(CREDENTIALS_FILEPATH))
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
#print(type(credentials), credentials) #> <class 'oauth2client.service_account.ServiceAccountCredentials'>

print("------------------------")
print("INITIALIZING THE API CLIENT...")
client = build("gmail", "v1", credentials=credentials)
#delegated_credentials = credentials.with_subject(MY_EMAIL_ADDRESS)
#client = build("gmail", "v1", credentials=delegated_credentials)
print(type(client)) #> <class 'googleapiclient.discovery.Resource'>
print(type(client.users())) #> <googleapiclient.discovery.Resource object at ____>
print(type(client.users().messages())) #> <googleapiclient.discovery.Resource object at ____>

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
    message_request = client.users().messages().send(userId="me", body=encoded_message)
    print("REQUEST", type(message_request)) #> <class 'googleapiclient.http.HttpRequest'>
    message_response = message_request.execute() #> googleapiclient.errors.HttpError: <HttpError 400 when requesting https://www.googleapis.com/gmail/v1/users/me/messages/send?alt=json returned "Invalid value for ByteString: Content-Type: text/plain; charset="us-ascii"
    print("RESPONSE:", type(message_response)) #> __________
except:
    print("OOPS, SOMETHING WENT WRONG")
