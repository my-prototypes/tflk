# Recomendações para um processo de bug-fix

Logo abaixo seguem algumas recomendações para um processo básico de correção de bugs: 

1. Identificação do bug: Os bugs podem ser relatados por usuários finais, testadores ou desenvolvedores durante o processo de desenvolvimento ou após a liberação do software. A primeira etapa é identificar o bug, o que pode ser feito por meio de relatórios de erro, registros de problemas ou solicitações de suporte.

2. Registro do bug: O bug é registrado em um sistema de rastreamento de problemas ou em uma ferramenta de gerenciamento de projetos. O registro deve conter informações detalhadas sobre o bug, como a descrição do problema, a sua gravidade, os passos para reproduzir o bug e outras informações relevantes.

3. Análise do bug: O desenvolvedor ou a equipe responsável pela correção do bug analisa o relatório para entender a causa raiz do problema e determinar a melhor abordagem para a correção.

4. Correção do bug: Com base na análise, o desenvolvedor faz as alterações necessárias no código para corrigir o bug. A correção pode envolver a modificação de código fonte, a correção de erros lógicos, a atualização de bibliotecas ou qualquer outra ação relevante para resolver o problema.

5. Testes de unidade: Após a correção, os testes de unidade são realizados para verificar se o bug foi corrigido adequadamente e se a mudança não causou novos problemas.

6. Testes de regressão: Além dos testes de unidade, são realizados testes de regressão para garantir que a correção não afetou outras partes do software. Os testes de regressão verificam se a correção não causou regressões em outras funcionalidades que estavam funcionando corretamente anteriormente.

7. Validação pelo retator: Se o bug foi relatado por um usuário ou cliente, a correção é validada pelo relator para garantir que suas expectativas foram atendidas e o problema foi resolvido conforme o esperado.

8. Implementação da correção: Após a validação e aprovação da correção, a alteração é implementada no código-base do software.

9. Atualização da documentação: A documentação relevante, como notas de lançamento ou documentos de suporte, devem ser atualizados para refletir a correção do bug.

10. Liberação da nova versão: Se o bug foi corrigido em uma versão futura do software, a nova versão é preparada e lançada com a correção incluída.

É importante notar que a gravidade e a prioridade do bug podem influenciar o cronograma e a abordagem de correção. Bugs críticos ou de alta prioridade podem exigir correção imediata, enquanto bugs de baixa prioridade podem ser programados para correção em futuras versões do software. O processo de bug-fix padrão é iterativo e contínuo, pois novos bugs podem ser identificados ao longo do ciclo de vida do software, e o processo é repetido para cada novo bug encontrado.

## Segue exemplo de fluxo de correção de bugs:

1. O processo inicia com o registro do defeito.

2. Em seguida, o defeito é atribuído ao Desenvolvedor responsável para correção.

3. O Desenvolvedor corrige o defeito e marca como concluído.

4. O Testador verifica a correção e decide se o defeito foi corrigido corretamente ou não.

- 4.1 Se o defeito estiver corrigido corretamente, ele é fechado e uma nova release é liberada.
- 4.2 Se o defeito não estiver corrigido, ele é reaberto e o Desenvolvedor responsável deve corrigi-lo novamente.

```
@startuml
title Diagrama de Status - Gestão de Defeitos
[*] --> Registrar_Defeito
Registrar_Defeito --> Corrigir_Defeito : Defeito Registrado
Corrigir_Defeito --> Verificar_Correcao : Concluído
Verificar_Correcao --> Defeito_Corrigido : "Defeito Corrigido Corretamente?"
Verificar_Correcao --> Reabrir_Defeito : "Defeito não Corrigido"
Defeito_Corrigido --> Fechar_Defeito : Sim
Reabrir_Defeito --> Corrigir_Defeito : Não
Fechar_Defeito --> Liberar_Nova_Release : Defeito Fechado
@enduml
```

![Gestao de defeitos](https://raw.githubusercontent.com/my-prototypes/tflk/main/docs/gestao_defeitos.png)
