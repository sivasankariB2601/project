import pandas as pd
file_name = input("Enter file name")
json_file = {'name':["aparna", "pankaj", "sudhir", "Geeku"],'degree': ["MBA", "BCA", "M.Tech", "MBA"],'score':[90, 40, 80, 98]}
df = pd.DataFramef(file_name).to_excel("excel.xlsx")
print(df)
