import pandas as pd
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Create a new project and service account on Google API backend.
creds = ServiceAccountCredentials.from_json_keyfile_name('auth/real_estate_gsuite_service.json', scope)

gsheets = gspread.authorize(creds)

# Need to use the API console and activate Google Sheets API and Google Drive API.
# You must give the service key email permissions via Spreadsheet Share.
wb = gsheets.open_by_url('https://docs.google.com/spreadsheets/d/13yyclvjqYpFK_5PW0CPgZlCI4RtkkIGaKLfBLIrrXH4/')
ws = wb.get_worksheet(index=0)

df = get_as_dataframe(ws)
df = df.dropna(subset=['customer_email', 'agent_email']).dropna(axis='columns', how='all') 

