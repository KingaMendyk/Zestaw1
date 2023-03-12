import webbrowser
import requests

pageUrl = input("Podaj adres strony: ")
for i in range(3):
    date = input("Podaj datę w formacie rok miesiąc dzień: ")

    url = "http://archive.org/wayback/available?url=" + pageUrl + "&timestamp=" + str(date)
    response = requests.get(url)
    page = response.json()["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page)