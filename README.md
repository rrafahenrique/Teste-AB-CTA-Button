![Badge-Em Andamento](https://img.shields.io/badge/Status-Concluído-green) ![Bagde-Version](https://img.shields.io/badge/Version-1.0-blue)


# 1. Sobre o projeto
Este projeto tem como objetivo explorar a aplicação de **testes A/B** por meio de três cenários experimentais distintos. A proposta é demonstrar como interpretar os resultados de um experimento, avaliar a existência de diferenças estatisticamente significativas e identificar possíveis problemas na distribuição dos participantes entre os grupos.

Os experimentos foram construídos para abordar três situações fundamentais:

- **Vitória clara:** identificação de um efeito estatisticamente significativo entre as variantes.
- **Ausência de evidências suficientes:** situação em que não se rejeita a hipótese nula, explorando também o conceito de poder estatístico.
- **Sample Ratio Mismatch (SRM):** identificação de uma distribuição inadequada dos participantes entre os grupos experimentais.

Todos os cenários utilizam os mesmos parâmetros estatísticos, definidos previamente à análise dos resultados, garantindo consistência metodológica e evitando ajustes orientados pelos resultados observados.

# 2. Metodologia de análise
Os experimentos seguem uma metodologia padronizada, composta por etapas que orientam a execução e a interpretação dos testes A/B. De maneira geral, o processo contempla:
- **Definição do cenário experimental**: identificação das variantes e da métrica que será avaliada.
- **Formulação das hipóteses**: estabelecimento das hipóteses nula (H₀) e alternativa (H₁).
- **Validação dos dados**: verificação da consistência dos registros e da distribuição dos participantes entre os grupos.
- **Análise das métricas**: cálculo e comparação das taxas de cliques observadas.
- **Inferência estatística**: aplicação dos testes estatísticos adequados a cada cenário.
- **Interpretação dos resultados**: avaliação do p-valor, teste z, dos intervalos de confiança e da significância estatística e prática.
- **Conclusão**: interpretação dos resultados e suas possíveis implicações para a tomada de decisão.

Embora compartilhem uma metodologia geral, os experimentos apresentam particularidades que exigem análises específicas, conforme descrito na próxima seção.

## 2.1 Estrutura do dataset
- `data-raw/` - datasets (CSV);
- `notebooks/` - notebooks de análise (.ipynb);
- `utils/` - arquivos com funções auxiliares.

# 3. Problema de Negócio
Você trabalha no departamento de ciência de dados de um empresa que oferece cursos, bootcamps e suporte de carreira para ajudar alunos a conquistarem um vaga na área de dados. Um belo dia você é designado para realizar um Teste AB, o objetivo é identificar qual versão do botão de chamada para ação (CTA) na página inicial da empresa apresenta um desempenho superior, com base na métrica de taxa de cliques (CTR, na sigla em inglês):

- **Grupo de Controle - (Versão A)** Exposto ao botão de CTA atual ("Garantir teste gratuito").
- **Grupo Experimental - (Versão B):** Exposto ao novo botão de CTA, de caráter mais geral ("Inscreva-se agora").

A taxa de cliques (CTR) mede a porcentagem de usuários que clicam em um botão ou link após visualizá-lo. Para a empresa, o CTR é importante, pois reflete o engajamento dos usuários com a plataforma e auxilia na avaliação da eficácia dos botões de chamada para ação em gerar inscrições e conversões.

Por fim, os resultados deste teste ajudarão a decidir se o novo botão deve ser implementado na página inicial.

<img src="img/banner.png" alt="banner" width="900">

# 4. Parâmetros experimentais
Os três experimentos utilizam os mesmos parâmetros, estabelecidos antes da observação dos resultados.

| Parâmetro | Valor | Significado |
|---|---:|---|
| Nível de significância (α) | 0,05 | Probabilidade máxima aceita de cometer um erro do tipo I, ou seja, rejeitar H₀ quando ela é verdadeira. |
| Poder estatístico (1 − β) | 0,80 | Probabilidade de detectar um efeito de determinada magnitude quando ele realmente existe. |
| Efeito mínimo detectável (MDE) | 0,02 | Menor diferença absoluta considerada relevante para o negócio, equivalente a 2 pontos percentuais. |

## 4.1 Interpretação dos parâmetros
- **α = 0,05:** estabelece um limite de 5% para o risco de falso positivo.
- **Poder = 0,80:** estabelece uma probabilidade de 80% de detectar o efeito definido no planejamento, caso ele exista.
- **MDE = 0,02:** representa uma diferença absoluta de 2 pontos percentuais entre as taxas de cliques das variantes.

Esses parâmetros orientam o planejamento e a interpretação dos experimentos e devem permanecer constantes entre os cenários.

# 5. Cenários analisados
O projeto contempla três cenários, cada um desenvolvido para demonstrar uma situação específica encontrada na prática de experimentação A/B.

| Cenário | Arquivo | Taxas de cliques esperadas | Objetivo |
|---|---|---|---|
| 1 | `cenario1-vitoria_clara` | 20% vs. 22% | Demonstrar um efeito estatisticamente significativo. |
| 2 | `cenario2-sem_efeito` | 20% vs. 20% | Demonstrar a não rejeição de H₀ e explorar o poder estatístico. |
| 3 | `cenario4-srm` | 20% vs. 22%, com divisão 55/45 | Demonstrar a identificação de Sample Ratio Mismatch (SRM). |

## 5.1. Cenário 1 — Vitória clara
Experimento em que a variante B possui uma taxa de clique superior à variante A (20% vs. 22%).
- Teste de hipóteses para comparação de proporções.
- Interpretação do p-valor e do intervalo de confiança.
- Significância estatística e significância prática.

## 5.2. Cenário 2 — Ausência de efeito
Experimento em que ambas as variantes possuem a mesma taxa de cliques esperada (20% vs. 20%).
- Interpretação da não rejeição da hipótese nula.
- Diferença entre ausência de evidências e comprovação de ausência de efeito.
- Relação entre tamanho amostral, poder estatístico.

## 5.3. Cenário 3 — Sample Ratio Mismatch (SRM)
Apresenta um experimento em que as variantes possuem taxas de cliques esperadas de 20% e 22%, mas a distribuição dos participantes ocorre na proporção de 55% para A e 45% para B, em vez da divisão esperada de 50/50.
- Conceito de incompatibilidade na proporção de participantes entre os grupos.
- Aplicação do teste qui-quadrado de aderência.
- Interpretação do resultado e impactos de uma distribuição inadequada na confiabilidade do experimento.

# 6. Estrutura dos notebooks
Cada notebook apresenta a análise individual de um dos cenários experimentais. Os fundamentos metodológicos e os parâmetros estatísticos são documentados neste README e não precisam ser reproduzidos integralmente em cada notebook.

Os notebooks devem priorizar a apresentação das particularidades de cada experimento, seus resultados e respectivas interpretações.

# 7. Como executar
1. Clone este repositório.
2. Instale as bibliotecas necessárias.
3. Abra o projeto em um ambiente compatível com Jupyter Notebook.
4. Acesse a pasta `notebooks/`.
5. Execute os notebooks individualmente para acompanhar cada cenário experimental.


