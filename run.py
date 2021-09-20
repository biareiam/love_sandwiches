# import Google API into Python
import gspread
from google.oauth2.service_account import Credentials

## set scope - it is the APIs the programm can access
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)  
SHEET = GSPREAD_CLIENT.open('love_sandwiches')  ## you are telling python what is the anme of the file you want to access 

## access the data in the sheet

sales = SHEET.worksheet('sales')  ## name of the tab you want to access


data = sales.get_all_values()

print(data)