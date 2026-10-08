"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st

import dados

def montar_tabela(livros):
    """Prepara as linhas que aparecem na tabela, com nomes de coluna amigáveis."""
    tabela = []
    for livro in livros:
        linha = {
            "Título": livro["titulo"],
            "Categoria": livro["categoria"],
            "Nota": livro["nota"] * "⭐",
            "Preço": f"£ {livro["preco"]:.2f}",
            "Faixa": classificar_preco(livro["preco"])
        }
        tabela.append(linha)
    return tabela

def classificar_preco(preco):
    """Classifica um preço em libras em uma faixa de texto."""
    if preco < 20:
        return "Barato"
    elif preco <= 40:
        return "Médio"
    else:
        return "Caro"

def contar_por_faixa(livros):
    """Conta quantos livros existem em cada faixa de preço: {"Caro": 403, ...}"""
    contagem = {}
    for livro in livros:
        faixa = classificar_preco(livro["preco"])
        if faixa in contagem:
            contagem[faixa] = contagem[faixa] + 1
        else:
            contagem[faixa] = 1

    return contagem

def listar_categorias(livros):
    categorias = []
    for livro in livros:
        if livro["categoria"] not in categorias:
            categorias.append(livro["categoria"])

    categorias.sort()
    return categorias


def filtrar_por_categoria(livros, categoria):
    resultado = []
    for livro in livros:
        if livro["categoria"] == categoria:
            resultado.append(livro)
    return



def main():
    st.set_page_config(page_title="Dashboard de Livros", page_icon="📚", layout="wide")
    st.title("📚 Dashboard de Livros")

    colbusca, colcategorias = st.columns(2)

    busca = colbusca.text_input("pesquisar por titulo ou categoria", "")
    buscacategoria = colcategorias.text_input("pesquisar por categoria", "")

    livros = dados.carregar_livros()
    if busca:
        busca = busca.lower()
        livros_filtrados = [
            livro for livro in livros 
            if busca in
            livro["titulo"].lower() or busca in livro["categoria"].lower()
        ]

    else:
        livros_filtrados = livros
    
    if not livros_filtrados:
        st.info("Nenhum livro encontrado para a busca informada.", icon="🔍")
        return

    if buscacategoria:
        buscacategoria = buscacategoria.strip().lower()
    
    if buscacategoria == "todas":
        livros_filtrados = livros
    else:
        livros_filtrados = [
            livro for livro in livros_filtrados
            if buscacategoria in livro["categoria"].lower()
        ]

    if not livros_filtrados:
        st.info("Nenhum livro encontrado para a busca informada.", icon="🔍")
        return
    tabela = montar_tabela(livros_filtrados)



    col1, col2, col3, col4 = st.columns(4)
    qtd_livros_encontrados = len(livros_filtrados)
    col1.metric("Livros encontrados", qtd_livros_encontrados)

    preco_medio = dados.calcular_preco_medio(livros_filtrados)
    col2.metric("Preço médio", f"£{preco_medio:.2f}")

    cinco_estrelas = dados.contar_cinco_estrelas(livros_filtrados)
    col3.metric("Qtd. livros 5 Estrelas", cinco_estrelas)

    mais_caro = dados.encontrar_mais_caro(livros_filtrados)
    col4.metric("Livro mais caro", f"£{mais_caro["preco"]}")
    col4.caption(mais_caro["titulo"])



    st.dataframe(tabela)


if __name__ == "__main__":
    main()