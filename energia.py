# =========================================
# ANÁLISE ENERGÉTICA
# =========================================

def analisar_energia(geracao, consumo, reserva):

    if consumo > geracao:
        diferenca = consumo - geracao
        return f"ALERTA: consumo maior que geração em {diferenca} unidades"

    elif geracao > consumo:
        excedente = geracao - consumo
        return f"SUGESTÃO: armazenar {excedente} unidades de energia"

    else:
        return "Energia equilibrada"
