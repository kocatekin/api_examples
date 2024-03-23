import requests
from bs4 import BeautifulSoup
from datetime import date

def main():
	url = "https://www.nadirdoviz.com/fiyatekrani"
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	res = soup.find_all("td", attrs={"class":"tdparitedeger tdpg"})
	my_dict = {}
	my_dict["date"] = date.today().strftime("%d-%m-%Y")
	my_dict["gold"] = {}
	my_dict["silver"] = {}
	my_dict["gold"]["buy"] = res[4].string
	my_dict["gold"]["sell"] = res[5].string
	my_dict["silver"]["buy"] = res[10].string
	my_dict["silver"]["sell"] = res[11].string
	return my_dict
	
if __name__ == "__main__":
	print(main())
