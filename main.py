import pandas as pd

EXCEL_FILE = "./data.xlsx"

def main():
  df = pd.read_excel(EXCEL_FILE)
  print(df)  

if __name__ == "__main__":
  main()