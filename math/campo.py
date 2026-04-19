"CAMPO MAGNÉTICO:"
#=====================#
# Quando se há uma corrente variável (AC ou chaveada) e uma alta frequência, é gerado um campo magnético variável (ruído) 
# que induz corrente em condutores próximos, gerando uma corrente parasita
#=====================#
# Quanto maior:
# - corrente
# - frequência
# - área de loop
# maior o ruído e perdas
#=====================#
# 1. Taxa de variação de corrente
# B = di/dt
# di ≈ ΔI
# dt ≈ 1 / fsw
# B ≈ ΔI * fsw
# ΔI = I * ripple_percent
# I = P / Vdc
# Onde:
# di -> variação de corrente
# dt -> variação de tempo

# Se for muito alto → risco de ruído
#=====================#
# EMI aumenta quando:

# ↑ frequência (fsw)
# ↑ ΔI (ripple)
# ↑ di/dt (variação rápida)
#=====================#
# EMI_index = fsw * ΔI
# ΔI = I * ripple_percent
# I = P / Vdc
# Onde: 
# fsw → frequência de chaveamento
# ΔI → ripple de corrente