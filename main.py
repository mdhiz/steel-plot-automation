import pandas as pd
import os

def read_input(filepath):
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print("Input file not found.")
        return pd.DataFrame()

def calculate_steel_weight(df):
    # Dummy calculation: cross-sectional area × length × density
    df['Weight (kg)'] = df['Diameter (mm)'] * df['Thickness (mm)'] * df['Length (m)'] * 0.00785
    return df

def export_report(df, output_path='output/report.csv'):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Report saved to {output_path}")

if __name__ == "__main__":
    input_path = 'sample_data/input_example.csv'
    df_input = read_input(input_path)
    
    if not df_input.empty:
        df_output = calculate_steel_weight(df_input)
        export_report(df_output)
