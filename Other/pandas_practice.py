import pandas as pd

data : dict[str, list] = { 'name': ['Rithesh', 'Deeksha', 'Ridhi'],
                'age': [30, 40, 9]}

df = pd.DataFrame(data)

print(df)

# print(df['name'])

print(df.to_dict(orient='records'))
