from django.shortcuts import render

def home(request):
    import requests
    import json

    #Get Crypto News
    news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    news = json.loads(news_request.content)

    #Get Currency Price
    currency_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,XRP,XLM&tsyms=BTC,USD,EUR"
    )
    currency = json.loads(currency_request.content)

    #Get Multiple Currency and full data
    currency_fulldata_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XLM,EOS,LTC,ADA,XRP,XMR,ELF&tsyms=USD,EUR")
    currency_fulldata = json.loads(currency_fulldata_request.content)

    return render(request, 'home.html', {'news': news, 'currency': currency,'currency_fulldata': currency_fulldata})

def info(request):
    if request.method == "POST":
        import requests
        import json
        param = request.POST['param']
        param = param.upper()
        info_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + param +"&tsyms=USD,EUR")
        info = json.loads(info_request.content)
        return render(request, 'info.html', {'info':info})
    else:
        return render(request, 'info.html', {})
