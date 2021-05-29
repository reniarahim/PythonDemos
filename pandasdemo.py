import pandas as pd
import openpyxl as pyxl

# Load the Excel data into Pandas Dataframe
dataframe = pd.read_excel("Sample.xlsx")
print(dataframe)

dataframe2 = dataframe[['card_no','trans_code','currency_code','credit_amount']] \
                .groupby(['trans_code','currency_code']).sum(['credit_amount'])

dataframe3 = dataframe[['plas_no','trans_code','currency_code']] \
                .groupby(['card_code','currency_code']).nunique('card_no')

print(dataframe2)
print(dataframe3)

resultdf = pd.concat([dataframe3,dataframe2],axis=1)
print(resultdf)
resultdf.to_csv('result.csv')