
import os

print("Current Working directory:", os.getcwd())

# data_path = "sales-analysis/data/sales.csv"
# data_path = "../ai_ml_python_classes/sales-analysis/data/sales.csv"
# if os.path.exists(data_path):
#     print(f"✅ Found {data_path}")
# else :
#     print(f"❌ Cannot find {data_path}")
#     print("Make sure you're running from the sales-analysis folder!")


with open("sales-analysis/data/sales.csv", "r") as file:
    content = file.read()
    print(content)



