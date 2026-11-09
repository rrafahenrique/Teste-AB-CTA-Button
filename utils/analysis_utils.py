import pandas as pd
import seaborn as sns

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

