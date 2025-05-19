import pandas as pd

def evaluar_riesgo(pago, bill):
    default_data = pd.read_csv('default_of_credit_card_clients.csv')
    default_data['RATIO'] = default_data.apply(lambda row: row[pago] / row[bill] if row[bill] > 0 else None, axis=1)
    default_data['RIESGO'] = default_data['RATIO'].apply(lambda x: 'ALTO' if x < 0.1 else ('MEDIO' if x < 0.3 else 'BAJO'))
    default_data.to_csv('output.csv', index=False)

evaluar_riesgo('PAY_AMT1', 'BILL_AMT1')