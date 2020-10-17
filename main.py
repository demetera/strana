from strana import Strana, Article
import sqlite3

#Getting simple list of articles

s = Strana(day='2018-07-25')
# s.get_articles()
# print(s.articles)


#Getting detailed list with date

s.get_full_articles()
db = sqlite3.connect('strana.db')
q = 'CREATE TABLE IF NOT EXISTS strana (time text, title text, url text)'
db.execute(q)
for art in s.articles:
    q = "INSERT INTO strana VALUES ('{}', '{}' ,'{}')".format(art[0], art[1], art[2])
    db.execute(q)
db.commit()
db.close()

#Getting article content in dict

# a_url='https://strana.ua/news/294494-v-ukraine-tolko-kirovohradskaja-oblast-hotova-smjahchit-karantin.html'
# a = Article(a_url)
# print(a.content)
