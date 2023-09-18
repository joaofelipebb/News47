#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests #Esta linha importa a biblioteca requests, que é usada para fazer solicitações HTTP, neste caso, para acessar a API do NewsAPI.

api_key = 'f33fc82c61d942cca4e6b5c359407394' #Esta chave é necessária para autenticar sua solicitação à API.

#URL da API do NewsAPI.
url_api_noticias = 'https://newsapi.org/v2/top-headlines'

#Esses foram os parâmetros usados para consultar à API.
parametros = {
    'apiKey': api_key,
    'category': 'business',  #Categoria de notícias de negócios.
    'pageSize': 10,           #Quantidade de notícias desejadas.
    'country': 'us',         #Alterado para o USA.
    'language': 'en'         #Definido para o idioma inglês.
}

#Esta linha faz uma solicitação GET à API do NewsAPI com os parâmetros definidos. A resposta da API é armazenada na variável "response".
response = requests.get(url_api_noticias, params=parametros)

#Verifica se a solicitação foi bem-sucedida. O código de status 200 indica uma resposta bem-sucedida.
if response.status_code == 200:
    #Se a solicitação for bem-sucedida, esta linha converte a resposta da API em um objeto Python. A resposta da API é retornada no formato JSON.
    noticias = response.json()

    #Aqui é o formato de exibição das notícias.
    for idx, noticia in enumerate(noticias['articles']):
        print(f"Notícia {idx + 1}:")
        print(f"Título: {noticia['title']}")
        print(f"Descrição: {noticia['description']}")
        print(f"URL: {noticia['url']}")
        print("\n")
else:
    print(f"Erro ao buscar notícias: Código {response.status_code}") #Se a solicitação à API não for bem-sucedida, este bloco de código imprime uma mensagem de erro junto com o código de status da resposta.


# In[2]:





# In[7]:





# In[ ]:




