# Análise de Dados de Corridas Uber

Projeto de análise exploratória de dados de corridas Uber, com foco no volume de reservas, cancelamentos, tipos de veículo e padrões temporais e geográficos.

## Objetivos

- Analisar o volume e o status das reservas.
- Investigar cancelamentos e seus motivos.
- Comparar os tipos de veículo por volume, distância e valor.
- Identificar padrões por horário, mês e localização.
- Explorar a relação entre avaliações e tempo de viagem.

## Tecnologias

Python, Pandas, PostgreSQL, SQL, SQLAlchemy, psycopg2, Jupyter Notebook, Matplotlib e Seaborn.

## Estrutura do projeto

```text
ProjetoAnaliseDeDadosCorridasUber/
├── dados/
│   ├── criacaoBanco.txt
│   └── ncr_ride_bookings.csv
├── notebooks/
│   ├── analise_cancelamentos.ipynb
│   ├── analise_correlacao_corridas.ipynb
│   ├── analise_geografica.ipynb
│   ├── analise_temporal.ipynb
│   ├── analise_tipo_veiculo.ipynb
│   └── visao_geral_operacao.ipynb
├── src/
│   ├── conexao_banco.py
│   └── tratamento_duplicidades.py
├── requirements.txt
└── README.md
```

## Análises realizadas

- **Visão geral:** reservas, viagens concluídas, valores e distâncias.
- **Cancelamentos:** distribuição e motivos registrados.
- **Tipos de veículo:** volume, distância e valor médio.
- **Análise geográfica:** locais de embarque e destino, valores e cancelamentos.
- **Análise temporal:** demanda por horário e mês.
- **Correlação:** relação entre avaliações e tempo de viagem.

## Principais observações

- A base contém **148.767 reservas**.
- Aproximadamente **62% das reservas foram concluídas**.
- A demanda apresenta pico por volta das **18h**, com movimento elevado entre **16h e 20h**.
- A maior parte dos cancelamentos analisados é atribuída aos motoristas.
- As correlações calculadas entre avaliações e tempo de viagem são próximas de zero.

Os resultados se referem à base analisada e não representam necessariamente toda a operação da Uber.

## Configuração do banco de dados

O projeto utiliza PostgreSQL. Para preparar o banco, siga os passos abaixo.

### 1. Criar o banco

Instale e inicie o PostgreSQL. No pgAdmin, conecte-se ao servidor, abra a ferramenta **Query Tool** e execute:

```sql
CREATE DATABASE db_ncr_ride_bookings;
```

Depois, conecte-se ao banco `db_ncr_ride_bookings`.

### 2. Criar a tabela

Abra o arquivo `dados/criacaoBanco.txt`. Copie o SQL do arquivo para a Query Tool do banco `db_ncr_ride_bookings` e execute-o. Esse script cria a tabela `ncr_ride_bookings_raw`, que receberá os dados originais do CSV.

### 3. Importar o CSV

Importe `dados/ncr_ride_bookings.csv` para a tabela `ncr_ride_bookings_raw` criada no passo anterior.

No pgAdmin:

1. No painel **Browser**, localize `db_ncr_ride_bookings` → **Schemas** → **public** → **Tables**.
2. Clique com o botão direito em `ncr_ride_bookings_raw` e escolha **Import/Export Data**.
3. Selecione **Import**, escolha o arquivo `dados/ncr_ride_bookings.csv` e configure o formato como **CSV**.
4. Habilite **Header**.
5. Use a vírgula como delimitador e confira se a codificação está compatível com o arquivo (normalmente UTF-8).
6. Inicie a importação e verifique se o processo terminou sem erros.

A ordem e os nomes das colunas do CSV devem corresponder à estrutura da tabela. Se a importação falhar por incompatibilidade de tipos, confira o SQL em `dados/criacaoBanco.txt` e as opções de importação.

### 4. Tratar duplicidades

Depois de importar os dados originais, execute:

```bash
python src/tratamento_duplicidades.py
```

O script remove duplicidades com base em `Booking_ID` e grava os dados tratados na tabela `ncr_ride_bookings`. Confira as configurações de conexão no arquivo antes de executar.

**Importante:** o script grava os dados tratados usando `append`. Se for executado novamente, pode inserir registros duplicados na tabela de destino. Limpe ou recrie a tabela de destino antes de repetir o processamento.

## Instalação e execução

Com Python instalado, abra o terminal na pasta do projeto e execute:

```bash
pip install -r requirements.txt
jupyter notebook
```

Abra os notebooks na pasta `notebooks/` e execute as células conforme a análise desejada.

## Segurança

Configure usuário, senha, host e porta do PostgreSQL nos scripts de conexão conforme o seu ambiente. Não publique senhas ou credenciais reais no GitHub; prefira variáveis de ambiente ou um arquivo `.env` excluído do versionamento.
