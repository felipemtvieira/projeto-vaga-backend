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
    git clone https://github.com/felipemtvieira/projeto-vaga-backend.git
    cd projeto-vaga-backend
    ```

2.  **Inicie os Containers:**
    Execute o comando a seguir na raiz do projeto. Ele irá construir as imagens, iniciar os serviços de banco de dados e da API, e aplicar as migrações automaticamente.
    ```bash
    docker-compose up
    ```

3.  **Acesse a API:**
    * Sua API estará disponível em `http://127.0.0.1:8000/`.
    * Recomenda-se a utilização da interface do Django REST Framework para visualização simples dos dados: `http://127.0.0.1:8000/api/`
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

## Observações

É importante notar que a rota /departamentos/ não retornará automaticamente os dados dos colaboradores vinculados a ele. Para isso é necessário adicionar o parâmetro de consulta `?colaboradores=true` no endpoint de `departamentos` : `/departamentos/?colaboradores=true`. Também é possível visualizar os colaboradores de um determinado departamento: `/departamentos/{id_departamento}/?colaboradores=true`. Optei por fazer dessa maneira para que o cliente da API tivesse a opção de realizar as duas buscas, sem que a API retornasse dados que o cliente não pediu. Em caso de grandes massas de dados, isso é melhor para performance e também é uma boa prática de desenvolvimento.

Para o desenvolvimento foi utilizado Django pois é o framework Python com o qual tenho maior familiaridade. Além disso ele permite um desenvolvimento rápido e seguro de APIs. Além disso, atentou-se à escalabilidade do projeto: com a divisão em Apps que o Django utiliza, não é  difícil ampliar o projeto conforme novas necessidades, mas sempre mantendo a organização do código.

Também adicionei um arquivo .pdf com a imagem do diagrama relacional para fácil visualizção da estrutura das tabelas.

### Formatos de Dados para Teste
Abaixo estão exemplos de como os dados devem ser formatados para realizar testes de criação (requisições `POST`) nos endpoints principais da API.

**1. Criar um novo Departamento (`POST` para `/api/departamentos/`)**
```json
{
    "nome": "Recursos Humanos"
}
```

**1. Criar um novo Colaborador (`POST` para `/api/colaboradores/`)**
```json
{
    "nome": "João da Silva",
    "departamento": 1  // ID do departamento ao qual o colaborador pertence
}
```

**1. Criar um novo Dependente (`POST` para `/api/dependentes/`)**
```json
{
    "nome": "Maria da Silva",
    "colaborador": 1 // ID do colaborador ao qual o dependente está relacionado
}
```

