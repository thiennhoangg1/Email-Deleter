# Gmail Bulk Email Deleter

<div align="center">

![Gmail Logo](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

I got really annoyed with over 40,000 emails and ran out of storage on Google and didn't want to pay for premium, so this python script helps delete emails in bulk.
</div>

## ✨ Features

- 📑 Delete emails from specific pages
- 📊 Real-time progress tracking
- ⚡ Deletes around 2 emails per second

## 🚀 Setup

Get Gmail API credentials:
  ```bash
  # Go on Google Cloud Console OAUth Consent and download the credentials file and rename it to 
  client-secret.json

Install requirements:
bashCopypip install google-auth-oauthlib google-api-python-client google-auth-httplib2

Run the script:
pythonCopyquery_string = ""  # Empty for all emails, add a keyword to delete by search
emails = search_emails(query_string, start_page=2, end_page=4) # Change start_page and end_page to pages of your inbox you want gone
delete_emails(emails)


🔑 Authentication
First-time use requires browser OAuth2 authentication.
