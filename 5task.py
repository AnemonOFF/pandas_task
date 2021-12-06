import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


works = pd.read_csv('works.csv')
python_salary = works.skills.dropna().str.lower().str.contains('python|питон')
print(f"Python skill salary: \n{works[works.skills.notna()][python_salary].salary}")
