
korting1 = 4 - (4 * 0.1)
smaak ='aardbei'
prijs = 4 
korting = 0.1
uitvoer = f'''Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting1} euro.'''

  
getal1 = 220
getal2 = 430
getal3 = 125
getal4 = 160
getal5 = 205
getal6 = 90
getal7 = 345
som_getallen = getal1 + getal2 + getal3 + getal4 + getal5 + getal6 + getal7
print(som_getallen) 

bedrag_excl_btw = 1575
print( "bedrag (exclusief btw): " + str(bedrag_excl_btw) )

btw = 0.09 * bedrag_excl_btw
print( "btw (9%): " +  str(btw) )

bedrag_incl_btw = bedrag_excl_btw + btw 
print( "bedrag (inclusief btw): " + str(bedrag_incl_btw) )
   
print( f" Het totaal van alle inkomsten van deze week is {bedrag_excl_btw} euro, waarover {btw} euro btw betaald dient te worden.")



print (max( 220, 430, 125, 160, 205, 90, 345 ) )
print (min( 220, 430, 125, 160, 205, 90, 345 ) )


dataset = [220, 430, 125, 160, 205, 90, 345]
lengte = len(dataset) 
  
som = sum(dataset) 
gemiddelde = som / lengte 
  
print("De gemiddelde inkomsten deze week zijn euro" + str(gemiddelde)) 


print (min( 220, 430, 125, 160, 205, 90, 345 ) )
print (max( 220, 430, 125, 160, 205, 90, 345 ) )


def combinatie(invoer_lijst_2):
korte_lijst = laag_en_hoog(invoer_lijst_2)
uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
return uitvoer