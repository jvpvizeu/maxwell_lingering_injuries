import pandas as pd
import random
import os
import re

current_directory = os.path.dirname(__file__)
nome_tabelas = ("acid", "bldg (bludgeoning)", "cold", "fire", "frce (force)", "lgtn (lightning)", "ncrt (necrotic)", "prcg (piercing)", "pois (poison)", "psyc (psychic)", "rdnt (radiant)", "slsh (slashing)", "tndr (thunder)")


def verifica_palavras_juntas(texto, palavra1, palavra2):
    padrao = r'\b{} {}\b'.format(re.escape(palavra1), re.escape(palavra2))
    if re.search(padrao, texto):
        return True
    else:
        return False
    
def verifica_palavra_na_lista(lista, palavra):
    for item in lista:
        item_sem_espacos = item.replace(" ", "").lower()
        palavra_sem_espacos = palavra.replace(" ", "").lower()
        if palavra_sem_espacos in item_sem_espacos:
            return True
    return False

while True:
    for damage in nome_tabelas:
        print(f'{damage}, ')
    tipo_de_dano = input("Insert damage type (four letter):")
    if not verifica_palavra_na_lista(nome_tabelas, tipo_de_dano):
        print("Not in the avaiable options")
        continue

    csv_file_path = f"{current_directory}/corrected_db/{tipo_de_dano}_table.csv"
    df = pd.read_csv(csv_file_path)

    dice_roll = random.randint(3,18)
    print(f"The table roll was {dice_roll} !")

    num_linhas = df.shape[0]

    def calcular_efeito(rolagem):
        for i in range(num_linhas):
            DC = df["DC"][i]
            if rolagem >= DC:
                efeito = df.iloc[i]
        return efeito
    
    efeito = calcular_efeito(dice_roll)
    print(efeito["Effect"])
    print(efeito["Treatment"])
    texto_treatment = efeito["Treatment"].lower()
    if verifica_palavras_juntas(texto_treatment, 'limb', 'table'):
        limb_file_path = f"{current_directory}/corrected_db/limb_table.csv"
        limbdf = pd.read_csv(limb_file_path)
        dice_roll = random.randint(1,20)
        print(f"The roll for lost member is {dice_roll} !")
        print(f'The lost member was {limbdf["Body Area"][dice_roll]} !')

    if verifica_palavras_juntas(texto_treatment, 'appendage', 'table'):
        appendage_file_path = f"{current_directory}/corrected_db/appendage_table.csv"
        appendagedf = pd.read_csv(appendage_file_path)
        dice_roll = random.randint(1,20)
        print(f"The roll for lost member is {dice_roll} !")
        print(f'The lost appendage was {appendagedf["Body Area"][dice_roll]} !')

    if verifica_palavras_juntas(texto_treatment, 'scar', 'chart'):
        scar_file_path = f"{current_directory}/corrected_db/scar_table.csv"
        scardf = pd.read_csv(scar_file_path)
        dice_roll = random.randint(1,100)
        print(f"The roll for scar location is {dice_roll} !")
        print(f'The scar is in {scardf["Body Area"][dice_roll]} !')
    print("\n")