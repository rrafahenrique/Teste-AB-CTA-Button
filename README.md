![Badge-Em Andamento](https://img.shields.io/badge/Status-Em_Andamento-orange) ![Bagde-Version](https://img.shields.io/badge/Version-1.0-blue)


# 1. Sobre o projeto
Este projeto tem como objetivo explorar a aplicação de **testes A/B** por meio de três cenários experimentais distintos. A proposta é demonstrar como interpretar os resultados de um experimento, avaliar a existência de diferenças estatisticamente significativas e identificar possíveis problemas na distribuição dos participantes entre os grupos.

Os experimentos foram construídos para abordar três situações fundamentais:

- **Vitória clara:** identificação de um efeito estatisticamente significativo entre as variantes.
- **Ausência de evidências suficientes:** situação em que não se rejeita a hipótese nula, explorando também o conceito de poder estatístico.
- **Sample Ratio Mismatch (SRM):** identificação de uma distribuição inadequada dos participantes entre os grupos experimentais.

Todos os cenários utilizam os mesmos parâmetros estatísticos, definidos previamente à análise dos resultados, garantindo consistência metodológica e evitando ajustes orientados pelos resultados observados.

# 2. Problema de Negócio
Você trabalha no departamento de ciência de dados de um empresa que oferece cursos, bootcamps e suporte de carreira para ajudar ajudar alunos a conquistarem um vaga na área de dados. Um belo dia você é designado para realizar um Teste AB, o objetivo é identificar qual versão do botão de chamada para ação (CTA) na página inicial da empresa apresenta um desempenho superior, com base na métrica de taxa de cliques (CTR, na sigla em inglês):

- **Grupo de Controle - (Versão A)** Exposto ao botão de CTA atual ("Garantir teste gratuito").
- **Grupo Experimental - (Versão B):** Exposto ao novo botão de CTA, de caráter mais geral ("Inscreva-se agora").

![banner](img/banner.png)

A taxa de cliques (CTR) mede a porcentagem de usuários que clicam em um botão ou link após visualizá-lo. Para a empresa, o CTR é importante, pois reflete o engajamento dos usuários com a plataforma e auxilia na avaliação da eficácia dos botões de chamada para ação em gerar inscrições e conversões.

Por fim, os resultados deste teste ajudarão a decidir se o novo botão deve ser implementado na página inicial.

## 2.1 Estrutura do dataset
- `data-raw/` - datasets (CSV)
- `notebooks/` - notebooks de análise (.ipynb)
- `utils/` - funções auxiliares


# 3. Parâmetros experimentais
Os três experimentos utilizam os mesmos parâmetros, estabelecidos antes da observação dos resultados.

| Parâmetro | Valor | Significado |
|---|---:|---|
| Nível de significância (α) | 0,05 | Probabilidade máxima aceita de cometer um erro do tipo I, ou seja, rejeitar H₀ quando ela é verdadeira. |
| Poder estatístico (1 − β) | 0,80 | Probabilidade de detectar um efeito de determinada magnitude quando ele realmente existe. |
| Efeito mínimo detectável (MDE) | 0,02 | Menor diferença absoluta considerada relevante para o negócio, equivalente a 2 pontos percentuais. |

## 3.1 Interpretação dos parâmetros

- **α = 0,05:** estabelece um limite de 5% para o risco de falso positivo.
- **Poder = 0,80:** estabelece uma probabilidade de 80% de detectar o efeito definido no planejamento, caso ele exista.
- **MDE = 0,02:** representa uma diferença absoluta de 2 pontos percentuais entre as taxas de conversão das variantes.

Esses parâmetros orientam o planejamento e a interpretação dos experimentos e devem permanecer constantes entre os cenários.

# 4. Cenários analisados

O projeto contempla três cenários, cada um desenvolvido para demonstrar uma situação específica encontrada na prática de experimentação A/B.

| Cenário | Arquivo | Taxas de conversão esperadas | Objetivo |
|---|---|---|---|
| 1 | `cenario1-vitoria_clara` | 20% vs. 22% | Demonstrar um efeito estatisticamente significativo. |
| 2 | `cenario2-sem_efeito` | 20% vs. 20% | Demonstrar a não rejeição de H₀ e explorar o poder estatístico. |
| 3 | `cenario4-srm` | 20% vs. 22%, com divisão 55/45 | Demonstrar a identificação de Sample Ratio Mismatch (SRM). |

## 4.1. Cenário 1 — Vitória clara

Apresenta um experimento em que a variante B possui uma taxa de conversão superior à variante A (20% vs. 22%).

**O que será explorado:**
- Formulação das hipóteses estatísticas.
- Comparação das taxas de conversão.
- Aplicação do teste de hipótese.
- Interpretação do p-valor.
- Intervalo de confiança.
- Avaliação da significância estatística e prática.

## 4.2. Cenário 2 — Ausência de efeito

Apresenta um experimento em que ambas as variantes possuem a mesma taxa de conversão esperada (20% vs. 20%).

**O que será explorado:**
- Interpretação da não rejeição da hipótese nula.
- Diferença entre ausência de evidências e comprovação de ausência de efeito.
- Relação entre tamanho amostral e poder estatístico.
- Possibilidade de erro do tipo II.

## 4.3. Cenário 3 — Sample Ratio Mismatch (SRM)

Apresenta um experimento em que as variantes possuem taxas de conversão esperadas de 20% e 22%, mas a distribuição dos participantes ocorre na proporção de 55% para A e 45% para B, em vez da divisão esperada de 50/50.

**O que será explorado:**
- Conceito de Sample Ratio Mismatch.
- Verificação da proporção de participantes entre os grupos.
- Aplicação do teste qui-quadrado de aderência.
- Interpretação do p-valor do teste de SRM.
- Impactos de uma distribuição inadequada na confiabilidade dos resultados.

# 5. Estrutura dos notebooks
Cada notebook apresenta a análise individual de um dos cenários experimentais. Os fundamentos metodológicos e os parâmetros estatísticos são documentados neste README e não precisam ser reproduzidos integralmente em cada notebook.

Os notebooks devem priorizar a apresentação das particularidades de cada experimento, seus resultados e respectivas interpretações.

# 6. Metodologia de análise
De maneira geral, os experimentos seguem uma estrutura de análise que contempla:

1. Definição do cenário experimental.
2. Formulação das hipóteses estatísticas.
3. Verificação da distribuição dos participantes, quando aplicável.
4. Cálculo das taxas de conversão.
5. Aplicação dos testes estatísticos pertinentes.
6. Análise do p-valor e do intervalo de confiança.
7. Interpretação da significância estatística e prática.
8. Elaboração da conclusão do experimento.

As etapas podem variar conforme as particularidades de cada cenário.

# 7. Como executar
1. Clone este repositório.
2. Instale as bibliotecas necessárias.
3. Abra o projeto em um ambiente compatível com Jupyter Notebook.
4. Acesse a pasta `notebooks/`.
5. Execute os notebooks individualmente para acompanhar cada cenário experimental.


