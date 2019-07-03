# Professor Rossetti's Gradebook Service (Python)

## Prerequisites

  + Git
  + Anaconda, Python 3.7, Pip

## Setup

Obtain credentials for Google Sheets API and GMail API, and store the file in this repository as "auth/credentials.json".

Setup a virtual environment:

```sh
conda create -n gradebook-env python=3.7
conda activate gradebook-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

```sh
python notification_service.py
```
