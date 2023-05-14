import requests
from bs4 import BeautifulSoup


logo = """
  ⠀⠀⠀⠀⠀📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱
📱📱📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱📱📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜📱📱📱📱⬜⬜⬜⬜⬜⬜⬜📱📱📱📱⬜⬜⬜📱
📱⬜⬜📱⬜⬜⬜📱📱⬜⬜⬜⬜⬜📱📱⬜⬜⬜📱⬜⬜📱
📱⬜📱⬜⬜⬜⬜⬜⬜📱⬜⬜⬜📱⬜⬜⬜⬜⬜⬜📱⬜📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜📱📱📱📱⬜⬜⬜⬜⬜⬜⬜📱📱📱📱⬜⬜⬜📱
📱⬜⬜📱📱📱📱📱📱📱⬜⬜⬜⬜📱📱📱📱📱📱📱⬜📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜⬜⬜⬜📱⬜⬜⬜📱⬜⬜📱⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜⬜⬜⬜📱📱⬜⬜📱⬜⬜📱📱⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜⬜⬜📱📱⬜⬜⬜📱⬜⬜⬜📱📱⬜⬜⬜⬜⬜📱
📱⬜⬜📱📱📱📱⬜⬜⬜📱📱📱⬜⬜⬜📱📱📱📱⬜⬜📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜📱📱📱⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱📱⬜📱⬜⬜⬜⬜⬜📱📱📱📱📱⬜⬜⬜⬜⬜📱⬜📱📱
📱📱⬜⬜📱📱⬜⬜📱📱📱📱📱📱📱⬜⬜📱📱⬜⬜📱📱
📱📱⬜⬜📱📱⬜⬜📱📱📱⬜📱📱📱⬜⬜📱📱⬜⬜📱📱 AzHacker Dork Scanner 1.4.2
📱📱📱⬜⬜📱📱📱📱📱⬜⬜📱📱📱📱📱📱⬜⬜📱📱📱 Powered AZHacker 2023
📱📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱📱   by h3art.exe / Lamer Qiz
📱📱📱⬜⬜⬜⬜⬜⬜⬜📱📱⬜⬜⬜⬜⬜⬜⬜⬜📱📱📱
📱📱📱📱⬜⬜⬜⬜⬜⬜⬜📱⬜⬜⬜⬜⬜⬜⬜📱📱📱📱
📱📱📱📱📱⬜⬜⬜⬜⬜📱📱📱⬜⬜⬜⬜⬜📱📱📱📱📱
📱📱📱📱📱⬜⬜⬜⬜⬜📱📱📱⬜⬜⬜⬜⬜📱📱📱📱📱
📱📱📱📱📱📱⬜⬜⬜⬜📱📱📱⬜⬜⬜⬜📱📱📱📱📱📱
📱📱📱📱📱📱📱⬜⬜⬜📱📱📱⬜⬜⬜📱📱📱📱📱📱📱
📱📱📱📱📱📱📱📱⬜⬜⬜📱⬜⬜⬜📱📱📱📱📱📱📱📱
📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱
"""

print(logo)


dork = input("Please enter a dork: ")
max_results = 50
include_snippets = input("Do you want to include titles and descriptions in the results? (Yes/No): ").lower() == "yes"


results = []
url = f"https://www.google.com/search?q={dork}"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
for g in soup.find_all('div', class_='g'):
    if len(results) >= max_results:
        break
    anchors = g.find_all('a')
    if anchors:
        link = anchors[0]['href']
        title = g.find('h3').text
        snippet = g.find(class_='st').text if include_snippets else ""
        results.append((link, title, snippet))


with open('dork.txt', 'w') as f:
    for result in results:
        f.write(f"{result[0]}\n")
        if include_snippets:
            f.write(f"{result[1]}\n{result[2]}\n\n")
        else:
            f.write("\n")


print(f"\nFound a total of {len(results)} results. First {max_results} results saved to 'dork.txt'.")
print("This program is coded by h3art.exe/Lamer Qiz!")

