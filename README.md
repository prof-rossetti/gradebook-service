# Professor Rossetti's Gradebook Service (Python)

## [System Objectives](/planning/system-objectives.pdf)

A system which reads gradebook data from Google Sheets, then distributes detailed grade reports to each student via email.

![](/planning/data-flow-diagram.jpg)

## Prerequisites

  + Git
  + Anaconda, Python 3.7, Pip

## Setup

Fork this repository, then clone to download it onto your local machine. Then navigate there from the command-line:

```sh
cd gradebook-service-py/
```

Setup a virtual environment:

```sh
conda create -n gradebook-env python=3.7
conda activate gradebook-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

Create a new file in this repository called ".env", where we will store secret credentials as environment variables so our program can access them.

### Sendgrid Setup

First, [sign up for a free Sendgrid account](https://signup.sendgrid.com/), then click the link in a confirmation email to verify your account. Then [create an API Key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions.

Then store the API Key value in the ".env" file as an environment variable called `SENDGRID_API_KEY`. Also set an environment variable called `MY_EMAIL_ADDRESS` to be the email address you just associated with your SendGrid account (e.g. "someone@example.com"):

   SENDGRID_API_KEY="abc123"
   MY_ADDRESS="someone@example.com"

### Google Sheets Setup

Navigate to your Google Sheets Gradebook, and observe its unique identifier from the URL. Then store that in the ".env" file as an environment variable called `GOOGLE_SHEET_ID`:

    GOOGLE_SHEET_ID="abc123"

Create a new project in the [Google Developer Console](https://console.developers.google.com). And enable its access to the Google Sheets API. Then generate new credentials for a service account, download the resulting credentials file, and store it in this repository as "auth/credentials.json".

Share your Google Sheets Gradebook file with the email address associated with your Google API service account (previous step). When you share, give your service account "editor" privileges. This will allow the service account to access the gradebook programmatically.





## Usage

Get information from the gradebook (optional sanity check):

```sh
python app/spreadsheet_service.py
```

Send example email (optional sanity check):

```sh
python app/notification_service.py
```

Perform the entire process:

```sh
python app/gradebook_service.py
```

## [License](/LICENSE.md)
