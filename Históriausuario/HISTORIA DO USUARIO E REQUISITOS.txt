Requisitos para o Jogo
Funcionalidades:
Simular a retirada aleatória de bolas numeradas de 1 a 20.
Definir o alvo como a soma dos valores das bolas sorteadas.
Permitir que o usuário faça palpites.
Verificar se o palpite do usuário é igual ao alvo.
Exibir mensagens de feedback para o usuário (acerto, erro, alvo excedido).
Manter um histórico das jogadas.
Regras
O alvo inicial é um número aleatório entre 1 e 20.
A cada erro, o novo alvo é a soma do alvo anterior com um novo número aleatório entre 1 e 20.
O usuário tem 10 tentativas para adivinhar o alvo.
Se o alvo ultrapassar 100 antes do usuário acertar, o computador vence.
Interface
Tela inicial com instruções do jogo.
Campo para o usuário inserir seu palpite.
Exibição do alvo e do palpite após cada tentativa.
Mensagens de feedback para o usuário.
Histórico das jogadas.
Desempenho:
O jogo deve ser rápido e responsivo.
O histórico das jogadas deve ser eficientemente armazenado e acessado.
Segurança
O sistema deve ser protegido contra entradas inválidas do usuário.
Testes
O jogo deve ser testado para garantir que todas as funcionalidades estejam funcionando corretamente.
Documentação
Deve ser criada documentação completa do jogo, incluindo requisitos, design, implementação e testes.
Manutenabilidade
O código do jogo deve ser bem organizado, documentado e fácil de manter.
Extensibilidade
O jogo deve ser facilmente extensível para permitir a inclusão de novas funcionalidades no futuro.
Portabilidade
O jogo deve ser portável para diferentes plataformas.
História do Usuário
Nome: Ana
Idade: 25 anos
Objetivo: Ana quer se divertir jogando um jogo desafiador e interativo.
Cenário: Ana está em casa, à noite, buscando uma forma de se distrair. Ela decide jogar o jogo de adivinhar o número.
Tarefas
1.	Ana lê as instruções do jogo e decide começar a jogar.
2.	Ana insere seu palpite para o alvo.
3.	O sistema verifica se o palpite está correto e exibe uma mensagem de feedback.
4.	Se o palpite estiver errado, Ana tem mais 9 tentativas para adivinhar o alvo.
5.	Se o palpite estiver correto, Ana vence o jogo.
6.	Se o alvo ultrapassar 100 antes de Ana adivinhar, o computador vence o jogo.
Requisitos de Não Aceitação:
Ana não pode inserir um palpite que não seja um número entre 1 e 20.
Ana não pode inserir o mesmo palpite duas vezes.
Design Orientado a Objetos
Classes
Jogo: Controla o fluxo do jogo.
Bola: Representa uma bola numerada.
Urna: Contém as bolas numeradas.
Alvo: Representa o número que o usuário precisa adivinhar.
Palpite: Representa o palpite do usuário.
Interface: Exibe informações para o usuário e recebe entradas do usuário.
Relacionamentos
A Urna contém Bolas.
O Jogo utiliza a Urna para sortear Bolas.
O Alvo é composto por Bolas.
O Jogo compara o Palpite com o Alvo.
A Interface interage com o Jogo e o Usuário.
Diagrama de Classes
[Classe Jogo]
- iniciarJogo()
- verificarPalpite()
- exibirMensagem()

[Classe Bola]
- valor: int

[Classe Urna]
- bolas: List<Bola>
- sortearBola(): Bola

[Classe Alvo]
- valor: int
- adicionarBola(bola: Bola)

[Classe Palpite]
- valor: int

[Classe Interface]
- exibirInstrucoes()
- receberPalpite(): int
- exibirFeedback(feedback: str)    main()
