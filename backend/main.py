import json
from flask import Flask, jsonify, request

import newspaper
from newspaper import Article

app = Flask(__name__)
app.json.sort_keys = False

# Downloading article to memory
article = Article("https://www.nytimes.com/2024/02/07/us/politics/united-states-support-ukraine.html")
article.download()
article.parse()
# article.nlp()

# Print out full text
print(article.text)

# To print out a summary of the text
# This works because newspaper3k has built in NLP tools
# print(article.summary)

# To print out the list of authors
print(article.authors)

# To print out the list of keywords
print(article.keywords)

paragraphs = article.text.split("\n")

articles = {'id': 0, 'title': article.title, 'author': article.authors, 'date': article.publish_date, 'image': article.top_image, 'content': paragraphs}

@app.route('/articles', methods=['GET'])
def get_articles():
 return jsonify(articles)


if __name__ == '__main__':
   app.run(port=5000, debug=True)
