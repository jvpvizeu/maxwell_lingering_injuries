import re
import pandas as pd
import os

# Diretório onde estão os arquivos CSV
input_directory = "/home/jvizeu/lingering_injuries/db"

# Diretório onde os arquivos CSV tratados serão salvos
output_directory = "/home/jvizeu/lingering_injuries/corrected_db"

# Expressão regular para extrair os dados
pattern = r'(\d+),([^"]*|".*?"),([^"]*|".*?")(?:\n|$)'

# Iterar sobre os arquivos CSV no diretório de entrada
for filename in os.listdir(input_directory):
    if filename.endswith(".csv"):
        # Construir o caminho completo para o arquivo de entrada
        input_file = os.path.join(input_directory, filename)
        
        # Ler o conteúdo do arquivo CSV
        with open(input_file, 'r') as file:
            text = file.read()
        
        # Extrair os dados usando a expressão regular
        matches = re.findall(pattern, text)
        
        # Organizar os dados em um DataFrame do pandas
        df = pd.DataFrame(matches, columns=['DC', 'Effect', 'Treatment'])
        
        # Construir o caminho completo para o arquivo de saída
        output_file = os.path.join(output_directory, filename)
        
        # Salvar o DataFrame como um arquivo CSV
        df.to_csv(output_file, index=False)
        
        print(f"Arquivo tratado salvo em: {output_file}")
