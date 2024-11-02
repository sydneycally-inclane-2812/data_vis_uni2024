'''
Quick script to put all column names to a common standard
and add location column to the data.
'''

import pandas as pd

# Import the data
y2021 = pd.read_csv('raw_data/diem_thi_thpt_2021.csv')
y2022 = pd.read_csv('raw_data/diem_thi_thpt_2022.csv')
y2023 = pd.read_csv('raw_data/diem_thi_thpt_2023.csv')
y2024 = pd.read_csv('raw_data/diem_thi_thpt_2024.csv')

# Unifying the column names
y2021.columns = ['id', 'math', 'literature', '2nd_lang', 'physics', 'chem', 'bio', 'his', 'geo', 'civic', 'location']

y2022['location'] = y2022['sbd'].astype(str).apply(lambda x: x[:2] if len(x) == 8 else x[:1])
y2022.columns = ['id', 'math', 'literature', '2nd_lang', 'physics', 'chem', 'bio', 'his', 'geo', 'civic', 'location']

y2023['location'] = y2023['sbd'].astype(str).apply(lambda x: x[:2] if len(x) == 8 else x[:1])
y2023.columns = ['id', 'math', 'literature', '2nd_lang', 'physics', 'chem', 'bio', 'his', 'geo', 'civic', '2nd_lang_code','location']

y2024['location'] = y2024['sbd'].astype(str).apply(lambda x: x[:2] if len(x) == 8 else x[:1])
y2024.columns = ['id', 'math', 'literature', '2nd_lang', 'physics', 'chem', 'bio', 'his', 'geo', 'civic', '2nd_lang_code','location']

# Save the data
y2021.to_csv('cleaned_data/diem_thi_thpt_2021.csv', index=False)
y2022.to_csv('cleaned_data/diem_thi_thpt_2022.csv', index=False)
y2023.to_csv('cleaned_data/diem_thi_thpt_2023.csv', index=False)
y2024.to_csv('cleaned_data/diem_thi_thpt_2024.csv', index=False)