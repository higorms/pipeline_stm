from etl.fluxos.ingestão_construtor_de_vendas_leads import fluxo_de_dados_de_leads_do_crm
from etl.fluxos.ingestão_leads_simplificado import fluxo_de_dados_de_leads_simplificado

# Executa os fluxos sequencialmente
fluxo_de_dados_de_leads_do_crm()
fluxo_de_dados_de_leads_simplificado() 