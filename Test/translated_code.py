import pandas as pd

class_data = pd.read_csv('default_of_credit_card_clients.csv')

adultos = class_data[class_data['AGE'] >= 18]

adultos.to_csv('output.csv', index=False)