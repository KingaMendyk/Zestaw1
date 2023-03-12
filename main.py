import webbrowser
import requests

pageUrl = input("Podaj strone: ")
for i in range(3):
    date = input("Podaj date: ")

    url = "http://archive.org/wayback/available?url=" + pageUrl + "&timestamp=" + str(date)
    response = requests.get(url)
    page = response.json()["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page)