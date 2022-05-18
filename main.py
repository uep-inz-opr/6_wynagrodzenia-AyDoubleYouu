
imie_wynagrodzenie =[]
ilosc_pracownikow = int(input())
for ilosc in range(ilosc_pracownikow):
    imie_wynagrodzenie.append(input().split(" "))

class Pracownik():
    def __init__(self, imie, wynagrodzenie):
        self.imie = str(imie)
        self.wynagrodzenie = wynagrodzenie

    def wynagrodzenie_netto(self):
        pozd = (float(self.wynagrodzenie) -float(self.wynagrodzenie)*0.0976 - float(self.wynagrodzenie)*0.015 - float(self.wynagrodzenie)*0.0245)
        poze = pozd * 0.09
        pozf = pozd * 0.0775
        pozh = round(pozd - 111.25)
        pozi = (pozh * 0.18) - 46.33
        pozj = round(pozi - pozf)
        netto = round(pozd - poze - pozj,2)
        #wynagrodzenia.append(netto)
        return netto 
    
    def skladki_pracodawcy(self):
        skladki = float(self.wynagrodzenie) - float(self.wynagrodzenie)* 0.0976 -float(self.wynagrodzenie)*0.065 - float(self.wynagrodzenie)* 0.0193 - float(self.wynagrodzenie)*0.0245 - float(self.wynagrodzenie)*0.001
        skladka = round(float(self.wynagrodzenie) - skladki,2)
        #skladki_na_pracownikow.append(skladka)
        return skladka

    def koszty_pracodawcy(self):
        pozl = float(self.wynagrodzenie) - float(self.wynagrodzenie)* 0.0976 -float(self.wynagrodzenie)*0.065 - float(self.wynagrodzenie)* 0.0193 - float(self.wynagrodzenie)*0.0245 - float(self.wynagrodzenie)*0.001
        koszt_pracodawcy = round(float(self.wynagrodzenie) + float(self.wynagrodzenie) - pozl,2)
        #cale_koszty.append(koszt_pracodawcy)
        return koszt_pracodawcy

lista_brutto_brutto =[]
for imie,wynagrodzenie in imie_wynagrodzenie:
    pracownik = Pracownik(imie,wynagrodzenie)
    wynagrodzenia = pracownik.wynagrodzenie_netto()
    skladki_na_pracownikow = pracownik.skladki_pracodawcy()
    cale_koszty= pracownik.koszty_pracodawcy()
    lista_brutto_brutto.append(cale_koszty)
    print(f"{pracownik.imie} {wynagrodzenia:.2f} {skladki_na_pracownikow:.2f} {cale_koszty:.2f}")
print(sum(lista_brutto_brutto))