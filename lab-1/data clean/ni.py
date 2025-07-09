import pandas as pd

df = pd.read_csv("lab1-datasets/employee_data.csv")
print("Initial Data:\n", df.head())

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

df['Department'] = df['Department'].str.lower()
df['Department'] = df['Department'].replace({
    'human resources': 'hr',
    'h.r.': 'hr',
    'hr': 'hr',
    'finance': 'finance',
    'it': 'it'
})

df = df.drop_duplicates(subset='ID', keep='first')
df.to_csv("lab1-datasets/cleaned_employee_data.csv", index=False)
print("✅ Cleaned data saved to 'cleaned_employee_data.csv'")
