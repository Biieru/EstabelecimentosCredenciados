# EstabelecimentosCredenciadosDS
Estudo sobre os estabelecimentos credenciados para operações com cartões de crédito e débito, utilizando dados da API do Banco Central (BCB).

# **Estatísticas de Estabelecimentos Credenciados**

Quantidade de estabelecimentos credenciados e ativos por bandeira e função do cartão, reportados trimestralmente.

## **Parâmetros**

| Nome | Tipo | Título | Descrição |
| --- | --- | --- | --- |
| trimestre | texto | Trimestre | Trimestre de referência no formato AAAAQ (A=ano, Q=trimestre 1-4) |
| $format | texto | $format | Tipo de conteúdo que será retornado |
| $select | texto | $select | Propriedades que serão retornadas |
| $filter | texto | $filter | Filtro de seleção de entidades |
| $orderby | texto | $orderby | Propriedades para ordenação das entidades |
| $skip | inteiro | $skip | Índice da primeira entidade que será retornada |
| $top | inteiro | $top | Número máximo de entidades que serão retornadas |

## **Resultado**
| Nome | Tipo | Título | Descrição |
| --- | --- | --- | --- |
| trimestre | texto | Trimestre | Trimestre de referência no formato AAAAQ |
| bandeira | texto | Bandeira | Bandeira do cartão (ex: Visa, Mastercard, etc) |
| funcaoCartao | texto | Função do Cartão | Função do cartão (crédito, débito, etc) |
| qtdEstabCredenciados | inteiro | Quantidade de Estabelecimentos Credenciados | Número total de estabelecimentos credenciados |
| qtdEstabAtivos | inteiro | Quantidade de Estabelecimentos Ativos | Número de estabelecimentos ativos |

## **Links**
- [BCB - Estabelecimentos Credenciados](https://dadosabertos.bcb.gov.br/dataset/estatisticas-meios-pagamentos/resource/523552bd-477b-4dcf-93aa-48ffc3c7a41b)

## **Grupo**
Gabriel Coelho de Araújo<br />
Cauan Warlley<br />


