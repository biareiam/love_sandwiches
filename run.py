""" import Google API into Python """
import gspread
from google.oauth2.service_account import Credentials

""" set scope - it is the APIs the programm can access """
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)  
""" you are telling python what is the anme of the file you want to access """
SHEET = GSPREAD_CLIENT.open('love_sandwiches') 

""" access the data in the sheet
## this code was only used to check if the program was working
#sales = SHEET.worksheet('sales')  ## name of the tab you want to access
#data = sales.get_all_values()
#print(data)
"""

""" 
Start of the code 
"""

def get_sales_data():
   """
    Get sales figures input from the user
   """
   print("Please enter sales data from the last market.")
   print("Data should be six numbers, separated by comma.")
   print("Example: 10,20,30,40,50,60\n")

   data_str = input("Enter your data here: ")
   print(f"The data provided is {data_str}")

get_sales_data()


 

