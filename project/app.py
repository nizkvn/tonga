from flask import Flask, render_template

import requests
from bs4 import BeautifulSoup

WEB_URL = "https://bongdaplus.vn/"

app = Flask(__name__)


def get_url(URL):
  re = requests.get(URL)
  soup = BeautifulSoup(re.text, 'html.parser')
  return soup

def get_data_primary(URL):
    soup = get_url(URL)
    primary_box = soup.find_all('div', class_='catprimebox', limit=10)
    # cat_box = soup.find_all('div', class_='catbox', limit=10)
    data=[]

    for da in primary_box:
        d=[]
        s = da.find('a', class_='lead')
        cap = {'title':'','link':''}
        cap['title']=s.text
        cap['link']=s['href']
        newfs= da.find('div', class_='col w32 news fst')
        nfs = {'title':'','link':'','img_url':'','description':''}
        nfs['title'] = newfs.find('span',class_='title').text.replace('\n','').replace('\r','')
        nfs['link'] = newfs.a['href']
        nfs['img_url'] = newfs.img['data-src']
        nfs['description'] = newfs.p.text.replace('\n','').replace('\r','')
        
        news = da.find('ul',class_='lst')
        for n in news:
            try:
                new = {'title':'','link':'','img_url':''}
                new['title'] = n.a.text.replace('\n','').replace('\r','')
                new['link'] = n.a['href']
                new['img_url'] = n.img['data-src']
            except:
                pass
            if new['title']!='':
                d.append(new)
        data.append([cap,nfs,d])
    return data
def get_data_cat(URL):
    soup = get_url(URL)
    cat_box = soup.find_all('div', class_='catbox')
    data=[]

    for da in cat_box:
        d=[]
        s = da.find('a', class_='lead')
        cap = {'title':'','link':''}
        cap['title']=s.text
        cap['link']=s['href']
        newfs= da.find('li', class_='news fst')
        nfs = {'title':'','link':'','img_url':''}
        nfs['title'] = newfs.find('span',class_='title').text.replace('\n','').replace('\r','')
        nfs['link'] = newfs.a['href']
        nfs['img_url'] = newfs.img['data-src']
        
        news = da.find('ul',class_='lst')
        for n in news:
            try:
                new = {'title':'','link':''}
                new['title'] = n.a.text.replace('\n','').replace('\r','')
                new['link'] = n.a['href']
            except:
                pass
            if new['title']!='':
                d.append(new)
        data.append([cap,nfs,d])
    return data


@app.route('/')
def index():
    data_primary = get_data_primary(WEB_URL)
    data_cat = get_data_cat(WEB_URL)
    return render_template('home.html',data_primary=data_primary, data_cat=data_cat)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 