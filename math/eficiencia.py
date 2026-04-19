"EFICIÊNCIA:"
#Medir a eficiencia de um circuíto é importante para identificar possíveis perdas em um circuíto
#=====================#
# 1. Perdas por condução
# Pcond = I² * R
# I = P / Vdc
# Onde
# I → Corrente média
# R → Resistencia
# ocorre em cabos, MOSFETs, indutores
# cresce MUITO com corrente
#=====================#
# 2. Perdas por chaveamento
# Psw ≈ Vdc * I * (ton + toff) * fsw
# I = P / Vdc
# Onde:
# V → Tensão no MOSFET (Vdc ou Vin)
# I → Corrente passada no MOSFET
# fsw → frequência de chaveamento
# ton → tempo que leva para ligar
# toff → tempo que leva para desligar
# Psw → perda de chaveamento
# acontece quando liga/desliga
# aumenta com frequência
#=====================#
# 3. Perdas magnéticas
# no núcleo do indutor
# dependem de frequência e fluxo magnético
#=====================#