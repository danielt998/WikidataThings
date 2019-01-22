from dump_things import dump

countries = ['Estonya', 'Arhentina ', 'Arhentina', 'Etiopia', 'Eslobenya', 'Eslobakya', 'El Salvador', 'Bosnia ug Herzegovina', 'Biyelorusya', 'Bolivia', 'Aserbaiyan', '...']

def the_filter(lang_str, desc_str):
    for country in countries:
        if country in lang_str or country in desc_str:
            return True
    return False

langs=['ceb']
dump(the_filter, "output/ceb_country_fixes", langs)