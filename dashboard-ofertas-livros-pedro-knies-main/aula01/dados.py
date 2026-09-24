from pathlib import Path
import csv

PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"

def ler_livros():
    livros = []
    try:
        with open(CAMINHO_LIVROS, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            
            print("--- CABEÇALHOS ENCONTRADOS NO CSV ---")
            print(leitor.fieldnames)
            
            for linha in leitor:
                livros.append(linha)
                
            print(f"Total de linhas lidas: {len(livros)}")
            if livros:
                print("Primeira linha:", livros[0])
                
    except Exception as erro:
        print("Erro ao ler o arquivo:", erro)
        
    return livros

if __name__ == "__main__":
    ler_livros()