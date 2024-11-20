import etl.extratores as extratores
import etl.transformadores as transformadores
import etl.carregadores as carregadores
from typing import IO
import pandas as pd


def fluxo_de_dados_de_leads_simplificado() -> IO:
    # Processar os leads
    df_leads = transformadores.json_cv.processar_leads(
        extratores.construtor_de_vendas.obter_leads_da_crm()
    )
    
    # Criar tabela simplificada
    df_leads_simplificado = df_leads[["idlead", "nome", "situacao"]].copy()
    df_leads_simplificado["situacao"] = "Todos os Leads"

    # Criar tabela completa para o BI
    df_origem = df_leads[["idlead", "nome", "situacao"]].copy()
    df_totais = pd.concat([df_leads_simplificado, df_origem])
    
    # Carregar no BigQuery
    carregadores.bigquery.subir_tabela(
        df_totais,
        id_projeto="bi-santa-maria",
        id_conjunto_de_dados="administrativo",
        id_tabela="leads_simplificado")


if __name__ == '__main__':
    fluxo_de_dados_de_leads_simplificado() 