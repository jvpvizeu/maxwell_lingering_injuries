import pandas as pd
import os

csv_directory = "/home/jvizeu/lingering_injuries/corrected_db"

csv_files = [file for file in os.listdir(csv_directory) if file.endswith(".csv")]

# Iterar sobre os arquivos CSV e imprimir seu conteúdo
for csv_file in csv_files:
    # Construa o caminho completo para o arquivo CSV
    csv_path = os.path.join(csv_directory, csv_file)
    # Leia o arquivo CSV em um DataFrame
    df = pd.read_csv(csv_path)
    # Imprima o DataFrame
    print(f"Conteúdo do arquivo CSV '{csv_file}':")
    print(df)
