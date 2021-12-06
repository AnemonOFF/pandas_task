import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


works = pd.read_csv('works.csv')
not_nan_skills = works[works.skills.notna()]
not_nan_skills_count = not_nan_skills.skills.count()
print(f"Not null skills count: {not_nan_skills_count}")
print(f"Not null skills: \n{not_nan_skills}")