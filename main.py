# Pandas: How to efficiently Read a Large CSV File 

import pandas as pd


file_name = 'example.csv'

rows_per_chunk = 5

with pd.read_csv(
        file_name,
        chunksize=rows_per_chunk
) as csv_reader:
    for chunk in csv_reader:
        print(chunk)
        print('-' * 50)
