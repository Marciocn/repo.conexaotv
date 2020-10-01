import requests,base64, re
from bs4 import *

def get_soup(url):
    text = requests.get(url).text
    soup = BeautifulSoup(text, "lxml")
    return soup

def clear_link(string):
    string = re.findall("hZC5jby9l(.*?)'", string)[0]
    stringCleaned = base64.b64decode(string)
    return stringCleaned

def listar_filmes(url):
    soup = get_soup(url)
    caixa = soup.find('div',{'class':'container caixa'})
    if not caixa:
        caixa = soup.find('div',{'class':'container'})
    filmes = caixa.findAll('div',{'class': 'caixa-filme pull-left'})
    for filme in filmes:
        name = filme.div.text
        url = filme.a['href']
        img = filme.a.img['src']
        #print()
        print(name, url,img)
    caixaNav = soup.find('div',{'class': 'wp-pagenavi'})
    if caixaNav:
        proximo = caixaNav.find('a',{'class': 'nextpostslink'})
        nextpage = proximo['href']
        print(nextpage)


def listar_categorias():
    soup = get_soup('https://ww2.pipoflix.com/')
    itens = soup.find('li',{'class':'dropdown'}).findAll('a',{'class':'dropdown-item'})
    for categoria in itens:
        name = categoria.text
        url = categoria['href']
        print(name,url)


def player(url):
    soup = get_soup(url)
    fontes = soup.findAll('div',{'class': 'pull-left opc'})
    for fonte in fontes:
        print(fonte)
    sources = soup.findAll('button', {'class': 'playMovie btn-xs btn-success'})
    for source in sources:
        name = source.text
        url = clear_link(source['onclick']).decode()
        print(name,url)
def listar_series(url):
    soup = get_soup(url)
    caixa = soup.find('div', {'class': 'container caixa'})
    series = caixa.findAll('div',{'class': 'caixa-serie pull-left'})
    for serie in series:
        name = serie.findAll('div')[1].text
        url = serie.a['href']
        img = serie.a.img['src']
        print(name,url,img)
    caixaNav = soup.find('div', {'class': 'wp-pagenavi'})
    if caixaNav:
        proximo = caixaNav.find('a', {'class': 'nextpostslink'})
        nextpage = proximo['href']
        print(nextpage)

def listar_temporadas(url):
    soup = get_soup(url)
    caixa = soup.find('ul',{'class':'nav nav-pills navCustom'})
    temporadas = caixa.findAll('li')
    for temporada in temporadas:
        name = temporada.a.text
        print(name)
def listar_episodios(name,url):
    soup = get_soup(url)
    caixa = soup.find('div',{'id':name.lower().replace(' ','-')})
    episodios = caixa.tbody.findAll('tr')
    for episodio in episodios:
        links = episodio.findAll('a',{'class':'episodio'})
        for link in links:
            name = re.findall('"(.*?)"',link['onclick'])[0].replace('-',' ')
            url = link['href']
            print(name,url)
        print()
        print('----')
def player_serie(url):
    soup = get_soup(url)
    print(soup)
player_serie('')

#listar_episodios('Temporada 2', 'http://pipocaofilmes.online/ver-seriado-s-w-a-t-todos-capitulos/')
#listar_temporadas('http://pipocaofilmes.online/ver-seriado-s-w-a-t-todos-capitulos/')
#listar_series('http://pipocaofilmes.online/ultimas-series-cadastradas/')
#player('http://pipocaofilmes.online/assistir-creed-nascido-para-lutar-legendado-online-1080p-brrip/')

#listar_categorias()
#listar_filmes('http://pipocaofilmes.online/ultimos-filmes/')

#print(clear_link("_stx('s_','hZC5jby9laHR0cHM6Ly9vcGVubG9hZC5jby9lbWJlZC9YdUNXX0l3b1d6Yy9EVUJMQURPLUNyZWVkLk5hc2NpZG8ucGFyYS5MdXRhci4yMDE2LjEwODBwLkJsdVJheS41LjEueDI2NC5EVUFMLUJMVURWLm1wNA==')"))