from sklearn.ensemble import IsolationForest
import pandas as pd


def detect_abnormal_windows(df_ecart_type, n_contamination):

    isoforest = IsolationForest(contamination=n_contamination, random_state=42)
    
    df_ecart_type['anomaly'] = isoforest.fit_predict(
        df_ecart_type[['p1_std', 'p2_std', 'p3_std', 'p4_std', 'p5_std', 
                       'p6_std', 'p7_std', 'p8_std', 'p9_std', 'p10_std', 'p11_std']])
    
    return df_ecart_type
    
def get_abnormal_windows(df_ecart_type):

    abnormal_windows = df_ecart_type[df_ecart_type['anomaly'] == -1]['day_cycle_window'].tolist()
    
    return abnormal_windows