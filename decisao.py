# =========================================
# SISTEMA DE DECISÃO
# =========================================

def verificar_energia(energia_total, consumo_total):

    if energia_total < 30:
        return "ALERTA CRÍTICO: ativar protocolos de emergência"

    elif energia_total < 50 and consumo_total > 60:
        return "ALERTA: ativar modo economia"

    elif energia_total < 50:
        return "ALERTA: reduzir consumo"

    elif consumo_total > energia_total:
        return "RISCO: consumo maior que geração"

    else:
        return "Sistema operando normalmente"


def priorizar_sistemas():

    essenciais = ["suporte_vida", "comunicacao"]
    nao_essenciais = ["lazer", "laboratorio"]

    return {
        "manter_ligado": essenciais,
        "desligar_primeiro": nao_essenciais
    }
