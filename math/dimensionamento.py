"DIMENSIONAMENTO:"
#A ideia do dimensionamento é coletar os valores de um indutor e capacitor para garantir que o sistema opere corretamente dentro das condições de operação.
#=====================#
#O indutor serve para suavizar a corrente, armazenar energia e evita variações repentinas. Sem ele, a corrente fica "pulsando" e faz do sistema algo isntável
#L = (Vin * D) / (ΔI * fsw) <- Fórmula base simplificada
# Onde:
# Vin → tensão de entrada
# D → duty cycle
# ΔI → ripple de corrente
# fsw → frequência de chaveamento
#=====================#
#O capacitor tem como função estabilizar a tensão do barramento e absorver variações rápidas de carga
#C = Iout / (ΔV * fsw) <- Fórmula base simplificada
# Onde:
# Iout → corrente da carga
# ΔV → ripple de tensão permitido
#=====================#

