# scaling-journey

Projeto para consulta de corretores cadastrados na SUSEP.
Utiliza FastAPI e SQLAlquemy.

Possui um job que atualiza diariamente os corretores PF ativos, que vendem seguros de pessoas.

O objetivo deste projeto é ter uma base de dados para pesquisar novos corretores cadastrados na SUSEP, para uma busca proativa de parceiros.

TODO LIST
1. Endpoint para novos corretores cadastrados diariamente.
2. Buscar alternativas de paralelizar a buscar sem causar abuso de uso na SUSEP.
3. Endpoint para cadastro de webhooks de atualização diária.
4. Parametrizar LOG e horário de ativação do job.
