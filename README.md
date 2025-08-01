# Projeto Vaga Back-end

Este projeto é um back-end de teste desenvolvido com Django e Django REST Framework.

O projeto foi construído com foco em boas práticas e modularidade. Abaixo estão os principais pontos de desenvolvimento:

### Separação das Camadas de Responsabilidade
A arquitetura do projeto segue o padrão MVC (Model-View-Controller) do Django. As responsabilidades são separadas em:
* **Modelagem de Dados**: O arquivo `models.py` define as entidades da aplicação (`Colaborador`, `Departamento`, `Dependente`) e seus relacionamentos.
* **Serialização**: Os serializers (`serializers.py`) são responsáveis por converter objetos Django complexos em formatos como JSON e vice-versa, e fazer validações.
* **Lógica de Negócio (Views)**: As views (`views.py`) contêm a lógica de negócio.

### Conteinerização
O projeto é totalmente conteinerizado com **Docker** e **Docker Compose**. A aplicação é executada em um container isolado do seu banco de dados **PostgreSQL**, que também é um container à parte.

### Testes Unitários
Para garantir a confiabilidade e a robustez do código, foram implementados testes unitários. Os testes podem ser executados no ambiente conteinerizado, verificando o comportamento de cada componente da aplicação.

### Referência de API (Swagger)
A documentação interativa da API é gerada automaticamente usando **drf-yasg**, seguindo o padrão OpenAPI (Swagger UI). A referência completa da API, com todos os endpoints, parâmetros e modelos, está disponível em `http://127.0.0.1:8000/swagger/`.

---

## Como Rodar o Projeto Localmente

Para rodar este projeto, você só precisa ter o **Docker** e o **Docker Compose** instalados na sua máquina.

1.  **Clone o Repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [pasta_do_projeto]
    ```

2.  **Inicie os Containers:**
    Execute o comando a seguir na raiz do projeto. Ele irá construir as imagens, iniciar os serviços de banco de dados e da API, e aplicar as migrações automaticamente.
    ```bash
    docker-compose up
    ```
    O primeiro `up` pode demorar um pouco, pois o Docker precisa baixar as imagens e instalar as dependências. Em execuções futuras, será muito mais rápido.

3.  **Acesse a API:**
    * Sua API estará disponível em `http://127.0.0.1:8000/`.
    * A documentação interativa da API (Swagger UI) está em `http://127.0.0.1:8000/swagger/`.

---

## Rodando os Testes

Para executar os testes do projeto, use o `docker-compose exec` para rodar o comando dentro do container da API.

1.  Certifique-se de que os containers estão em execução (`docker-compose up`).
2.  Execute o comando de teste em um novo terminal:
    ```bash
    docker-compose exec web python manage.py test
    ```

---

## Observação: Parâmetro de Documentação

Apesar de configurada, a documentação gerada não detalha explicitamente o parâmetro de consulta `?colaboradores=true` no endpoint de `departamentos`. Essa funcionalidade, embora não documentada no Swagger, está ativa. Optamos por manter o código como está, pois o comportamento é funcional e segue as boas práticas de serialização condicional.