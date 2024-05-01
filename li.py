import shutil
import os
import pandas as pd
import tabula
from tabula.io import read_pdf
pdf_path = "/home/jvizeu/Downloads/maxwell_li.pdf"
output_directory = "/home/jvizeu/lingering_injuries/db"

nome_tabelas = ("acid_table", "bldg_table", "cold_table", "fire_table", "frce_table", "lgtn_table", "ncrt_table", "prcg_table", "pois_table", "psyc_table", "rdnt_table", "slsh_table", "tndr_table")

i = 0

# Defina as páginas das tabelas
pages = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]

# Lista para armazenar os nomes dos arquivos CSV
csv_files = []

for page in pages:
    tables = tabula.read_pdf(pdf_path, pages=page, multiple_tables=True)
    # Se houver tabelas nesta página
    if tables:
        # Concatenar todos os DataFrames em um único DataFrame
        concatenated_df = pd.concat(tables)
        # Defina o nome do arquivo CSV
        csv_file = f"{nome_tabelas[i]}.csv"
        # Construa o caminho completo para o arquivo CSV
        csv_path = os.path.join(output_directory, csv_file)
        # Salve o DataFrame como um arquivo CSV
        concatenated_df.to_csv(csv_path, index=False)
        print(f"Arquivo CSV salvo para página {page}")
    i += 1
print("Processo concluído!")