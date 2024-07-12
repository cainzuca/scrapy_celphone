import psycopg2
import os
import pandas as pd

data = pd.read_csv('/usr/local/airflow/tasks/src/coleta/data.csv')

server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT')

conn_str = (
    f"dbname='{database}' "
    f"user='{username}' "
    f"password='{password}' "
    f"host='{server}' "
    f"port='{port}' " 
)

# Estabelece a conexão com o banco de dados PostgreSQL
def criar_conexao():
    return psycopg2.connect(conn_str)

cnxn = criar_conexao()
cursor = cnxn.cursor()


create_table_query = '''
CREATE TABLE IF NOT EXISTS scrapy_cel (
    id SERIAL PRIMARY KEY,
    title TEXT,
    price INTEGER,
    brand VARCHAR(255),
    model VARCHAR(255),
    GB VARCHAR(255),
    ultima_atualizacao DATE
);
'''

cursor.execute(create_table_query)
cnxn.commit()


def inserir_dados(data, cursor, cnxn):
    for index, row in data.iterrows():
        insert_query = '''
        INSERT INTO scrapy_cel (title, price, brand, model, GB, ultima_atualizacao)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(insert_query, (row['title'], row['price'], row['brand'], row['model'], row['GB'], row['ultima_atualizacao']))
    cnxn.commit()

# Inserir os dados
inserir_dados(data, cursor, cnxn)

# Fechar a conexão
cursor.close()
cnxn.close()