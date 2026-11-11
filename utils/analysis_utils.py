import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# É necessário instalar o pacote jinja2 (pip install jinja2)
def df_summary_report(df: pd.DataFrame) -> pd.DataFrame:
    """
    Gera um relatório descritivos dos valores do dataframe.

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame a ser analisado.
    
    Retorno
    -------
    pandas.DataFrame
        DataFrame contendo o resumo das colunas com as seguintes informações:

        - nome_coluna : nome da coluna
        - tipo : tipo de dado (dtype)
        - valores_nao_vazios : quantidade de valores não nulos
        - valores_vazios : quantidade de valores nulos
        - valores_unicos : quantidade de valores únicos
        - valor_mais_frequente : valor com maior ocorrência
        - frequencia : frequência do valor mais recorrente
        - perc_unicidade : porcentagem de valores únicos
        - perc_vazios : porcentagem de valores ausentes
        - memoria_mb : consumo de memória da coluna
    """

    moda = df.mode().iloc[0]

    mem_consumo = df.memory_usage(deep=True, index=False)/1024**2
    total = sum(mem_consumo)

    freq = df.apply(
        lambda col: col.value_counts(dropna=True).iloc[0]
        if not col.dropna().empty else None
    )

    resumo = pd.DataFrame({
        'Coluna': df.columns,            #Lista os nomes das colunas do DataFrame.
        'Tipo': df.dtypes.values,        #Retorna o tipo de dado (dtype) de cada coluna.
        'Quantidade de Dados Não Vazios': df.notna().sum().values,  #Conta a quantidade de valores não nulos por coluna.
        'Quantidade de Dados Vazios': df.isna().sum().values,       #Conta a quantidade de valores nulos (NaN) por coluna.
        'Valores Únicos': df.nunique().values,       #Conta a quantidade de valores únicos de cada coluna
        'Valor mais Frequente': moda,    #Calcula a moda de cada coluna    
        'Frequência': freq,               #Mostra a frequência da moda
        'Porcentagem de Unicidade': ((df.nunique() / len(df)) * 100).round(2).values,    #Cardinalidade - baixa cardinalidade indica alta repetição; alta cardinalidade indica baixa repetição
        'Porcentagem de Valor Vazios (%)': (df.isna().mean() * 100).round(2).values,  #Calcula a porcentagem de valores nulos por coluna.
        f'Consumo de Memória - Total: {total:.2f} (MB)': mem_consumo    #Calcula a quantidade de memória usada pelo dataset
    }).reset_index(drop=True)

    #colormaps
    cmap_vazios = sns.light_palette("#BD2A2E", as_cmap=True)
    cmap_unicidade = sns.light_palette("#13678A", as_cmap=True)
    cmap_unique = sns.light_palette("#1f77b4", as_cmap=True)
    cmap_freq = sns.light_palette("#13678A", as_cmap=True)

    styled = (resumo.style
        .set_properties(**{
            'background-color': "#101719",
            'color': '#E0E0E0',  
            'border': '1px solid #2F3D40',
            'text-align': 'center'
        })
        .background_gradient(subset=['Porcentagem de Valor Vazios (%)'], cmap=cmap_vazios, vmin=0, vmax=100)
        .background_gradient(subset=['Porcentagem de Unicidade'], cmap=cmap_unicidade, vmin=0, vmax=100)
        .background_gradient(subset=["Valores Únicos"],cmap=cmap_unique)
        .background_gradient(subset=["Frequência"],cmap=cmap_freq)
        .background_gradient(subset=[f"Consumo de Memória - Total: {total:.2f} (MB)"], cmap=cmap_freq)
        .bar(subset=['Quantidade de Dados Vazios'], color="#BD2A2E")
        .format({'Porcentagem de Valor Vazios (%)': '{:.2f}', 'Porcentagem de Unicidade': '{:.2f}'})
        .set_table_styles([{
                'selector': 'th',
                'props': [
                    ('background-color', "#0c2845"),
                    ('color', 'white'),
                    ('text-align', 'center'),
                    ('font-size', '13px')
                ]
            }
        ])
        .set_properties(
            subset=pd.IndexSlice[:, resumo.columns[0]],**{
                'background-color': '#012030',
                'font-weight': 'bold',
                'color': '#FFFFFF'
            })
        
    )
    return styled
#----------------------------------------------------------------------------------------------------------------------
def plot_click(df):
    """
    Gera um gráfico de barras comparando a contagem de cliques e não cliques
    entre os grupos de controle e experimental de um Teste A/B.
    
    Parâmetros
    ----------
    df : pandas.DataFrame
        DataFrame contendo os dados do experimento.

    Retorno
    -------
        Exibe o gráfico utilizando Matplotlib.
    """

    ordem = ["con", "exp"]
    rotulos = {"con": "Controle", "exp": "Experimental"}

    fig, ax = plt.subplots(figsize=(7, 5))
    sns.countplot(data=df, x="group", hue="click", order = ordem,
                palette={0: "#D92525", 1: "#3D5A73"}, ax=ax)

    ax.set_xticks(range(len(ordem)))
    ax.set_xticklabels([rotulos[g] for g in ordem])
    ax.set_title("Contagem de Cliques - Controle vs. Experimental", weight="bold")
    ax.set_xlabel("")
    ax.set_ylabel("Contagem")
    ax.legend(title="Clicou?", labels=["Não", "Sim"])


    totais = df["group"].value_counts()
    # ax.containers[0] = barras de click=0 (uma por grupo); ax.containers[1] = click=1
    for container in ax.containers:
        for barra, grupo in zip(container, ordem):
            pct = barra.get_height()/totais[grupo]*100
            ax.annotate(f"{pct:.1f}%", (barra.get_x() + barra.get_width()/2, barra.get_height()),
                        ha="center", va="bottom", fontsize=10)
    plt.show()
