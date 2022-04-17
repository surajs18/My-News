from GoogleNews import GoogleNews

news=GoogleNews()

country =input("Enter your country: ")
days = input("Enter the number of days: ")
news = GoogleNews(period=days+'d')
news.search(country)
result = news.results()
for x in result:
    print('-'*80)
    print("Title:-", x['title'])
    print("Date/Time:-", x['date'])
    print('Link:- ', x['link'])
