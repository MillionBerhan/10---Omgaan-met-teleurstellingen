
print("Vacature: Circusdirecteur voor Circus HotelDeBotel")

while True:

    try:    
        acrobatiek = int(input("hoeveel jaar heeft u ervaring met acrobatiek?\nInvoer:"))
        jongleren = int(input("Hoeveel jaar heeft u ervaring met Jongleren?\nInvoer:"))
        diploma = input("Bent u in het bezit van een Diploma MBO-4 ondernemen?ja/nee\nInvoer:")
        hoed = input("Bent u in het bezit van een hoge hoed?ja/nee\nInvoer:")
        man = int(input("Heeft u als man een snor? Zo, ja van hoeveel cm?\nInvoer:"))
        vrouw = int(input("heeft u als vrouw rood krulhaar, zo ja van hoeveel cm?\nInvoer:"))
        lengte = int(input("Wat is uw lengte?\nInvoer:"))
        gewicht = int(input("Wat is uw lichaamsgewicht?\nInvoer:"))
        praktijkervaring = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?\nInvoer:"))
        certificaat = input("Bent u in het bezit van een certificaat (Overleven met gevaarlijk personeel)?ja/nee\nInvoer:")
        hobbys = input("heeft u nog hobby's?ja/nee\nInvoer:")
        toekomst = input("Wilt u kinderen?ja/nee\nInvoer:")
        partner = input("Heeft u een partner?ja/nee\nInvoer:")
        clown = input("Houd u ervan om graag de clown uit te hangen?ja/nee\nInvoer:")

        if acrobatiek>=3 and jongleren>4 and diploma == "ja" and hoed == "ja" and man>=10 and vrouw >=20 and gewicht >=90 and praktijkervaring>=4 and certificaat == "ja" and lengte >170:
            print ("Bedankt voor het beantwoorden van de laatste vraag, u komt in aanmerking voor een de baan bij Circus HotelDeBotel!")
            exit()
        else:
            print("U bent helaas niet gekwalificeerd voor deze functie, wij wensen u namens Circus HoteldeBotel heel veel succes bij eventuele andere functies!")
            exit()

    except ValueError:
        print("Er is iets fout gegaan!")