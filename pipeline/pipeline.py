'''
A simple data pipeline that:
1: Download CSV data from the web
2: Transform and clean the data with pandas
3: Load it into PostgreSQL for querying
4: Process data in chunks to handle large files

'''
import pandas as pd
import sys # sys is a built-in Python module that gives access to system-related features.



print('arguments', sys.argv)

month = int(sys.argv[1]) #sys.argv[1] == First argument

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f"output_{month}.parquet")

print(f'hello pipeline, month={month}')