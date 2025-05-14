import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(amount: str, quote: str, base: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты <b>{base}</b>')

        try:
            quote_ticker = keys[quote.title()]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту <b>{quote}</b>')

        try:
            base_ticker = keys[base.title()]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту <b>{base}</b>')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество <b>{amount}</b>')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base.title()]]

        return total_base
