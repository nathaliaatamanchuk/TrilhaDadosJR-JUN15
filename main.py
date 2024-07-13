import os
import pandas as pd

data = 'course_data.txt'
archive = 'selling_courses_data.csv'
read_data = ''

if not os.path.isfile(archive):
    with open (data, 'r', encoding='utf-8-sig') as open_file, \
         open(archive, 'w', encoding='utf-8-sig') as file:
        for line in open_file:
            read_data = line.replace(',', ';')
            file.write(read_data)
else:
    print('The file already exists!')

df = pd.read_csv(archive, sep=';')
df['Receita Total Gerada'] = (df['Quantidade de Vendas'] * df['Preço Unitário']).round(2)
receita_total_de_vendas = df['Receita Total Gerada'].sum().round(2)

if 'Total:' in df['Data'].values:
    df.loc[df['Data'] == 'Total:', 'Receita Total Gerada'] = receita_total_de_vendas
else:
    nova_linha = pd.DataFrame({
        'Data': ['Total:'],
        'Receita Total Gerada': [receita_total_de_vendas]
    })
    df = pd.concat([df, nova_linha], ignore_index=True)

try:
    df.to_csv(archive, sep=';', index=False, encoding='utf-8-sig')
    print("Dados salvos com sucesso no arquivo:", archive)
except Exception as e:
    print("Falha ao salvar os dados:", e)