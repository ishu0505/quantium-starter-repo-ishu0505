import pandas
import glob

import pandas as pd

combinedDataList = []
for file in glob.glob('data/daily_sales_data_*.csv'):
    df = pd.read_csv(file)

    df = df.drop(df[df['product'] != 'pink morsel'].index)

    df['price'] = df['price'].str.replace('$', '')

    df['price'] = pd.to_numeric(df.price, errors='coerce')

    df['sales($)'] = df['price'] * df['quantity']

    df = df.drop(['quantity', 'price'], axis=1)

    combinedDataList.append(df)

finalData = pd.concat(combinedDataList)
finalData = finalData.drop('product', axis=1)
print(finalData)

finalData.to_csv('pink_morcel_data.csv', index=False)


# print(df)