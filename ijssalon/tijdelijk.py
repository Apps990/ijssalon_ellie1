prijzen = {
    'aardbei' : '3',
    'vanille': '4',
    'chocolade' : '5'
}

aanbieding = prijzen['aardbei'] * 0.8

reclame_tekst = f"'Vandaag in de aanbieding: vanille-ijs, 1 liter  slechts € {aanbieding}"



reclame_tekst2 = reclame_tekst[:63]

reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split()

"""
    Verwerkt een string en print deze met hoofdletters of kleine letters,
    afhankelijk van de lengte.
    """
    for el in reclame_tekst4
        if len(el) > 4:
            print(el.upper())
        else 
            print(el.lower())
    

for el in reclame_tekst4:

    el.lower()


def format_string(reclame_tekst4):

    if len(reclame_tekst4) >= 5:
        return reclame_tekst4[:100].upper() 
    elif len(reclame_tekst4) == 4:
        return reclame_tekst4.lower()
