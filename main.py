import uuid, re, math
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, url_for
from mysql.connector import connect

app = Flask(__name__)

uuid = uuid.uuid4().hex

app.config['SECRET_KEY'] = uuid

var = None
email = None
total = 0


@app.route('/')
def home():
    if var == 'PROFILE':
        return render_template('home.html', var='PROFILE', button_var='PRODUCT')
    else:
        return render_template('home.html', var='LOGIN', button_var='SIGN UP')


@app.route('/product/')
def product():
    if var == 'PROFILE':
        return render_template('product.html', var="PROFILE", button_var='PRODUCT')
    else:
        return render_template('product.html', var='LOGIN', button_var='SIGN_UP')


@app.route('/product/<itemname>')
def products(itemname):
    if itemname == 'item1':
        if var == 'PROFILE':
            return render_template('products/item1.html', var='PROFILE')
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item2':
        if var == "PROFILE":
            return render_template('products/item2.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item3':
        if var == "PROFILE":
            return render_template('products/item3.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item4':
        if var == "PROFILE":
            return render_template('products/item4.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item5':
        if var == "PROFILE":
            return render_template('products/item5.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item6':
        if var == "PROFILE":
            return render_template('products/item6.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item7':
        if var == "PROFILE":
            return render_template('products/item7.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item8':
        if var == "PROFILE":
            return render_template('products/item8.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item9':
        if var == "PROFILE":
            return render_template('products/item9.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item10':
        if var == "PROFILE":
            return render_template('products/item10.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item11':
        if var == "PROFILE":
            return render_template('products/item11.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item12':
        if var == "PROFILE":
            return render_template('products/item12.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item13':
        if var == "PROFILE":
            return render_template('products/item13.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item14':
        if var == "PROFILE":
            return render_template('products/item14.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item15':
        if var == "PROFILE":
            return render_template('products/item15.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item16':
        if var == "PROFILE":
            return render_template('products/item16.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item17':
        if var == "PROFILE":
            return render_template('products/item17.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item18':
        if var == "PROFILE":
            return render_template('products/item18.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item19':
        if var == "PROFILE":
            return render_template('products/item19.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item20':
        if var == "PROFILE":
            return render_template('products/item20.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item21':
        if var == "PROFILE":
            return render_template('products/item21.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item22':
        if var == "PROFILE":
            return render_template('products/item22.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item23':
        if var == "PROFILE":
            return render_template('products/item23.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')
    if itemname == 'item24':
        if var == "PROFILE":
            return render_template('products/item24.html', var="PROFILE")
        else:
            return render_template('error1.html', error_message='Please Login or Create an Account')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    global var

    if request.method == 'GET':
        return render_template('signup.html')

    if request.method == 'POST':
        email = request.form['email-address']
        passwd = request.form['passwd']
        conn = connect(host='localhost', password='', user='root', database='main')
        conn2 = connect(host='localhost', password='', user='root', database='carts')
        cur = conn2.cursor()
        cursor = conn.cursor()
        cursor.execute('SELECT Email_Address FROM profile')
        ers = cursor.fetchall()
        if any(email in rs for rs in ers):
            return render_template('error3.html', error_message='Account Already Registered Please Login')
        else:
            cursor.execute('INSERT INTO profile(Email_Address, Password) VALUES(%s, %s);', (email, passwd))
            conn.commit()
            cur.execute('show tables;')
            rs = cur.fetchall()
            if any(email in result for result in rs):
                return render_template('error3.html', error_message='Account Already Registered Please Login')
            else:
                cur.execute('create table `%s`(Product varchar(255), Price float(10,2));', (email,))
                conn2.commit()
                return render_template('home.html', var='LOGIN', button_var='SIGN UP')


@app.route('/login', methods=['POST', 'GET'])
def login():
    global var, email

    if request.method == 'GET':
        return render_template('login.html', button_var='SIGN UP')

    if request.method == 'POST':
        email = request.form['email-address']
        passwd = request.form['passwd']
        conn = connect(host='localhost', user='root', password='', database='main')
        cur = conn.cursor()

        cur.execute('SELECT Email_Address FROM profile WHERE Email_Address = %s;', (email,))
        rv = cur.fetchone()
        cur.execute('SELECT Password FROM profile WHERE Email_Address = %s;', (email,))
        rvp = cur.fetchone()
        if rv[0] == email and rvp[0] == passwd:
            var = 'PROFILE'
            return redirect(url_for('home'))
        else:
            return render_template('login.html'), email


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    global email, var

    if request.method == 'GET':
        return render_template('profile.html', account_var=email)
    if request.method == 'POST':
        currpass = request.form['current']
        newpass = request.form['new']
        conn = connect(host='localhost', user='root', password='', database='main')
        cur = conn.cursor()
        cur.execute('SELECT Password FROM profile WHERE Email_Address = %s', (email,))
        pvr = cur.fetchone()
        if currpass == pvr[0]:
            sql = "UPDATE profile SET Password = %s WHERE Email_Address = %s;"
            data = (newpass, email,)
            cur.execute(sql, data)
            conn.commit()
            return redirect(url_for('home'))
        if 'logout' in request.form:
            var = 'LOGIN'
            conn2 = connect(host='localhost', user='root', password='', database='carts')
            cur2 = conn2.cursor()
            cur2.execute('DELETE FROM `%s`', (email,))
            conn2.commit()
            return redirect(url_for('home'))


@app.route('/cart', methods=['POST'])
def cart():
    global email, var, total, proname

    file1 = open('templates/products/item1.html')
    file2 = open('templates/products/item2.html')
    file3 = open('templates/products/item3.html')
    file4 = open('templates/products/item4.html')
    file5 = open('templates/products/item5.html')
    file6 = open('templates/products/item6.html')
    file7 = open('templates/products/item7.html')
    file8 = open('templates/products/item8.html')
    file9 = open('templates/products/item9.html')
    file10 = open('templates/products/item10.html')
    file11 = open('templates/products/item11.html')
    file12 = open('templates/products/item12.html')
    file13 = open('templates/products/item13.html')
    file14 = open('templates/products/item14.html')
    file15 = open('templates/products/item15.html')
    file16 = open('templates/products/item16.html')
    file17 = open('templates/products/item17.html')
    file18 = open('templates/products/item18.html')
    file19 = open('templates/products/item19.html')
    file20 = open('templates/products/item20.html')
    file21 = open('templates/products/item21.html')
    file22 = open('templates/products/item22.html')
    file23 = open('templates/products/item23.html')
    file24 = open('templates/products/item24.html')

    content1 = file1.read()
    content2 = file2.read()
    content3 = file3.read()
    content4 = file4.read()
    content5 = file5.read()
    content6 = file6.read()
    content7 = file7.read()
    content8 = file8.read()
    content9 = file9.read()
    content10 = file10.read()
    content11 = file11.read()
    content12 = file12.read()
    content13 = file13.read()
    content14 = file14.read()
    content15 = file15.read()
    content16 = file16.read()
    content17 = file17.read()
    content18 = file18.read()
    content19 = file19.read()
    content20 = file20.read()
    content21 = file21.read()
    content22 = file22.read()
    content23 = file23.read()
    content24 = file24.read()

    soup1 = BeautifulSoup(content1, 'lxml')
    soup2 = BeautifulSoup(content2, 'lxml')
    soup3 = BeautifulSoup(content3, 'lxml')
    soup4 = BeautifulSoup(content4, 'lxml')
    soup5 = BeautifulSoup(content5, 'lxml')
    soup6 = BeautifulSoup(content6, 'lxml')
    soup7 = BeautifulSoup(content7, 'lxml')
    soup8 = BeautifulSoup(content8, 'lxml')
    soup9 = BeautifulSoup(content9, 'lxml')
    soup10 = BeautifulSoup(content10, 'lxml')
    soup11 = BeautifulSoup(content11, 'lxml')
    soup12 = BeautifulSoup(content12, 'lxml')
    soup13 = BeautifulSoup(content13, 'lxml')
    soup14 = BeautifulSoup(content14, 'lxml')
    soup15 = BeautifulSoup(content15, 'lxml')
    soup16 = BeautifulSoup(content16, 'lxml')
    soup17 = BeautifulSoup(content17, 'lxml')
    soup18 = BeautifulSoup(content18, 'lxml')
    soup19 = BeautifulSoup(content19, 'lxml')
    soup20 = BeautifulSoup(content20, 'lxml')
    soup21 = BeautifulSoup(content21, 'lxml')
    soup22 = BeautifulSoup(content22, 'lxml')
    soup23 = BeautifulSoup(content23, 'lxml')
    soup24 = BeautifulSoup(content24, 'lxml')

    productname1 = soup1.find('div', {'class': "header1"}).text
    productname2 = soup2.find('div', {'class': 'header1'}).text
    productname3 = soup3.find('div', {'class': 'header1'}).text
    productname4 = soup4.find('div', {'class': "header1"}).text
    productname5 = soup5.find('div', {'class': 'header1'}).text
    productname6 = soup6.find('div', {'class': 'header1'}).text
    productname7 = soup7.find('div', {'class': "header1"}).text
    productname8 = soup8.find('div', {'class': 'header1'}).text
    productname9 = soup9.find('div', {'class': 'header1'}).text
    productname10 = soup10.find('div', {'class': "header1"}).text
    productname11 = soup11.find('div', {'class': 'header1'}).text
    productname12 = soup12.find('div', {'class': 'header1'}).text
    productname13 = soup13.find('div', {'class': "header1"}).text
    productname14 = soup14.find('div', {'class': 'header1'}).text
    productname15 = soup15.find('div', {'class': 'header1'}).text
    productname16 = soup16.find('div', {'class': "header1"}).text
    productname17 = soup17.find('div', {'class': 'header1'}).text
    productname18 = soup18.find('div', {'class': 'header1'}).text
    productname19 = soup19.find('div', {'class': "header1"}).text
    productname20 = soup20.find('div', {'class': 'header1'}).text
    productname21 = soup21.find('div', {'class': 'header1'}).text
    productname22 = soup22.find('div', {'class': "header1"}).text
    productname23 = soup23.find('div', {'class': 'header1'}).text
    productname24 = soup24.find('div', {'class': 'header1'}).text

    price1 = soup1.find('div', class_='header2').text
    price2 = soup2.find('div', class_='header2').text
    price3 = soup3.find('div', class_='header2').text
    price4 = soup4.find('div', class_='header2').text
    price5 = soup5.find('div', class_='header2').text
    price6 = soup6.find('div', class_='header2').text
    price7 = soup7.find('div', class_='header2').text
    price8 = soup8.find('div', class_='header2').text
    price9 = soup9.find('div', class_='header2').text
    price10 = soup10.find('div', class_='header2').text
    price11 = soup11.find('div', class_='header2').text
    price12 = soup12.find('div', class_='header2').text
    price13 = soup13.find('div', class_='header2').text
    price14 = soup14.find('div', class_='header2').text
    price15 = soup15.find('div', class_='header2').text
    price16 = soup16.find('div', class_='header2').text
    price17 = soup17.find('div', class_='header2').text
    price18 = soup18.find('div', class_='header2').text
    price19 = soup19.find('div', class_='header2').text
    price20 = soup20.find('div', class_='header2').text
    price21 = soup21.find('div', class_='header2').text
    price22 = soup22.find('div', class_='header2').text
    price23 = soup23.find('div', class_='header2').text
    price24 = soup24.find('div', class_='header2').text

    price_amt1 = float(re.search('[0.00-9.99]+', price1).group(0))
    price_amt2 = float(re.search('[0.00-9.99]+', price2).group(0))
    price_amt3 = float(re.search('[0.00-9.99]+', price3).group(0))
    price_amt4 = float(re.search('[0.00-9.99]+', price4).group(0))
    price_amt5 = float(re.search('[0.00-9.99]+', price5).group(0))
    price_amt6 = float(re.search('[0.00-9.99]+', price6).group(0))
    price_amt7 = float(re.search('[0.00-9.99]+', price7).group(0))
    price_amt8 = float(re.search('[0.00-9.99]+', price8).group(0))
    price_amt9 = float(re.search('[0.00-9.99]+', price9).group(0))
    price_amt10 = float(re.search('[0.00-9.99]+', price10).group(0))
    price_amt11 = float(re.search('[0.00-9.99]+', price11).group(0))
    price_amt12 = float(re.search('[0.00-9.99]+', price12).group(0))
    price_amt13 = float(re.search('[0.00-9.99]+', price13).group(0))
    price_amt14 = float(re.search('[0.00-9.99]+', price14).group(0))
    price_amt15 = float(re.search('[0.00-9.99]+', price15).group(0))
    price_amt16 = float(re.search('[0.00-9.99]+', price16).group(0))
    price_amt17 = float(re.search('[0.00-9.99]+', price17).group(0))
    price_amt18 = float(re.search('[0.00-9.99]+', price18).group(0))
    price_amt19 = float(re.search('[0.00-9.99]+', price19).group(0))
    price_amt20 = float(re.search('[0.00-9.99]+', price20).group(0))
    price_amt21 = float(re.search('[0.00-9.99]+', price21).group(0))
    price_amt22 = float(re.search('[0.00-9.99]+', price22).group(0))
    price_amt23 = float(re.search('[0.00-9.99]+', price23).group(0))
    price_amt24 = float(re.search('[0.00-9.99]+', price24).group(0))

    conn2 = connect(host='localhost', user='root', password='', database='billing_info')
    cur2 = conn2.cursor()

    if request.method == 'POST':
        conn = connect(host='localhost', user='root', password='', database='carts')
        cur = conn.cursor()
        if 'addcart1' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname1, price_amt1))
            conn.commit()
            return redirect(url_for('products', itemname='item1'))
        elif 'addcart2' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname2, price_amt2))
            conn.commit()
            return redirect(url_for('products', itemname='item2'))
        elif 'addcart3' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname3, price_amt3))
            conn.commit()
            return redirect(url_for('products', itemname='item3'))
        elif 'addcart4' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname4, price_amt4))
            conn.commit()
            return redirect(url_for('products', itemname='item4'))
        elif 'addcart5' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname5, price_amt5))
            conn.commit()
            return redirect(url_for('products', itemname='item5'))
        elif 'addcart6' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname6, price_amt6))
            conn.commit()
            return redirect(url_for('products', itemname='item6'))
        elif 'addcart7' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname7, price_amt7))
            conn.commit()
            return redirect(url_for('products', itemname='item7'))
        elif 'addcart8' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname8, price_amt8))
            conn.commit()
            return redirect(url_for('products', itemname='item8'))
        elif 'addcart9' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname9, price_amt9))
            conn.commit()
            return redirect(url_for('products', itemname='item9'))
        elif 'addcart10' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname10, price_amt10))
            conn.commit()
            return redirect(url_for('products', itemname='item10'))
        elif 'addcart11' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname11, price_amt11))
            conn.commit()
            return redirect(url_for('products', itemname='item11'))
        elif 'addcart12' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname12, price_amt12))
            conn.commit()
            return redirect(url_for('products', itemname='item12'))
        elif 'addcart13' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname13, price_amt13))
            conn.commit()
            return redirect(url_for('products', itemname='item13'))
        elif 'addcart14' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname14, price_amt14))
            conn.commit()
            return redirect(url_for('products', itemname='item14'))
        elif 'addcart15' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname15, price_amt15))
            conn.commit()
            return redirect(url_for('products', itemname='item15'))
        elif 'addcart16' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname16, price_amt16))
            conn.commit()
            return redirect(url_for('products', itemname='item16'))
        elif 'addcart17' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname17, price_amt17))
            conn.commit()
            return redirect(url_for('products', itemname='item17'))
        elif 'addcart18' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname18, price_amt18))
            conn.commit()
            return redirect(url_for('products', itemname='item18'))
        elif 'addcart19' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname19, price_amt19))
            conn.commit()
            return redirect(url_for('products', itemname='item19'))
        elif 'addcart20' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname20, price_amt20))
            conn.commit()
            return redirect(url_for('products', itemname='item20'))
        elif 'addcart21' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname21, price_amt21))
            conn.commit()
            return redirect(url_for('products', itemname='item21'))
        elif 'addcart22' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname22, price_amt22))
            conn.commit()
            return redirect(url_for('products', itemname='item22'))
        elif 'addcart23' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname23, price_amt23))
            conn.commit()
            return redirect(url_for('products', itemname='item23'))
        elif 'addcart24' in request.form:
            cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, productname24, price_amt24))
            conn.commit()
            return redirect(url_for('products', itemname='item24'))

        elif 'Buy1' in request.form:
            proname = productname1
            total = int(math.ceil(2399.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy2' in request.form:
            proname = productname2
            total = int(math.ceil(1399.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy3' in request.form:
            proname = productname3
            total = int(math.ceil(999.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy4' in request.form:
            proname = productname4
            total = int(math.ceil(459.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy5' in request.form:
            proname = productname5
            total = int(math.ceil(3699.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy6' in request.form:
            proname = productname6
            total = int(math.ceil(1299.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy7' in request.form:
            proname = productname7
            total = int(math.ceil(1899.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy8' in request.form:
            proname = productname8
            total = int(math.ceil(2999.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy9' in request.form:
            proname = productname9
            total = int(math.ceil(1349.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy10' in request.form:
            proname = productname10
            total = int(math.ceil(1239.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy11' in request.form:
            proname = productname11
            total = int(math.ceil(649.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy12' in request.form:
            proname = productname12
            total = int(math.ceil(1799.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy13' in request.form:
            proname = productname13
            total = int(math.ceil(199.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy14' in request.form:
            proname = productname14
            total = int(math.ceil(899.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy15' in request.form:
            proname = productname15
            total = int(math.ceil(249.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy16' in request.form:
            proname = productname16
            total = int(math.ceil(619.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy17' in request.form:
            proname = productname17
            total = int(math.ceil(34.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy18' in request.form:
            proname = productname18
            total = int(math.ceil(39.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy19' in request.form:
            proname = productname19
            total = int(math.ceil(119.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy20' in request.form:
            proname = productname20
            total = int(math.ceil(179.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy21' in request.form:
            proname = productname21
            total = int(math.ceil(349.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy22' in request.form:
            proname = productname22
            total = int(math.ceil(79.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy23' in request.form:
            proname = productname23
            total = int(math.ceil(99.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy24' in request.form:
            proname = productname24
            total = int(math.ceil(43.99))
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')

        elif 'buyall' in request.form:
            proname = ''
            if var == 'PROFILE':
                cur2.execute('SELECT Email_Address FROM billing_info')
                ers = cur2.fetchall()
                if any(email in i for i in ers):
                    return redirect(url_for('purchase'))
                else:
                    return render_template('payment.html')


@app.route('/dashboard')
def dashboard():
    global email, var, total

    conn = connect(host='localhost', user='root', password='', database='carts')
    cur = conn.cursor()

    if var == 'PROFILE':
        cur.execute('SELECT * FROM `%s`', (email,))
        data = cur.fetchall()
        cur.execute('SELECT Price FROM `%s`', (email,))
        prs = cur.fetchall()
        total = int(math.ceil(int(sum(map(sum, prs)))))
        return render_template('cart.html', var='PROFILE', data=data, total = total)
    else:
        return render_template('error1.html', error_message='Please Login or Create an Account')


@app.route('/payment', methods=['POST'])
def payment():
    global email

    conn = connect(host='localhost', user='root', password='', database='billing_info')
    cur = conn.cursor()

    cur.execute('SELECT * FROM billing_info')
    crs = cur.fetchall()

    if request.method == 'POST':
        cur.execute('SELECT Email_Address FROM billing_info')
        ers = cur.fetchall()
        if any(email in i for i in ers) or any(crs in i for i in ers):
            return redirect(url_for('purchase'))
        else:
            if 'submit' in request.form:
                fname = request.form['fname']
                lname = request.form['lname']
                address = request.form['Address']
                city = request.form['City']
                zip_code = request.form['zip']
                noc = request.form['noc']
                creditno = request.form['creditno']
                expdate = request.form['expdate']
                cur.execute(
                    'INSERT INTO billing_info (First_Name, Last_Name, Email_Address, Address, City, Zip_Code, Name_On_Card, Credit_Card_Number, Expire_Date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    (fname, lname, email, address, city, zip_code, noc, creditno, expdate,))
                conn.commit()
                return redirect(url_for('home'))


@app.route('/purchase', methods=['POST', 'GET'])
def purchase():
    global total, email, proname

    if request.method == 'GET':
        return render_template('purchase.html', total = total, name = proname)
    if request.method == 'POST':
        if 'amt_submit' in request.form:
            amt = request.form['amt']
            if total <= float(amt):
                rem = int(amt) - total
                conn2 = connect(host='localhost', user='root', password='', database='carts')
                conn3 = connect(host = 'localhost', user = 'root', password = '', database = 'revenue')
                cur2 = conn2.cursor()
                cur3 = conn3.cursor()
                cur2.execute('SELECT * FROM `%s`', (email,))
                res = cur2.fetchall()
                for rows in res:
                    cur3.execute('INSERT INTO revenue VALUES(%s, %s, %s)', (rows[0], email, rows[1]))
                    conn3.commit()
                    cur3.execute("DELETE FROM revenue WHERE `Product Purchased` = '';")
                    conn3.commit()
                else:
                    cur3.execute('INSERT INTO revenue VALUES(%s, %s, %s)', (proname, email, total))
                    conn3.commit()
                    cur3.execute("DELETE FROM revenue WHERE `Product Purchased` = '';")
                    conn3.commit()
                cur2.execute('DELETE FROM `%s`', (email,))
                conn2.commit()
                return render_template('purchase_success.html', rem=rem)
            else:
                return render_template('error2.html', error_message='Amount is too low')


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        if 'success' in request.form:
            return redirect(url_for('product'))


@app.route('/error', methods=['POST'])
def error():
    if request.method == 'POST':
        if 'account_404' in request.form:
            return redirect(url_for('login'))
        if 'low_amt' in request.form:
            return redirect(url_for('purchase'))
        if 'already_reg' in request.form:
            return redirect(url_for('login'))

@app.route('/admin', methods = ['GET', 'POST'])
def admin():
        
        email = 'admin@gmail.com'

        conn1 = connect(host = 'localhost', user = 'root', passwd = '', database = 'main')
        conn2 = connect(host = 'localhost', user = 'root', passwd = '', database = 'billing_info')
        conn3 = connect(host = 'localhost', user = 'root', passwd = '', database = 'carts')
        conn4 = connect(host = 'localhost', user = 'root', passwd = '', database = 'revenue')
    
        cur1 = conn1.cursor()
        cur2 = conn2.cursor()
        cur3 = conn3.cursor()
        cur4 = conn4.cursor()

        cur1.execute('SELECT * FROM profile');
        cur2.execute('SELECT * FROM billing_info');
        cur3.execute('SELECT * FROM `%s`', (email,))

        res1 = cur1.fetchall()
        res2 = cur2.fetchall()
        res3 = cur3.fetchall()

        cur4.execute('SELECT * FROM revenue')
        res4 = cur4.fetchall()

        cur4.execute('SELECT SUM(`Product Price`) FROM revenue')
        totalres = cur4.fetchall()[0][0]

        vat = int(totalres) * 13/100
        Service_Tax = int(totalres) * 10/100

        netres = int(totalres) - (vat + Service_Tax)

        if request.method == 'GET':
            return render_template('admin_login.html')
        if request.method == 'POST':

            admin_usr = request.form['adminuser']
            admin_pass = request.form['adminpass']

            if admin_usr == 'admin' and admin_pass == 'admin': 
                return render_template('admin.html', account_data = res1, billing_data = res2, revenue = res4, net = netres)
            else:
                return render_template('admin_login.html')

app.run(host='0.0.0.0', port=8080, debug=True)
