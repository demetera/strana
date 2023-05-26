# strana.news (Ukrainian news website) basic parser

Basic parser for strana.ua news website
Early alpha version

Example:
```python
from strana import Strana
s1 = Strana() # Recent articles
s2 = Strana(page=3) # Page 3 for today's articles
s3 = Strana(day='2018-04-01') # Recent articles for 1st of April 2018
s4 = Strana(day='2020-01-01', page=2) # Page 2 for 1st of January 2020 articles
s5 = Strana(query='Mind') # First page for query `Mind`
s6 = Strana(query='Ukraine', page=4) # Page 4 for query `Ukraine`
s1.get_full_articles() # Extract list with given parameters
print(s.articles) # Printing extracted list 
