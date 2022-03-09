import webbrowser,time
print("Welkom bij Pizzeria Berhano!")
print("Wat wilt u bestellen?") 
priceSM = 3.99
priceME = 4.99
priceLA = 5.99

while True:
    try:
        aantalsmall = int(input("how many small pizza's do you want?")) 
        if aantalsmall <1:
            raise ValueError

        aantalmedium = int(input("how many medium pizza's do you want?"))
        if aantalmedium <1:
            raise ValueError

        aantallarge = int(input("how many large pizza's do you want?"))
        if aantallarge < 1:
            raise ValueError

        break
    except:
        print("Er is iets onverwachts opgetreden!")

total = (aantalsmall * priceSM + aantalmedium * priceME + aantallarge * priceLA)

print (f"you chose {aantalsmall}, small will cost you £{round(priceSM * aantalsmall,2)}\nyou chose {aantalmedium}, medium will cost you £{round(priceME * aantalmedium,2)}\nyou chose {aantallarge}, large will cost you £{round(priceLA * aantallarge,2)}")

print("--------------------------")
print (f"Total price Incl.VAT:£{round(total,2)}")
print ("Bedankt voor de bestelling namens Milliono Berhano, wensen wij u een fijne dag toe!\nHeeft u nog vragen neem dan gerust contact op met ons op!\nContact&Service:\nKlantenservice:085-7078975\nMail:PizzeriaBerhano71@yahoo.com\nAdres:Mollenburgseweg 82\n4205NB Gorinchem\nPostbus 859\nDe beste pizza's vind je bij Pizzeria Berhano!")
time.sleep(5)
webbrowser.open("https://www.youtube.com/watch?v=Arlcn4e6sTE")
