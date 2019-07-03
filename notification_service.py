
# adapted from: https://github.com/s2t2/wip-gmail-py/blob/master/list_messages.py

import os

from googleapiclient.discovery import build
from oauth2client import file, client, tools

print("INITIALIZING THE API CLIENT...")

credentials_filepath = os.path.join(os.path.dirname(__file__), "auth", "credentials.json")
print(os.path.isfile(credentials_filepath))

credentials_filestore = file.Storage(credentials_filepath)
credentials = credentials_filestore.get() #> KeyError: '_module'
print(type(credentials), credentials)

service = build("gmail", "v1", credentials=creds)
print(type(service))

breakpoint()








#print("SENDING AN EMAIL HERE....")
