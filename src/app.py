"""Web app that creates memes uses the Quote Engine and Meme Generator."""

import random
import os
import requests
#from flask import Flask, render_template, abort, request
from flask import Flask, render_template, abort, request, url_for
from quote_engine import Ingestor, QuoteModel
from meme_engine import MemeGenerator

#app = Flask(__name__)

#meme = MemeGenerator('./mysite/src/static/')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './mysite/src/static/'
meme = MemeGenerator(app.config['UPLOAD_FOLDER'])


def setup():
    """Load all resources."""
    quote_files = ['./mysite/src/_data/DogQuotes/DogQuotesTXT.txt',
                   './mysite/src/_data/DogQuotes/DogQuotesDOCX.docx',
                   './mysite/src/_data/DogQuotes/DogQuotesPDF.pdf',
                   './mysite/src/_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    img_path = "./mysite/src/_data/photos/dog/"
    imgs = [os.path.join(img_path, name) for name in os.listdir(img_path)]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    #return render_template('meme.html', path=path)
    return render_template('meme.html', path=url_for('static', filename=os.path.basename(path)))



@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user-defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    response = requests.get(image_url)
    temp_file = f'./mysite/src/static/tmp_{random.randint(0, 100000)}.jpg'

    with open(temp_file, 'wb') as file:
        file.write(response.content)

    path = meme.make_meme(temp_file, body, author)
    os.remove(temp_file)

    #return render_template('meme.html', path=path)
    return render_template('meme.html', path=url_for('static', filename=os.path.basename(path)))


if __name__ == "__main__":
    app.run()
