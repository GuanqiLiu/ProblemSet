# 文件: fed/data.py
import pandas as pd

def load_data(file_path):
    """
    Load GDP data from a CSV file.
    :param file_path: Path to the CSV file
    :return: DataFrame containing the GDP data
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(data):
    """
    Clean the GDP data.
    :param data: Raw DataFrame
    :return: Cleaned DataFrame
    """
    # Remove rows with missing values
    data = data.dropna()
    
    # Rename columns for consistency (optional)
    data.columns = [col.strip().lower().replace(" ", "_") for col in data.columns]
    
    # Convert from wide format to long format (to have year and GDP in separate columns)
    year_columns = [col for col in data.columns if col.isdigit()]  # Find all columns representing years
    data = pd.melt(
        data,
        id_vars=['country_name', 'country_code', 'indicator_name', 'indicator_code'],
        value_vars=year_columns,
        var_name='year',
        value_name='gdp'
    )

    # Convert year column to integer type
    data['year'] = data['year'].astype(int)
    
    return data

