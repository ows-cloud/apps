"""
http://www.upu.int/en/activities/addressing/postal-addressing-systems-in-member-countries.html
http://www.upu.int/en/activities/addressing/s42-standard/compliant-countries.html
"""

address_format = {
    "AD": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Andorra
    "AE": "%(street)s\n%(street2)s\n%(state_name)s\n%(country_name)s",  # United Arab Emirates (the)
    "AF": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Afghanistan
    "AG": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Antigua and Barbuda
    "AI": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Anguilla
    "AL": "%(street)s\n%(street2)s\n%(zip)s\n%(city)s\n%(country_name)s",  # Albania
    "AM": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Armenia
    "AO": "%(street)s\n%(street2)s\n%(zip)s\n%(city)s\n%(country_name)s",  # Angola
    "AR": "%(street)s\n%(street2)s\n%(state_code)s%(zip)s %(city)s\n%(country_name)s",  # Argentina
    "AT": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Austria
    "AU": "%(street)s\n%(street2)s\n%(city)s %(state_code)s %(zip)s\n%(country_name)s",  # Australia
    "AW": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Aruba
    "AX": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Åland Islands
    "AZ": "%(street)s\n%(street2)s\n%(country_code)s %(zip)s %(city)s\n%(country_name)s",  # Azerbaijan
    "BA": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Bosnia and Herzegovina
    "BB": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Barbados
    "BD": "%(street)s\n%(street2)s\n%(city)s – %(zip)s\n%(country_name)s",  # Bangladesh
    "BE": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Belgium
    "BF": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Burkina Faso
    "BG": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Bulgaria
    "BH": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Bahrain
    "BI": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Burundi
    "BJ": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Benin
    "BM": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Bermuda
    "BN": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Brunei Darussalam
    "BO": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Bolivia (Plurinational State of)
    "BR": "%(street)s\n%(street2)s\n%(city)s – %(state_code)s\n%(zip)s\n%(country_name)s",  # Brazil
    "BS": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Bahamas (the)
    "BT": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Bhutan
    "BW": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Botswana
    "BY": "%(street)s\n%(street2)s\n%(zip)s, %(city)s\n%(country_name)s",  # Belarus
    "BZ": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Belize
    "CA": "%(street)s\n%(street2)s\n%(city)s %(state_code)s %(zip)s\n%(country_name)s",  # Canada
    "CD": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Congo (the Democratic Republic of the)
    "CF": "%(street)s\n%(street2)s\n%(zip)s\n%(city)s\n%(country_name)s",  # Central African Republic (the)
    "CG": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Congo (the)
    "CH": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Switzerland
    "CI": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Côte d'Ivoire
    "CK": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Cook Islands (the)
    "CL": "%(street)s\n%(street2)s\n%(zip)s\n%(city)s\n%(country_name)s",  # Chile
    "CM": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Cameroon
    "CN": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # China
    "CO": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(state_name)s\n%(country_name)s",  # Colombia
    "CR": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Costa Rica
    "CU": "%(street)s\n%(street2)s\n%(country_code)s %(zip)s %(city)s\n%(country_name)s",  # Cuba
    "CV": "%(street)s\n%(street2)s\n%(zip)s\n%(city)s\n%(country_name)s",  # Cabo Verde
    "CY": "%(street)s\n%(street2)s\n%(country_code)s-%(zip)s %(city)s\n%(country_name)s",  # Cyprus
    "CZ": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Czechia
    "DE": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Germany
    "DJ": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Djibouti
    "DK": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Denmark
    "DM": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Dominica
    "DO": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Dominican Republic (the)
    "DZ": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Algeria
    "EC": "%(street)s\n%(street2)s\n%(zip)s - %(city)s\n%(country_name)s",  # Ecuador
    "EE": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Estonia
    "EG": "%(street)s\n%(street2)s\n%(city)s\n%(state_name)s\n%(zip)s\n%(country_name)s",  # Egypt
    "ER": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Eritrea
    "ES": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(state_name)s\n%(country_name)s",  # Spain
    "ET": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Ethiopia
    "FI": "%(street)s\n%(street2)s\n%(country_code)s-%(zip)s %(city)s\n%(country_name)s",  # Finland
    "FJ": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Fiji
    "FK": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Falkland Islands (the) [Malvinas]
    "FO": "%(street)s\n%(street2)s\n%(country_code)s %(zip)s %(city)s\n%(country_name)s",  # Faroe Islands (the)
    "FR": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # France
    "GA": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Gabon
    "GB": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # United Kingdom of Great Britain and Northern Ireland (the)
    "GD": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Grenada
    "GE": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Georgia
    "GF": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # French Guiana
    "GG": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Guernsey
    "GH": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Ghana
    "GI": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Gibraltar
    "GL": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Greenland
    "GM": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Gambia (the)
    "GN": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Guinea
    "GP": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Guadeloupe
    "GQ": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Equatorial Guinea
    "GR": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Greece
    "GS": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # South Georgia and the South Sandwich Islands
    "GT": "%(street)s\n%(street2)s\n%(zip)s–%(state_name)s\n%(country_name)s",  # Guatemala
    "GW": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Guinea-Bissau
    "GY": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Guyana
    "HK": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Hong Kong
    "HN": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Honduras
    "HR": "%(street)s\n%(street2)s\n%(country_code)s-%(zip)s %(city)s\n%(country_name)s",  # Croatia
    "HT": "%(street)s\n%(street2)s\n%(country_code)s%(zip)s %(city)s\n%(country_name)s",  # Haiti
    "HU": "%(city)s\n%(street)s\n%(street2)s\n%(zip)s\n%(country_name)s",  # Hungary
    "ID": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Indonesia
    "IE": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Ireland
    "IL": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Israel
    "IM": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Isle of Man
    "IN": "%(street)s\n%(street2)s\n%(city)s\n%(state_name)s\n%(zip)s\n%(country_name)s",  # India
    "IO": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # British Indian Ocean Territory (the)
    "IQ": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Iraq
    "IR": "%(city)s\n%(street)s\n%(street2)s\n%(zip)s\n%(country_name)s",  # Iran (Islamic Republic of)
    "IS": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Iceland
    "IT": "%(street)s\n%(street2)s\n%(zip)s %(city)s %(state_code)s\n%(country_name)s",  # Italy
    "JM": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Jamaica
    "JO": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Jordan
    "JP": "%(street)s\n%(street2)s\n%(city)s\n%(state_name)s\n%(zip)s %(country_name)s",  # Japan
    "KE": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Kenya
    "KG": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Kyrgyzstan
    "KH": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Cambodia
    "KI": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Kiribati
    "KM": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Comoros (the)
    "KN": "%(street)s\n%(street2)s\n%(city)s\n%(country_code)s%(zip)s",  # Saint Kitts and Nevis
    "KP": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Korea (the Democratic People's Republic of)
    "KR": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Korea (the Republic of)
    "KW": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Kuwait
    "KY": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Cayman Islands (the)
    "KZ": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s\n%(zip)s",  # Kazakhstan
    "LA": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Lao People's Democratic Republic (the)
    "LB": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Lebanon
    "LC": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Saint Lucia
    "LK": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Sri Lanka
    "LR": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Liberia
    "LS": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Lesotho
    "LT": "%(street)s\n%(street2)s\n%(country_code)s–%(zip)s %(city)s\n%(country_name)s",  # Lithuania
    "LU": "%(street)s\n%(street2)s\nL-%(zip)s %(city)s\n%(country_name)s",  # Luxembourg
    "LV": "%(street)s\n%(street2)s\n%(city)s, %(country_code)s–%(zip)s\n%(country_name)s",  # Latvia
    "LY": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Libya
    "MA": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Morocco
    "MC": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Monaco
    "MD": "%(street)s\n%(street2)s\n%(country_code)s-%(zip)s %(city)s\n%(country_name)s",  # Moldova (the Republic of)
    "ME": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Montenegro
    "MG": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Madagascar
    "MK": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Macedonia (the former Yugoslav Republic of)
    "ML": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Mali
    "MM": "%(street)s\n%(street2)s\n%(city)s, %(zip)s\n%(country_name)s",  # Myanmar
    "MN": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Mongolia
    "MO": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Macao
    "MR": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Mauritania
    "MS": "%(street)s\n%(street2)s\n%(city)s, %(zip)s\n%(country_name)s",  # Montserrat
    "MT": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Malta
    "MU": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Mauritius
    "MV": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Maldives
    "MW": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Malawi
    "MX": "%(street)s\n%(street2)s\n%(zip)s %(city)s, %(state_code)s\n%(country_name)s",  # Mexico
    "MY": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(state_name)s\n%(country_name)s",  # Malaysia
    "MZ": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Mozambique
    "NA": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Namibia
    "NC": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # New Caledonia
    "NE": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Niger (the)
    "NG": "%(street)s\n%(street2)s\n%(zip)s\n%(city)s\n%(country_name)s",  # Nigeria
    "NI": "%(street)s\n%(street2)s\n%(zip)s\n%(city)s\n%(country_name)s",  # Nicaragua
    "NL": "%(street)s\n%(street2)s\n%(zip)s  %(city)s\n%(country_name)s",  # Netherlands (the)
    "NO": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Norway
    "NP": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Nepal
    "NR": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Nauru
    "NU": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Niue
    "NZ": "%(street)s\n%(street2)s\n%(city)s\n%(state_name)s %(zip)s\n%(country_name)s",  # New Zealand
    "OM": "%(street)s\n%(street2)s\n%(zip)s\n%(city)s\n%(country_name)s",  # Oman
    "PA": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Panama
    "PE": "%(street)s\n%(street2)s\n%(zip)s\n%(city)s\n%(country_name)s",  # Peru
    "PF": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # French Polynesia
    "PG": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Papua New Guinea
    "PH": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Philippines (the)
    "PK": "%(street)s\n%(street2)s\n%(city)s–%(zip)s\n%(country_name)s",  # Pakistan
    "PL": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Poland
    "PT": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Portugal
    "PY": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Paraguay
    "QA": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Qatar
    "RO": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Romania
    "RS": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Serbia
    "RU": "%(street)s\n%(street2)s\n%(city)s\n%(state_name)s\n%(country_name)s\n%(zip)s",  # Russian Federation (the)
    "RW": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Rwanda
    "SA": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Saudi Arabia
    "SB": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Solomon Islands
    "SC": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Seychelles
    "SD": "%(street)s\n%(street2)s\n%(zip)s\n%(city)s\n%(country_name)s",  # Sudan (the)
    "SE": "%(street)s\n%(street2)s\n%(country_code)s-%(zip)s %(city)s\n%(country_name)s",  # Sweden
    "SG": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Singapore
    "SH": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Saint Helena, Ascension and Tristan da Cunha
    "SI": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Slovenia
    "SK": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Slovakia
    "SL": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Sierra Leone
    "SM": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # San Marino
    "SN": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Senegal
    "SO": "%(street)s\n%(street2)s\n%(city)s, %(zip)s\n%(country_name)s",  # Somalia
    "SR": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Suriname
    "SS": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # South Sudan
    "ST": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Sao Tome and Principe
    "SV": "%(street)s\n%(street2)s\n%(zip)s – %(city)s\n%(country_name)s",  # El Salvador
    "SY": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Syrian Arab Republic
    "SZ": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Eswatini
    "TD": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Chad
    "TG": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Togo
    "TH": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Thailand
    "TJ": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Tajikistan
    "TL": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Timor-Leste
    "TM": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Turkmenistan
    "TN": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Tunisia
    "TO": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Tonga
    "TR": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Turkey
    "TT": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Trinidad and Tobago
    "TV": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Tuvalu
    "TZ": "%(street)s\n%(street2)s\n%(zip)s\n%(city)s\n%(country_name)s",  # Tanzania, United Republic of
    "UA": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # Ukraine
    "UG": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Uganda
    "US": "%(street)s\n%(street2)s\n%(city)s %(state_code)s %(zip)s\n%(country_name)s",  # United States of America (the)
    "UY": "%(street)s\n%(street2)s\n%(zip)s – %(city)s\n%(country_name)s",  # Uruguay
    "UZ": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s\n%(zip)s",  # Uzbekistan
    "VA": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Holy See (the)
    "VC": "%(street)s\n%(street2)s\n%(city)s %(country_code)s%(zip)s\n%(country_name)s",  # Saint Vincent and the Grenadines
    "VE": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Venezuela (Bolivarian Republic of)
    "VG": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Virgin Islands (British)
    "VN": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Viet Nam
    "VU": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Vanuatu
    "WS": "%(street)s\n%(street2)s\n%(city)s %(country_code)s%(zip)s\n%(country_name)s",  # Samoa
    "YE": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Yemen
    "YT": "%(street)s\n%(street2)s\n%(zip)s %(city)s\n%(country_name)s",  # Mayotte
    "ZA": "%(street)s\n%(street2)s\n%(city)s\n%(zip)s\n%(country_name)s",  # South Africa
    "ZM": "%(street)s\n%(street2)s\n%(city)s %(zip)s\n%(country_name)s",  # Zambia
    "ZW": "%(street)s\n%(street2)s\n%(city)s\n%(country_name)s",  # Zimbabwe
}
