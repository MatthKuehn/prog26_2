# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 23:05:08 2026

@author: kuehnbam
"""

import pandas as pd

dt={'name':['Martin','Maren', 'Ahmed','Lauren', 'Rebekka','Sören', 'Wilhelm','Lotte'],
    'alter':[9,33,54,66,98,14,34,56],
    'stadt':['Immenstadt', 'Waltenhofen','Bühl','Waltenhofen','Bühl','Waltenhofen','Immenstadt','Bühl'],
    'note':[1.3,2.7,2,2.3,5,4,3,2]}

students=pd.DataFrame(dt)
print(type(students),students.columns, students)


student_stats=students.groupby("stadt")['alter'].agg(['min','mean','max'])


student_stats2.reset_index(inplace=True)
student_stats=students.groupby("stadt").agg({'alter':['min','mean','max'],'note':['min','mean','max']})
student_stats.columns = ['_'.join(col).strip() for col in student_stats.columns.values]
student_stats.reset_index(inplace=True)



df_sliced=df.iloc[1:3,1:2]


dt={'name':['Martin','Maren', 'Ahmed']}
df=pd.DataFrame(dt)
print(type(df),df.columns, df)

type(df)

