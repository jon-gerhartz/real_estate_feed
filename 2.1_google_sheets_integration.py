import pandas as pd
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Create a new project and service account on Google API backend.
creds = ServiceAccountCredentials.from_json_keyfile_name('auth/fieyo_gsuite_service.json', scope)

gsheets = gspread.authorize(creds)

# Need to use the API console and activate Google Sheets API and Google Drive API.
# You must give the service key email permissions via Spreadsheet Share.
wb = gsheets.open_by_url('https://docs.google.com/spreadsheets/d/1UPx6fJCqY2KYXf3_S_QKe-RBLD0zuzOZTAgekRA_mxo/edit?usp=sharing&fbclid=IwAR3BJRJFBVZLz_MViROz5L4hj3Fe1bG-U-WekIisEECZuSqV-nLSlkQMX_Y')
ws = wb.get_worksheet(index=0)

df = get_as_dataframe(ws)
df = df.dropna(subset=['contact_email', 'agent_email']).dropna(axis='columns', how='all') 

import ipdb; ipdb.set_trace()
