from codigo import calcular_total_vendas, vendas_mensais
import sys  # Coloque aqui no topo, junto com os outros imports

def testar_total_vendas():
    resultado = calcular_total_vendas(vendas_mensais)

    limite_minimo = 5000
    limite_maximo = 10000

    if limite_minimo <= resultado <= limite_maximo:
        print("✅ Teste passou! Total de vendas dentro da faixa esperada.")
    else:
        print("❌ Teste falhou! Valor fora da faixa. Resultado obtido:", resultado)
        sys.exit(1)  # <- Isso aqui agora vai interromper corretamente o workflow
