# Testes da Aplicação

## Testes Unitários (CT-TU)

### CT-TU-01Teste de unidade para a classe [UsuarioRepository](https://github.com/my-prototypes/tflk/blob/main/app/repository.py):
CT-TU-01-c1 Verificar se a tabela de usuários é criada corretamente no banco de dados.

CT-TU-01-c2 Testar o método cadastrar_usuario para garantir que um usuário seja inserido corretamente no banco de dados.

CT-TU-01-c3 Testar o método listar_usuarios para verificar se a lista de usuários é retornada corretamente.

CT-TU-01-c4 Testar o método buscar_usuario_por_username para verificar se um usuário é encontrado corretamente com base no nome de usuário.


### CT-TU-02 Teste de unidade para a classe [ImagemRepository](https://github.com/my-prototypes/tflk/blob/main/app/repository.py):
CT-TU-02-c1 Verificar se a tabela de imagens é criada corretamente no banco de dados.

CT-TU-02-c2 Testar o método cadastrar_imagem para garantir que uma imagem seja inserida corretamente no banco de dados.

CT-TU-02-c3 Testar o método listar_imagens para verificar se a lista de imagens é retornada corretamente.

### CT-TU-03 Teste de unidade para a função validar_credenciais no módulo [auth.py](https://github.com/my-prototypes/tflk/blob/main/app/controllers/auth.py):
CT-TU-03-c1 Testar se as credenciais de um usuário válido são validadas corretamente.

CT-TU-03-c2 Testar se as credenciais de um usuário inválido são rejeitadas corretamente.

### CT-TU-04 Teste de unidade para a função verificar_autenticacao no módulo [auth.py](https://github.com/my-prototypes/tflk/blob/main/app/controllers/auth.py):
CT-TU-04-c1 Testar se a função retorna True quando o usuário está autenticado.

CT-TU-04-c2 Testar se a função retorna False quando o usuário não está autenticado.

## Testes de Integração (CT-TI)

### CT-TI-01 Teste de integração do fluxo de autenticação:

CT-TI-01-c1 Simule o envio de credenciais de usuário válidas e verifique se o usuário é redirecionado para a página de dashboard.

CT-TI-01-c2 Simule o envio de credenciais inválidas e verifique se o usuário recebe uma mensagem de erro.

### CT-TI-02 Teste de integração do cadastro de usuários:

CT-TI-02-c1 Simule o preenchimento do formulário de cadastro de usuários com dados válidos e verifique se o usuário é redirecionado para a página de listagem de usuários.

- Verifique se o usuário cadastrado é exibido corretamente na lista de usuários.

### CT-TI-03 Teste de integração do upload de imagens:

CT-TI-03-c1 Simule o envio de um arquivo de imagem válido e verifique se a imagem é salva corretamente no diretório de upload.

- Verifique se a imagem cadastrada é exibida corretamente na lista de imagens.

### CT-TI-04 Teste de integração do acesso restrito:

CT-TI-04-c1 Verifique se o acesso às páginas restritas, como a página de dashboard, é bloqueado para usuários não autenticados.

CT-TI-04-c2 Verifique se o acesso às páginas restritas é permitido apenas para usuários autenticados.

## Teste de Sistema (CT-TS)

### CT-TS-01 Casos de Testes para a Feature F1

Para o caso de uso "Login de usuário". Aqui estão os cenários de teste correspondentes:

CT-TS-01-c1 Cenário de teste 1: Fluxo Principal - Login de usuário válido

Entradas:
- Nome de usuário válido
- Senha válida
Passos:
- Acesse a página de login do usuário.
- Insira um nome de usuário válido.
- Insira uma senha válida.
- Pressione o botão de login.

Resultado esperado:
- O sistema deve autenticar com sucesso o usuário.
- O sistema deve redirecionar o usuário para a página de dashboard.

CT-TS-01-c2 Cenário de teste 2: Fluxo de Exceção - Login de usuário inválido

Entradas:
- Nome de usuário inválido
- Senha inválida

Passos:
- Acesse a página de login do usuário.
- Insira um nome de usuário inválido.
- Insira uma senha inválida.
- Pressione o botão de login.

