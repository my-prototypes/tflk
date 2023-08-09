# Controle de Branches

Segue exemplo de desenvolvimento paralelo de 6 funcionalidades (feature1, feature2, feature3, feature4, feature5 e feature6) construídas por 3 desenvolvedores (desenvolvedor1, desenvolvedor2 e desenvolvedor3). Cada desenvolvedor cria seu próprio ramo (dev1, dev2, dev3) e faz commits em cada ramo. O desenvolvedor1 implementa as funcionalidades 1 e 2, o desenvolvedor2 implementa as funcionalidades 3 e 4, e o desenvolvedor3 implementa as funcionalidades 5 e 6. O ramo principal estável é o main.

Você pode criar este esquema de controle versão através de scripts Mermaid (https://mermaid.js.org) usando a sintaxe Gitgraph (https://mermaid.js.org/syntax/gitgraph.html) abaixo

## Devs integrando no branch principal (main)

```
gitGraph
   commit id: "init repository"
   commit id: "Frameworks e Libs"
   commit id: "Integra Back-end"
   commit id: "Integra Front-end"
   branch dev1
   branch dev2
   branch dev3
   checkout dev1
   commit id: "Feature 1"
   commit id: "Feature 2"
   commit id: "Testes de Integração1"
   checkout main
   merge dev1 id: "Integra F1 e F2"
   commit id: "Resolve conflitos dev1"
   checkout dev2
   commit id: "Feature 3"
   commit id: "Feature 4"
   commit id: "Testes de Integração2"
   checkout main
   merge dev2 id: "Integra F3 e F4"
   commit id: "Resolve conflitos dev2"
   checkout dev3
   commit id: "Feature 5"
   commit id: "Feature 6"
   commit id: "Testes de Integração3"
   checkout main
   merge dev3 id: "Integra F5 e F6"
   commit id: "Resolve conflitos dev3"
   commit id: "Testes de Integração4"
   commit id: "Testes de Sistema"
   commit id: "Prototipo1"
```

O diagrama resultante é: 

![Esquema de branches!](https://raw.githubusercontent.com/my-prototypes/tflk/main/docs/branches_cenario1.png) "Branches: main, dev1, dev2 e dev3"

## Devs integrando no branch de desenvolvimento

```
gitGraph
   commit id: "init repository"
   commit id: "Frameworks e Libs"
   commit id: "Integra Back-end"
   commit id: "Integra Front-end"
   branch desenvolvimento
   branch dev1
   branch dev2
   branch dev3
   checkout dev1
   commit id: "Feature 1"
   commit id: "Feature 2"
   commit id: "Testes de Integração (F1,F2)"
   checkout desenvolvimento
   merge dev1 id: "Integra F1 e F2"
   commit id: "Resolve conflitos dev1"
   checkout dev2
   commit id: "Feature 3"
   commit id: "Feature 4"
   commit id: "Testes de Integração (F3,F4)"
   checkout desenvolvimento
   merge dev2 id: "Integra F1,F2,F3 e F4"
   commit id: "Resolve conflitos dev2"
   checkout dev3
   commit id: "Feature 5"
   commit id: "Feature 6"
   commit id: "Testes de Integração (F5,F6)"
   checkout desenvolvimento
   merge dev3 id: "Integra F1,F2,F3,F4,F5 e F6"
   commit id: "Resolve conflitos dev3"
   commit id: "Testes de Integração4 (F1,..,F6)"
   commit id: "Testes de Sistema"
   commit id: "Prototipo1"
   checkout main
   merge desenvolvimento id: "Integra Features (F1,...,F6)"
   commit id: "Release 1.0.0" tag: "v1.0.0"
```

O diagrama resultante é: 

![Esquema de branches!](https://raw.githubusercontent.com/my-prototypes/tflk/main/docs/branch_desenvolvimento.png) "Branches: main, desenvolvimento, dev1, dev2 e dev3"

### Descrição do fluxo de integração no branch de desenvolvimento

O diagrama começa com quatro commits iniciais ("repositório inicial," "Frameworks e Bibliotecas," "Integração do Back-end," "Integração do Front-end") no branch principal (main).

São criados quatro branches: desenvolvimento, dev1, dev2 e dev3.

O diagrama mostra as seguintes ações no branch dev1:

- O branch dev1 é verificado (o HEAD se move para dev1).
- Duas novas funcionalidades ("Funcionalidade 1" e "Funcionalidade 2") são adicionadas ao branch dev1.
- Um commit para "Testes de Integração (F1,F2)" é adicionado ao branch dev1.
- Em seguida, o branch é verificado novamente (HEAD volta para desenvolvimento).
- É feito um merge de dev1 para desenvolvimento, criando um novo commit com a mensagem "Integra F1 e F2" no branch desenvolvimento.

Um novo commit ("Resolver conflitos dev1") é feito no branch desenvolvimento para resolver quaisquer conflitos que ocorreram durante o merge.

Uma sequência similar de ações é repetida para o branch dev2, onde duas novas funcionalidades ("Funcionalidade 3" e "Funcionalidade 4") são adicionadas, seguidas por um merge para desenvolvimento, resolvendo conflitos e adicionando um novo commit no branch desenvolvimento.

O mesmo é feito para o branch dev3, onde duas novas funcionalidades ("Funcionalidade 5" e "Funcionalidade 6") são adicionadas, seguidas por um merge para desenvolvimento, resolvendo conflitos e adicionando um novo commit no branch desenvolvimento.

Commits adicionais ("Testes de Integração4 (F1,..,F6)," "Testes de Sistema," "Protótipo 1") são feitos no branch desenvolvimento após os merges.

Por fim, o branch main é verificado e é feito um merge de desenvolvimento para main, criando um novo commit com a mensagem "Integra Funcionalidades (F1,...,F6)" no branch main.

Um novo commit ("Release 1.0.0") é feito no branch main, e uma tag "v1.0.0" é adicionada para marcar a versão da release contendo todas as features implementadas.

O diagrama representa o fluxo de desenvolvimento com múltiplos branches (dev1, dev2 e dev3) de desenvolvedores que implementam suas respectivas funcionalidades, onde cada dev faz o merge com o branch de desenvolvimento, e por fim, o branch de desenvolvimento é mesclado no branch principal (main) para gerar uma release marcada com a tag "v1.0.0". 
