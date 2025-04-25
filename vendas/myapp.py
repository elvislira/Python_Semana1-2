from src.processor import processar_vendas
from pathlib import Path
import os


if __name__ == '__main__':
    INPUT_PATH = f'{Path(__file__).parent}/data/vendas.csv'
    OUTPUT_PATH = f'{Path(__file__).parent}/output/relatorio.json'

    os.system('clear')

    processar_vendas(INPUT_PATH, OUTPUT_PATH)