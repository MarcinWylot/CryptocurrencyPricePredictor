from flask import Flask
from flask import request

import requests
import json
from statsmodels.tsa.api import ExponentialSmoothing
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route("/predict")
def predict():
    coin = request.args.get('coin')
    
    url = 'https://min-api.cryptocompare.com/data/histohour?tsym=EUR&limit=300&fsym={}'.format(coin)
    response = requests.get(url)

    json_array = json.loads(response.text)
    df = pd.DataFrame(json_array['Data'], columns = ['close','time'])
    df.set_index('time', inplace=True)
    
    y = df[295:300].copy()
    y.index = y.index +6*3600

    fit1 = ExponentialSmoothing(np.asarray(df['close']) ,seasonal_periods=7 ,trend='add', seasonal='mul',).fit()
    y['Holt_Winter'] = fit1.forecast(len(y))


    return y['Holt_Winter'].to_json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

