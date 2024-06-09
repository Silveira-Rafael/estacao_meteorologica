import csv
import locale
from datetime import datetime
import matplotlib.pyplot as plt

def upload_file():
    data = []
    with open('Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv', 'r', newline='', encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=',') #Cria um objeto CSV Reader para ler o arquivo CSV especificando que o delimitador é ','
        header = next(file_csv) #Lê a primeira linha do arquivo CSV (o cabeçalho) e a armazena em 'header'     
        for line in file_csv:            
            date = line[0] #Extrai a data da primeira coluna (índice 0) da linha atual e converte para um valor float
            precip = float(line[1]) #Extrai a precipitação (coluna 2) da linha atual e converte para um valor float
            max_temp = float(line[2]) #Extrai a temperatura máxima (coluna 3) da linha atual e converte para um valor float
            min_temp = float(line[3]) #Extrai a temperatura mínima (coluna 4) da linha atual e converte para um valor float
            moisture = float(line[6]) #Extrai a umidade (coluna 7) da linha atual e converte para um valor float
            wind_speed = float(line[7]) #Extrai a velocidade do vento (coluna 8) da linha atual e converte para um valor float
            data.append({'Data' : date, 'Precipitação': precip, 'Temperatura máxima': max_temp, 'Temperatura mínima': min_temp, 'Umidade': moisture, 'Velocidade do vento': wind_speed}) #Cria um dicionário com os valores extraídos e adiciona esse dicionário à lista 'data'
    return data

# Carrega os dados do arquivo
data = upload_file()

def search_values(): #Função para o usuário informar o período que quer ver, ou seja, deve indicar o mês e ano iniciais bem como o mês e ano finais que deseja visualizar os dados
    m_s = int(input("\nInforme o mês de início (1 a 12): "))
    while m_s < 1 or m_s > 12:
        print("\nMês inválido! Informe um valor de 1 a 12!") 
        m_s = int(input("\nInforme o mês de início: "))

    y_s = int(input("Informe o ano de início: "))
    while y_s < 1961 or y_s > 2016:
        print("\nAno inválido! O ano deve ser de 1961 a 2016!")
        y_s = int(input("Informe o ano de início: "))

    m_e = int(input("Informe o mês final (1 a 12): "))
    while m_e < 1 or m_e > 12:
        print("\nMês inválido. Informe um valor de 1 a 12!")
        m_e = int(input("Informe o mês final (): "))

    y_e = int(input("Informe o ano final: "))
    while y_e < 1961 or y_e > 2016:
        print("\nAno inválido! O ano deve ser de 1961 a 2016!")
        y_e = int(input("Informe o ano final: "))

    d_s = datetime(y_s, m_s, 1)
    d_e = datetime(y_s, m_e, 1)

    return d_s, d_e

def filter_all(d_s, d_e): #Função que filtra os dados de acordo com o intervalo de datas informado 
    interval = [] #Armazena o intervalo informado para a busca
    for register in data:
        filtred_range = datetime.strptime(register['Data'], '%d/%m/%Y') #Datetime para converter uma string no formato dia/mes/ano para um objeto datetime para a manipulação de datas
        if d_s <= filtred_range <= d_e:
            interval.append(register) 

    for register in interval:
        print(f"\n{register}")

def filter_precip(d_s, d_e): #Função referente a precipitação
    for register in data:
        filtered_range = datetime.strptime(register['Data'], '%d/%m/%Y')
        if d_s <= filtered_range <= d_e and register['Precipitação'] >= 0: #Verifica se a data do registro está dentro do intervalo especificado pela data inicial e pela data final e se a precipitação do registro é maior ou igual a 0
            preci = register['Precipitação']
            print(f"\nPrecipitação: {preci}")

