from flask import Flask, render_template, request
from cosine import detectFakeWithCosine
from jaccard import detectFakeWithJaccard


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cosine', methods=['GET', 'POST'])
def cosine():
    if request.method == 'POST':
        # Get the news article text from the form
        bench = request.form['bench']
        news_text = request.form['news_text']
        threshold = request.form['threshold']

        # Call your fake news detection program with the news_text input
        result = detectFakeWithCosine(bench, news_text, threshold)

        # Render a template with the result
        return render_template('index.html', result=result)
    else:
        # Render the form template
        return render_template('index.html')

@app.route('/jaccard', methods=['GET', 'POST'])
def jaccard():
    if request.method == 'POST':
        # Get the news article text from the form
        bench = request.form['bench']
        news_text = request.form['news_text']
        thresh = request.form['threshold']
        threshold = float(thresh)

        # Call your fake news detection program with the news_text input
        result = detectFakeWithJaccard(bench, news_text, threshold)

        # Render a template with the result
        return render_template('index.html', result=result, threshold=threshold)
    else:
        # Render the form template
        return render_template('index.html')




@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)