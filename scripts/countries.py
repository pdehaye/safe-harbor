countries = {
 'Austria': 'AUT',
 'Belgium': 'BEL',
 'Bulgaria': 'BGR',
 'Croatia': 'HRV',
 'Cyprus': 'CYP',
 'Czech Republic': 'CZE',
 'Denmark': 'DNK',
 'Estonia': 'EST',
 'Finland': 'FIN',
 'France': 'FRA',
 'Germany': 'DEU',
 'Greece': 'GRC',
 'Hungary': 'HUN',
 'Iceland': 'ISL',
 'Ireland': 'IRL',
 'Italy': 'ITA',
 'Latvia': 'LVA',
 'Liechtenstein': 'LIE',
 'Lithuania': 'LTU',
 'Luxembourg': 'LUX',
 'Malta': 'MLT',
 'Netherlands': 'NLD',
 'Norway': 'NOR',
 'Poland': 'POL',
 'Portugal': 'PRT',
 'Romania': 'ROU',
 'Slovakia': 'SVK',
 'Slovenia': 'SVN',
 'Spain': 'ESP',
 'Sweden': 'SWE',
 'Switzerland': 'CHE',
 'United Kingdom': 'GBR'
}

def parse_countries(string):
    countries_list = filter(lambda _: bool(_), string.split(", "))
    return [countries[long_name] for long_name in countries_list]