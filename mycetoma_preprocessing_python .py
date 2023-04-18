'''
This file does the following:
1. Transformed all the numerical values to original text (for categorical variables that were coded previously in the form of numbers) for clarity.
2. Remove missed value (coded as 999).
3. Separate cured patients data into a different excel file.
'''

import pandas as pd
import numpy as np

# read the excel sheet:
df = pd.read_excel("C:\\Users\\khans\\OneDrive\\Desktop\\python_work\\Data\\raw_data.xlsx")

# Transform all the categorical variables from numerical to text again for clarity:
df['sex'].replace({1: 'male', 2: 'female'}, inplace=True)
df['occupation'].replace({0: 'house wife', 1: 'worker', 2: 'farmer', 3: 'clark', 4: 'jobless', 5: 'others', 6: 'student', 7: 'employee'}, inplace=True)
df['family_hx'].replace({1:'yes', 2: 'no'}, inplace=True)
df['concomittent_dx'].replace({1: 'none', 2: 'hypertension', 3: 'asthma', 4: 'diabetes', 5: 'diabetes and hypertension',
                               6: 'sickle cell aneamia', 7: 'others'}, inplace=True)
df['site'].replace({1: 'left foot', 2: 'right foot', 3: 'left big toe', 4: 'right big toe', 5: 'left other toes', 6: 'right other toes',
                    7: 'right foot', 8: 'left ankle', 9: 'right leg and knee',
                    10: 'left leg and knee', 11: 'right thigh', 12: 'left thigh', 13: 'right buttock', 14: 'left buttock', 15: 'right axilla',
                    16: 'left axilla', 17: 'right arm and forearm', 18: 'left arm and forearm',
                    19: 'right ahnd', 20: 'left hand', 21: 'chest wall', 22: 'head and neck', 23: 'back', 24: 'abdominal wall', 25: 'perineum', 26: 999,
                    27: 'others', 28: 'multiple', 29: 'both feet', 30: 'right shoulder', 31: 'left shoulder'}, inplace=True)
df['size_1st_presenation'].replace({1: 'less than 5', 2: 'from 5 to 10', 3: 'more than 10', 4: 'operated'}, inplace=True)
df['organism'].replace({0: 'no organism', 1: 'MM', 2: 'SS', 3: 'AM', 4: 'AP', 5: 'N', 6: 'ES', 7: 'MF', 8: 'SP'}, inplace=True)
df['x_ray'].replace({2: 'soft tissue swelling', 3: 'bone destruction', 4: 'combination', 5: 'normal', 6: 'perioseal reaction'}, inplace=True)
df['us_1st_presentation'].replace({1: 'EM', 2: 'AM', 3: 'no grains', 4: 'non specific', 5: 'normal'}, inplace=True)
df['sinuses_1st_presentation'].replace({1: 'none', 2: 'active', 3: 'healed', 4: 'both', 5: 'operated'}, inplace=True)
df['surgery_pre_tx'].replace({0: 'none', 1: 'once', 2: 'twice', 3: '3 times', 4: 'more'}, inplace=True)
df['type_tx'].replace({0: 'Itraconazole', 1: 'Ketoconazole', 2: 'Penicillin + Gresufution', 3: 'Streptomycin + Dapson', 4: 'Streptomycin + Septrin',
                       5: 'others', 6: 'Amikacin + Septrin', 7: 'no treatment', 8: 'Septrin', 10: 'Septrin + Dapson + Folic acid', 11: 'combined',
                       12: 'Dapson', 13: 'Amoclan + Septrin + Folic acid'}, inplace=True)
df['side_effects'].replace({1: 'ototoxicity', 2: 'renal toxicity', 3: 'GI symptoms', 4: 'No side effects', 5: 'others'}, inplace=True)
df['action_towards_side_effects'].replace({1: 'MM', 2: 'SS', 3: 'AM'}, inplace=True)
df['surgery_during_tx'].replace({1: 'yes', 2: 'no'}, inplace=True)
df['causes_surgery_during_tx'].replace({1: 'patient condition', 2: 'disease resistance', 3: 'drug side effects'}, inplace=True)
df['missed_followups'].replace({1: '0-1 times', 2: '2-4 times', 3: '>4 times'}, inplace=True)
df['regular_tx'].replace({1: 'yes', 2: 'no'}, inplace=True)
df['causes_irregular_tx'].replace({1: 'financial', 2: 'drug side effect', 3: 'busy work famiily etc', 4: 'other', 5: 'pregnancy'}, inplace=True)
df['us_now'].replace({1: 'no residual mycetoma', 2: 'residual mycetoma'}, inplace=True)
df['sinuses_now'].replace({1: 'none', 2: 'active', 3: 'healed', 4: 'both', 5: 'operated'}, inplace=True)
df['tx_status'].replace({1: 'cured', 2: 'continue on treatment', 3: 'drop out'}, inplace=True)

# Make an excel sheet of the new data form, and read the respective file:
df.to_excel("processed_999_data.xlsx", sheet_name='Sheet1')
df_processed_999 = pd.read_excel("processed_999_data.xlsx")

# Replace 999 with empty cells, make an excel file from it, then read the file:
df_processed_999 = df_processed_999.replace(999, np.nan)
df_processed_999.to_excel("processed_no999_data.xlsx", sheet_name='Sheet1')
df_processed_no999 = pd.read_excel("processed_no999_data.xlsx")

# Separate the cured patients into a different dataframe and make an excel file from it:
df_cured = df_processed_no999.loc[df.tx_status=='cured']
df_cured.to_excel("cured_data.xlsx", sheet_name='Sheet1')