def filter_temp(d_s, d_e): #Função referente a temperatura 
    for register in data:
        filtered_range = datetime.strptime(register['Data'], '%d/%m/%Y')
        if d_s <= filtered_range <= d_e and register['Temperatura máxima'] > 0 and register['Temperatura mínima'] > 0: #Verifica se a data do registro está dentro do intervalo especificado pela data inicial e pela data final e se as temperaturas máxima e mínima do registro são maiores que zero
            max_temp = register['Temperatura máxima'] #Obtém o valor da temperatura máxima do registro atual e o armazena em 'max_temp'
            min_temp = register['Temperatura mínima']
            print(f"\nTemperatura máxima: {max_temp} \nTemperatura mínima: {min_temp}")

def filter_mois_wind(d_s, d_e): #Função referente a umidade e velocidade do vento
    for register in data:
        filtered_range = datetime.strptime(register['Data'], '%d/%m/%Y')
        if d_s <= filtered_range <= d_e and register['Umidade'] > 0 and register['Velocidade do vento'] > 0: #Verifica se a data do registro está dentro do intervalo especificado pela data inicial e pela data final e se a umidade e a velocidade do vento do registro são maiores que zero
            mois = register['Umidade']
            wind = register['Velocidade do vento']
            print(f"\nUmidade: {mois} \nVelocidade do vento: {wind}") 

def less_rainy(d_s, d_e): #Função referente ao mês e ano com menor indice de preciptação
    interval = []
    min_precip = float('inf') #Atribuindo um valor positivo infinito para a variável para acompanharmos o menor indice de precipitação
    min_precip_m = None #Atribuindo None a variável que vai armazenar o mês e ano com o menor indice de precipitação

    for register in data:
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8') #Formatando data para o Português Brasileiro para informar o nome do mês em Português
        filtered_range = datetime.strptime(register['Data'], '%d/%m/%Y')
        if d_s <= filtered_range <= d_e and register['Precipitação'] >= 0:
            precip = register['Precipitação']
            interval.append(precip) 

            if precip < min_precip: # Verificação se a precipitação atual é menor do que a menor precipitação registrada até agora
                min_precip = precip
                min_precip_m = filtered_range.strftime('%B de %Y') # Atualizando a variável com o mês e ano

    if min_precip_m:
        print(f"\nMês menos chuvoso foi: {min_precip_m} com precipitação de {min_precip}mm")

def average_temp_min_m(data, m): #Função referente a média da temperatura mínima do mês
    min_temp_m = []
    for register in data: #Loop que percorre cada registro (dicionário) em 'data'
        filtered_range = datetime.strptime(register['Data'], '%d/%m/%Y')
        if filtered_range.month == m: #Verifica se o mês do registro corresponde ao mês informado
            min_temp_m.append(register['Temperatura mínima'])
    
    if min_temp_m:
        average = sum(min_temp_m) / len(min_temp_m) #Calcula a média da temperatura mínima do mês
        return average
    else:
        return None

def average_temp_min_general(data, month=None): #Função referente a média da temperatura mínima geral
    temp_min_general = []
    for register in data:
        temp_min_general.append(register['Temperatura mínima'])
    
    if temp_min_general: #Verifica se a lista 'temp_min_general' não está vazia
        average = sum(temp_min_general) / len(temp_min_general) #Calcula a média das temperaturas mínimas presentes na lista 'temp_min_general'
        return average
    else:
        return None

def average_temp_min_m_usu(data, m_usu): #Função referente a média da temperatura mínima do mês do usuário
    temp_min_m_ago = []
    
    for register in data:
        filtered_range = datetime.strptime(register['Data'], '%d/%m/%Y') #Converte a data do registro em um objeto datetime
        if 2006 <= filtered_range.year <= 2016 and filtered_range.month == m_usu: #Verifica se o ano do registro está entre 2006 e 2016 e se o mês corresponde ao mês informado pelo usuário
            temp_min_m_ago.append(register['Temperatura mínima'])
    
    if temp_min_m_ago:
        average = sum(temp_min_m_ago) / len(temp_min_m_ago) #Calcula a média das temperaturas mínimas presentes na lista 'temp_min_m_ago'
        return average
    else:
        return None

