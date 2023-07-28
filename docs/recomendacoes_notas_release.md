# Recomendações para criação de notas de release

Logo abaixo seguem algumas recomendações para a produção de notas de release:

1. Resumo das principais alterações: Um breve resumo ou visão geral das principais alterações e aprimoramentos introduzidos na nova versão. Por exemplo: "A versão 2.0 inclui uma interface de usuário totalmente redesenhada, suporte a novos recursos de compartilhamento de arquivos e melhorias significativas no desempenho."

2. Lista de novos recursos: Uma seção que destaca os novos recursos adicionados na versão. Por exemplo: "Novo recurso: Chat em tempo real para comunicação instantânea entre usuários."

3. Correções de bugs: Uma lista das correções aplicadas para resolver problemas conhecidos na versão anterior. Por exemplo: "Corrigido: O problema de congelamento do aplicativo ao enviar arquivos grandes foi resolvido."

4. Melhorias de desempenho: Informações sobre otimizações ou aprimoramentos no desempenho do software. Por exemplo: "A velocidade de inicialização do aplicativo foi aprimorada em 30%."

5. Alterações de interface do usuário: Se houver mudanças significativas na interface do usuário, é importante comunicá-las. Por exemplo: "Nova barra de navegação na parte inferior para facilitar o acesso a recursos importantes."

6. Compatibilidade e requisitos do sistema: Informações sobre requisitos de hardware ou software atualizados para a nova versão. Por exemplo: "A partir da versão 3.0, o aplicativo requer Android 8.0 ou superior."

7. Notas adicionais: Outras informações relevantes, como avisos importantes, soluções alternativas para problemas conhecidos ou qualquer outra informação que os usuários precisem estar cientes.

## Criando uma Tag no GitHub:

1. No repositório principal 

https://github.com/xyz/seu_repositorio/releases

2. Escolha a opção "Create a new release" ou "Draft a new release"

3. Escolha o branch "alvo" e descreva as informações da release

4. Publique a release

## Criando uma Tag via Git:

Para criar uma tag na sua branch atual, execute o seguinte:

```bash
git tag <nome-da-tag>
```

Se você quiser incluir uma descrição com a sua tag, adicione -a para criar uma tag anotada:

```bash
git tag <nome-da-tag> -a
```

Isso criará uma tag local com o estado atual da branch que você está. Ao fazer push para o seu repositório remoto, as tags NÃO são incluídas por padrão. Você precisará dizer explicitamente que quer fazer push das suas tags para o seu repositório remoto:

```bash
git push origin --tags
```

Para uma explicação mais detalhada sobre tags no Git, você pode consultar a documentação oficial: https://git-scm.com/book/en/v2/Git-Basics-Tagging.
