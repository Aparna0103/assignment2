import numpy as np
import pandas as pd
Test_set = pd.read_csv(r"C:\Users\Ankita Sriwastawa\Desktop\Java\Python\Test_set.csv")
print(Test_set.head())


inds1 = list(set(np.random.randint(0, len(Test_set), 10)))
inds2 = list(set(np.random.randint(0, len(Test_set), 15)))
Test_set['Airline'] = [val if i not in inds1 else np.nan for i, val in enumerate(Test_set['Airline'])]
Test_set['Source'] = [val if i not in inds2 else np.nan for i, val in enumerate(Test_set['Source'])]
print(Test_set.isnull().sum())

from missingpy import MissForest
imputer = MissForest()
X = Test_set.drop('Duration', axis = 1)
X_imputed = imputer.fit_tranform(X)

Test_set1['MF Airline'] = X_imputed[:, 0]
Test_set1['MF Source'] = X_imputed[:, -1]
comparison_df['ABS Error Airline'] = np.abs(comaprison_df['Airline'] - comparison_df['MF Airline'])
comparison_df['ABS Error Source'] = np.abs(comaprison_df['Source'] - comparison_df['MF Source'])
comparison_df.iloc[sorted([*inds1, *inds2])]
