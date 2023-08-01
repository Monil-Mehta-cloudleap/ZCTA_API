from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

@app.route('/<zcta>', methods=['GET'])
def get_data(zcta):
    data = read_csv_file('ZCTA_Data.csv')

    if zcta == 'data':
        return jsonify(data), 200
    
    results = [row for row in data if row['ZCTA'] == zcta]

    if not results:
        return jsonify({'error': f'ZCTA {zcta} not found.'}), 404

    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True)
