Feature: Login de usuário
  Como usuário
  Eu quero fazer login na aplicação
  Para acessar minha conta e meus dados

  Scenario: Login com dados válidos
    Dado que eu tenho uma conta de usuário
    Quando eu faço login com meu nome de usuário e senha corretos
    Então eu devo receber um token de acesso

  Scenario: Login com dados inválidos
    Dado que eu tenho uma conta de usuário
    Quando eu faço login com um nome de usuário ou senha incorretos
    Então eu devo receber um erro de autenticação

  Scenario: Login sem credenciais
    Quando eu tento fazer login sem fornecer o nome de usuário ou senha
    Então eu devo receber um erro de validação
