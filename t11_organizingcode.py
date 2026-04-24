

# before this we learn code or project sturcture, that how can we well structure our project. 
# learn how to use python paths, using os module, and learn how do we get out currently working directory using os.getcwd() function. and check for a path that exist in the existing path or not.
# learn how to open .csv, .json, .xlsx file using pandas library, using these according function pandas.read_csv(), pandas.read_json(), pandas.read_xlsx() file.
# learn how to save pandas dataframe into different file extension, using these function, pd.to_csv(), pd.to_json(), pd.to_excel() 
# learn how to open file using with open("today_sales_report.json", "r") as f:
# all these topics are in sales-analysis folder. so first learn this then come here to read.


# here we learn how to organize code. and how to split code into reusable functions.
# first create a helper.py and there i created some function that i import in this program file as a module. instead of having all the function in one file i make it modular.

import pandas as pd
import os

from helper import calculate_total, format_currency

df = pd.read_csv("sales-analysis/data/sales.csv")
# os.getcwd()


# finding total and adding it to the database
# method 1 :
totals = []
for index, row in df.iterrows():
    total = calculate_total(row["quantity"], row["price"])
    totals.append(total)

df["total"] = totals

# method 2 :
# df["total"] = df["quantity"] * df["price"]



# Display with formated total
print("Sales Data : ")

for index, row in df.iterrows():
    print(f"{row["product"]} : {format_currency(row["total"])}")


# finding Grand total and displaying it.

grand_total = df["total"].sum()
print(f"Grand Total : {format_currency(grand_total)}")




