# livro_flask

Instalação do projeto nos capítulos 1 e 2 do livro.

## Qual versão usar

Este repositório acompanha o livro Flask de A a Z, e o código muda de uma edição para outra. Use a versão que corresponde ao seu livro (para saber a sua edição, confira a ficha técnica do livro):

* Se você está lendo a edição de 2019, use a tag [livro-edicao-1-2019](https://github.com/tiagoluizrs/livro_flask/tree/livro-edicao-1-2019) como referência.
* Se você está lendo a segunda edição, lançada em 2027, use a tag [livro-edicao-2-2027](https://github.com/tiagoluizrs/livro_flask/tree/livro-edicao-2-2027).

A branch `main` acompanha a segunda edição.

## Python

O projeto foi desenvolvido com o Python 3.15 (as versões das `libs` do `requirements.txt` foram congeladas nele) e as imagens Docker usam a mesma versão (`python:3.15-slim`).

## Dados de exemplo

O arquivo `dados_de_exemplo.sql` popula o banco com funções, uma categoria, produtos e os usuários a seguir. Ele contém apenas os dados, então deve ser importado depois de aplicar as migrações (`alembic upgrade head`). Todos os usuários usam a senha `123456`:

| E-mail | Função |
|---|---|
| admin@email.com | Admin |
| gerente@email | Gerente |
| lojista@email | Lojista |
| usuario@email | Cliente |

Para saber mais conheça o livro. https://www.casadocodigo.com.br/products/livro-flask-a-z
