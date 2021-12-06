import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


works = pd.read_csv('works.csv')
total = len(works.index)
print(f"Total count: {total}")
men_count = works[works['gender'] == 'Мужской'].shape[0]
print(f"Men count: {men_count}")
women_count = works[works['gender'] == 'Женский'].shape[0]
print(f"Women count: {women_count}")