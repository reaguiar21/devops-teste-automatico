vendas_mensais = [1000, 2000, 400]

def calcular_total_vendas(vendas):
    return sum(vendas)

def gerar_relatorio():
    total = calcular_total_vendas(vendas_mensais)
    print("Relatório de vendas - Março")
    print("Total de vendas: R$", total)

gerar_relatorio()