Resultado esperado:
- O sistema deve exibir uma mensagem de erro informando que as credenciais são inválidas.

CT-TS-01-c3 Cenário de teste 3: Fluxo Alternativo - Recuperação de senha

Entradas:
- E-mail do usuário para recuperação de senha
  
Passos:
- Acesse a página de login do usuário.
- Clique no link de recuperação de senha.
- Insira o e-mail do usuário.
- Pressione o botão de envio.

Resultado esperado:
- O sistema deve enviar um e-mail de lembrete para o usuário com as instruções para recuperar a senha.

### CT-TS-02 Casos de Testes para a Feature F2

Para o caso de uso "Logout de usuário", podemos identificar o seguinte fluxo principal de teste:

CT-TS-02-c1 Cenário de teste: Fluxo Principal - Logout de usuário

Pré-condições:
- O usuário está na tela de dashboard, ou seja, está autenticado.

Passos:
- O usuário clica no botão ou link de logout na tela de dashboard.
- O sistema encerra a sessão do usuário.
- O sistema redireciona o usuário para a página de login.

Resultado esperado:
- O sistema deve encerrar a sessão do usuário com sucesso.
- O sistema deve redirecionar o usuário para a página de login.

### CT-TS-03 Casos de Testes para a feature F3

Para o caso de uso "Registro de novo usuário", podemos identificar os seguintes fluxos de teste:

CT-TS-03-c1 Cenário de teste: Fluxo Principal - Registro de novo usuário

Passos:
- O usuário acessa a página de registro de novo usuário.
- O usuário fornece um nome de usuário válido.
- O usuário fornece seu nome completo.
- O usuário fornece um e-mail válido.
- O usuário fornece uma senha.
- O usuário confirma a senha.
- O sistema verifica se o nome de usuário, nome completo e e-mail não estão duplicados no sistema.
- O sistema registra o novo usuário com as informações fornecidas.
- O sistema loga com as informações do novo usuário.
- O sistema carrega a página de dashboard do usuário.

Resultado esperado:
- O sistema deve registrar o novo usuário com sucesso.
- O sistema deve logar com as informações do novo usuário.
- O sistema deve redirecionar o usuário para a página de dashboard.

Cenários de teste adicionais:
Além do fluxo principal, podemos considerar os seguintes cenários de teste para os fluxos de exceção:

CT-TS-03-c2 Cenário de teste: Usuário já existente - Nome de usuário duplicado

Passos:
- O usuário acessa a página de registro de novo usuário.
- O usuário fornece um nome de usuário que já existe no sistema.
- O sistema verifica se o nome de usuário já está cadastrado.
- O sistema exibe uma mensagem informando que o nome de usuário já existe.

Resultado esperado:
- O sistema deve exibir uma mensagem informando que o nome de usuário já existe.

CT-TS-03-c3 Cenário de teste: Usuário já existente - E-mail duplicado

Passos:
- O usuário acessa a página de registro de novo usuário.
- O usuário fornece um e-mail que já está cadastrado no sistema.
- O sistema verifica se o e-mail já está cadastrado.
- O sistema exibe uma mensagem informando que o e-mail já existe.

Resultado esperado:
- O sistema deve exibir uma mensagem informando que o e-mail já existe.

Estes são os principais cenários de teste para o caso de uso "Registro de novo usuário". É importante verificar a validação das entradas, evitar registros duplicados e garantir que o usuário seja registrado com sucesso no sistema.

### CT-TS-04 - Testes da feature Dashboard 

Para o caso de uso "Dashboard do usuário", podemos identificar os seguintes pontos de teste:

CT-TS-04-c1 Testar a renderização correta da página de dashboard:
- Verificar se o cabeçalho (nome do sistema, menu de opções, nome do usuário logado) está presente.
- Verificar se o menu de opções (navbar) está presente e contém as opções corretas (Listar minhas imagens, Fazer o upload de uma imagem, Buscar uma imagem, Logout).
- Verificar se o corpo de conteúdo (conteiner) está presente.
- Verificar se o rodapé (nome do sistema, data corrente) está presente.

