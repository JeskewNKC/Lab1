import pandas as pd
# import lxml
url = 'https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015'
table = pd.read_html(url)
table = table[0]
# table[0].to_csv("testParse3.csv")
# f=pd.read_csv('testParse3.csv')
# below code defines the columns
col = ['Rank', 'Player', 'Team', 'Points', 'Games', 'Avg']
file = table[col]
file.to_csv('testParse3.csv', index=False)
