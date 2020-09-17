# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 15:08:15 2020

@author: ckall
"""

#pip install CensusData
import pandas as pd
import censusdata
import re

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 2)

geo_county = censusdata.geographies(censusdata.censusgeo([('state', '*'), ('county', '*')]), 'acs5', 2018, '815f420d7978fe1866f81df31947126f9e1cc460')
geo_county_keys = list(dict.keys(geo_county))

dict_county_name = dict()
for i in geo_county_keys:
    k = ((i[:i.find(',')].rstrip()))
    j = (i[i.find(', '):]).replace(', ', '')
    if j not in dict_county_name:
        dict_county_name[j] = [k]
    else:
        value = k 
        county = dict_county_name[j]
        county.append(value)
        dict_county_name[j] = county
        
dict_county_code = dict()
for i in range(len(geo_county_keys)):
    i = str(geo_county[geo_county_keys[i]])
    j = i[26:i.find('>')]
    k = i[37:]
    if j not in dict_county_code:
        dict_county_code[j] = [k]
    else:
        value = k 
        county = dict_county_code[j]
        county.append(value)
        dict_county_code[j] = county

geo_city = censusdata.geographies(censusdata.censusgeo([('state', '*'), ('place', '*')]), 'acs5', 2018, '815f420d7978fe1866f81df31947126f9e1cc460')
geo_city_keys = list(dict.keys(geo_city))

dict_city_name = dict()
for i in geo_city_keys:
    k = ((i[:i.find(',')].rstrip()))
    j = (i[i.find(', '):]).replace(', ', '')
    if j not in dict_city_name:
        dict_city_name[j] = [k]
    else:
        value = k 
        city = dict_city_name[j]
        city.append(value)
        dict_city_name[j] = city
        
dict_city_code = dict()
for i in range(len(geo_city_keys)):
    i = str(geo_city[geo_city_keys[i]])
    j = i[26:i.find('>')]
    k = i[37:]
    if j not in dict_city_code:
        dict_city_code[j] = [k]
    else:
        value = k 
        city = dict_city_code[j]
        city.append(value)
        dict_city_code[j] = city
        
state_code = str((input('Please enter the State Code: ')))
print('--------')
print('Please choose the granularity of the data:\n1. City\n2. Block Group\n')
granu = (input('Please enter 1 or 2: '))

if(granu == '1'):
    data_city = []
    for i in range(len(dict_city_code[state_code])):
        data_city.append(censusdata.download('acs5', 2018,
                                 censusdata.censusgeo([('state', state_code), ('place', '*')]),
                                 ['B23025_005E', 'B19052_002E', 'B02001_002E', 'B02001_003E', 
                                  'B02001_004E', 'B02001_005E', 'B01001_001E', 'B01001_002E', 
                                  'B01001_026E', 'B15003_017E', 'B15003_018E', 'B15003_019E',
                                  'B15003_020E', 'B15003_021E', 'B15003_022E', 'B15003_023E',
                                  'B15003_024E', 'B15003_025E'], '815f420d7978fe1866f81df31947126f9e1cc460'))
    pd.concat(data_city).to_csv(r'~/data_city.csv')
    data_city = pd.read_csv(r'~/data_city.csv')

    data_city = data_city.rename(columns={"Unnamed: 0": "Detail", "B23025_005E": "Unemploy", "B19052_002E": "Income", "B02001_002E": "White", 
                                "B02001_003E": "Black", "B02001_004E": "Indian_Alaskan", "B02001_005E": "Asian", "B01001_001E": "Population", 
                                "B01001_002E": "Male", "B01001_026E": "Female", "B15003_017E": "High_school", "B15003_018E": "GED", 
                                "B15003_019E": "College_Less_1yr", "B15003_020E": "College_More_1YR", "B15003_021E": "Associate", 
                                "B15003_022E": "Bachelor", "B15003_023E": "Master", "B15003_024E": "Professional", 
                                "B15003_025E": "Doctorate"})
    
    city_code = []
    for i in data_city['Detail']:
        match = re.search(r'> place:([0-9]{5})', i)
        if match:
            city_code.append(match.group(1))
    data_city['City Code'] = city_code
          
    state_code = []
    for i in data_city['Detail']:
        match = re.search(r', state:([0-9]{2})', i)
        if match:
               state_code.append(match.group(1))
    data_city['State Code'] = state_code
    
    pd.concat([data_city]).to_csv(r'~/data_city_cleaned.csv')

else:
    data_county = []
    for i in range(len(dict_county_code[state_code])):
        data_county.append(censusdata.download('acs5', 2018,
                                 censusdata.censusgeo([('state', state_code), ('county', dict_county_code[state_code][i]), ('block group', '*')]),
                                 ['B23025_005E', 'B19052_002E', 'B02001_002E', 'B02001_003E', 
                                  'B02001_004E', 'B02001_005E', 'B01001_001E', 'B01001_002E', 
                                  'B01001_026E', 'B15003_017E', 'B15003_018E', 'B15003_019E',
                                  'B15003_020E', 'B15003_021E', 'B15003_022E', 'B15003_023E',
                                  'B15003_024E', 'B15003_025E'], '815f420d7978fe1866f81df31947126f9e1cc460'))
    pd.concat(data_county).to_csv(r'~/data_county.csv')
    data_county = pd.read_csv(r'~/data_county.csv')
    
    data_county = data_county.rename(columns={"Unnamed: 0": "Detail", "B23025_005E": "Unemploy", "B19052_002E": "Income", "B02001_002E": "White", 
                                "B02001_003E": "Black", "B02001_004E": "Indian_Alaskan", "B02001_005E": "Asian", "B01001_001E": "Population", 
                                "B01001_002E": "Male", "B01001_026E": "Female", "B15003_017E": "High_school", "B15003_018E": "GED", 
                                "B15003_019E": "College_Less_1yr", "B15003_020E": "College_More_1YR", "B15003_021E": "Associate", 
                                "B15003_022E": "Bachelor", "B15003_023E": "Master", "B15003_024E": "Professional", 
                                "B15003_025E": "Doctorate"})
   
    block = []
    for i in data_county['Detail']:
        match = re.search(r'block group:(\S+)', i)
        if match:
                block.append(match.group(1))
    data_county['Block Group'] = block
        
    tract = []
    for i in data_county['Detail']:
        match = re.search(r'> tract:([0-9]{6})', i)
        if match:
            tract.append(match.group(1))
    data_county['Tract'] = tract
        
    county_code = []
    for i in data_county['Detail']:
        match = re.search(r'> county:([0-9]{3})', i)
        if match:
            county_code.append(match.group(1))
    data_county['County Code'] = county_code
        
    state_code = []
    for i in data_county['Detail']:
        match = re.search(r', state:([0-9]{2})', i)
        if match:
            state_code.append(match.group(1))
    data_county['State Code'] = state_code
    
    pd.concat([data_county]).to_csv(r'~/data_county_cleaned.csv')