mijn_prijzen = {
    'aardbei' : '3',
    'vanille': '4',
    'chocolade' : '5'
}

aanbieding = 3 * 0.8

reclame_tekst = 'Vandaag in de aanbieding: vanille-ijs, 1 liter  slechts € {aanbieding}'



reclame_tekst2 = round(aanbieding, 2)
'Vandaag in de aanbieding: vanille-ijs, 1 liter  slechts € {aanbieding}'

reclame_tekst3 = ('Vandaag in de aanbieding: vanille-ijs, 1 liter  slechts {aanbieding}').upper()
reclame_tekst4 = ['Vandaag', 'in', 'de', 'aanbieding:', 'vanille-ijs', '1 liter',  'slechts', '€ <aanbieding>']
def verwerk_string(reclame_tekst):
    """
    Verwerkt een string en print deze met hoofdletters of kleine letters,
    afhankelijk van de lengte.
    """
    for woord in reclame_tekst.split():
        if len(woord) == 5:
            print(woord.upper())
        elif len(woord) == 4:
            print(woord.lower())
        else:
            print(woord)

# Voorbeeldgebruik
reclame_tekst4 = 'Vandaag in de aanbieding: vanille-ijs, 1 liter  slechts € aanbieding'
verwerk_string(reclame_tekst4)

for el in reclame_tekst4:

    el.lower()


def format_string(input_string):

    if len(input_string) >= 5:
        return input_string[:100].upper() 
    elif len(input_string) == 4:
        return input_string.lower()
