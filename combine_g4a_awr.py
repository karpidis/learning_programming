import pandas as pd

# Read in the first Excel file
df1 = pd.read_excel("awr_rankings_0502.xlsx")

# Read in the second Excel file
df2 = pd.read_excel("Landing_Pages_050223_combox.xlsx")

# Strip the common part of the URL in the first Excel file and only keep the relative URL
df1["URL"] = df1["URL"].str.replace("https://www.combox-networks.com", "")
# Strip the trailing '/'
df1['URL'] = df1['URL'].str.rstrip('/')

# Rename the "URL" column in the second Excel file to match the "Landing page" column in the first Excel file
df1 = df1.rename(columns={"URL": "Landing page"})

# Merge the two DataFrames based on the "Landing page" column
result = pd.merge(df1, df2, on="Landing page", how="outer")

# Write the combined DataFrame to a new Excel file
result.to_excel("combined_file.xlsx", index=False)
