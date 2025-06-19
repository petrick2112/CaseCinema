# 🎟️ Sistema de Ingressos

## Visão Geral
O **Sistema de Ingressos** é uma aplicação Python para gerenciar clientes, reservas e compras em um cinema. Com uma interface simples, você pode cadastrar clientes, fazer reservas, comprar ingressos e adicionar produtos como pipoca e bebidas! 🍿🥤

## Estrutura do Projeto
```
projeto_ingressos_atualizado
├── main.py                  # Ponto de entrada da aplicação
├── requirements.txt         # Dependências do projeto
├── .gitignore               # Arquivos ignorados pelo Git
├── README.md                # Documentação do projeto
├── models                   # Modelos de dados
│   ├── cliente.py           # Classe Cliente
│   ├── compra.py            # Classe Compra
│   ├── produto.py           # Classe Produto
│   └── reserva.py           # Classe Reserva
├── services                 # Lógica de negócio
│   ├── cliente_service.py    # Operações de cliente
│   ├── compra_service.py     # Operações de compra
│   ├── produto_service.py    # Operações de produto
│   └── reserva_service.py    # Operações de reserva
└── utils                    # Utilitários
    └── logger.py            # Registro de logs
```

## Funcionalidades ✨
- **Gestão de Clientes**: Cadastre, liste e pesquise clientes por ID.
- **Gestão de Reservas**: Crie reservas para filmes, veja todas as reservas e gerencie por cliente.
- **Gestão de Compras**: Compre ingressos e adicione produtos como pipoca e bebidas.
- **Logs**: Todas as ações são registradas para facilitar o acompanhamento e a resolução de problemas.

## Instalação 🚀
Clone o repositório e instale as dependências:

```bash
pip install -r requirements.txt
```

## Como Usar ▶️
Execute a aplicação com:

```bash
python main.py
```

Siga o menu na tela para gerenciar clientes, reservas e compras de forma fácil e rápida!

## Logs 📝
Os logs ficam na pasta `logs`, no arquivo `app.log`. Eles ajudam a monitorar tudo o que acontece no sistema.

## Testes 🧪
Utilize o `pytest` para rodar os testes:

```bash
pytest
```

## Contribua! 🤝
Sugestões e melhorias são bem-vindas! Envie um pull request ou abra uma issue.

## Licença 📄
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais