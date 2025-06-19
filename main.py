from services.cliente_service import ClienteService
from services.produto_service import ProdutoService
from services.reserva_service import ReservaService
from services.compra_service import CompraService
from utils.logger import Logger

cliente_service = ClienteService()
produto_service = ProdutoService()
reserva_service = ReservaService()
compra_service = CompraService()
logger = Logger()

def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("Email: ")
    cliente = cliente_service.cadastrar(nome, email)
    logger.info(f"Cliente cadastrado: {cliente.nome} ({cliente.email}) ID: {cliente.id}")  
    print(f"Cliente cadastrado com ID: {cliente.id}\n")

def listar_clientes():
    clientes = cliente_service.listar()
    logger.info("Listando clientes")  
    print("\n### Clientes ###")
    for c in clientes:
        print(f"{c.id} - {c.nome} ({c.email})")
    print()

def fazer_reserva():
    listar_clientes()
    cliente_id = input("ID do cliente: ")
    cliente = cliente_service.buscar_por_id(cliente_id)
    if not cliente:
        logger.warning(f"Tentativa de reserva para cliente inexistente: {cliente_id}")  
        print("Cliente não encontrado.\n")
        return

    filme = input("Nome do filme: ")
    qtd_ingressos = int(input("Quantidade de ingressos: "))
    reserva = reserva_service.criar_reserva(cliente, filme, qtd_ingressos)
    logger.info(f"Reserva criada: {reserva.id} para cliente {cliente.nome} ({cliente.id})")  
    print(f"Reserva realizada com ID: {reserva.id}\n")

def comprar_ingresso():
    listar_clientes()
    cliente_id = input("ID do cliente: ")
    cliente = cliente_service.buscar_por_id(cliente_id)
    if not cliente:
        logger.warning(f"Tentativa de compra para cliente inexistente: {cliente_id}")  
        print("Cliente não encontrado.\n")
        return

    reservas_cliente = reserva_service.buscar_por_cliente(cliente)
    if reservas_cliente:
        print("\nReservas disponíveis:")
        for i, r in enumerate(reservas_cliente):
            print(f"{i+1}. ID {r.id} - {r.filme} ({r.qtd_ingressos} ingressos)")
        escolha = input("Escolha a reserva para comprar (ou pressione 'Enter' para compra direta): ")
        if escolha:
            index = int(escolha) - 1
            reserva = reservas_cliente[index]
            qtd_ingressos = reserva.qtd_ingressos
            filme = reserva.filme
            reserva_service.remover(reserva)
            logger.info(f"Reserva {reserva.id} convertida em compra para cliente {cliente.id}")  
        else:
            filme = input("Nome do filme: ")
            qtd_ingressos = int(input("Quantidade de ingressos: "))
    else:
        logger.info(f"Nenhuma reserva encontrada para cliente {cliente.id}, seguindo para compra direta")  
        print("Nenhuma reserva encontrada. Seguindo para compra.")
        filme = input("Nome do filme: ")
        qtd_ingressos = int(input("Quantidade de ingressos: "))

    compra = compra_service.criar_compra(cliente, filme, qtd_ingressos)
    logger.info(f"Compra criada: {compra.id} para cliente {cliente.id}")  

    produtos = produto_service.listar()
    print("\nDeseja incluir um adicional para seu filme?")
    for i, p in enumerate(produtos):
        print(f"{i + 1}. {p.nome} - R${p.preco:.2f}")

    while True:
        escolha = input("Escolha um produto (Ou pressione 'Enter' para finalizar): ")
        if not escolha:
            break
        index = int(escolha) - 1
        if 0 <= index < len(produtos):
            quantidade = int(input("Quantidade: "))
            compra.adicionar_produto(produtos[index], quantidade)
            logger.info(f"Produto adicionado à compra {compra.id}: {produtos[index].nome} x{quantidade}")  

    print(f"\nCompra realizada com ID: {compra.id}")
    print(f"Total: R${compra.total():.2f}\n")

def listar_reservas():
    reservas = reserva_service.listar()
    logger.info("Listando reservas")  
    print("\n### Reservas ###")
    for r in reservas:
        print(f"ID: {r.id} | Cliente: {r.cliente.nome} | Filme: {r.filme} | Qtd: {r.qtd_ingressos}")
    print()

def listar_compras():
    compras = compra_service.listar()
    logger.info("Listando compras")  
    print("\n### Compras ###")
    for c in compras:
        print(f"Compra {c.id} - Cliente: {c.cliente.nome} - Filme: {c.filme}")
        print(f"Ingressos: {c.qtd_ingressos}")
        if c.produtos:
            print("Produtos:")
            for produto, qtd in c.produtos:
                print(f"  - {produto.nome} x{qtd} = R${produto.preco * qtd:.2f}")
        print(f"Total: R${c.total():.2f}\n")

def menu():
    while True:
        print("\n### Bem vindo ao cinema! ###")
        print("\n1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Fazer reserva")
        print("4. Comprar ingresso")
        print("5. Listar reservas")
        print("6. Listar compras")
        print("0. Sair")

        op = input("\nEscolha uma opção: ")

        if op == "1":
            cadastrar_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            fazer_reserva()
        elif op == "4":
            comprar_ingresso()
        elif op == "5":
            listar_reservas()
        elif op == "6":
            listar_compras()
        elif op == "0":
            print("Sistema finalizado")
            break
        else:
            print("Erro! opção inválida!\n")

if __name__ == "__main__":
    menu()