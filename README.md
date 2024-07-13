<h1>scrapy_cel</h1> 

<p align="center">
  <img src="http://img.shields.io/static/v1?label=License&message=MIT&color=green&style=for-the-badge"/>
   <img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge"/>
</p>

> Status do Projeto: Concluido :heavy_check_mark:

### Tópicos 

:small_blue_diamond: [Sobre o projeto](https://github.com/cainzuca/scrapy_celphone.git)

:small_blue_diamond: [Arquitetura](https://github.com/cainzuca/scrapy_celphone.git)

:small_blue_diamond: [Pré-requisitos](#pré-requisitos)

:small_blue_diamond: [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)


## Sobre o projeto 

<p align="justify">
  Este projeto tem o objetivo de extrair dados de celulares usados do mercado livre, para fazer análises de price. Com isso, utiliza python, junto com a biblioteca "scrapy" para fazer a extração dos dados. Após a extração, os dados são transformados com pandas, e carregados em um banco de dados PostgreSQL, que está alocado em um cluster na Google Cloud. Todo esse processo é orquestrado com o airflow, que é reponsável de automatizar todo o processo.
</p>

## Arquitetura

  ![diagrama scrapy drawio](https://github.com/user-attachments/assets/75f6fae0-74ea-459d-9a06-b53431c36fa5)
  

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

Copyright :copyright: Ano - Titulo do Projeto
