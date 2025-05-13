#Mini projeto parte 1
print("Mini projeto parte 1")
nome_completo = "Antonieta da Silva"

dia_nascimento = 16
mes_nascimento = 5
ano_nascimento = 1998
data_nascimento = f"{dia_nascimento}/{mes_nascimento}/{ano_nascimento}" 
dia_atual = 14
mes_atual = 5
ano_atual = 2025
idade = 2024 - ano_nascimento

dias_em_um_ano = 365
dias_em_um_mes = 30

dias_de_anos_vividos = (ano_atual - ano_nascimento) * dias_em_um_ano
dias_de_mes_vividos = (mes_atual - mes_nascimento) * dias_em_um_mes
dias_vividos_no_mes = dia_atual - dia_nascimento

total_de_dias_vividos = dias_de_anos_vividos + dias_de_mes_vividos + dias_vividos_no_mes

print (f"{nome_completo}, nascida em {data_nascimento}")
print (f"{nome_completo} tem {total_de_dias_vividos} dias de vida")
print (f"{nome_completo} tem {idade} anos de vida")

#Mini projeto parte 2
print("\nMini projeto parte 2")
patrimonio = 2000.00
recebimentos_mensais = 1518.00
gastos = 1077.00
investimentos_mensais = 150.00
salario_minimo = 1518.00

equivalente_salario_minimo = recebimentos_mensais / salario_minimo
equivalente_gastos = gastos / recebimentos_mensais * 100
patrimonio_em_um_mes = patrimonio + investimentos_mensais
saldo_livre = recebimentos_mensais - gastos - investimentos_mensais
print(f"{nome_completo} recebe mensalmente R${recebimentos_mensais:.2f}")
print(f"Os recebimentos equivalem a {equivalente_salario_minimo} salários mínimos")
print(f"{nome_completo} tem um patrimonio de R${patrimonio:.2f}")
print(f"{nome_completo} gasta R${gastos:.2f} por mês")
print(f"Os gastos equivalem a {equivalente_gastos}% da sua renda")
print(f"{nome_completo} investe mensalmente R${investimentos_mensais:.2f}")
print(f"{nome_completo} após 1 mês está com o patrimonio de R${patrimonio_em_um_mes:.2f}")
print(f"O saldo de dinheiro livre no mês foi de R${saldo_livre:.2f}")

#Mini projeto parte 3
meses_em_um_ano = 12
taxa_de_rendimento = 0.005
rendimento_em_um_ano = patrimonio * ((1 + taxa_de_rendimento) ** meses_em_um_ano - 1)
patrimonio_final = patrimonio + rendimento_em_um_ano

print("\nMini projeto parte 3")
print(f"Se {nome_completo} não investir nada,")
print(f"após {meses_em_um_ano} meses o patrimônio")
print(f"terá rendido R${rendimento_em_um_ano} e será R${patrimonio_final}")

