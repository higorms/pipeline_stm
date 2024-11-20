import time
import json
import os

import requests

# Carrega as credenciais da API
def carregar_credenciais_API():
    json_path = os.path.join(os.path.dirname(__file__), '..', 'credenciais', 'dados_API.json')
    with open(json_path, 'r') as f:
        credentials = json.load(f)
    return credentials

# Obtém as credenciais
credenciais = carregar_credenciais_API()

# Atribui os valores do JSON para variáveis
API_URL = credenciais['API_URL']
API_URL_LEADS = credenciais['API_URL_LEADS']
API_URL_RESERVAS = credenciais['API_URL_RESERVAS']
API_URL_HISTORICO_LEADS = credenciais['API_URL_HISTORICO_LEADS']
EMAIL = credenciais['EMAIL']
TOKEN_DA_API_CONSTRUTOR_DE_VENDAS = credenciais['TOKEN_DA_API_CONSTRUTOR_DE_VENDAS']


def obter_vendas_da_crm() -> list[dict]:
    headers = {
        'accept': 'application/json',
        'email': EMAIL,
        'token': TOKEN_DA_API_CONSTRUTOR_DE_VENDAS,
        'Content-Type': 'application/json'
    }
    
    vendas = []
    pagina_atual = 1
    total_de_paginas = 1
    
    while pagina_atual <= total_de_paginas:
        print(f"Carregando página {pagina_atual} das vendas...")
        response = requests.get(API_URL, headers=headers, params={'pagina': pagina_atual})
        response.raise_for_status()
        dados = response.json()
        
        vendas.extend(dados['dados'])
        total_de_paginas = dados['total_de_paginas']
        pagina_atual += 1
        
        time.sleep(3)  # Espera 3 segundos entre cada requisição
    
    return vendas

def obter_leads_da_crm() -> list[dict]:
    headers = {
        'accept': 'application/json',
        'email': EMAIL,
        'token': TOKEN_DA_API_CONSTRUTOR_DE_VENDAS,
        'Content-Type': 'application/json'
    }
    
    leads = []
    pagina_atual = 1
    total_de_paginas = 1
    
    while pagina_atual <= total_de_paginas:
        print(f"Carregando página {pagina_atual} dos leads...")
        response = requests.get(API_URL_LEADS, headers=headers, params={'pagina': pagina_atual, "registros_por_pagina": 100})
        response.raise_for_status()
        dados = response.json()
        
        leads.extend(dados['dados'])
        total_de_paginas = dados['total_de_paginas']
        pagina_atual += 1
        
        time.sleep(3)  # Espera 3 segundos entre cada requisição
    
    return leads

def obter_reservas_da_crm() -> list[dict]:
    headers = {
        'accept': 'application/json',
        'email': EMAIL,
        'token': TOKEN_DA_API_CONSTRUTOR_DE_VENDAS,
        'Content-Type': 'application/json'
    }
    
    reservas = []
    pagina_atual = 1
    total_de_paginas = 1
    
    while pagina_atual <= total_de_paginas:
        print(f"Carregando página {pagina_atual} das reservas...")
        response = requests.get(API_URL_RESERVAS, 
                              headers=headers, 
                              params={'pagina': pagina_atual, "registros_por_pagina": 100})
        response.raise_for_status()
        dados = response.json()
        
        reservas.extend(dados['dados'])
        total_de_paginas = dados['total_de_paginas']
        pagina_atual += 1
        
        time.sleep(3)  # Espera 3 segundos entre cada requisição
    
    return reservas

def obter_historico_leads() -> list[dict]:
    headers = {
        'accept': 'application/json',
        'email': EMAIL,
        'token': TOKEN_DA_API_CONSTRUTOR_DE_VENDAS,
        'Content-Type': 'application/json'
    }
    
    historico = []
    pagina_atual = 1
    total_de_paginas = 1
    
    while pagina_atual <= total_de_paginas:
        print(f"Carregando página {pagina_atual} do histórico de leads...")
        response = requests.get(
            API_URL_HISTORICO_LEADS, 
            headers=headers, 
            params={'pagina': pagina_atual, "registros_por_pagina": 100}
        )
        response.raise_for_status()
        dados = response.json()
        
        historico.extend(dados['dados'])
        total_de_paginas = dados['total_de_paginas']
        pagina_atual += 1
        
        time.sleep(3)  # Espera 3 segundos entre cada requisição
    
    return historico

if __name__ == '__main__':
    vendas = obter_vendas_da_crm()
    leads = obter_leads_da_crm()
    reservas = obter_reservas_da_crm()
    historico = obter_historico_leads()
    print(f"Total de vendas obtidas: {len(vendas)}")
    print(f"Total de leads obtidos: {len(leads)}")
    print(f"Total de reservas obtidas: {len(reservas)}")
    print(f"Total de histórico de leads obtidos: {len(historico)}")