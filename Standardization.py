crypto_ticker = ['EUR/USD','GBP/USD','ETH/USD','BTC/USD']

#Metrics Standarization 
def metric_normalizer(data):
        '''This function standardize the metrics - neeeds to be edited'''
        multiplier_dict = {
            "EUR/USD": 10000,
            "USD/JPY": 0.1,
            "AUD/USD": 10000,
            "GBP/USD": 10000,
            "USD/CHF": 10000,
            "XAU/USD": 10,
            "ETH/USD": 1,
            "BTC/USD": 10
        }

        # Iterate through rows of the DataFrame
        for index, row in data.iterrows():
            ticker = row['Ticker']
            multiplier_value = multiplier_dict.get(ticker, 1)  # Default to 1 if ticker not found

            if ticker in ['EUR/USD', 'GBP/USD']:
                data.at[index, 'Spread'] *= multiplier_value
                data.at[index, '2D Low in Pips'] *= multiplier_value
                data.at[index, '2D High in Pips'] *= multiplier_value
                data.at[index, '2D Hard Stop Loss'] *= multiplier_value
                data.at[index, '2D Trend Change Stop Loss'] *= multiplier_value
#                 data.at[index, '2D Hybrid Stop Loss'] *= multiplier_value
            elif ticker == 'BTC/USD':
                data.at[index, 'Spread'] /= multiplier_value
                data.at[index, '2D Low in Pips'] /= multiplier_value
                data.at[index, '2D High in Pips'] /= multiplier_value
                data.at[index, '2D Hard Stop Loss'] /= multiplier_value
                data.at[index, '2D Trend Change Stop Loss'] /= multiplier_value
#                 data.at[index, '2D Hybrid Stop Loss'] *= multiplier_value
            elif ticker == 'XAU/USD':
                data.at[index, 'Spread'] *= multiplier_value
                data.at[index, '2D Low in Pips'] *= multiplier_value
                data.at[index, '2D High in Pips'] *= multiplier_value
                data.at[index, '2D Hard Stop Loss'] *= multiplier_value
                data.at[index, '2D Trend Change Stop Loss'] *= multiplier_value
#                 data.at[index, '2D Hybrid Stop Loss'] *= multiplier_value

        return data