CT-TS-04-c2 Testar a exibição correta do card de quantidade de imagens do usuário:
- Verificar se o card está presente na área de informações do usuário.
- Verificar se o card exibe corretamente a quantidade de imagens do usuário.

CT-TS-04-c3 Testar o redirecionamento correto ao clicar nas opções do menu de opções:
- Ao clicar em "Listar minhas imagens", verificar se o sistema redireciona corretamente para a página de listagem de imagens do usuário.
- Ao clicar em "Fazer o upload de uma imagem", verificar se o sistema redireciona corretamente para a página de upload de imagens.
- Ao clicar em "Buscar uma imagem", verificar se o sistema redireciona corretamente para a página de busca de imagens (se implementada).
- Ao clicar em "Logout", verificar se o sistema encerra corretamente a sessão do usuário e redireciona para a página de login.

CT-TS-04-c4 Testar a atualização correta da quantidade de imagens do usuário:
- Após fazer o upload de uma nova imagem, verificar se o card de quantidade de imagens é atualizado corretamente para refletir o número atualizado de imagens do usuário.

Esses são alguns pontos de teste que podem ser considerados para o caso de uso "Dashboard do usuário". É importante verificar a renderização correta da página, a presença e funcionamento adequado dos elementos visuais e a interação correta com as opções do menu. Além disso, é necessário garantir que a quantidade de imagens seja exibida corretamente e atualizada quando necessário.

### CT-TS-05 - Testes da features Listar imagens

Para o caso de uso "Listar imagens", podemos identificar os seguintes pontos de teste:

CT-TS-05-c1 estar a renderização correta da página de listagem de imagens:
- Verificar se a lista de imagens cadastradas pelo usuário é exibida corretamente.
- Verificar se os dados de cada imagem são exibidos corretamente, incluindo o ID da imagem, o nome da imagem e o thumbnail da imagem.
- Verificar se as opções de visualização e exclusão estão disponíveis para cada imagem.

CT-TS-05-c2 Testar a funcionalidade de exibir imagem selecionada:
- Ao clicar na opção de "Exibir" de uma imagem, verificar se o sistema redireciona corretamente para a página de exibição da imagem em tamanho completo.
- Verificar se a imagem selecionada é exibida corretamente em tamanho completo.

CT-TS-05-c3 Testar a funcionalidade de deletar imagem selecionada:
- Ao clicar na opção de "Deletar" de uma imagem, verificar se o sistema solicita confirmação antes de excluir a imagem.
- Verificar se a imagem é removida corretamente da lista de imagens cadastradas após a confirmação de exclusão.

CT-TS-05-c4 Testar o tratamento correto quando nenhuma imagem está cadastrada:
- Verificar se, quando o usuário não possui imagens cadastradas, o sistema exibe corretamente a mensagem "Nenhuma imagem cadastrada".

Esses são alguns pontos de teste que podem ser considerados para o caso de uso "Listar imagens". É importante verificar a renderização correta da página, a exibição correta dos dados das imagens e o funcionamento adequado das opções de visualização e exclusão. Além disso, é necessário lidar corretamente com o caso em que o usuário não possui imagens cadastradas.

### CT-TS-06 - Testes da feature “Exibir Imagem"

Para o caso de uso "Exibir imagem", o fluxo principal é simples e envolve apenas exibir a imagem selecionada pelo usuário. No entanto, podemos identificar alguns pontos de teste relevantes:

CT-TS-06-c1 Testar se a página de exibição de imagem é carregada corretamente:
- Verificar se a página é carregada corretamente ao selecionar uma imagem para exibir.
- Verificar se a imagem selecionada é exibida corretamente na página.

CT-TS-06 Testar o redimensionamento da imagem:
- Verificar-c2 se a imagem é redimensionada corretamente para se ajustar à página de exibição.
- Verificar se a proporção de aspecto da imagem é mantida durante o redimensionamento.

CT-TS-06-c3 Testar a navegação para outras imagens:
- Verificar se o sistema permite a navegação para outras imagens, caso existam várias imagens cadastradas pelo usuário.
- Verificar se a navegação entre as imagens é feita corretamente, garantindo que a página de exibição seja atualizada com a imagem selecionada.

