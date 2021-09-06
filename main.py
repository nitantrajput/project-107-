import csv 
import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv('copypath.csv')
student = df.loc[df['student_id'] == 'TRL_xsl']
print(student.groupby('level')['attempt'].mean())
fig = go.Figure(go.Bar(
    x = student.groupby('level')['attempt'].mean(),
    y = ['level1' , 'level2' , 'level3' , 'level4'],
    orientation = 'h'
))
fig.show()