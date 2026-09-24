import streamlit as st
from dados import ler_livros


st.set_page_config(page_title="Dashboard de Livros", layout="wide")


livros = ler_livros()

def calcular_preco_medio(lista_livros):
    """Calcula o preço médio dos livros convertendo a string de preço para float."""
    if not lista_livros:
        return 0.0
    
    soma_precos = 0.0
    contador = 0
    
    for livro in lista_livros:
        preco_str = str(livro.get("preco", "0")).replace("£", "").replace("$", "").strip()
        try:
            soma_precos += float(preco_str)
            contador += 1
        except ValueError:
            continue
            
    return soma_precos / contador if contador > 0 else 0.0

def contar_cinco_estrelas(lista_livros):
    """Conta quantos livros possuem avaliação de 5 estrelas baseado na coluna 'nota'."""
    contador = 0
    for livro in lista_livros:
        nota = str(livro.get("nota", "")).strip().lower()
        if nota in ["five", "5", "5.0"]:
            contador += 1
    return contador

def encontrar_livro_mais_caro(lista_livros):
    """Percorre a lista para encontrar o livro de maior preço e retorna o título e o preço."""
    if not lista_livros:
        return "Nenhum", 0.0
    
    mais_caro = lista_livros[0]
    try:
        preco_max = float(str(mais_caro.get("preco", "0")).replace("£", "").replace("$", "").strip())
    except ValueError:
        preco_max = 0.0
    
    for livro in lista_livros:
        try:
            preco = float(str(livro.get("preco", "0")).replace("£", "").replace("$", "").strip())
            if preco > preco_max:
                preco_max = preco
                mais_caro = livro
        except ValueError:
            continue
            
    titulo = mais_caro.get("titulo", "Desconhecido")
    return titulo, preco_max

st.title("📚 Dashboard de Biblioteca")
st.markdown("---")

total_livros = len(livros)
preco_medio = calcular_preco_medio(livros)
qtd_cinco_estrelas = contar_cinco_estrelas(livros)
titulo_mais_caro, preco_mais_caro = encontrar_livro_mais_caro(livros)


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total de Livros", total_livros)

with col2:
    st.metric("Preço Médio", f"£{preco_medio:.2f}")

with col3:
    st.metric("Livros 5 Estrelas", qtd_cinco_estrelas)

with col4:
    st.metric("Livro Mais Caro", f"£{preco_mais_caro:.2f}")
    st.caption(titulo_mais_caro)  

st.markdown("---")


st.subheader("📋 Relação de Livros Cadastrados")
if livros:
    st.dataframe(livros, use_container_width=True)
else:
    st.warning("Nenhum dado encontrado ou arquivo `livros.csv` ausente.")