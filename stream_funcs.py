# import mysql.connector
import pandas as pd
import streamlit as st

@st.cache_data
# def find_matching_chemicals_from_cid(cid):
#
#     host = 'localhost'
#     port = '3306'
#     username = 'hash'
#     password = 'zihaxz12'
#     database = 'export_db'
#
#     connection = mysql.connector.connect(
#         host=host,
#         port=port,
#         user=username,
#         password=password,
#         database=database
#     )
#
#     cursor = connection.cursor()
#     sql = """SELECT trade_info.*
#             FROM chemicals
#             INNER JOIN trade_info ON chemicals.chem_key = trade_info.chem_key
#             WHERE chemicals.pubchem_CID = %s;"""
#
#     cursor.execute(sql, (cid,))
#     result = cursor.fetchall()
#     column_names = [i[0] for i in cursor.description]
#
#     cursor.close()
#     connection.close()
#
#     return pd.DataFrame(result, columns=column_names)




# def find_matching_chemicals(chemical_name, pubchem=False, partial=True):
#
#     host = 'localhost'
#     port = '3306'
#     username = 'hash'
#     password = 'zihaxz12'
#     database = 'export_db'
#
#     connection = mysql.connector.connect(
#         host=host,
#         port=port,
#         user=username,
#         password=password,
#         database=database
#     )
#
#     cursor = connection.cursor()
#
#     # SQL query to find matching chemical keys
#     if pubchem:
#         len_chem = 11
#
#         if partial:
#             find_chem_key_sql = """
#                 SELECT chem_key FROM chemicals
#                 WHERE gpt_chem_name LIKE %s OR chem_synonym_1 LIKE %s OR chem_synonym_2 LIKE %s OR
#                       chem_synonym_3 LIKE %s OR chem_synonym_4 LIKE %s OR chem_synonym_5 LIKE %s OR
#                       chem_synonym_6 LIKE %s OR chem_synonym_7 LIKE %s OR chem_synonym_8 LIKE %s OR
#                       chem_synonym_9 LIKE %s OR chem_synonym_10 LIKE %s
#             """
#             cursor.execute(find_chem_key_sql, [f"%{chemical_name}%"] * len_chem)
#         else:
#             find_chem_key_sql = """
#                 SELECT chem_key FROM chemicals
#                 WHERE gpt_chem_name = %s OR chem_synonym_1 = %s OR chem_synonym_2 = %s OR
#                       chem_synonym_3 = %s OR chem_synonym_4 = %s OR chem_synonym_5 = %s OR
#                       chem_synonym_6 = %s OR chem_synonym_7 = %s OR chem_synonym_8 = %s OR
#                       chem_synonym_9 = %s OR chem_synonym_10 = %s
#             """
#             cursor.execute(find_chem_key_sql, [chemical_name] * len_chem)
#
#     else:
#         len_chem = 1
#
#         if partial:
#             find_chem_key_sql = """
#                 SELECT chem_key FROM chemicals
#                 WHERE gpt_chem_name LIKE %s
#             """
#             cursor.execute(find_chem_key_sql, [f"%{chemical_name}%"] * len_chem)
#         else:
#             find_chem_key_sql = """
#                 SELECT chem_key FROM chemicals
#                 WHERE gpt_chem_name = %s
#             """
#             cursor.execute(find_chem_key_sql, [chemical_name] * len_chem)
#
#     chem_keys = cursor.fetchall()
#     chem_keys = [key[0] for key in chem_keys]  # Flatten the list of tuples to list of chem_keys
#
#     if not chem_keys:
#         cursor.close()
#         connection.close()
#         return pd.DataFrame()  # Return an empty dataframe if no matching chem_keys found
#
#     # SQL query to find rows in trade_info table where chem_key matches
#     find_trade_info_sql = """
#         SELECT * FROM trade_info WHERE chem_key IN (%s)
#     """ % ', '.join(['%s'] * len(chem_keys))
#
#     cursor.execute(find_trade_info_sql, chem_keys)
#     result = cursor.fetchall()
#     column_names = [i[0] for i in cursor.description]
#
#     cursor.close()
#     connection.close()
#
#     return pd.DataFrame(result, columns=column_names)