Esses são alguns pontos de teste que podem ser considerados para o caso de uso "Exibir imagem". O foco principal é garantir que a imagem selecionada seja exibida corretamente na página de exibição e que o redimensionamento seja adequado para ajustar a imagem à página. Além disso, é importante verificar se a navegação entre as imagens funciona corretamente, caso existam várias imagens cadastradas pelo usuário.

### CT-TS-07 - Testes da feature Upload de Imagem

Para o caso de uso "Upload de imagem", podemos identificar os seguintes pontos de teste:

CT-TS-07-c1 Testar o carregamento da página de upload de imagem:
- Verificar se a página de upload de imagem é carregada corretamente.
- Verificar se os campos de entrada (nome da imagem, escolher arquivo) estão presentes na página.

CT-TS-07-c2 Testar o envio de uma imagem válida:

Selecionar uma imagem válida (formatos jpg ou png).
- Verificar se o sistema realiza o upload da imagem corretamente.
- Verificar se a mensagem "Upload realizado com sucesso!" é exibida.

CT-TS-07-c3 Testar o envio de uma imagem inválida:

Selecionar um arquivo que não é uma imagem válida (por exemplo, um arquivo de texto).
- Verificar se o sistema trata corretamente o envio de um arquivo inválido.
- Verificar se a mensagem "Upload inválido" é exibida.

CT-TS-07-c4 Testar o tratamento de erros durante o upload:

Simular um erro durante o upload da imagem (por exemplo, falta de permissões de escrita no diretório de upload).
- Verificar se o sistema trata corretamente o erro e exibe uma mensagem adequada.

Esses são alguns pontos de teste que podem ser considerados para o caso de uso "Upload de imagem". O objetivo é garantir que o sistema realize o upload correto de imagens válidas, trate adequadamente casos de envio de arquivos inválidos ou erros durante o upload, e exiba as mensagens apropriadas para o usuário.

### CT-TS-08 - Testes da feature Deletar Imagem

Para o caso de uso "Deletar imagem", podemos identificar os seguintes pontos de teste:

CT-TS-08-c1 Testar a exibição da lista de imagens do usuário:
- Verificar se o sistema lista corretamente as imagens cadastradas pelo usuário.
- Verificar se as informações relevantes de cada imagem (ID, nome, thumbnail) são exibidas corretamente.

CT-TS-08-c2 Testar o processo de exclusão de uma imagem:

Selecionar uma imagem da lista para exclusão.
- Verificar se o sistema deleta a imagem corretamente.
- Verificar se a lista de imagens é atualizada e a imagem deletada não está mais presente.

CT-TS-08-c3 Testar o tratamento de erros durante a exclusão:

Simular um erro ao tentar deletar uma imagem (por exemplo, a imagem não existe ou ocorreu um erro de permissão).
- Verificar se o sistema trata corretamente o erro e exibe uma mensagem de erro adequada.

Esses são alguns pontos de teste que podem ser considerados para o caso de uso "Deletar imagem". O objetivo é garantir que o sistema exiba corretamente a lista de imagens, permita a exclusão adequada de uma imagem selecionada e trate adequadamente erros durante o processo de exclusão.

### CT-TS-09 - Testes da feature Buscar Imagem

Para o caso de uso "Buscar imagem", podemos identificar os seguintes pontos de teste:

CT-TS-09-c1 Testar a funcionalidade de busca por nome de imagem:

Inserir um nome de imagem válido na caixa de busca.
- Verificar se o sistema exibe corretamente a imagem ou lista de imagens correspondentes ao nome procurado.
- Verificar se as informações relevantes das imagens são exibidas corretamente.

CT-TS-09-c2 Testar o tratamento de busca sem resultados:

Inserir um nome de imagem que não corresponde a nenhuma imagem cadastrada.
- Verificar se o sistema exibe corretamente a mensagem "Nenhuma imagem encontrada!".

Esses são alguns pontos de teste que podem ser considerados para o caso de uso "Buscar imagem". O objetivo é garantir que o sistema realize corretamente a busca de imagens com base no nome fornecido e exiba os resultados esperados. Além disso, é importante verificar se o sistema trata adequadamente a situação em que nenhuma imagem é encontrada.
