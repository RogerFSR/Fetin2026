"ESTABILIDADE:"
#=====================#
#Esse módulo serve com o propósito de manter a tensão do barramento praticamente constante.
#=====================#
# Ripple de tensão
# ΔV = I / (C * fsw)
# I = P / Vdc
# Onde:
# ΔV → ripple de tensão permitido
# I → Corrente média
# C → Capacitor
#=====================#
# Efeito ESR (muito importante)
# ΔV_ESR = I * ESR
# I = P / Vdc
# Onde:
# ESR → resistência interna do capacitor
# I → Corrente média
#=====================#
# O que causa instabilidade:
# - carga variando rápido
# - capacitor pequeno
# - ESR alto
# - resposta lenta do sistema
#=====================#
# Métrica prática:
# Ripple (%) = (ΔV / Vdc) * 100
# Onde:
# ΔV → ripple de tensão permitido
# Vdc → tensão do barramento DC

# Regra prática:
# < 2% → excelente
# 2–5% → aceitável

# 5% → problema