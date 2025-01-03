from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib
import http.client

conn = http.client.HTTPSConnection("rapid-translate-multi-traduction.p.rapidapi.com")
API_KEY="add your api key here"############ add your api key here
headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': "rapid-translate-multi-traduction.p.rapidapi.com",
    'Content-Type': "application/json"
}
#Setting-up Selenium
options = Options()
options.page_load_strategy = 'normal'  
cService = webdriver.ChromeService(executable_path='./chromedriver-mac/chromedriver')
driver = webdriver.Chrome(service = cService,options=options)

#Visit the website El País, a Spanish news outlet.
driver.get("https://elpais.com/opinion/")

#Scrape Articles from the Opinion Section.
file_ = open("output.txt", "a") 
count_art=0
repeated_word=dict()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
articles = soup.find_all('article')
for article in articles:
    
    link=article.find('h2').find("a")['href']
    title=article.find('h2').find("a").text
    driver.get(link)
    html=driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    try:
        paras=soup.find("article").find_all("p")
        img_link=soup.find('article').find("img")['src']
    except:
        print("No Images or Paragraphs")
        continue
    if img_link:
        urllib.request.urlretrieve(img_link, title+".jpg")
    print(title)
    file_.write(title + '\n\n')
    for para in paras:
        file_.write(para.text+'\n') 
        print(para.text)
    file_.write('\n\n\n') 

    
    # Translate Article Headers:
    payload = ('{"from":"auto","to":"en","q":"'+title+'"}').encode('utf-8')
    conn.request("POST", "/t", payload, headers)

    res = conn.getresponse()
    data = res.read()
    data=data.decode("utf-8")
    file_.write(data+'\n\n\n')
    print(data)
    #Analyze Translated Headers
    startind=data.find('"')
    endind=data.find('"',startind+1)
    if startind!=-1 and endind!=-1:
        data=data[startind+1:endind]
        for word in data.split(' '):
            word=word.lower()
            repeated_word[word] = repeated_word.get(word, 0) + 1 

    count_art+=1
    if count_art==5:
        break
    
print(repeated_word)
for key,val in repeated_word.items():
    if val>1:
        print(key," ",val)

file_.close()  
driver.quit()

    






#Cross-Browser Testing