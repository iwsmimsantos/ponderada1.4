import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1 - Ler dados do arquivo
    df = pd.read_csv('epa-sea-level.csv')

    # 2 - Criar gráfico de dispersão
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # 3 - Criar primeira linha de melhor ajuste (de 1880 até 2050)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, intercept + slope * years_extended, color='red', label='Fit Line (1880-2050)')

    # 4 - Criar segunda linha de melhor ajuste (apenas de 2000 até o mais recente)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Gerar valores preditivos para a linha de melhor ajuste recente (de 2000 até 2050)
    years_recent = pd.Series(range(2000, 2051))  # Corrigir para 2000 até 2050
    plt.plot(years_recent, intercept_recent + slope_recent * years_recent, color='green', label='Fit Line (2000-2050)')

    # 5 - Adicionar rótulos e título
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # Salvar gráfico e retornar dados para teste (NÃO MODIFICAR)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Não modifique as próximas duas linhas
if __name__ == "__main__":
    draw_plot()
