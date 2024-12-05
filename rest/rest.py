from flask import Flask, json, request, redirect, abort, jsonify
import os
import psycopg2
from datetime import date

api = Flask(__name__)
db_tables = {
    'Cielo':('Aeroporto', 'ArrPart', 'LuogoAeropoto',
             'Volo', 'Compagnia')
}

def get_db_connection(database:str):
    conn = psycopg2.connect(
            host="172.21.24.242",   #da cambiare ogni volta
            database=database,      #con "ip addr show"
            user='postgres',        #172.21.24.242
            password='postgres',
            port='5432'
            )
    conn.autocommit = True
    return conn

def table_fetch(req_database:str, req_table:list):
    with get_db_connection(database=req_database) as conn:
        with conn.cursor() as cur:
            cur.execute(f'SELECT * FROM {req_table};')
            table = cur.fetchall()
    return table

@api.route('/', methods=['GET', 'POST'])
def index():
    redata = request.json.get('context', 0)
    print(f"\n\n{redata}\n\n")
    req_db = redata['req_db']

    match int(req_db):
        case 1:
            database_name = 'Cielo'
        case _:
            abort(422)
    
    try:
        table_name = redata['req_tab']
        if table_name not in db_tables[database_name]:
            raise TypeError(f"{table_name} does not exist in this database!")

        sendata = table_fetch(req_database=database_name,
                              req_table=table_name)
    except Exception as e:
        sendata = "Errore, query invalida"
            
    return jsonify(sendata)



if __name__ == '__main__':
    api.run(host="0.0.0.0", port=4160)