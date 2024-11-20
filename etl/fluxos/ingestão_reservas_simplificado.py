import etl.extratores as extratores
import etl.transformadores as transformadores
import etl.carregadores as carregadores
from typing import IO
import pandas as pd


def fluxo_de_dados_de_reservas_simplificado() -> IO:
    # Processar os leads
    df_reservas = transformadores.json_cv.processar_reservas(
        extratores.construtor_de_vendas.obter_reservas_da_crm()
    )
    
    # Criar tabela simplificada
    df_reservas_simplificado = df_reservas[["idreserva", "cliente", "situacao"]].copy()
    df_reservas_simplificado["situacao"] = "Todas as Reservas"

    # Criar tabela completa para o BI
    df_origem = df_reservas[["idreserva", "cliente", "situacao"]].copy()
    df_totais = pd.concat([df_reservas_simplificado, df_origem])
    
    # Carregar no BigQuery
    carregadores.bigquery.subir_tabela(
        df_totais,
        id_projeto="bi-santa-maria",
        id_conjunto_de_dados="administrativo",
        id_tabela="reservas_simplificado")


if __name__ == '__main__':
    fluxo_de_dados_de_reservas_simplificado() 