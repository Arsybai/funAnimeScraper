import requests, json
from bs4 import BeautifulSoup

"""
Please use for learning only!
arsybai
"""

class scrape:
	def __init__(self):
		return None

	def aniChara(self,q):
		link = 'https://myanimelist.net/character.php?q={}'.format(q)
		r = requests.get(link)
		soup = BeautifulSoup(r.content,"lxml")
		url = soup.find('div',{'class':'picSurround'}).a["href"]
		req = requests.get(url)
		char = BeautifulSoup(req.content,"lxml")
		img = char.find('div',{'style':'text-align: center;'}).img["src"]
		detail = char.find('tr')
		detail = detail.findAll('td',{'style':'padding-left: 5px;'})
		temp = []
		for tt in detail:
			temp.append(tt.text)
			res = temp[0].split('Character')[1]
			res = 'Age '+res.split('Voice Actors')[0]
		ret_ = {
			'img':img,
			'url':url,
			'detail':res.split('>')[1].strip()
		}
		return ret_

	def aniSearch(self,q):
		data = []
		url = 'https://myanimelist.net/anime.php?q={}'.format(q)
		req = requests.get(url)
		soup = BeautifulSoup(req.content,"lxml")
		for tt in soup.findAll('a',{'class':'hoverinfo_trigger'}):
			link = tt["href"]
			title = tt.text
			if "\n\n" not in title:
				data.append({'title':title,'url':link})
		res = {
			'status':'OK',
			'creator':'https://arsybai.xyz',
			'result':data
		}
		return res

	def aniGetInfo(self,url):
		"""The url get from aniSearch"""
		titles = []
		inf = []
		data = {'creator':'https://arsybai.xyz','alternativeTitles':[],'information':[],'synopsis':'null','note':'AlternativeTitles and Information may have different data or variable!'}
		req = requests.get(url)
		soupa = BeautifulSoup(req.content,"lxml")
		soup = soupa.find('div',{'class':'js-scrollfix-bottom'})
		for ati in soup.findAll('div',{'class','spaceit_pad'}):
			titles.append(ati)
		for out in titles:
			title = out.find('span',{'class':'dark_text'}).text
			alt = out.text.replace(title,'').strip()
			data['alternativeTitles'].append({title:alt})
		for inff in soup.findAll('div',{'class','spaceit'}):
			inf.append(inff)
		for out2 in inf:
			a = out2.find('span',{'class':'dark_text'}).text
			b = out2.text.replace(a,'').strip()
			data['information'].append({a:b})
		syn = soupa.find('span',{'itemprop':'description'}).text
		data['synopsis'] = syn
		return data

	def aniHDimage(self,q):
		datas = []
		def search(q):
			temp_ = []
			link = 'https://wall.alphacoders.com/search.php?search={}'.format(q)
			req = requests.get(link)
			soup = BeautifulSoup(req.content,"lxml")
			for thumb in soup.findAll('div',{'class':'thumb-container-big '}):
				t_ = thumb.find('div',{'class':'boxgrid'})
				t_ = t_.a["href"]
				temp_.append(t_)
			return temp_

		def getImages(q):
			link = 'https://wall.alphacoders.com/'+q
			req = requests.get(link)
			soup = BeautifulSoup(req.content,"lxml")
			img_ = soup.find('div',{'class':'center img-container-desktop'})
			datas.append(img_.a["href"])
	
		s_ = search(q)
		for g_ in s_:
			getImages(g_)
		ret_ = {
			'status':'OK',
			'creator':'Arsybai',
			'result':datas
		}
		return ret_