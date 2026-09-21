# Desafio 01 — Transfer Learning

Classificação binária de imagens de gatos e cachorros em Python, usando TensorFlow/Keras no Google Colab.

**Status:** código preparado; treinamento e análise dos resultados pendentes de execução no Colab.

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cauelaz/machine-learning/blob/main/desafios/01-transfer-learning/transfer-learning.ipynb)

O link funciona após publicar os arquivos na branch `main`. Antes disso, faça upload de `transfer-learning.ipynb` pelo menu de abertura de notebooks do Colab.

## Objetivo e abordagem

Reutilizar os filtros visuais de uma MobileNetV2 pré-treinada no ImageNet e treinar uma nova camada classificadora para duas classes. O notebook implementa:

1. Carregamento do Cats vs Dogs via TensorFlow Datasets.
2. Divisão fixa e sem sobreposição: 80% treino, 10% validação e 10% teste.
3. Redimensionamento para 160 × 160 pixels e aumento de dados durante o treino.
4. Normalização de pixels de [0, 255] para [-1, 1], compatível com MobileNetV2.
5. Treinamento do classificador com a base congelada.
6. Fine-tuning opcional das últimas camadas, com taxa de aprendizado menor e BatchNormalization congelada.
7. Seleção do modelo pela perda de validação e avaliação final no teste.
8. Gráficos, matriz de confusão, exemplos de previsões e exportação dos artefatos.

O conjunto de teste fica reservado para a avaliação final. Não o utilize para escolher épocas, arquitetura ou hiperparâmetros. A saída sigmoid estima a probabilidade da classe 1; os nomes e índices das classes são obtidos do dataset.

## Executar no Colab

1. Abra o notebook e, em **Ambiente de execução → Alterar tipo de ambiente de execução**, escolha GPU.
2. Execute todas as células em ordem. A primeira instala o TensorFlow Datasets; TensorFlow, NumPy e Matplotlib são fornecidos pelo Colab.
3. Ajuste os parâmetros na célula de configuração se desejar. Para executar apenas a primeira fase, use `RUN_FINE_TUNING = False`.
4. Analise as métricas e baixe `transfer-learning-artefatos.zip` na última célula.

O download inicial do dataset exige cerca de 787 MiB, além de espaço para os dados preparados e pesos. A leitura usa lotes e prefetch, sem manter todo o dataset em cache na RAM. Uma seed é definida para facilitar comparações, mas hardware e versões podem alterar os resultados.

O ZIP contém o modelo `.keras`, o histórico, as métricas de teste, configurações, versões das bibliotecas e gráficos. Os arquivos em `/content` são temporários e podem ser perdidos ao encerrar o ambiente. O modelo exportado já inclui redimensionamento e normalização; forneça imagens RGB com pixels em [0, 255].

## Registro da experiência

Preencha depois de executar, usando os resultados reais:

| Item | Registro |
| --- | --- |
| Data e GPU utilizada | A preencher |
| Épocas executadas e hiperparâmetros | A preencher |
| Acurácia e perda no teste | A preencher |
| Efeito do fine-tuning na validação | A preencher |
| Erros observados e sinais de overfitting | A preencher |
| Aprendizados e próximos experimentos | A preencher |

Capturas de tela podem ser adicionadas a uma pasta `images/` dentro deste desafio. Não há métricas ou evidências de treinamento geradas previamente neste repositório.

## Referências

- [Notebook de referência indicado no desafio](https://colab.research.google.com/github/kylemath/ml4a-guides/blob/master/notebooks/transfer-learning.ipynb).
- [Cats vs Dogs — catálogo TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog/cats_vs_dogs): descrição, tamanho e tratamento de imagens corrompidas.
- [Dataset original — Microsoft](https://www.microsoft.com/en-us/download/details.aspx?id=54765).
- [Tutorial oficial de Transfer Learning e fine-tuning](https://www.tensorflow.org/tutorials/images/transfer_learning).

A implementação deste repositório utiliza MobileNetV2 e Cats vs Dogs; a referência do enunciado serve como material complementar.

## Se o TFDS apresentar AttributeError em load

A primeira célula instala as dependências e reinstala os arquivos do pacote TFDS.
Se a biblioteca já tiver sido importada, reinicie a sessão do Colab após essa
célula e continue a partir da célula de imports. Reinstalar não substitui os
módulos já carregados na memória do Python.

A célula de imports mostra a versão e o caminho do TFDS e verifica se load está
disponível antes de baixar os dados. Se o erro persistir, verifique se um arquivo
local chamado tensorflow_datasets.py ou um pacote com esse nome está ocultando
a biblioteca instalada. Renomeie somente o arquivo conflitante e reinicie a
sessão; a pasta de cache de datasets não precisa ser apagada.
## Se faltar importlib_resources

Execute uma célula com `%pip install -q "importlib-resources>=6.5,<8"` e tente
novamente a célula de carregamento do dataset. A instalação inicial do notebook
já inclui essa dependência explicitamente.

O aviso de ausência de `dataset_info.json` indica que os metadados do dataset
preparado não foram encontrados. No traceback relatado, a execução foi
interrompida pela dependência ausente, não pelo aviso. Não é necessário apagar
a pasta do dataset para corrigir esse ModuleNotFoundError.