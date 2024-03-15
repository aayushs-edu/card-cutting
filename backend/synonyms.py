import os
import docx.opc.exceptions as err
from docx import Document
import polars as pl

# Get tagline : body dict of all cards in dataset
def data(numGroups : int = -1):
    DATA_PATH = os.path.join(os.getcwd(), 'data', '2013')

    cardTitles = []
    taglines = []
    bodies = []

    if numGroups == -1: all_cards = os.listdir(DATA_PATH)
    else: all_cards = os.listdir(DATA_PATH)[:numGroups]

    for card_group in all_cards:
        group_path = os.path.join(DATA_PATH, card_group)
        for card in os.listdir(group_path):
            card_path = os.path.join(group_path, card)
            try: doc = Document(card_path)
            except err.PackageNotFoundError: continue
            paras = doc.paragraphs
            nParas = len(paras)

            tagline = None
            tIndex = 0
            while not tagline:
                tagline = paras[tIndex].text
                tIndex += 1
            taglines.append(tagline)

            body = paras[-1]
            bIndex = -1
            while len(body.text) < 20:
                body = paras[bIndex]
                bIndex -= 1
            bodies.append(body)
            cardTitles.append(os.path.basename(os.path.normpath(card_path))[:-5])

    df = pl.DataFrame({
        "card" : cardTitles,
        "tagline" : taglines,
        "body" : bodies
    })

    return df.unique(subset=['tagline'])



