## Descrição

O ToothPaste é um sistema de gestão de dentistas que foi desenvolvido no primeiro semestre de 2023. O nome é uma combinação das palavras "tooth" (dente) e "paste" 
(pasta), remetendo tanto à pasta de dente quanto à organização de arquivos. O objetivo é concluir o projeto até o final de 2023 e proporcionar uma solução 
completa para dentistas.

## Documentação

Para mais detalhes de diagramas e documentação do RUP consultar:  [ToothPaste Documentation](https://github.com/odenath/docs-toothpaste).

## Requisitos

Inicialmente o projeto não tem Docker, mas existem planos de adiciona-lo no projeto. Por hora, alguns detalhes devem ser levados em consideração:

- É necessário utilizar o sistema operacional Windows.
- É necessário utilizar o Python 3.10.11 (outras versões podem ser compatíveis).
- É necessário baixar e instalar o MySQL e criar um usuário, senha e banco de dados de acordo com as configurações definidas no arquivo `settings.py` dentro
 da pasta `project`.

## Instalação e configuração

Para realizar a instalação e configuração do projeto, siga as instruções abaixo:

1. Faça o download do código-fonte ou realize um fork do repositório. O projeto está disponível sob a licença MIT.
2. Crie um ambiente virtual para isolar as dependências do projeto.
3. Baixe todas as dependências e arquivos necessários para o projeto, incluindo o Django e outras bibliotecas utilizadas.
- Execute o seguinte comando no terminal (Windows-PowerShel):
   ```shell
   python -m venv venv
   .\venv\Scripts\Activate
    pip install -r requirements.txt


## Como funciona na prática

Na versão do primeiro semestre de 2023, o ToothPaste possui as seguintes funcionalidades implementadas: cadastrar usuário e cadastrar cliente.

Para utilizar o sistema siga os passos abaixo:

1. Rode o servidor com o seguinte comando no terminal:

   ```shell
   python manage.py runserver
2. Certifique-se de estar no diretório raiz do projeto ao executar o comando acima.

3. Faça login na sua conta. Caso não possua uma conta, você pode criar uma nova conta, que funcionará como a conta de um dentista.

4. Uma vez logado você poderá cadastrar clientes, editar informações de clientes existentes e também deletar clientes.

5. Os campos do banco de dados são preenchidos automaticamente e também são deletados automaticamente.

Por enquanto, o sistema permite que você cadastre sua conta de usuário (dentista) e, dentro da sua conta, você pode cadastrar clientes e editar suas informações.


## Dúvidas e sugestões

Entre em contato pelo e-mail gustavo.odenath@edu.unifil.br






