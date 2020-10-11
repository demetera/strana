from strana import Strana, Article


s = Strana(day='2019-12-31', page=3)
s.get_articles()
print(s.articles)

s.get_full_articles()
for art in s.articles:
    print(art)


a_url='https://strana.ua/news/294494-v-ukraine-tolko-kirovohradskaja-oblast-hotova-smjahchit-karantin.html'
a = Article(a_url)
print(a.content)
