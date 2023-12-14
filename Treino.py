# AULA 56
# from openpyxl import Workbook
#
# wb = Workbook()
#
# nome_arquivo = 'primeiro_arquivo.xlsx'
#
# ws1 = wb.active
# ws1.title = 'Planilha 1'
#
# dados = [
#      ['Ano', 'Lucro', 'Custos'],
#     [2021, '30%', '40%'],
#     [2021, '30%', '40%'],
#     [2021, '30%', '40%']
# ]
# for linha in dados:
#     ws1.append(linha)
#
# ws1['H13']= 13
# wb.save(filename=nome_arquivo)

# AULA 57
# from openpyxl import load_workbook
#
#
# wb = load_workbook('nomes.xlsx')
#
# planilha = wb['Planilha1']
#
# for i in range(2,5):
#     print('%s tem %s anos.' % (planilha['A%s' % i].value, planilha['B%s' % i].value))

# AULA 59
# from openpyxl import Workbook

# print('Iniciando o robô...')
# print('Lendo dados do arquivo de texto...')
# with open('gastos.txt', 'r', encoding='utf-8' ) as file:
#
# # lê o arquivo
#  arquivo = file.read()
#
# lista = arquivo.splitlines()
#
# for i in range(0, len(lista)):
#     lista[i] = lista[i].split(',')
#

# # Criando arquivo
# print('criando arquivo excel...')
# wb = Workbook()
# ws = wb.active
#
# for row in lista:
#     ws.append(row)
#
# wb.save('gastos.xlsx')