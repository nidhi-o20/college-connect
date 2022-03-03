import tabula
import pandas as pd
import os
tabula.read_pdf(r'cutoff_pdf.pdf', pages='all')
tabula.convert_into(r'cutoff_pdf.pdf', r'cutoff1.csv', pages='all',
                    output_format='csv', stream=False)

df = pd.read_csv("cutoff1.csv",encoding='cp1252')
df['Merit (Score)'] = df['Merit (Score)'].str.replace(
    r"^[^\\(]+", "", regex=True)
df['Merit (Score)'] = df['Merit (Score)'].str.replace(r"(", "", regex=True)
df['Merit (Score)'] = df['Merit (Score)'].str.replace(r")", "", regex=True)
df = df.drop(columns=df.columns[-3:])
df.to_excel("modified_cutoffs.xlsx", index=False)

data = pd.read_excel("modified_cutoffs.xlsx")
new = data.loc[data['Course Name'].str.contains("Computer", case=False)]
abc = pd.DataFrame(new)
abc['Merit (Score)'] = pd.to_numeric(abc['Merit (Score)'])
abc.dropna(subset=["Choice Code"], inplace=True)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("Computers.xlsx", index=False)


data = pd.read_excel("modified_cutoffs.xlsx")
new = data.loc[data['Course Name'].str.contains("Information", case=False)]
abc = pd.DataFrame(new)
abc['Merit (Score)'] = pd.to_numeric(abc['Merit (Score)'])
abc.dropna(subset=["Choice Code"], inplace=True)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("IT.xlsx", index=False)

data = pd.read_excel("modified_cutoffs.xlsx")
new = data.loc[data['Course Name'].str.contains("Civil", case=False)]
abc = pd.DataFrame(new)
abc['Merit (Score)'] = pd.to_numeric(abc['Merit (Score)'])
abc.dropna(subset=["Choice Code"], inplace=True)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("civil.xlsx", index=False)

data = pd.read_excel("modified_cutoffs.xlsx")
new = data.loc[data['Course Name'].str.contains(
    "Electronics and Telecommunication", case=False)]
abc = pd.DataFrame(new)
abc['Merit (Score)'] = pd.to_numeric(abc['Merit (Score)'])
abc.dropna(subset=["Choice Code"], inplace=True)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("EXTC.xlsx", index=False)

data = pd.read_excel("modified_cutoffs.xlsx")
new = data.loc[data['Course Name'].str.contains("Mechanical", case=False)]
abc = pd.DataFrame(new)
abc['Merit (Score)'] = pd.to_numeric(abc['Merit (Score)'])
abc.dropna(subset=["Choice Code"], inplace=True)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("Mech.xlsx", index=False)


