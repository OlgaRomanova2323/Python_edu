# Задача: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1
# столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as mpl
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

data.loc[data['whoAmI'] == 'robot', 'robot'] = '1'
data.loc[data['whoAmI'] == 'human', 'robot'] = '0'
data.loc[data['whoAmI'] == 'robot', 'human'] = '0'
data.loc[data['whoAmI'] == 'human', 'human'] = '1'
data.drop('whoAmI', axis= 1 , inplace= True )
print(data)
