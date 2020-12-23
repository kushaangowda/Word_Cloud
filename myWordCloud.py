import wikipedia
from wordcloud import WordCloud, STOPWORDS
import os
from PIL import Image
import numpy as np

current_directory = os.path.dirname(__file__)

def get_wiki(query):
	title = wikipedia.search(query)[0]
	page = wikipedia.page(title)
	return page.content

def create_word_cloud(text):
	mask = np.array(Image.open(os.path.join(current_directory,"cloud.png")))
	stopwords = set(STOPWORDS)
	wc = WordCloud(background_color='white',
					mask=mask,
					max_words=150,
					stopwords=stopwords)
	wc.generate(text)
	wc.to_file(os.path.join(current_directory,'wc.png'))




create_word_cloud(get_wiki('word cloud'))