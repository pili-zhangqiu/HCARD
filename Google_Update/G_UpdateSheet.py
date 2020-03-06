# Import Google Sheets API libraries
from __future__ import print_function  
from googleapiclient.discovery import build  
from httplib2 import Http  
# from oauth2client import file, client, tools  
from oauth2client.service_account import ServiceAccountCredentials  
import datetime

import gspread

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def update_sheet(sheetname, AccX, AccY, AccZ, GyroX, GyroY, GyroZ):  
    """update_sheet method:
       appends a row of a sheet in the spreadsheet with the 
       the latest temperature, pressure and humidity sensor data
    """
    
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    secret_file = os.path.join(os.getcwd(), 'client_secret.json')
    creds = ServiceAccountCredentials.from_json_keyfile_name(secret_file, scopes=SCOPES)
    
    #gc = gspread.authorize(creds)

    # My Spreadsheet ID ... See google documentation on how to derive this
    MY_SPREADSHEET_ID = '1t6TAtEzQJR_f0QxkzZNffVh7axkTvgVT0Zb-uqnPLko'
    
    service = build('sheets', 'v4', http=creds.authorize(Http()))
    # service = build('sheets', 'v4', credentials=creds)
    
    # Call the Sheets API, append the next row of sensor data
    # values is the array of rows we are updating, its a single row
    values = [ [ str(datetime.datetime.now()), 
        AccX, AccY, AccZ, GyroX, GyroY, GyroZ ] ]
    body = { 'values': values }
    
    # call the append API to perform the operation
    result = service.spreadsheets().values().append(
                spreadsheetId=MY_SPREADSHEET_ID, 
                range=sheetname + '!A1:G1',
                valueInputOption='USER_ENTERED', body=body).execute()            