def graph_temperatures(data, month): #Função do gráfico
    years = range(2006, 2017)  #Cria uma sequência de anos de 2006 a 2016 e armazena em 'years'
    monthly_averages = []

    for year in years:
        temperatures = []
        for register in data:
            register_date = datetime.strptime(register['Data'], '%d/%m/%Y')
            if register_date.year == year and register_date.month == month:
                temperatures.append(register['Temperatura mínima']) 
        
        if temperatures:
            monthly_averages.append(sum(temperatures) / len(temperatures)) #Calcula a média das temperaturas do mês atual e a adiciona à lista 'monthly_averages'
        else:
            monthly_averages.append(None)

    plt.figure(figsize=(10, 6)) #Tamanho da figura do gráfico
    plt.plot(years, monthly_averages, marker='o', linestyle='-', color='b', label=f'Média do mês {month}')
    plt.xlabel('Ano') #Rótulo do eixo x
    plt.ylabel('Média da temperatura mínima (°C)') #Rótulo do eixo y
    plt.title(f'Médias da temperatura mínima para o mês {month} nos últimos 11 Anos') #Título do gráfico
    plt.xticks(years) #Valores do eixo x como os anos
    plt.legend()
    plt.grid(True) #Habilita as linhas de grade no gráfico
    plt.show()
    
def preview_options(): #Função para o usuário informar se quer visualizar todos os dados , ou dados de precipitação, ou dados de temperatura ou dados de umidade e vento 

    print("\n1 - Todos os dados. \n2 - Dados de precipitação. \n3 - Dados de temperatura \n4 - Dados de umidade e vento. \n5 - Mês menos chuvoso. \n6 - Média e gráfico em barras da temperatura mínima de um determinado mês. \n7 - Sair.")

while True:
    
    preview_options()
    choice = input("\nInforme a opção desejada: ")
    
    try:
        choice = int(choice)
        if choice == 1:
            d_s, d_e = search_values()
            filter_all(d_s, d_e)
        
        elif choice == 2:
            d_s, d_e = search_values()
            filter_precip(d_s, d_e)            

        elif choice == 3:
            d_s, d_e = search_values()
            filter_temp(d_s, d_e)
        
        elif choice == 4:
            d_s, d_e = search_values()
            filter_mois_wind(d_s, d_e)
        
        elif choice == 5:
            d_s, d_e = search_values()
            less_rainy(d_s, d_e) 
        
        elif choice == 6:            
            m_usu = int(input("\nInforme o mês (1 a 12): "))
            while m_usu < 1 or m_usu > 12:
                print("\nMês inválido. Informe um valor de 1 a 12!")
                m_usu = int(input("\nInforme o mês: "))
           
            average_min_temp_mes = average_temp_min_m(data, m_usu) #Chamando a função average_temp_min_m para calcular a média da temperatura mínima para o mês especificado pelo usuário
            average_temp_min_g = average_temp_min_general(data) #Chamando a função average_temp_min_general para calcular a média geral da temperatura mínima para todo o período
            average_temp_min_m_u = average_temp_min_m_usu(data, m_usu) #Chamando a função average_temp_min_m_usu para calcular a média da temperatura mínima para o mês especificado pelo usuário

            if average_min_temp_mes is not None:
                print(f'\nA média da temperatura mínima para o mês {m_usu} é: {average_min_temp_mes:.2f}°C')
            else:
                print(f'Não há dados disponíveis para o mês {m_usu} nos últimos 11 anos.')

            if average_temp_min_g is not None:
                print(f'A média geral da temperatura mínima para todo o período é: {average_temp_min_g:.2f}°C')
            else:
                print('Não há dados disponíveis para calcular a média geral.')

            if average_temp_min_m_u is not None:
                print(f'A média da temperatura mínima para o mês {m_usu} nos últimos 11 anos é: {average_temp_min_m_u:.2f}°C')
            else:
                print('Não há dados disponíveis para o mês de agosto nos últimos 11 anos.')

            graph_temperatures(data, m_usu) #O gráfico pode demorar alguns segundos para ser exibido
      
        elif choice == 7:
            break
        else:
            print("\nOpção inválida!")
    except ValueError:
        print("\nOpção inválida!")
