# Arquitetura de um sistema de grande porte: Netflix

**Nome:** Guilherme Reis Carvalho  
**Disciplina:** Arquitetura de Software  
**Modelo de documentação:** C4 Model — níveis 1 e 2  
**Estilos exigidos:** Backend for Frontend (BFF), Microservices, Database per Service e API Gateway

## 1. Objetivo e recorte

O sistema escolhido é a plataforma de streaming da **Netflix**. O recorte deste trabalho cobre a experiência de descoberta e reprodução de conteúdo: autenticação, perfis, catálogo, recomendações, assinatura e playback.

A proposta combina fatos públicos com uma adaptação acadêmica. A Netflix publica componentes de sua plataforma, como o **Zuul**, descrito como a porta de entrada das requisições dos dispositivos e sites para o backend de streaming. Já os nomes, limites e bancos dos serviços abaixo são uma decomposição didática coerente com os quatro estilos solicitados — não uma declaração de que todos esses detalhes sejam exatamente iguais aos da implementação interna da Netflix.

## 2. Pesquisa do sistema de referência

O Zuul é um gateway de camada 7 com roteamento dinâmico, monitoramento, resiliência e segurança. A documentação pública também cita autenticação, métricas, roteamento para clusters, redução de carga e resiliência entre regiões.

O ecossistema público da Netflix também mostra uma forte orientação a serviços independentes e a componentes especializados. Por exemplo, o serviço Simone possui servidor, cliente e interface web próprios, usa Cassandra para persistência e Kafka para distribuição de eventos. Isso sustenta a escolha de uma arquitetura distribuída, embora o diagrama desta entrega seja uma simplificação voltada à disciplina.

## 3. Entendimento dos quatro estilos arquiteturais

### 3.1 API Gateway

É o ponto de entrada único para os clientes. Ele funciona como proxy reverso e pode fazer roteamento, autenticação, limitação de requisições, terminação TLS, observabilidade, cache e agregação. O cliente não precisa conhecer os endereços internos dos microsserviços.

**Aplicação na proposta:** o **Netflix API Gateway / Zuul** recebe chamadas de web, mobile e TV, valida o token, aplica políticas e encaminha a requisição para o BFF adequado.

**Benefícios:** menor superfície pública, políticas centralizadas e desacoplamento entre cliente e serviços.  
**Riscos:** pode virar gargalo ou concentrar lógica demais; por isso deve ser replicado, monitorado e manter apenas responsabilidades transversais.

### 3.2 Backend for Frontend (BFF)

É um backend específico para cada tipo de frontend. Em vez de obrigar web, mobile e TV a consumirem exatamente o mesmo contrato, cada BFF adapta payloads, paginação, agregação e quantidade de dados à experiência do cliente.

**Aplicação na proposta:** há três BFFs: **Web BFF**, **Mobile BFF** e **TV BFF**. O mobile prioriza respostas menores e cache; a TV prioriza navegação com controle remoto e pré-carregamento; a web pode receber respostas mais completas.

**Benefícios:** evolução independente das interfaces e respostas mais adequadas.  
**Riscos:** duplicação de código e mais componentes para operar. Regras de negócio continuam nos microsserviços, não nos BFFs.

### 3.3 Microservices

Divide a aplicação em serviços pequenos, autônomos e orientados a capacidades de negócio. Cada serviço pode ser implantado e escalado independentemente, com contrato de API próprio.

**Aplicação na proposta:** identidade, perfil, catálogo, recomendação, playback e assinatura são serviços separados. Uma falha no serviço de recomendação, por exemplo, não deve impedir a reprodução de um título.

**Benefícios:** isolamento de falhas, deploy independente e escala por domínio.  
**Riscos:** maior complexidade operacional, latência de rede, observabilidade distribuída e necessidade de lidar com consistência eventual.

### 3.4 Database per Service

Cada microsserviço possui e controla seu próprio armazenamento. Outros serviços não acessam tabelas internas diretamente; a integração ocorre por APIs ou eventos.

**Aplicação na proposta:** Catálogo acessa apenas o Catálogo DB; Recomendação acessa apenas o Recommendation DB; e assim por diante. A tecnologia pode variar conforme o caso de uso.

**Benefícios:** baixo acoplamento, autonomia de schema e possibilidade de escolher o banco adequado.  
**Riscos:** consultas que cruzam domínios precisam de composição, projeções de leitura ou eventos; transações distribuídas devem ser evitadas ou tratadas com Saga.

## 4. Arquitetura adaptada

### Componentes principais

