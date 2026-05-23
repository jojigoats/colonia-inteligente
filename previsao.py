# =========================================
# PREVISÃO DE ENERGIA EÓLICA
# REGRESSÃO LINEAR SIMPLES
# =========================================

def prever_energia_eolica(vento):

    ventos = [8, 10, 12]
    energias = [20, 25, 30]

    media_x = sum(ventos) / len(ventos)
    media_y = sum(energias) / len(energias)

    numerador = 0
    denominador = 0

    for i in range(len(ventos)):
        numerador += (ventos[i] - media_x) * (energias[i] - media_y)
        denominador += (ventos[i] - media_x) ** 2

    a = numerador / denominador
    b = media_y - a * media_x

    previsao = a * vento + b

    return round(previsao, 2)
