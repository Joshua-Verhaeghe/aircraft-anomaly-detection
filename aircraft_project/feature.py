from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def split_columns(df):

    df[['day', 'cycle', 'window']] = df['day_cycle_window'].str.split('_', expand=True)
    df['day'] = df['day'].astype(int)
    df['cycle'] = df['cycle'].astype(int)
    df['window'] = df['window'].astype(int)

    return df

def create_time_index(df):

    df = df.sort_values(by=['day', 'cycle', 'window']).reset_index(drop=True)
    df['time_index'] = range(1, len(df)+1)
    
    return df

def normalisation(df, params):

    scaler = MinMaxScaler()
    df_normalise = df.copy()
    #df_normalise = pd.DataFrame(scaler.fit_transform(df_normalise[params]), columns=params ) # perdait en tete colonnes
    
    df_normalise[params] = scaler.fit_transform(df_normalise[params])

    return df_normalise

def standard_deviation(df):

    df_ecart_type = pd.DataFrame(columns=['day_cycle_window', 'p1_std', 'p2_std', 'p3_std', 'p4_std', 'p5_std', 'p6_std', 'p7_std', 'p8_std', 'p9_std', 'p10_std', 'p11_std'])
    for w in df['day_cycle_window'].unique() :

        ecart_type = df[df['day_cycle_window'] == w][['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11']].std()
        df_ecart_type = pd.concat([df_ecart_type, pd.DataFrame([[w] + ecart_type.tolist()], columns=df_ecart_type.columns)], ignore_index=True)

    return df_ecart_type

