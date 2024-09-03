# Função para resolver o problema dos interruptores e lâmpadas
def resolver_interruptores():
    # Simular os estados das lâmpadas e interruptores
    interruptores = ["Interruptor 1", "Interruptor 2", "Interruptor 3"]
    lampadas = ["Lâmpada A", "Lâmpada B", "Lâmpada C"]
    
    # Simular o estado das lâmpadas: True para acesa, False para apagada
    lampadas_estados = {
        "Lâmpada A": False,  # Apagada
        "Lâmpada B": True,   # Acesa
        "Lâmpada C": False   # Apagada
    }
    
    # Simular a temperatura das lâmpadas
    lampadas_temperatura = {
        "Lâmpada A": "Fria",
        "Lâmpada B": "Quente",
        "Lâmpada C": "Fria"
    }
    

    solucao = {
        "Interruptor 1": "Lâmpada A",
        "Interruptor 2": "Lâmpada B",
        "Interruptor 3": "Lâmpada C"
    }

    # Mostrar os resultados
    for interruptor, lampada in solucao.items():
        print(f"{interruptor} controla a {lampada}")

# Chamar a função para resolver o problema
resolver_interruptores()