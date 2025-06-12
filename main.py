import pandas as pd
from src.extractTransform import estabelecimentos_credenciados
from src.load import saveCsv, saveSQLite, saveMySQL

dadosEstabelecimentos = estabelecimentos_credenciados("20241")
saveCsv(dadosEstabelecimentos, "./src/datasets/estabelecimentos_credenciados.csv", ";", ".")

saveSQLite(dadosEstabelecimentos, "src/datasets/dadosEstabelecimentos.db", "estabelecimentos_credenciados")

#saveMySQL(dadosEstabelecimentos, "root", "root", "localhost", "etlbcb", "estabelecimentos_credenciados")
