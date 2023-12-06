from sqlite3


a=sqlite3.connect('gul.db')
b=a.cursor()


b.execute('''
CREATE TABLE IF NOT EXISTS gul(
    nom TEXT
    rang TEXT
    son INTEGER

)''')


b.execute('''
CREATE TABLE IF NOT EXISTS mebel(
    nom TEXT
    rang TEXT
    son INTEGER

)''')



b.execute('''
CREATE TABLE IF NOT EXISTS darslik(
    nom TEXT
    belgi TEXT
    son INTEGER

)''')


b.execute('''
CREATE TABLE IF NOT EXISTS daraxt(
    nom TEXT
    rang TEXT
    son INTEGER

)''')


b.execute('''
CREATE TABLE IF NOT EXISTS meva(
    nom TEXT
    rang TEXT
    son INTEGER

)''')