import re
from pathlib import Path

from google.oauth2 import service_account
import pandas_gbq


CAMINHO_PARA_CREDENCIAIS = (Path(__file__)
                            .parent
                            .parent
                            / "credenciais"
                            / "conta_de_serviço.json")

def subir_tabela(tabela, id_projeto, id_conjunto_de_dados, id_tabela, adicionar=False):
    tabela.columns = [re.sub(r"\W", "_", coluna) for coluna in tabela.columns]

    destino = f"{id_conjunto_de_dados}.{id_tabela}"
    credenciais = service_account.Credentials.from_service_account_file(CAMINHO_PARA_CREDENCIAIS)

    pandas_gbq.to_gbq(tabela,
                      destino,
                      project_id=id_projeto,
                      if_exists=("replace" if not adicionar else "append"),
                      credentials=credenciais)
    print(f"Dados enviados com sucesso para {destino} no BigQuery.")
