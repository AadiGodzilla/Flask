import uuid, re, math, json, html, markupsafe
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, url_for
from mysql.connector import connect

app = Flask(__name__)

uuid = uuid.uuid4().hex

app.config['SECRET_KEY'] = uuid

var = None
email = None
total = 0
header1 = 0
header2 = 0

with open('static/json/about.json') as f:
    js = json.load(f)

about_list = list(js.values())

mainconn = connect(host = 'localhost', user = 'root', password = '')
maincur = mainconn.cursor()

maincur1 = mainconn.cursor()
maincur2 = mainconn.cursor()
maincur3 = mainconn.cursor()
maincur4 = mainconn.cursor()

maincur.execute('CREATE DATABASE IF NOT EXISTS main')
maincur.execute('CREATE DATABASE IF NOT EXISTS carts')
maincur.execute('CREATE DATABASE IF NOT EXISTS billing_info')
maincur.execute('CREATE DATABASE IF NOT EXISTS revenue')
mainconn.commit()

maincur1.execute('USE main')
maincur1.execute('create table IF NOT EXISTS profile(Email_Address varchar(255), Password varchar(255));')
mainconn.commit()

maincur2.execute('USE carts')
maincur2.execute("create table IF NOT EXISTS `'admin@gmail.com'`(Product varchar(255), Price float(10,2))")
mainconn.commit()

maincur3.execute('USE billing_info')
maincur3.execute('create table IF NOT EXISTS billing_info(First_Name varchar(255), Last_Name varchar(255), Email_Address varchar(255), Address varchar(255), City varchar(255), Zip_Code int, Name_On_Card varchar(255), Credit_Card_Number bigint, Expire_Date date);')
mainconn.commit()

maincur3.execute('USE revenue')
maincur3.execute("create table IF NOT EXISTS revenue (`Product Purchased` varchar(255), `Customer's Email Address` varchar(255), `Product Price` int);")
mainconn.commit()

