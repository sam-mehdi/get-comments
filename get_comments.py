import os
import constant as constant
print("Importing Pandas, this may take a bit!")
import pandas as pd
print("Pandas Imported")

# Import the header file
header = pd.read_csv(constant.header, header=0, encoding='utf-8-sig')

# Import the data
print("Reading the data, this will take a while")
if constant.input_as_xlsx:
    df = pd.read_excel(constant.filename)
else:
    df = pd.read_csv(constant.filename, encoding='utf-8-sig')

# Extract only the relevant columns from df
keep_columns = header['Original_Header']

print("Deleting some columns. Here are the before and after shapes:")
print(df.shape)
df = df[keep_columns]
print(df.shape)

# Create the dictionary with the original_header as the keys and working_header as values
transform_columns = header['Working_Header']
rename_dict = {k:v for k,v in zip(keep_columns, transform_columns)}

# rename the dataframe's headers
#df.rename(columns=transform_columns, inplace=True)
df.columns = transform_columns

if not os.path.exists('output'):
    os.makedirs('output')

print("Outputting")

cwd = os.getcwd()
os.chdir('output')
if constant.output_as_xlsx:
    df.to_excel("output.xlsx", index=False)
else:
    df.to_csv("output.csv", index=False)
os.chdir(cwd)
print("Done!")