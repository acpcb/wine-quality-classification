# Wine Quality Classification — Tech Challenge Fase 2

Projeto de Machine Learning para classificar vinhos como **alta qualidade** ou **baixa/média qualidade** a partir de características físico-químicas.

## Objetivo

Transformar `quality` em variável binária:

- Alta qualidade: `quality >= 7`
- Baixa/média qualidade: `quality < 7`

## Estrutura

```text
wine-quality-classification-completo/
├── data/WineQT.csv
├── notebooks/TechChallenge_Wine_Quality.ipynb
├── src/preprocessing.py
├── results/
├── presentation/Storytelling_Wine_Quality.pptx
├── presentation/roteiro_video_5min.md
├── requirements.txt
└── README.md
```

## Modelos avaliados

- Baseline
- Regressão Logística
- Random Forest

## Resultado resumido

Modelo selecionado: **Random Forest**

Métricas de teste:

| modelo              |   accuracy |   precision |   recall |    f1 |   roc_auc |
|:--------------------|-----------:|------------:|---------:|------:|----------:|
| Random Forest       |      0.917 |       0.842 |    0.5   | 0.627 |     0.911 |
| Regressão Logística |      0.795 |       0.368 |    0.656 | 0.472 |     0.862 |
| Baseline            |      0.86  |       0     |    0     | 0     |     0.5   |

Top variáveis por importância: alcohol, alcohol_density_ratio, sulphates, total sulfur dioxide, acidity_ratio.

## Como executar

```bash
pip install -r requirements.txt
jupyter notebook notebooks/TechChallenge_Wine_Quality.ipynb
```

No Google Colab, envie o notebook e o arquivo `WineQT.csv`, depois execute todas as células.
