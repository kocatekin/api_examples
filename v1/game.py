import requests as req
import random

def main():
	url = "https://opentdb.com/api.php?amount=10&category=11&difficulty=easy&type=multiple"
	res = req.get(url)
	sonuc = res.json()
	skor = 0
	for i in range(10):
		soru = sonuc["results"][i]["question"]
		dogruCevap = sonuc["results"][i]["correct_answer"]
		yanlisCevaplar = sonuc["results"][i]["incorrect_answers"]
		yanlisCevaplar.append(dogruCevap)
		random.shuffle(yanlisCevaplar)
		print(soru)
		for idx,cevap in enumerate(yanlisCevaplar):
			print(f"{idx+1}: {cevap}")
		print("")
		choice = int(input("cevap?"))
		if (choice-1) == yanlisCevaplar.index(dogruCevap):
			print("dogru cevap")
			skor += 1
		else:
			print("yanlis cevap")
			print(f"Dogru cevap: {dogruCevap}")
	print("oyun bitti")
	print(f"skor: {skor}")
if __name__ == "__main__":
	main()
