import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from csv import writer

all_data = []
meanings = []
words = []

#TO DO
#エクセルを上書きではなく、データを追加していく。
#urban dictionary からスクレイピングする
#ウェブ上で動かす


while True:

    spell = input("spell: ")

    url = "https://ejje.weblio.jp/content/" + spell
    source = requests.get(url)
    source.encoding = source.apparent_encoding
    data = BeautifulSoup(source.text, "html.parser")
    explanation_list = data.select("td.content-explanation")

    for idx, txt in tqdm(enumerate(explanation_list)):
        meanings.append(explanation_list[idx].text)
        words.append(spell)
        all_data = ({'words': words, 'meanings': meanings})

    print(all_data)
    df = pd.DataFrame(data=all_data)

    print(df)

    df.to_excel('dict1.xlsx')


#     workbook = xlsxwriter.Workbook('sample.xlsx')
#     worksheet = workbook.add_worksheet()

#     row = 0
#     for col, data in enumerate(all_data):
#         worksheet.write_column(row, col, data)
#     # for row in ws.iter_cols():
#     #     for cell in row:
#     #         cell = words[cell]
#     #         print(cell.value)
#     #         ws["a1"] = "test"
#     workbook.close()
