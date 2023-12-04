import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

dict={}
for n in data['whoAmI']: 
    if n not in dict:
        dict.update({n : len(dict)})

columns=['#']        
columns+=list(dict.keys())
values=[]
for i in data['whoAmI']:
    temp=[dict[i]]
    for n in range(len(columns)-1):
        if i==columns[n+1]:
            temp.append(1)
        else:
            temp.append(0)
    
    values.append(temp)

data_new=pd.DataFrame(values, columns=columns)