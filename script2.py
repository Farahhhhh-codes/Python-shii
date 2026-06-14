import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\HomePC\\Desktop\\Hospital.csv")
df_clean = df.dropna().reset_index(drop=True)
mapping = {1: "Male", 0: "Female"}
df_clean["Sex"] = df_clean["Sex"].map(mapping)


while True:
    column_head = input("Enter the column you want to see: ")
    if column_head in df_clean.columns:
        long = input("Do you want the full display? Yes/No: ").upper()
        if long != "YES":
         print(df_clean[column_head])
        elif long == "YES":
            print(df_clean[column_head].to_string())
        break
    else:
        print(

            f"Column not found.Here are the columns available: Age,Sex,Chest pain type,BP,Cholesterol,FBS over 120,EKG results,Max HR,Exercise angina,ST depression,Slope of ST,Number of vessels fluro,Thallium,Heart Disease")

while True:
    others = input("Do you want to see a another one? Yes/No: ").upper()
    if others == "YES":
        new = input("What column? ")
        if new in df_clean.columns:
            short = input("Do you want the full display? Yes/No: ").upper()
            if short == "NO":
              print(df_clean[new])
            else:
              print(df_clean[new].to_string())
        else:
            print(
                f"Column not found.Here are the columns available: Age,Sex,Chest pain type,BP,Cholesterol,FBS over 120,EKG results,Max HR,Exercise angina,ST depression,Slope of ST,Number of vessels fluro,Thallium,Heart Disease")
    else:
        print("Code exited!")
        break
