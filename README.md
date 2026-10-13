# livro_flask

Instalação do projeto nos capítulos 1 e 2 do livro.

## Python

O projeto foi desenvolvido com o Python 3.15 (as versões das `libs` do `requirements.txt` foram congeladas nele) e também foi testado com o Python 3.14, que é o usado nas imagens Docker.

## Dados de exemplo

O arquivo `dados_de_exemplo.sql` popula o banco com funções, uma categoria, produtos e os usuários a seguir. Ele contém apenas os dados, então deve ser importado depois do `flask db upgrade`. Todos os usuários usam a senha `123456`:

| E-mail | Função |
|---|---|
| admin@email.com | Admin |
| gerente@email | Gerente |
| lojista@email | Lojista |
| usuario@email | Cliente |

Para saber mais conheça o livro. https://www.casadocodigo.com.br/products/livro-flask-a-z
