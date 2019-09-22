import pandas as pd
data = pd.read_excel('EpiData_3_row.xls','EpiData文件 1李晓晔',index_col=0)
data.to_csv('EpiData_3_row.csv',encoding='utf-8')