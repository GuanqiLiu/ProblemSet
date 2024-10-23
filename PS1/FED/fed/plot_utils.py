# 文件: fed/plot_utils.py
import matplotlib.pyplot as plt


def plot_gdp(data, country, country_column='country_name', frequency='yearly'):
    """
    Plot GDP data for a specific country.
    :param data: DataFrame containing the GDP data
    :param country: Country name to plot
    :param country_column: Column name for countries in the DataFrame
    :param frequency: 'yearly' or 'monthly'
    """
    country_data = data[data[country_column] == country]
    
    if frequency == 'yearly':
        x = country_data['year']
        y = country_data['gdp']
    elif frequency == 'monthly':
        x = country_data['date']  # Assuming date column is formatted properly
        y = country_data['gdp']
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o')
    plt.title(f'{country} GDP ({frequency})')
    plt.xlabel('Year' if frequency == 'yearly' else 'Date')
    plt.ylabel('GDP (in billion USD)')
    plt.grid(True)
    plt.show()


