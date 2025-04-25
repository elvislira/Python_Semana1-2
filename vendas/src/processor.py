from src.utils import log_time
from src.filemanager import FileManager
import csv
import json


def _retorna_dados_arquivo(input_path: str) -> list:
    # Ler o arquivo CSV
    with FileManager(input_path) as file:
        reader = csv.DictReader(file)
        vendas = list(reader)

    return vendas

def _retorna_vendas_validas(vendas: list) -> list:
    # Validar os dados do arquivo
    vendas_validas = []

    for venda in vendas:
        try:
            venda["quantidade"] = int(venda["quantidade"])
            venda["preco_unitario"] = float(venda["preco_unitario"])
            vendas_validas.append(venda)
        except (ValueError, KeyError) as e:
            print(f'⚠️ Erro na venda ID {venda.get('id')}: {e}')

    return vendas_validas

def _calcula_metricas(vendas: list) -> list:
    # Calcular métricas
    qtd_vendas = len(vendas)
    produtos = [registro["produto"] for registro in vendas]
    produto_mais_vendido = max(set(produtos), key=produtos.count)
    receita_total = sum(registro["quantidade"] * registro["preco_unitario"] for registro in vendas)
    media_preco = receita_total / qtd_vendas if qtd_vendas > 0 else 0

    return [
        qtd_vendas,
        produto_mais_vendido,
        receita_total,
        media_preco
    ]

def _gera_relario(metricas: list) -> dict:
    relatorio = {
        "qtd_vendas": metricas[0],
        "produto_mais_vendido": metricas[1],
        "receita_total": metricas[2],
        "media_preco": metricas[3]
    }

    return relatorio

def _salva_relatorio(relatorio: dict, output_file: str) -> None:
    with FileManager(output_file, 'w') as file:
        json.dump(relatorio, file, indent=2)

    print(f'✅ Relatório gerado em: {output_file}')


@log_time
def processar_vendas(input_path, output_path):
    try:
        vendas = _retorna_dados_arquivo(input_path)
        vendas_validas = _retorna_vendas_validas(vendas)
        metricas = _calcula_metricas(vendas_validas)
        relatorio = _gera_relario(metricas)
        _salva_relatorio(relatorio, output_path)
    except FileExistsError:
        print(f'❌ Arquivo não encontrado: {input_path}')
