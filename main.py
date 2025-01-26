import time
from google_apis import create_service

# grab client-secret.json file from google cloud console, download client-secret.json file from OAuth consent screen 
CLIENT_FILE = 'client-secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']


gmail_service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)

# search for emails

def search_emails(query, start_page=1, end_page=1, labels=None, results_per_page=500):
    try:
        email_messages = []
        page_count = 1
        next_page_token = None

        # skips to start page
        while page_count < start_page:
            message_response = gmail_service.users().messages().list(
                userId='me',
                labelIds=labels,
                q=query,
                maxResults=results_per_page,
                pageToken=next_page_token
            ).execute()
            next_page_token = message_response.get('nextPageToken')
            if not next_page_token:
                print(f"Reached end of emails at page {page_count}")
                return []
            page_count += 1

        # collect emails from input pages
        while page_count <= end_page:
            message_response = gmail_service.users().messages().list(
                userId='me',
                labelIds=labels,
                q=query,
                maxResults=results_per_page,
                pageToken=next_page_token
            ).execute()
            
            messages = message_response.get('messages', [])
            if not messages:
                print(f"No more emails found at page {page_count}")
                break
                
            email_messages.extend(messages)
            print(f'Processing page {page_count}')
            
            next_page_token = message_response.get('nextPageToken')
            if not next_page_token:
                break
            page_count += 1
            time.sleep(0.5)
            
        return email_messages
    except Exception as e:
        print(f"Error: {e}")
        return []

def delete_emails(email_list, delay=0.1):
    try:
        total = len(email_list)
        for i, email in enumerate(email_list, 1):
            gmail_service.users().messages().trash(
                userId='me',
                id=email['id']
            ).execute()
            print(f"Deleted {i}/{total}: {email['id']}")
            time.sleep(delay)
    except Exception as e:
        print(f"Error deleting emails: {e}")

# how to use, change start_page and end_page to desired pages and run file in python
query_string = ""
emails = search_emails(query_string, start_page=2, end_psage=4) 
delete_emails(emails)