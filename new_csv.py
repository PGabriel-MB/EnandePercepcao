# script criado para gerar o outro csv necessário para se trabalhar melhor com pandas
filename = "MICRODADOS_ENADE_2017.txt"

f = open(filename)
colunas = f.readline().split(';')
novo = open(r'new_csv.csv', 'w')

novo.write(colunas[60] + ';' + colunas[61] + ';' + colunas[62] + ';' + colunas[63] + ';' + colunas[64] + ';' + colunas[66] + ';' + colunas[68] +'\n')
for campos in f:
    campos = campos.split(';')
    novo.write(campos[60] + ';' + campos[61] + ';' + campos[62] + ';' + campos[63] + ';' + campos[64] + ';' + campos[66] + ';' + campos[68] +'\n')

f.close()
novo.close()