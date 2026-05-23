# =========================================
# SISTEMA INTELIGENTE DA COLÔNIA
# =========================================

from dados import colonia
from decisao import verificar_energia, priorizar_sistemas
from previsao import prever_energia_eolica
from energia import analisar_energia


energia_total = (
    colonia["energia"]["solar"] +
    colonia["energia"]["eolica"] +
    colonia["energia"]["reserva"]
)

consumo_total = sum(colonia["consumo"].values())

decisao = verificar_energia(energia_total, consumo_total)

vento = colonia["clima"]["vento"]
previsao = prever_energia_eolica(vento)

analise = analisar_energia(
    energia_total,
    consumo_total,
    colonia["energia"]["reserva"]
)

prioridades = priorizar_sistemas()

print("\n===== COLÔNIA INTELIGENTE =====\n")

print(f"Energia total: {energia_total}")
print(f"Consumo total: {consumo_total}")

print(f"Previsão de energia eólica: {previsao}")

print("\nDecisão do sistema:")
print(decisao)

print("\nAnálise energética:")
print(analise)

print("\nPriorização de sistemas:")
print(f"Essenciais: {prioridades['manter_ligado']}")
print(f"Não essenciais: {prioridades['desligar_primeiro']}")

print("\n================================")
