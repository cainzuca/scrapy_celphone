# %%
import pandas as pd
import re
import datetime
import subprocess
import numpy as np

subprocess.call('echo oi', shell=True)

def convert_price(value):
    return float(value.replace('.', '').replace(',', '.'))

data = pd.read_csv(r'/usr/local/airflow/tasks/src/coleta/data.csv', converters={'price':convert_price})
data.head()

data['price'] = data['price'].astype(str)
data['price'] = data['price'].astype('Float64')

# %%
'''data['brand'] = np.select(
    [
        data['title'].str.contains('Samsung', na=False),
        data['title'].str.contains('Moto|Motorola', na=False),
        data['title'].str.contains('Lenovo', na=False),
        data['title'].str.contains('Blackberry', na=False),
        data['title'].str.contains('LG|Lg|lg', na=False),
        data['title'].str.contains('IPHONE|iPhone|IPhone', na=False)
    ],
    [
        'Samsung',
        'Motorola',
        'Lenovo',
        'Blackberry',
        'LG',
        'iPhone'
    ],
    default='Marca desconhecida'
)
'''

def determine_brand(title):
    if 'Samsung' in title:
        return 'Samsung'
    elif 'Moto' in title or 'Motorola' in title:
        return 'Motorola'
    elif 'Lenovo' in title:
        return 'Lenovo'
    elif 'Blackberry' in title:
        return 'Blackberry'
    elif 'LG' in title or 'Lg' in title or 'lg' in title:
        return 'LG'
    elif 'IPHONE' in title or 'iPhone' in title or 'IPhone' in title:
        return 'iPhone'
    else:
        return 'Marca desconhecida'

# Aplicar a função personalizada
data['brand'] = data['title'].apply(determine_brand)
# %%
patterns = {
    'Samsung': r'Galaxy \w+',
    'Motorola': r'Moto \w+',
    'Lenovo': r'Lenovo \w+',
    'Blackberry': r'Blackberry\d+',
    'LG': r'(G\d+ \w+)|(K\d+ \w+)',
    'iPhone': r'(iPhone \d+)|(iPhone \w+)'
}

def extract_model(title):
    for brand, pattern in patterns.items():
        match = re.search(pattern, title)
        if match:
            return match.group(0)
    return 'Modelo desconhecido'

data['model'] = data['title'].apply(extract_model)

# %%
data['title'] = data['title'].str.upper()

# %%
patterns = {
    'a': r'(\d+GB)|(\d+ GB+)'
}

def extract_model(title):
    for brand, pattern in patterns.items():
        match = re.search(pattern, title)
        if match:
            return match.group(0)
    return 'GB desconhecido'

data['GB'] = data['title'].apply(extract_model).str.replace(' ','')
data['GB'] = np.where(data['GB']=='GBdesconhecido','GB desconhecido',data['GB'])

# %%
data['ultima_atualizacao'] = datetime.datetime.today().date()


data.to_csv('/usr/local/airflow/tasks/src/coleta/data.csv')