def countries_from_multiselect(multilist):
    mapping = {"🇦🇹 - Austria": ["Austria"],
               "🇧🇪 - Belgium": ["Belgium"],
               "🇧🇬 - Bulgaria": ["Bulgaria"],
               "🇭🇷 - Croatia": ["Croatia"],
                "🇨🇾 - Cyprus": ["Cyprus"],
               "🇨🇿 - Czech Republic": ["Czech Republic"],
               "🇩🇰 - Denmark": ["Denmark"],
                "🇪🇪 - Estonia": ["Estonia"],
               "🇫🇮 - Finland": ["Finland"],
               "🇫🇷 - France": ["France"],
               "🇩🇪 - Germany": ["Germany"],
                "🇬🇷 - Greece": ["Greece"],
               "🇭🇺 - Hungary": ["Hungary"],
               "🇮🇪 - Ireland": ["Ireland"],
               "🇮🇹 - Italy": ["Italy"],
                "🇱🇻 - Latvia": ["Latvia"],
               "🇱🇹 - Lithuania": ["Lithuania"],
               "🇱🇺 - Luxembourg": ["Luxembourg"],
               "🇲🇹 - Malta": ["Malta"],
                "🇳🇱 - Netherlands": ["Netherlands"],
               "🇵🇱 - Poland": ["Poland"],
               "🇵🇹 - Portugal": ["Portugal"],
                "🇷🇴 - Romania": ["Romania"],
               "🇸🇰 - Slovakia": ["Slovakia"],
               "🇸🇮 - Slovenia": ["Slovenia"],
               "🇪🇸 - Spain": ["Spain"],
                "🇸🇪 - Sweden": ["Sweden"],
               "🇬🇧 - United Kingdom": ["United Kingdom"],
               "🇦🇺 - Australia": ["Australia"],
                "🇨🇦 - Canada": ["Canada"],
               "🇨🇳 - China": ["China"],
               "🇭🇰 - Hong Kong": ["Hong Kong"],
                "🇮🇳 - India": ["India"],
               "🇮🇩 - Indonesia": ["Indonesia"],
               "🇯🇵 - Japan": ["Japan"],
               "🇲🇾 - Malaysia": ["Malaysia"],
                "🇲🇽 - Mexico": ["Mexico"],
               "🇳🇿 - New Zealand": ["New Zealand"],
               "🇵🇭 - Philippines": ["Philippines"],
                "🇸🇬 - Singapore": ["Singapore"],
               "🇰🇷 - South Korea": ["South Korea"],
               "🇹🇼 - Taiwan": ["Taiwan"],
               "🇹🇭 - Thailand": ["Thailand"],
               "🇦🇷 - Argentina": ["Argentina"],
               "🇧🇷 - Brazil": ["Brazil"],
                "🇨🇱 - Chile": ["Chile"],
               "🇨🇴 - Colombia": ["Colombia"],
               "🇪🇨 - Ecuador": ["Ecuador"],
               "🇵🇪 - Peru": ["Peru"],
                "🇿🇦 - South Africa": ["South Africa"],
               "🇹🇷 - Turkey": ["Turkey"],
               "🇺🇾 - Uruguay": ["Uruguay"],
                "🇻🇳 - Vietnam": ["Vietnam"],
               "🇦🇪 - United Arab Emirates": ["United Arab Emirates"],
               "🇦🇫 - Afghanistan": ["Afghanistan"],
                "🇦🇱 - Albania": ["Albania"],
               "🇩🇿 - Algeria": ["Algeria"],
               "🇦🇴 - Angola": ["Angola"],
                "🇦🇲 - Armenia": ["Armenia"],
               "🇦🇼 - Aruba": ["Aruba"],
               "🇵🇰 - Pakistan": ["Pakistan"],
                "🇦🇿 - Azerbaijan": ["Azerbaijan"],
               "🇧🇭 - Bahrain": ["Bahrain"],
               "🇧🇩 - Bangladesh": ["Bangladesh"],
                "🇧🇾 - Belarus": ["Belarus"],
               "🇧🇯 - Benin": ["Benin"],
               "🇧🇴 - Bolivia": ["Bolivia"],
                "🇧🇦 - Bosnia and Herzegovina": ["Bosnia and Herzegovina"],
               "🇧🇼 - Botswana": ["Botswana"],
                "🇧🇫 - Burkina Faso": ["Burkina Faso"],
               "🇧🇮 - Burundi": ["Burundi"],
               "🇰🇭 - Cambodia": ["Cambodia"],
                "🇨🇲 - Cameroon": ["Cameroon"],
               "🇨🇫 - Central African Republic": ["Central African Republic"],
               "🇹🇩 - Chad":[ "Chad"],
                "🇰🇲 - Comoros": ["Comoros"],
               "🇨🇩 - Congo": ["Congo"],
               "🇨🇷 - Costa Rica": ["Costa Rica"],
                "🇨🇮 - Cote d'Ivoire": ["Cote d'Ivoire"],
               "🇨🇺 - Cuba": ["Cuba"],
                "🇺🇸 - United States": ['USA', 'US', 'UNITED STATES', 'UNITED STATES OF AMERICA'],
               'America': ['CANADA', 'MEXICO',' GUATEMALA', 'EL SALVADOR', 'COSTA RICA', 'PANAMA', 'HONDURAS', 'NICARAGUA',
                                   'BELIZE', 'BRAZIL', 'ARGENTINA', 'PERU', 'COLOMBIA', 'CHILE', 'ECUADOR',
                                 'VENEZUELA, BOLIVARIAN REPUBLIC OF', 'PARAGUAY', 'URUGUAY',
                                 'BOLIVIA, PLURINATIONAL STATE OF', 'GUYANA', 'SURINAME', 'BOLIVARIAN REPUBLIC OF',
                                 'BOLIVIA', 'FRENCH GUIANA'],
               'Caribbean': ['DOMINICAN REPUBLIC', 'CUBA', 'JAMAICA', 'BAHAMAS', 'TRINIDAD AND TOBAGO', 'BARBADOS',
                             'ST VINCENT', 'PUERTO RICO'],
               'South America': ['BRAZIL', 'ARGENTINA', 'PERU', 'COLOMBIA', 'CHILE', 'ECUADOR',
                                 'VENEZUELA, BOLIVARIAN REPUBLIC OF', 'PARAGUAY', 'URUGUAY',
                                 'BOLIVIA, PLURINATIONAL STATE OF', 'GUYANA', 'SURINAME', 'BOLIVARIAN REPUBLIC OF',
                                 'BOLIVIA', 'FRENCH GUIANA'],
               'Europe': ['UNITED KINGDOM', 'GERMANY', 'FRANCE', 'ITALY', 'SPAIN', 'POLAND', 'BELGIUM', 'NETHERLANDS',
                          'SWEDEN', 'AUSTRIA', 'SWITZERLAND', 'GREECE', 'IRELAND', 'HUNGARY', 'ROMANIA',
                          'CZECH REPUBLIC', 'SLOVAKIA', 'DENMARK', 'FINLAND', 'NORWAY', 'LITHUANIA', 'BELARUS',
                          'UKRAINE', 'ESTONIA', 'LATVIA', 'CROATIA', 'BOSNIA AND HERZEGOVINA', 'ALBANIA', 'SERBIA',
                          'BULGARIA', 'SLOVENIA', 'MALTA', 'MOLDOVA, REPUBLIC OF',
                          'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF', 'ICELAND', 'LUXEMBOURG', 'ANDORRA',
                          'SAN MARINO', 'MONACO', 'LIECHTENSTEIN', 'MONTENEGRO', 'TURKEY', 'DE', 'FR', 'GB', 'IT', 'ES',
                          'NL', 'BE', 'SE', 'AT', 'DK', 'FI', 'IE', 'PT'],
               'EU': ['AUSTRIA', 'BELGIUM', 'BULGARIA', 'CROATIA', 'CYPRUS', 'CZECH REPUBLIC', 'DENMARK', 'ESTONIA',
                      'FINLAND', 'FRANCE', 'GERMANY', 'GREECE', 'HUNGARY', 'IRELAND', 'ITALY', 'LATVIA', 'LITHUANIA',
                      'LUXEMBOURG', 'MALTA', 'NETHERLANDS', 'POLAND', 'PORTUGAL', 'ROMANIA', 'SLOVAKIA', 'SLOVENIA',
                      'SPAIN', 'SWEDEN'],
               'Asia': ['RUSSIAN FEDERATION', 'CHINA', 'JAPAN', 'INDIA', 'KAZAKHSTAN', 'THAILAND', 'MALAYSIA',
                        'SINGAPORE', 'PHILIPPINES', 'VIETNAM, DEMOCRATIC REP. OF', 'MYANMAR', 'AFGHANISTAN', 'PAKISTAN',
                        'BANGLADESH', 'NEPAL', 'SRI LANKA', 'TAIWAN, PROVINCE OF CHINA', 'HONG KONG', 'MONGOLIA',
                        'CAMBODIA', 'LAO PEOPLE`S DEMOCRATIC REPUBLIC', 'KOREA, REPUBLIC OF',
                        'KOREA, DEMOCRATIC PEOPLE`S REPUBLIC OF', 'BRUNEI DARUSSALAM', 'INDONESIA', 'MALDIVES',
                        'BHUTAN', 'TIMOR-LESTE', 'ARMENIA', 'AZERBAIJAN', 'GEORGIA'],
               'Middle East': ['IRAN, ISLAMIC REPUBLIC OF', 'SAUDI ARABIA', 'UNITED ARAB EMIRATES', 'ISRAEL', 'JORDAN',
                               'LEBANON', 'OMAN', 'QATAR', 'KUWAIT', 'BAHRAIN', 'IRAQ', 'YEMEN, DEMOCRATIC',
                               'SYRIAN ARAB REPUBLIC', 'SYRIA', 'PALESTINE, STATE OF', 'CYPRUS', 'PALESTINE STATE'],
               'Africa': ['SOUTH AFRICA', 'NIGERIA', 'GHANA', 'MOROCCO', 'ALGERIA', 'TUNISIA', 'LIBYA', 'SUDAN',
                          'SENEGAL', 'MALI', 'GUINEA', 'COTE D`IVOIRE', 'BURKINA FASO', 'NIGER', 'TOGO', 'BENIN',
                          'MAURITANIA', 'LIBERIA', 'SIERRA LEONE', 'GUINEA-BISSAU', 'GAMBIA', 'CAPE VERDE', 'ETHIOPIA',
                          'EGYPT', 'DR CONGO', 'CONGO', 'ANGOLA', 'KENYA', 'UGANDA', 'TANZANIA, UNITED REPUBLIC OF',
                          'RWANDA', 'BURUNDI', 'DJIBOUTI', 'ERITREA', 'SOMALIA', 'COMOROS', 'MAURITIUS', 'SEYCHELLES',
                          'MADAGASCAR', 'ZIMBABWE', 'ZAMBIA', 'MALAWI', 'SOUTH SUDAN', 'BOTSWANA', 'NAMIBIA', 'LESOTHO',
                          'SWAZILAND', 'MOZAMBIQUE', 'MALAGASY REPUBLIC', 'REUNION', 'MAYOTTE'],
               'Oceania': ['AUSTRALIA', 'NEW ZEALAND', 'PAPUA NEW GUINEA', 'VANUATU', 'SOLOMON ISLANDS', 'GUAM',
                           'KIRIBATI', 'MICRONESIA, FEDERATED STATES OF', 'PALAU', 'MARSHALL ISLANDS', 'SAMOA', 'FIJI',
                           'TONGA', 'TUVALU', 'NAURU', 'COOK ISLANDS', 'NIUE', 'AMERICAN SAMOA', 'FRENCH POLYNESIA',
                           'NEW CALEDONIA', 'WALLIS AND FUTUNA'],

               }

    # Initialize an empty list to store the result
    result = []

    # Iterate through each country/continent in the multilist
    for item in multilist:
        # Check if the item exists as a key in the dictionary (i.e., it's a continent or abbreviation)
        if item in mapping:
            # Extend the result list with all countries under this continent/abbreviation
            result.extend(mapping[item])
        else:
            # Check if the item exists as a country in any of the dictionary values
            for countries in mapping.values():
                if item in countries:
                    result.append(item)

    # making the list upper case
    result = [x.upper() for x in result]

    return list(set(result))