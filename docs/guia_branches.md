# Controle de Branches

Segue exemplo de desenvolvimento paralelo de 6 funcionalidades (feature1, feature2, feature3, feature4, feature5 e feature6) construídas por 3 desenvolvedores (desenvolvedor1, desenvolvedor2 e desenvolvedor3). Cada desenvolvedor cria seu próprio ramo (dev1, dev2, dev3) e faz commits em cada ramo. O desenvolvedor1 implementa as funcionalidades 1 e 2, o desenvolvedor2 implementa as funcionalidades 3 e 4, e o desenvolvedor3 implementa as funcionalidades 5 e 6. O ramo principal estável é o main.

Você pode criar este esquema de controle versão através de scripts Mermaid usando a sintax Gitgraph (https://mermaid.js.org/syntax/gitgraph.html) abaixo

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

xxx
