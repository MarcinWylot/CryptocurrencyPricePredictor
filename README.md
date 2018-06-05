# CryptocurrencyPricePredictor

The api predicst actually price , which is easier for wisualization, predicting movement (-1 down +1 up 0 still) can bu acieved simply by substractign the predictions from the last price (of an avg of last 1-2-3-n prices) and extracgin sign.

docker build -t <your-rest-api-docker-image> .
docker run -t <your-rest-api-docker-image> -d
curl http://<DOCKER-IP>:5000/predict?coin=BTC
