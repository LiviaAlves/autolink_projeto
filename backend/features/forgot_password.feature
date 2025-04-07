Feature: Resetar senha
  Como usuário
  Eu quero resetar minha senha
  Para poder recuperar o acesso à minha conta

  Scenario: Enviar email de reset de senha para um usuário válido
    Dado que eu tenho uma conta de usuário
    Quando eu solicito o reset de senha com meu email
    Então eu devo receber uma mensagem informando que o código foi enviado

  Scenario: Tentar resetar senha com código inválido
    Dado que eu tenho uma conta de usuário
    Quando eu tento resetar a senha com um código inválido
    Então eu devo receber um erro informando que o código é inválido ou expirado
