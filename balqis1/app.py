# Flask application
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for items (books)
items = [
    {'name': 'Buku A', 'image': '2.png', 'code': 'A001'},
    {'name': 'Buku B', 'image': '3.png', 'code': 'B002'},
    {'name': 'Buku C', 'image': '4.png', 'code': 'C003'}
]

# Dummy user credentials
user_credentials = {
    'username': 'balqisSelvia',
    'password': 'balqis123'
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    if username == user_credentials['username'] and password == user_credentials['password']:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('fail'))

@app.route('/index')
def index():
    search_query = request.args.get('search')
    if search_query:
        filtered_items = [item for item in items if search_query.lower() in item['name'].lower()]
    else:
        filtered_items = items
    return render_template('index.html', items=filtered_items)

@app.route('/pinjam/<item_name>')
def pinjam(item_name):
    item = next((item for item in items if item['name'] == item_name), None)
    if item:
        return render_template('pinjam.html', item=item)
    else:
        return redirect(url_for('index'))

@app.route('/pinjam/submit', methods=['POST'])
def submit_pinjam():
    name = request.form['name']
    book_code = request.form['book_code']
    borrow_date = request.form['borrow_date']
    address = request.form['address']
    phone_number = request.form['phone_number']

    # Validasi panjang nomor HP
    if len(phone_number) < 10 or len(phone_number) > 12:
        return "Nomor HP harus terdiri dari 10 hingga 12 digit."

    # Simulasi penyimpanan data peminjaman
    print(f'Peminjaman: Nama: {name}, Kode Buku: {book_code}, Tanggal Pinjam: {borrow_date}, Alamat: {address}, Nomor HP: {phone_number}')
    return redirect(url_for('finish'))

@app.route('/finish')
def finish():
    return render_template('finish.html')

@app.route('/fail')
def fail():
    return render_template('fail.html')

if __name__ == '__main__':
    app.run(debug=True)
