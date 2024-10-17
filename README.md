<h1>scrapy_cel</h1> 

<p align="center">
  <img src="http://img.shields.io/static/v1?label=License&message=MIT&color=green&style=for-the-badge"/>
   <img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge"/>
</p>

> Status do Projeto: Concluido :heavy_check_mark:

### Tópicos 

:small_blue_diamond: [Sobre o projeto](#sobre-o-projeto)

:small_blue_diamond: [Arquitetura](#arquitetura)

:small_blue_diamond: [Pré-requisitos](#pré-requisitos)

:small_blue_diamond: [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)


## Sobre o projeto 

<p align="justify">
  Este projeto visa extrair dados de celulares usados do Mercado Livre para realizar análises baseadas no preço dos produtos. Utilizando Python e a biblioteca Scrapy, os dados são extraídos e transformados com Pandas. Em seguida, são carregados em um banco de dados PostgreSQL, alocado em um cluster na Google Cloud. Todo o processo é orquestrado pelo Apache Airflow, que automatiza a extração, transformação e carregamento dos dados.
</p>

## Arquitetura

  ![diagrama scrapy drawio](https://github.com/user-attachments/assets/75f6fae0-74ea-459d-9a06-b53431c36fa5)

## Pré requisitos

:warning:[Python](https://www.python.org/downloads/) <br>
:warning:[Docker](https://www.docker.com/products/docker-desktop/) <br>

## Como rodar a aplicação :arrow_forward:

No terminal, clone o projeto: 

```
git clone https://github.com/cainzuca/scrapy_celphone.git
```

No terminal, instale o astro CLI: 

```
winget install -e --id Astronomer.Astro
```

No terminal, inicie o docker: 

```
astro dev start
```

## Licença 

The [MIT License]() (MIT)

Copyright :copyright: 2024 - scrapy_cel
