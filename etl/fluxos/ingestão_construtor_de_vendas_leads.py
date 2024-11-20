import etl.extratores as extratores
import etl.transformadores as transformadores
import etl.carregadores as carregadores
from typing import IO


def fluxo_de_dados_de_leads_do_crm() -> IO:
    # Carregar os dados processados no BigQuery
    carregadores.bigquery.subir_tabela(
        transformadores.json_cv.processar_leads(
            extratores.construtor_de_vendas.obter_leads_da_crm()
        ),
        id_projeto="bi-santa-maria",
        id_conjunto_de_dados="administrativo",
        id_tabela="leads")


def fluxo_de_dados_historico_leads() -> IO:
    # Carregar os dados processados no BigQuery
    carregadores.bigquery.subir_tabela(
        transformadores.json_cv.processar_historico_leads(
            extratores.construtor_de_vendas.obter_historico_leads()
        ),
        id_projeto="bi-santa-maria",
        id_conjunto_de_dados="administrativo",
        id_tabela="historico_leads")


if __name__ == '__main__':
    fluxo_de_dados_de_leads_do_crm()
    fluxo_de_dados_historico_leads() 