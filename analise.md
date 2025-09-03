## Tabelas/Entidades do Sistema

* usuario
    - uuid  _(UUID/TEXTO)_
    - nome   _(TEXTO 100)_
    - email  _(TEXTO 255)_
    - senha  _(TEXTO 255)_
    - nivel_acesso _(TEXTO 20)_ (ADMIN/MEMBRO)
    - ativo _(BOOLEAN)_
    - data_criacao _(DATETIME)_
    - ultima_atualizacao _(DATETIME)_

* clinica
    - uuid_clinica _(UUID/TEXTO)_
    - uuid_usuario  _(UUID/TEXTO)_
    - nome_representante _(UUID/TEXTO)_
    - documento_representante  _(TEXTO 25)_
    - endereco _(TEXTO 255)_   **> pode unir vários campos por vírgula ou criar separado**
    - registro_crmv _(NUMERICO 12)_
    - biografia _(TEXTO 255)_  **> colocar observações sobre a clínica**

* funcionario
    - uuid_clinica _(UUID/TEXTO)_
    - uuid_usuario  _(UUID/TEXTO)_

* tutor
    - uuid_tutor _(UUID/TEXTO)_
    - nome_completo _(TEXTO 100)_
    - documento _(TEXTO 25)_
    - endereco _(TEXTO 255)_   **> pode unir vários campos por vírgula ou criar separado**
    - email _(TEXTO 255)_
    - contato _(TEXTO 20)_
    - data_criacao _(DATETIME)_
    - ultima_atualizacao _(DATETIME)_

* pet
    - uuid_tutor _(UUID/TEXTO)_
    - uuid_pet _(UUID/TEXTO)_
    - registro _(TEXTO 20)_ **> Nem sei se existe**
    - nome _(TEXTO 50)_
    - especie _(TEXTO 50)_   **> melhor deixar enum fixo no código**
    - raca _(TEXTO 100)_
    - cor _(TEXTO 50)_  **> melhor deixar enum fixo no código**
    - ano_nascimento _(NUMERO 4)_
    - ativo _(BOOLEAN)_ **> Falescimento/Doação...**
    - observacoes _(TEXTO 255)_ **> Alergia a remédio, exemplo**

* atendimento
    - uuid_clinica _(UUID/TEXTO)_
    - uuid_pet _(UUID/TEXTO)_
    - data_atendimento _(DATETIME)_
    - status _(VARCHAR 15)_ **> Pensando em melhor controle PENDENTE/CONFIRMADO/CANCELADO, pode gerar métricas depois, cliente pode receber link onde atualiza o status**
    - atividade _(VARCHAR 255)_


---
## Rotas iniciais

* Autenticação
> /api/v1/auth/login

* Clínica
> /api/v1/clinica/salvar **(APENAS DA CLÍNICA LOGADA)**

> /api/v1/clinica/editar **(APENAS DA CLÍNICA LOGADA)**

* Funcionário
> /api/v1/funcionario/listar  **(POR CLÍNICA LOGADA, GERAL, POR NOME FUNCIONÁRIO)**

> /api/v1/funcionario/salvar  **(APENAS DA CLÍNICA LOGADA)**

> /api/v1/funcionario/editar **(APENAS DA CLÍNICA LOGADA)**

* Tutor
> /api/v1/tutor/listar **(APENAS DA CLÍNICA LOGADA, NOME TUTOR)**

> /api/v1/tutor/salvar **(APENAS DA CLÍNICA LOGADA)**

> /api/v1/tutor/editar **(APENAS DA CLÍNICA LOGADA)**

* Pet
> /api/v1/pet/listar **(APENAS DA CLÍNICA LOGADA, POR NOME e POR TUTOR)**

> /api/v1/pet/salvar **(APENAS DA CLÍNICA LOGADA)**

> /api/v1/pet/editar **(APENAS DA CLÍNICA LOGADA)**

* Atendimento
> /api/v1/atendimento/listar **(APENAS DA CLÍNICA LOGADA, POR RANGE DE DATA, DATA ESPECÍFICA, TUTOR OU PET)**

> /api/v1/atendimento/salvar **(APENAS DA CLÍNICA LOGADA)**

> /api/v1/atendimento/editar  **(APENAS DA CLÍNICA LOGADA)**
