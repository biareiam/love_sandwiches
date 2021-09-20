""" import Google API into Python """
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated by commas. 
    The loop will repeatetly request data, until the entry is valid.
   """
   while True:
     print("Please enter sales data from the last market.")
     print("Data should be six numbers, separated by comma.")
     print("Example: 10,20,30,40,50,60\n")

     data_str = input("Enter your data here: ")
     """
      We use print statement just to check values in our code. After it is confirmed
      the statement can be deleted
      print(f"T he data provided is {data_str}")
     """
     """
     split() method returns the broken values as a list
     """
     sales_data = data_str.split(",")
     validate_data(sales_data)

     if  validate_data(sales_data):
        print("Data is valid!")
        break

   return sales_data   

"""
Function to validade the data
"""

def validate_data(values):
   """
   Inside the try, converts all string values into integers.
   raise ValueError if strings cannot be converted into int,
   or if there are not exactly 6 numbers.
   """
   
   try:
      [int(value) for value in values]
      if len(values) != 6:
         raise ValueError(
            f"Exactly 6 values required, you provided {len(values)}"
         )
   except ValueError as e:
      print(f"Invalid data {e}, plase try again.\n")
      return False

   return True

   """
   This two function do the same thing, so we will refactor it.
   refactoring is the restructuring of the code to improve its operation, without altering
   its functionality
   """
   """
   def update_sales_worksheet(data):
   """
   """
   Update sales worksheet, add new row with the list data provided.
   """
   """
   print("Updating sales wroksheet...\n")   
   sales_worksheet = SHEET.worksheet("sales")
   sales_worksheet.append_row(data)
   print("Sales worksheet updated successfuly.\n")


def update_surplus_worksheet(data):
   """
   """
   Update surplus worksheet, add new row with the list data provided.
   """
   """
   print("Updating sales wroksheet...\n")   
   surplus_worksheet = SHEET.worksheet("surplus")
   surplus_worksheet.append_row(data)
   print("Surplus worksheet updated successfuly.\n")
   """

def update_worksheet(data,worksheet):
   """
   Receives a list of integers to be inserted into a worksheet
   Update the relevant worksheet with the data provided.
   """
   print(f"Updating {worksheet} wroksheet...\n")   
   worksheet_to_update = SHEET.worksheet(worksheet)
   worksheet_to_update.append_row(data)
   print(f"{worksheet} worksheet updated successfully.\n")




def calculate_surplus_data(sales_row):
   """
   Compare sales with stock and calculate the surplus for each item type.

   The surplus is defined as the sales figure subtracted from the stock:
   - Positive surplus indicates waste
   - Negative surplus indicates extra made when stock was sold out.
   """
   print("Calcuting surplus data...\n") 
   stock = SHEET.worksheet("stock").get_all_values()
   stock_row = stock[-1]
   

   surplus_data = [] 
   """ 
   The zip code is used to iterate 2 lists at the same time
   """

   for stock, sales in zip(stock_row,sales_row):
      surplus = int(stock) - sales
      surplus_data.append(surplus)
   

   return surplus_data  

def get_last_5_entries_sales():
   """
   Collects collumns of data from sales worksheet, collecting
   the last 5 entries for each sandwich and returns the data 
   as a list of lists.
   """
   sales = SHEET.worksheet("sales")
   ##column = sales.col_values(3)
   ##print(column)

   columns = []
   for ind in range(1, 7):
     column = sales.col_values(ind)
     columns.append(column[-5:])

   return columns








def main():
   """
   Run all program functions
   """
   data = get_sales_data()
   sales_data = [int(num) for num in data]
   """
   update_sales_worksheet(sales_data)
   """
   update_worksheet(sales_data,"sales")
   new_surplus_data = calculate_surplus_data(sales_data)
   """
   update_surplus_worksheet(new_surplus_data)
   """
   update_worksheet(new_surplus_data, "surplus")

   


print("Welcome to Love Sandwiches Data Automation")
#main()


sales_columns = get_last_5_entries_sales()
   






 