mainconn.close()

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
    global header1, header2
    if itemname == 'item1':
        header1 = 'LAPTOP1'
        header2 = 2399.99
        if var == 'PROFILE':
            return render_template('item.html', var='PROFILE', imgsrc = '../static/images/product1.jpg', Buy = 'Buy1', addcart = 'addcart1', header1 = header1, header2 = header2, about = list(about_list[0].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item2':
        header1 = 'LAPTOP2'
        header2 = 1399.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/product2.jpg', Buy = 'Buy2', addcart = 'addcart2', header1 = header1, header2 = header2, about = list(about_list[1].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item3':
        header1 = 'LAPTOP3'
        header2 = 999.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/product3.jpg', Buy = 'Buy2', addcart = 'addcart3', header1 = header1, header2 = header2, about = list(about_list[2].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item4':
        header1 = 'LAPTOP4'
        header2 = 459.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/product4.jpg', Buy = 'Buy3', addcart = 'addcart4', header1 = header1, header2 = header2, about = list(about_list[3].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item5':
        header1 = 'LAPTOP5'
        header2 = 3699.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/product5.jpg', Buy = 'Buy4', addcart = 'addcart5', header1 = header1, header2 = header2, about = list(about_list[4].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item6':
        header1 = 'LAPTOP6'
        header2 = 1299.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/product6.jpg', Buy = 'Buy5', addcart = 'addcart6', header1 = header1, header2 = header2, about = list(about_list[5].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item7':
        header1 = 'LAPTOP7'
        header2 = 1899.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/product7.jpg', Buy = 'Buy6', addcart = 'addcart7', header1 = header1, header2 = header2, about = list(about_list[6].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item8':
        header1 = 'LAPTOP8'
        header2 = 2999.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/product8.jpg', Buy = 'Buy7', addcart = 'addcart8', header1 = header1, header2 = header2, about = list(about_list[7].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item9':
        header1 = 'DESKTOP1'
        header2 = 1349.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/cpu1.jpg', Buy = 'Buy8', addcart = 'addcart9', header1 = header1, header2 = header2, about = list(about_list[8].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item10':
        header1 = 'DESKTOP2'
        header2 = 1239.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/cpu2.jpg', Buy = 'Buy10', addcart = 'addcart10', header1 = header1, header2 = header2, about = list(about_list[9].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item11':
        header1 = 'DESKTOP3'
        header2 = 649.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/cpu3.jpg', Buy = 'Buy11', addcart = 'addcart11', header1 = header1, header2 = header2, about = list(about_list[10].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item12':
        header1 = 'DESKTOP4'
        header2 = 1799.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/cpu4.jpg', Buy = 'Buy12', addcart = 'addcart12', header1 = header1, header2 = header2, about = list(about_list[11].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item13':
        header1 = 'DESKTOP5'
        header2 = 199.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/cpu5.jpg', Buy = 'Buy13', addcart = 'addcart13', header1 = header1, header2 = header2, about = list(about_list[12].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item14':
        header1 = 'DESKTOP6'
        header2 = 899.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/cpu6.jpg', Buy = 'Buy14', addcart = 'addcart14', header1 = header1, header2 = header2, about = list(about_list[13].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item15':
        header1 = 'DESKTOP7'
        header2 = 249.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/cpu7.jpg', Buy = 'Buy15', addcart = 'addcart15', header1 = header1, header2 = header2, about = list(about_list[14].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item16':
        header1 = 'DESKTOP8'
        header2 = 619.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/cpu8.jpg', Buy = 'Buy16', addcart = 'addcart16', header1 = header1, header2 = header2, about = list(about_list[15].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item17':
        header1 = 'MISC1'
        header2 = 34.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/per1.jpg', Buy = 'Buy17', addcart = 'addcart17', header1 = header1, header2 = header2, about = list(about_list[16].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item18':
        header1 = 'MISC2'
        header2 = 39.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/per2.jpg', Buy = 'Buy18', addcart = 'addcart18', header1 = header1, header2 = header2, about = list(about_list[17].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item19':
        header1 = 'MISC3'
        header2 = 119.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/per3.jpg', Buy = 'Buy19', addcart = 'addcart19', header1 = header1, header2 = header2, about = list(about_list[18].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item20':
        header1 = 'MISC4'
        header2 = 179.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/per4.jpg', Buy = 'Buy20', addcart = 'addcart20', header1 = header1, header2 = header2, about = list(about_list[19].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item21':
        header1 = 'MISC5'
        header2 = 349.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/per5.jpg', Buy = 'Buy21', addcart = 'addcart21', header1 = header1, header2 = header2, about = list(about_list[20].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item22':
        header1 = 'MISC6'
        header2 = 79.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/per6.jpg', Buy = 'Buy22', addcart = 'addcart22', header1 = header1, header2 = header2, about = list(about_list[21].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item23':
        header1 = 'MISC7'
        header2 = 99.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/per7.jpg', Buy = 'Buy23', addcart = 'addcart23', header1 = header1, header2 = header2, about = list(about_list[22].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')
    if itemname == 'item24':
        header1 = 'MISC8'
        header2 = 43.99
        if var == "PROFILE":
            return render_template('item.html', var="PROFILE", imgsrc = '../static/images/per8.jpg', Buy = 'Buy24', addcart = 'addcart24', header1 = header1, header2 = header2, about = list(about_list[23].values()))
        else:
            return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')


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
            return render_template('error.html', error_message='Account Already Registered Please Login', btn_name = 'already_reg')
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
        try:
            if rv[0] == email and rvp[0] == passwd:
                var = 'PROFILE'
                return redirect(url_for('home'))
            else:
                return render_template('login.html'), email
        except TypeError:
            return render_template('error.html', error_message = 'Account not registered', btn_name = 'ac_not_reg')


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

    file1 = open('templates/products/item1.html').read()
    file2 = open('templates/products/item2.html').read()
    file3 = open('templates/products/item3.html').read()
    file4 = open('templates/products/item4.html').read()
    file5 = open('templates/products/item5.html').read()
    file6 = open('templates/products/item6.html').read()
    file7 = open('templates/products/item7.html').read()
    file8 = open('templates/products/item8.html').read()
    file9 = open('templates/products/item9.html').read()
    file10 = open('templates/products/item10.html').read()
    file11 = open('templates/products/item11.html').read()
    file12 = open('templates/products/item12.html').read()
    file13 = open('templates/products/item13.html').read()
    file14 = open('templates/products/item14.html').read()
    file15 = open('templates/products/item15.html').read()
    file16 = open('templates/products/item16.html').read()
    file17 = open('templates/products/item17.html').read()
    file18 = open('templates/products/item18.html').read()
    file19 = open('templates/products/item19.html').read()
    file20 = open('templates/products/item20.html').read()
    file21 = open('templates/products/item21.html').read()
    file22 = open('templates/products/item22.html').read()
    file23 = open('templates/products/item23.html').read()
    file24 = open('templates/products/item24.html').read()

    soup1 = BeautifulSoup(file1, 'lxml')
    soup2 = BeautifulSoup(file2, 'lxml')
    soup3 = BeautifulSoup(file3, 'lxml')
    soup4 = BeautifulSoup(file4, 'lxml')
    soup5 = BeautifulSoup(file5, 'lxml')
    soup6 = BeautifulSoup(file6, 'lxml')
    soup7 = BeautifulSoup(file7, 'lxml')
    soup8 = BeautifulSoup(file8, 'lxml')
    soup9 = BeautifulSoup(file9, 'lxml')
    soup10 = BeautifulSoup(file10, 'lxml')
    soup11 = BeautifulSoup(file11, 'lxml')
    soup12 = BeautifulSoup(file12, 'lxml')
    soup13 = BeautifulSoup(file13, 'lxml')
    soup14 = BeautifulSoup(file14, 'lxml')
    soup15 = BeautifulSoup(file15, 'lxml')
    soup16 = BeautifulSoup(file16, 'lxml')
    soup17 = BeautifulSoup(file17, 'lxml')
    soup18 = BeautifulSoup(file18, 'lxml')
    soup19 = BeautifulSoup(file19, 'lxml')
    soup20 = BeautifulSoup(file20, 'lxml')
    soup21 = BeautifulSoup(file21, 'lxml')
    soup22 = BeautifulSoup(file22, 'lxml')
    soup23 = BeautifulSoup(file23, 'lxml')
    soup24 = BeautifulSoup(file24, 'lxml')

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

    price_amt1 = float(re.search('[0.00-9.99]+',soup1.find('div', class_='header2').text).group(0))
    price_amt2 = float(re.search('[0.00-9.99]+',soup2.find('div', class_='header2').text).group(0))
    price_amt3 = float(re.search('[0.00-9.99]+',soup3.find('div', class_='header2').text).group(0))
    price_amt4 = float(re.search('[0.00-9.99]+',soup4.find('div', class_='header2').text).group(0))
    price_amt5 = float(re.search('[0.00-9.99]+',soup5.find('div', class_='header2').text).group(0))
    price_amt6 = float(re.search('[0.00-9.99]+',soup6.find('div', class_='header2').text).group(0))
    price_amt7 = float(re.search('[0.00-9.99]+',soup7.find('div', class_='header2').text).group(0))
    price_amt8 = float(re.search('[0.00-9.99]+',soup8.find('div', class_='header2').text).group(0))
    price_amt9 = float(re.search('[0.00-9.99]+',soup9.find('div', class_='header2').text).group(0))
    price_amt10 = float(re.search('[0.00-9.99]+', soup10.find('div', class_='header2').text).group(0))
    price_amt11 = float(re.search('[0.00-9.99]+', soup11.find('div', class_='header2').text).group(0))
    price_amt12 = float(re.search('[0.00-9.99]+', soup12.find('div', class_='header2').text).group(0))
    price_amt13 = float(re.search('[0.00-9.99]+', soup13.find('div', class_='header2').text).group(0))
    price_amt14 = float(re.search('[0.00-9.99]+', soup14.find('div', class_='header2').text).group(0))
    price_amt15 = float(re.search('[0.00-9.99]+', soup15.find('div', class_='header2').text).group(0))
    price_amt16 = float(re.search('[0.00-9.99]+', soup16.find('div', class_='header2').text).group(0))
    price_amt17 = float(re.search('[0.00-9.99]+', soup17.find('div', class_='header2').text).group(0))
    price_amt18 = float(re.search('[0.00-9.99]+', soup18.find('div', class_='header2').text).group(0))
    price_amt19 = float(re.search('[0.00-9.99]+', soup19.find('div', class_='header2').text).group(0))
    price_amt20 = float(re.search('[0.00-9.99]+', soup20.find('div', class_='header2').text).group(0))
    price_amt21 = float(re.search('[0.00-9.99]+', soup21.find('div', class_='header2').text).group(0))
    price_amt22 = float(re.search('[0.00-9.99]+', soup22.find('div', class_='header2').text).group(0))
    price_amt23 = float(re.search('[0.00-9.99]+', soup23.find('div', class_='header2').text).group(0))
    price_amt24 = float(re.search('[0.00-9.99]+', soup24.find('div', class_='header2').text).group(0))

    conn2 = connect(host='localhost', user='root', password='', database='billing_info')
    conn3 = connect(host='localhost', user='root', password='', database='carts')
    cur2 = conn2.cursor()
    cur3 = conn3.cursor()

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
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy2' in request.form:
            proname = productname2
            total = int(math.ceil(1399.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy3' in request.form:
            proname = productname3
            total = int(math.ceil(999.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy4' in request.form:
            proname = productname4
            total = int(math.ceil(459.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy5' in request.form:
            proname = productname5
            total = int(math.ceil(3699.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy6' in request.form:
            proname = productname6
            total = int(math.ceil(1299.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy7' in request.form:
            proname = productname7
            total = int(math.ceil(1899.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy8' in request.form:
            proname = productname8
            total = int(math.ceil(2999.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy9' in request.form:
            proname = productname9
            total = int(math.ceil(1349.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy10' in request.form:
            proname = productname10
            total = int(math.ceil(1239.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy11' in request.form:
            proname = productname11
            total = int(math.ceil(649.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy12' in request.form:
            proname = productname12
            total = int(math.ceil(1799.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy13' in request.form:
            proname = productname13
            total = int(math.ceil(199.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy14' in request.form:
            proname = productname14
            total = int(math.ceil(899.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy15' in request.form:
            proname = productname15
            total = int(math.ceil(249.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy16' in request.form:
            proname = productname16
            total = int(math.ceil(619.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy17' in request.form:
            proname = productname17
            total = int(math.ceil(34.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy18' in request.form:
            proname = productname18
            total = int(math.ceil(39.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy19' in request.form:
            proname = productname19
            total = int(math.ceil(119.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy20' in request.form:
            proname = productname20
            total = int(math.ceil(179.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy21' in request.form:
            proname = productname21
            total = int(math.ceil(349.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy22' in request.form:
            proname = productname22
            total = int(math.ceil(79.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy23' in request.form:
            proname = productname23
            total = int(math.ceil(99.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
            cur2.execute('SELECT Email_Address FROM billing_info')
            ers = cur2.fetchall()
            if any(email in i for i in ers):
                return redirect(url_for('purchase'))
            else:
                return render_template('payment.html')
        elif 'Buy24' in request.form:
            proname = productname24
            total = int(math.ceil(43.99))
            cur3.execute('DELETE FROM `%s`', (email,))
            conn3.commit()
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
        return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')


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
                return render_template('error.html', error_message='Amount is too low', btn_name = 'low_amt')


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
        if 'ac_not_reg' in request.form:
            return redirect(url_for('signup'))

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