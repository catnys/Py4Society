import cv2
import numpy as np
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join('uploads/', filename))
            return redirect(url_for('analyze', filename=filename))
    return render_template_string(open("index.html").read(), title='Home')

@app.route('/analyze/<filename>')
def analyze(filename):
    # Color analysis logic will go here
    return f"Analyzing {filename}"


@app.route('/analyze/<filename>')
def analyze(filename):
    img_path = os.path.join('uploads/', filename)
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pixels = np.float32(img.reshape(-1, 3))

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, _ = cv2.kmeans(pixels, 10, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(cv2.kmeans(pixels, 10, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)[1])

    # Convert RGB to HEX
    hex_colors = ['#{:02x}{:02x}{:02x}'.format(int(c[0]), int(c[1]), int(c[2])) for c in centers]

    return ', '.join(hex_colors)


if __name__ == '__main__':
    app.run(debug=True)