writer = pd.ExcelWriter('Computers2.xlsx')
df = pd.read_excel('Computers.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()

writer = pd.ExcelWriter('IT2.xlsx')
df = pd.read_excel('IT.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()

writer = pd.ExcelWriter('civil2.xlsx')
df = pd.read_excel('civil.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()

writer = pd.ExcelWriter('EXTC2.xlsx')
df = pd.read_excel('EXTC.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()

writer = pd.ExcelWriter('Mech2.xlsx')
df = pd.read_excel('Mech.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()


data = pd.read_excel("Computers2.xlsx")
new = data.loc[data['Institute'].str.contains("Mumbai", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("ComputersMumbai.xlsx", index=False)

writer = pd.ExcelWriter('ComputersMumbai2.xlsx')
df = pd.read_excel('ComputersMumbai.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("ComputersMumbai.xlsx")

data = pd.read_excel("IT2.xlsx")
new = data.loc[data['Institute'].str.contains("Mumbai", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("ITMumbai.xlsx", index=False)

writer = pd.ExcelWriter('ITMumbai2.xlsx')
df = pd.read_excel('ITMumbai.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("ITMumbai.xlsx")

data = pd.read_excel("Mech2.xlsx")
new = data.loc[data['Institute'].str.contains("Mumbai", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("MechMumbai.xlsx", index=False)

writer = pd.ExcelWriter('Mech2Mumbai.xlsx')
df = pd.read_excel('MechMumbai.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("MechMumbai.xlsx")


data = pd.read_excel("EXTC2.xlsx")
new = data.loc[data['Institute'].str.contains("Mumbai")]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("EXTCMumbai.xlsx", index=False)

writer = pd.ExcelWriter('Extc2Mumbai.xlsx')
df = pd.read_excel('EXTCMumbai.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("EXTCMumbai.xlsx")


data = pd.read_excel("civil2.xlsx")
new = data.loc[data['Institute'].str.contains("Mumbai")]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("civilMumbai.xlsx", index=False)

writer = pd.ExcelWriter('civil2Mumbai.xlsx')
df = pd.read_excel('civilMumbai.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("civilMumbai.xlsx")


data = pd.read_excel("Computers2.xlsx")
new = data.loc[data['Institute'].str.contains("Pune", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("ComputersPune.xlsx", index=False)

writer = pd.ExcelWriter('ComputersPune2.xlsx')
df = pd.read_excel('ComputersPune.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("ComputersPune.xlsx")

data = pd.read_excel("IT2.xlsx")
new = data.loc[data['Institute'].str.contains("Pune", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("ITPune.xlsx", index=False)

writer = pd.ExcelWriter('ITPune2.xlsx')
df = pd.read_excel('ITPune.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("ITPune.xlsx")

data = pd.read_excel("Mech2.xlsx")
new = data.loc[data['Institute'].str.contains("Pune", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("MechPune.xlsx", index=False)

writer = pd.ExcelWriter('Mech2Pune.xlsx')
df = pd.read_excel('MechPune.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("MechPune.xlsx")


data = pd.read_excel("EXTC2.xlsx")
new = data.loc[data['Institute'].str.contains("Pune")]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("EXTCPune.xlsx", index=False)

writer = pd.ExcelWriter('Extc2Pune.xlsx')
df = pd.read_excel('EXTCPune.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("EXTCPune.xlsx")


data = pd.read_excel("civil2.xlsx")
new = data.loc[data['Institute'].str.contains("Pune")]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("civilPune.xlsx", index=False)

writer = pd.ExcelWriter('civil2Pune.xlsx')
df = pd.read_excel('civilPune.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("civilPune.xlsx")


data = pd.read_excel("Computers2.xlsx")
new = data.loc[data['Institute'].str.contains("Nagpur", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("ComputersNagpur.xlsx", index=False)

writer = pd.ExcelWriter('ComputersNagpur2.xlsx')
df = pd.read_excel('ComputersNagpur.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("ComputersNagpur.xlsx")

data = pd.read_excel("IT2.xlsx")
new = data.loc[data['Institute'].str.contains("Nagpur", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("ITNagpur.xlsx", index=False)

writer = pd.ExcelWriter('ITNagpur2.xlsx')
df = pd.read_excel('ITNagpur.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("ITNagpur.xlsx")

data = pd.read_excel("Mech2.xlsx")
new = data.loc[data['Institute'].str.contains("Nagpur", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("MechNagpur.xlsx", index=False)

writer = pd.ExcelWriter('Mech2Nagpur.xlsx')
df = pd.read_excel('MechNagpur.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("MechNagpur.xlsx")


data = pd.read_excel("EXTC2.xlsx")
new = data.loc[data['Institute'].str.contains("Nagpur")]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("EXTCNagpur.xlsx", index=False)

writer = pd.ExcelWriter('Extc2Nagpur.xlsx')
df = pd.read_excel('EXTCNagpur.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("EXTCNagpur.xlsx")


data = pd.read_excel("civil2.xlsx")
new = data.loc[data['Institute'].str.contains("Nagpur")]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("civilNagpur.xlsx", index=False)

writer = pd.ExcelWriter('civil2Nagpur.xlsx')
df = pd.read_excel('civilNagpur.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("civilNagpur.xlsx")

data = pd.read_excel("Computers2.xlsx")
new = data.loc[data['Institute'].str.contains("Nashik", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("ComputersNashik.xlsx", index=False)

writer = pd.ExcelWriter('ComputersNashik2.xlsx')
df = pd.read_excel('ComputersNashik.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("ComputersNashik.xlsx")

data = pd.read_excel("IT2.xlsx")
new = data.loc[data['Institute'].str.contains("Nashik", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("ITNashik.xlsx", index=False)

writer = pd.ExcelWriter('ITNashik2.xlsx')
df = pd.read_excel('ITNashik.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("ITNashik.xlsx")

data = pd.read_excel("Mech2.xlsx")
new = data.loc[data['Institute'].str.contains("Nashik", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("MechNashik.xlsx", index=False)

writer = pd.ExcelWriter('Mech2Nashik.xlsx')
df = pd.read_excel('MechNashik.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("MechNashik.xlsx")


data = pd.read_excel("EXTC2.xlsx")
new = data.loc[data['Institute'].str.contains("Nashik")]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("EXTCNashik.xlsx", index=False)

writer = pd.ExcelWriter('Extc2Nashik.xlsx')
df = pd.read_excel('EXTCNashik.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("EXTCNashik.xlsx")


data = pd.read_excel("civil2.xlsx")
new = data.loc[data['Institute'].str.contains("Nashik")]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("civilNashik.xlsx", index=False)

writer = pd.ExcelWriter('civil2Nashik.xlsx')
df = pd.read_excel('civilNashik.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("civilNashik.xlsx")

data = pd.read_excel("Computers2.xlsx")
new = data.loc[data['Institute'].str.contains("Aurangabad", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("ComputersAurangabad.xlsx", index=False)

writer = pd.ExcelWriter('ComputersAurangabad2.xlsx')
df = pd.read_excel('ComputersAurangabad.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("ComputersAurangabad.xlsx")

data = pd.read_excel("IT2.xlsx")
new = data.loc[data['Institute'].str.contains("Aurangabad", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("ITAurangabad.xlsx", index=False)

writer = pd.ExcelWriter('ITAurangabad2.xlsx')
df = pd.read_excel('ITAurangabad.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("ITAurangabad.xlsx")

data = pd.read_excel("Mech2.xlsx")
new = data.loc[data['Institute'].str.contains("Aurangabad", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("MechAurangabad.xlsx", index=False)

writer = pd.ExcelWriter('Mech2Aurangabad.xlsx')
df = pd.read_excel('MechAurangabad.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("MechAurangabad.xlsx")


data = pd.read_excel("EXTC2.xlsx")
new = data.loc[data['Institute'].str.contains("Aurangabad")]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("EXTCAurangabad.xlsx", index=False)

writer = pd.ExcelWriter('Extc2Aurangabad.xlsx')
df = pd.read_excel('EXTCAurangabad.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("EXTCAurangabad.xlsx")


data = pd.read_excel("civil2.xlsx")
new = data.loc[data['Institute'].str.contains("Aurangabad")]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("civilAurangabad.xlsx", index=False)

writer = pd.ExcelWriter('civil2Aurangabad.xlsx')
df = pd.read_excel('civilAurangabad.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("civilAurangabad.xlsx")

data = pd.read_excel("Computers2.xlsx")
new = data.loc[data['Institute'].str.contains("Amravati", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("ComputersAmravati.xlsx", index=False)

writer = pd.ExcelWriter('ComputersAmravati2.xlsx')
df = pd.read_excel('ComputersAmravati.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("ComputersAmravati.xlsx")

data = pd.read_excel("IT2.xlsx")
new = data.loc[data['Institute'].str.contains("Amravati", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("ITAmravati.xlsx", index=False)

writer = pd.ExcelWriter('ITAmravati2.xlsx')
df = pd.read_excel('ITAmravati.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("ITAmravati.xlsx")

data = pd.read_excel("Mech2.xlsx")
new = data.loc[data['Institute'].str.contains("Amravati", case=False)]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("MechAmravati.xlsx", index=False)

writer = pd.ExcelWriter('Mech2Amravati.xlsx')
df = pd.read_excel('MechAmravati.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("MechAmravati.xlsx")


data = pd.read_excel("EXTC2.xlsx")
new = data.loc[data['Institute'].str.contains("Amravati")]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("EXTCAmravati.xlsx", index=False)

writer = pd.ExcelWriter('Extc2Amravati.xlsx')
df = pd.read_excel('EXTCAmravati.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("EXTCAmravati.xlsx")


data = pd.read_excel("civil2.xlsx")
new = data.loc[data['Institute'].str.contains("Amravati")]
abc = pd.DataFrame(new)
abcd = abc.reset_index()
abc['Sr.No.'] = abcd.index + 1
abc.to_excel("civilAmravati.xlsx", index=False)

writer = pd.ExcelWriter('civil2Amravati.xlsx')
df = pd.read_excel('civilAmravati.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
writer.save()
os.remove("civilAmravati.xlsx")
os.remove("Computers.xlsx")
os.remove("IT.xlsx")
os.remove("civil.xlsx")
os.remove("EXTC.xlsx")
os.remove("Mech.xlsx")
