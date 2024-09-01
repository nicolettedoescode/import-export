from flask import Flask, request, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    df = pd.read_csv(file)
    csv = df.to_csv(index=False)
    return send_file(io.StringIO(csv), mimetype='text/csv', as_attachment=True, download_name='data.csv')

if __name__ == '__main__':
    app.run(debug=True)
