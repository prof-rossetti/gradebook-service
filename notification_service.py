
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
MY_ADDRESS = os.getenv("MY_ADDRESS")
#print(MY_ADDRESS, SENDGRID_API_KEY)

client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
print("CLIENT:", type(client))

print("------------------------")
print("ASSEMBLING MESSAGE CONTENTS...")
subject = "Grade Details - 'Shopping Cart' Project"
html_content = "<p>Hello, thanks for submitting your 'Shopping Cart' Project.</p>"
html_content += "<p>I've evaluated your submission, and the final score is <strong>91.09 / 100</strong>.<p>"
html_content += "<p>Please see details below for a score break-down by rubric category.</p>"
html_content += "<p>If you have any questions about your grade, please follow-up within the next few days.</p>"
html_content += "<p>Thanks, and see you in class!</p>"
html_content += "<p>- Prof Rossetti</p>"
message = Mail(from_email=MY_ADDRESS, to_emails=MY_ADDRESS, subject=subject, html_content=html_content)
print(type(message))
print(html_content)

try:
    print("------------------------")
    print("SENDING...")
    response = client.send(message)
    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
    print(response.status_code) #> 202 indicates SUCCESS
except Exception as e:
    print("OOPS, SOMETHING WENT WRONG...", e)
    print(response.body)
    print(response.headers)
