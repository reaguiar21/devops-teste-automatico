from codigo import calcular_total_vendas, vendas_mensais

def testar_total_vendas():
    resultado = calcular_total_vendas(vendas_mensais)

    limite_minimo = 5000
    limite_maximo = 10000

    if limite_minimo <= resultado <= limite_maximo:
        print("✅ Teste passou! Total de vendas dentro da faixa esperada.")
    else:
        print("❌ Teste falhou! Valor fora da faixa. Resultado obtido:", resultado)

testar_total_vendas()
