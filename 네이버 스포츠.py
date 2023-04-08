import requests


headers = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}


url = 'https://sports.news.naver.com/news?oid=468aid=0000932872'
site = requests.get(url, headers = headers)
source_data = site.text

count1 = source_data.count('<h4 class="title">"')

for i in range(count1):

      pos1 = source_data.find('<h4 class="title">"')+ len('<h4 class="title">"')
      source_data = source_data[pos1:]

      pos2 = source_data.find('</h4>')
      a_data = source_data[: pos2]

      source_data = source_data[pos2+1:]
      print(i+1, a_data)

      
      
