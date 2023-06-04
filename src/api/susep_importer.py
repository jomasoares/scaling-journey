import requests
import schedule
import time

from datetime import datetime

from . import crud, models
from .database import SessionLocal

page_size = 6

def susep_daily_job(log : bool, start_time : str):
    schedule.every().day.at(start_time).do(import_from_susep(log=True))

#TODO: importar PJ tambem.
def import_from_susep(log : bool):
    if log:
        print("Starting daily Job at " + datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
    num_pages = 30
    current_page = 1
    while current_page <= num_pages:
        if log:
            print("Importing page " + str(current_page) + "...", end='')
        api_url = "https://www2.susep.gov.br/safe/corretoresapig/dadospublicos/pesquisar?tipoPessoa=PF&produto=303&situacao=101&produtos=303&situacoes=101&page="
        response = requests.get(api_url+str(current_page))
        json = response.json()
        num_pages = json["retorno"]["totalRegistros"] / page_size
        print("of " + str(num_pages) + " pages.")
        insert_corretores(corretores=json["retorno"]["registros"])
        current_page+=1
        time.sleep(0.2) # Delay to avoid status 429
    if log:
        print("Ending daily Job at " + datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))

    

def insert_corretores(corretores : any):
    today = datetime.today().strftime("%d-%m-%Y")
    db = SessionLocal()
    for corretor in corretores:
        corretor_in_db = crud.get_corretor(db, corretor_id=corretor["corretorId"])
        if corretor_in_db == None:
            db_corretor = models.Corretor(
                corretorId=corretor["corretorId"],
                cpfCnpj=corretor["cpfCnpj"],
                protocolo=corretor["protocolo"],
                nome=corretor["nome"],
                recadastrado=corretor["recadastrado"],
                situacao=corretor["situacao"],
                produtos=corretor["produtos"],
                dataInsercao=today)
            crud.create_corretor(db=db, corretor=db_corretor)
    db.close()




