from dotenv import load_dotenv
import os
from pprint import pprint

import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

DOCUMENT_ID = os.getenv("GOOGLE_SHEET_ID")
print(DOCUMENT_ID)

#
# AUTHORIZATION
#

CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "auth", "credentials.json")

AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)

#
# READ SHEET VALUES
#

client = gspread.authorize(credentials) #> <class 'gspread.client.Client'>

doc = client.open_by_key(DOCUMENT_ID) #> <class 'gspread.models.Spreadsheet'>

print("-----------------")
print("SPREADSHEET:", doc.title)
print("-----------------")

sheet_name = "example-gradesheet" # input("Please input the name of the grading sheet: (e.g. 'example-gradesheet'):")
sheet = doc.worksheet(sheet_name) #> <class 'gspread.models.Worksheet'>

rows = sheet.get_all_records() #> <class 'list'>

for row in rows:
    pprint(row) #> <class 'dict'>
