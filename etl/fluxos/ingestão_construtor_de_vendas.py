import etl.extratores as extratores
import etl.transformadores as transformadores
import etl.carregadores as carregadores
import pandas as pd
from typing import IO


def fluxo_de_dados_de_vendas_do_crm() -> IO:
    # Carregar os dados processados no BigQuery
    carregadores.bigquery.subir_tabela(
        transformadores.json_cv.processar_vendas(
            extratores.construtor_de_vendas.obter_vendas_da_crm()
        ),
        id_projeto="bi-santa-maria",
        id_conjunto_de_dados="administrativo",
        id_tabela="vendas")


if __name__ == '__main__':
    fluxo_de_dados_de_vendas_do_crm()