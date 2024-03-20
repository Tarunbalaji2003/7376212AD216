from flask import Flask, jsonify
import requests

app = Flask(__name__)

def get_prime():
    response = requests.get('http://20.244.56.144/numbers/primes')  
    return response.json()

def get_even():
    response = requests.get('http://20.244.56.144/numbers/even')
    return response.json()

def get_fibonacci():
    response = requests.get('http://20.244.56.144/numbers/fibo')
    return response.json()

def get_random():
    response = requests.get('http://20.244.56.144/numbers/rand')
    return response.json()

@app.route('/numbers/<string:numberid>', methods=['GET'])
def get_number(numberid):
    if numberid == 'prime':
        return jsonify(get_prime())
    elif numberid == 'even':
        return jsonify(get_even())
    elif numberid == 'fibo':
        return jsonify(get_fibonacci())
    elif numberid == 'rand':
        return jsonify(get_random())
    else:
        return jsonify({'error': 'Invalid numberid'}), 400
    


if __name__ == '__main__':
    app.run(debug=True)
