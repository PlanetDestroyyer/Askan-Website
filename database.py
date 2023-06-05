import pandas as pd

# def append(appendind_data):
#     df1 = pd.DataFrame(appendind_data)
#     print(df1)
#     df1.to_csv('new1.csv', mode='a', index=False, header=False)
#     print(df1)
    
# append({"Name": ["Pranav"],"Password":["pranav@359"]})
df = pd.read_csv('new1.csv')
for name,password in df:
    print(name,password)