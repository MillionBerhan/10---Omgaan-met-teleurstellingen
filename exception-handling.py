import time
print ("Welkom, bestel maar lekker raak!")
crossaintjes = 0.39
stokbroden = 2.78

while True:
    try:
        crossaintjesAantal= int(input('Hoeveel crossaintjes wilt u?'))
        if crossaintjesAantal <1 or not int:
            raise ValueError

        StokbrodenAantal= int(input('Hoeveel stokbroden wilt u?'))
        if StokbrodenAantal <1 or not int:
            raise ValueError
        break 
    except:
        print("Er iets iets onverwachts opgetreden!")

totaalprijs = crossaintjesAantal*crossaintjes+StokbrodenAantal*stokbroden
print("--------------------------------")
print (f"Prijs crossaintjes: €{round(crossaintjesAantal*crossaintjes,2)}")
print (f"Prijs stokbroden: €{round(StokbrodenAantal*stokbroden,2)}")
print (f"Totaalprijs Incl.BTW(6%): €{round(totaalprijs,2)}")
time.sleep(15)