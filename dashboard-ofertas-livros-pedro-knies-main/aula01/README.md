# Aula 1: Ambiente local, leitura de dados e primeiras estatísticas

## O que vimos hoje
- Colab × ambiente local: Python, VS Code, terminal
- Git: fork, clone, commit e push pelo VS Code
- Ambiente virtual (`venv`) e `pip install -r requirements.txt`
- `if __name__ == "__main__":`
- Ler um arquivo CSV com `csv.DictReader`: cada linha vira um **dicionário**, e o arquivo vira uma **lista de dicionários**
- Percorrer a lista com `for` para **somar** (preço médio) e **contar** (livros com 5 estrelas)
- `st.metric`, `st.columns` e `st.dataframe`

## Como rodar
```powershell
.venv\Scripts\Activate.ps1
python aula01/dados.py          # testa só a leitura do arquivo
streamlit run aula01/app.py     # abre o app no navegador
```

## Atividade (entrega hoje, com prazo até o início da próxima aula)

**Parte 1: reproduza o que foi feito em aula**
- [ ] `ler_livros()` em `dados.py`, devolvendo a lista de dicionários
- [ ] `calcular_preco_medio()` e `contar_cinco_estrelas()` em `app.py`
- [ ] No `app.py`: métricas no topo (total de livros, preço médio, livros com 5 estrelas) + tabela com todos os livros

**Parte 2: atividade da aula**

Ao lado das outras métricas, mostre com `st.metric` o **preço do livro mais caro**, com o título dele
logo abaixo (`st.caption`).

> 💡 Dicas
> - O preço vem como texto: `"£51.77"`. Veja como o `calcular_preco_medio` converte o preço em número.
> - Para achar o maior: comece com o primeiro livro como "mais caro até agora" e percorra a lista com `for`, trocando sempre que achar um mais caro.
> - Precisa de mais uma coluna: `col1, col2, col3, col4 = st.columns(4)`.
>   Documentação: https://docs.streamlit.io/develop/api-reference/data/st.metric