| Camada | Componentes | Responsabilidade |
|---|---|---|
| Clientes | Web, Mobile, Smart TV/console | Interação do assinante |
| Entrada | API Gateway / Zuul | Autenticação, rate limit, roteamento, cache, tracing |
| Experiência | Web BFF, Mobile BFF, TV BFF | Contrato específico por frontend e agregação de respostas |
| Negócio | Identity, Profile, Catalog, Recommendation, Playback, Subscription | Capacidades de negócio isoladas |
| Dados | Um banco por serviço | Persistência privada de cada domínio |
| Externos | Identity Provider, Payment Provider, CDN de vídeo | Serviços fora do núcleo da plataforma |

### Relação entre os estilos

O fluxo é: **cliente → API Gateway → BFF → microsserviços → banco privado do serviço**. O gateway é a borda comum; o BFF adapta a experiência; os microsserviços executam o negócio; o Database per Service protege a autonomia dos domínios.

Para uma tela inicial, por exemplo, o Mobile BFF pode chamar Profile, Catalog e Recommendation em paralelo e devolver um payload compacto. O aplicativo faz uma chamada; o BFF compõe a resposta; cada serviço consulta somente seu próprio banco.

### Fluxo de reprodução

1. O cliente solicita a reprodução de um título ao API Gateway.
2. O gateway valida o token e roteia ao BFF correspondente.
3. O BFF chama Playback e, se necessário, Profile e Subscription.
4. Playback verifica autorização, plano e disponibilidade.
5. Playback retorna um manifesto/licença; o conteúdo de vídeo é entregue pela CDN, sem atravessar todos os microsserviços.
6. Eventos de início, pausa e conclusão podem ser publicados para analytics e atualização de recomendações.

### Decisões de consistência e resiliência

- A leitura da home pode aceitar consistência eventual em recomendações e catálogo.
- Assinaturas e cobrança exigem idempotência, auditoria e integração segura com o provedor de pagamento.
- BFFs usam timeout, retry limitado, circuit breaker e respostas parciais para que uma falha de recomendação não bloqueie a home.
- O gateway e os BFFs devem ser stateless e replicados em múltiplas zonas/regiões.
- Tracing distribuído usa um correlation ID do gateway até os microsserviços.
- Nenhum serviço consulta diretamente o banco de outro serviço.

## 5. Leitura dos diagramas C4

### Nível 1 — System Context

Mostra o sistema Netflix Streaming como uma caixa única, seus usuários/clientes e sistemas externos: provedor de identidade, provedor de pagamento e CDN. O objetivo é delimitar o sistema e suas relações, sem detalhar tecnologia interna.

### Nível 2 — Containers

Abre o sistema Netflix Streaming e apresenta seus containers executáveis/deployáveis: API Gateway, BFFs, microsserviços, bancos privados, barramento de eventos e componentes externos. A legenda diferencia clientes, entrada, BFF, serviços, bancos e sistemas externos.

## 6. Referências consultadas

1. [Netflix Zuul — documentação oficial do projeto](https://github.com/Netflix/zuul/wiki): Zuul como porta de entrada do streaming e suas funções de roteamento, segurança, monitoramento e resiliência.
2. [Netflix Zuul — repositório oficial](https://github.com/Netflix/zuul): gateway de camada 7 e recursos de roteamento dinâmico, monitoramento, resiliência e segurança.
3. [Netflix TechBlog — Simone](https://netflixtechblog.com/https-medium-com-netflix-techblog-simone-a-distributed-simulation-service-b2c85131ca1b): exemplo público de serviço distribuído com servidor, cliente, Cassandra e Kafka.
4. [Microsoft Azure Architecture Center — Backends for Frontends](https://learn.microsoft.com/azure/architecture/patterns/backends-for-frontends): definição, usos, benefícios e trade-offs do BFF.
5. [Microsoft Azure Architecture Center — API gateways](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/gateway): gateway como ponto único, roteamento, agregação e offloading.
6. [Microsoft Azure Architecture Center — Gateway Aggregation](https://learn.microsoft.com/en-us/azure/architecture/patterns/gateway-aggregation): composição de chamadas de vários serviços em uma resposta.

## 7. Roteiro curto para apresentação

1. Apresentar a Netflix e delimitar o recorte.
2. Explicar no nível 1 quem usa o sistema e quais sistemas externos participam.
3. Abrir o nível 2 e seguir o fluxo cliente → gateway → BFF → serviço → banco.
4. Destacar que o BFF é específico por frontend e que o gateway concentra políticas transversais.
5. Mostrar um exemplo de Database per Service e explicar por que não existe banco compartilhado.
6. Fechar com os trade-offs: escalabilidade e autonomia versus complexidade distribuída.
