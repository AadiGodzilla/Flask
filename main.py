# libraries
import uuid, math, json, datetime
from flask import Flask, render_template, request, redirect, url_for
from mysql.connector import connect, IntegrityError, DatabaseError

# webapp Initialization
app = Flask(__name__)
uuid = uuid.uuid4().hex

app.config['SECRET_KEY'] = uuid

var = None
email = None
total = 0
header1 = 0
header2 = 0
proname = ''

with open('static/json/about.json') as f:
    js = json.load(f)

about_list = list(js.values())

#automatic database and table creation in mysql
mainconn = connect(host = 'localhost', user = 'root', password = 'aadi')
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
maincur3.execute('create table IF NOT EXISTS billing_info(First_Name varchar(255), Last_Name varchar(255), Email_Address varchar(255), Address varchar(255), Phone_Number bigint ,City varchar(255), Zip_Code int, Name_On_Card varchar(255), Credit_Card_Number bigint, Expire_Date date);')
mainconn.commit()

maincur3.execute('USE revenue')
maincur3.execute("create table IF NOT EXISTS revenue (`Product Purchased` varchar(255), `Customer's Email Address` varchar(255), `Product Price` int);")
mainconn.commit()

mainconn.close()

# main page route and function
@app.route('/')
def home():
    if var == 'PROFILE':
        return render_template('home.html', var='PROFILE', button_var='PRODUCT')
    else:
        return render_template('home.html', var='LOGIN', button_var='SIGN UP')

# product page route and function
@app.route('/product/')
def product():
    if var == 'PROFILE':
        return render_template('product.html', var="PROFILE", button_var='PRODUCT')
    else:
        return render_template('product.html', var='LOGIN', button_var='SIGN_UP')

# individual item page route and function
@app.route('/product/<itemname>')
def products(itemname):
    global header1, header2

    if itemname == 'item1':
        header1 = 'LAPTOP1'
        header2 = 2399.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/laptop1.jpg', Buy = 'Buy1', addcart = 'addcart1', header1 = header1, header2 = header2, about = list(about_list[0].values())[0])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/laptop1.jpg', Buy = 'Buy1', addcart = 'addcart1', header1 = header1, header2 = header2, about = list(about_list[0].values())[0])
    if itemname == 'item2':
        header1 = 'LAPTOP2'
        header2 = 1399.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/laptop2.jpg', Buy = 'Buy2', addcart = 'addcart2', header1 = header1, header2 = header2, about = list(about_list[0].values())[1])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/laptop2.jpg', Buy = 'Buy2', addcart = 'addcart2', header1 = header1, header2 = header2, about = list(about_list[0].values())[1])
    if itemname == 'item3':
        header1 = 'LAPTOP3'
        header2 = 999.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/laptop3.jpg', Buy = 'Buy3', addcart = 'addcart3', header1 = header1, header2 = header2, about = list(about_list[0].values())[2])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/laptop3.jpg', Buy = 'Buy3', addcart = 'addcart3', header1 = header1, header2 = header2, about = list(about_list[0].values())[2])
    if itemname == 'item4':
        header1 = 'LAPTOP4'
        header2 = 459.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/laptop4.jpg', Buy = 'Buy4', addcart = 'addcart4', header1 = header1, header2 = header2, about = list(about_list[0].values())[3])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/laptop4.jpg', Buy = 'Buy4', addcart = 'addcart4', header1 = header1, header2 = header2, about = list(about_list[0].values())[3])
    if itemname == 'item5':
        header1 = 'LAPTOP5'
        header2 = 3699.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/laptop5.jpg', Buy = 'Buy5', addcart = 'addcart5', header1 = header1, header2 = header2, about = list(about_list[0].values())[4])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/laptop5.jpg', Buy = 'Buy5', addcart = 'addcart5', header1 = header1, header2 = header2, about = list(about_list[0].values())[4])
    if itemname == 'item6':
        header1 = 'LAPTOP6'
        header2 = 1299.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/laptop6.jpg', Buy = 'Buy6', addcart = 'addcart6', header1 = header1, header2 = header2, about = list(about_list[0].values())[5])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/laptop6.jpg', Buy = 'Buy6', addcart = 'addcart6', header1 = header1, header2 = header2, about = list(about_list[0].values())[5])
    if itemname == 'item7':
        header1 = 'LAPTOP7'
        header2 = 1899.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/laptop7.jpg', Buy = 'Buy7', addcart = 'addcart7', header1 = header1, header2 = header2, about = list(about_list[0].values())[6])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/laptop7.jpg', Buy = 'Buy7', addcart = 'addcart7', header1 = header1, header2 = header2, about = list(about_list[0].values())[6])
    if itemname == 'item8':
        header1 = 'LAPTOP8'
        header2 = 2999.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/laptop8.jpg', Buy = 'Buy8', addcart = 'addcart8', header1 = header1, header2 = header2, about = list(about_list[0].values())[7])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/laptop8.jpg', Buy = 'Buy8', addcart = 'addcart8', header1 = header1, header2 = header2, about = list(about_list[0].values())[7])
    if itemname == 'item9':
        header1 = 'DESKTOP1'
        header2 = 1349.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/cpu1.jpg', Buy = 'Buy9', addcart = 'addcart9', header1 = header1, header2 = header2, about = list(about_list[0].values())[8])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/cpu1.jpg', Buy = 'Buy9', addcart = 'addcart9', header1 = header1, header2 = header2, about = list(about_list[0].values())[8])
    if itemname == 'item10':
        header1 = 'DESKTOP2'
        header2 = 1239.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/cpu2.jpg', Buy = 'Buy10', addcart = 'addcart10', header1 = header1, header2 = header2, about = list(about_list[0].values())[9])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/cpu2.jpg', Buy = 'Buy10', addcart = 'addcart10', header1 = header1, header2 = header2, about = list(about_list[0].values())[9])
    if itemname == 'item11':
        header1 = 'DESKTOP3'
        header2 = 649.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/cpu3.jpg', Buy = 'Buy11', addcart = 'addcart11', header1 = header1, header2 = header2, about = list(about_list[0].values())[10])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/cpu3.jpg', Buy = 'Buy11', addcart = 'addcart11', header1 = header1, header2 = header2, about = list(about_list[0].values())[10])
    if itemname == 'item12':
        header1 = 'DESKTOP4'
        header2 = 1799.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/cpu4.jpg', Buy = 'Buy12', addcart = 'addcart12', header1 = header1, header2 = header2, about = list(about_list[0].values())[11])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/cpu4.jpg', Buy = 'Buy12', addcart = 'addcart12', header1 = header1, header2 = header2, about = list(about_list[0].values())[11])
    if itemname == 'item13':
        header1 = 'DESKTOP5'
        header2 = 199.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/cpu5.jpg', Buy = 'Buy13', addcart = 'addcart13', header1 = header1, header2 = header2, about = list(about_list[0].values())[12])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/cpu5.jpg', Buy = 'Buy13', addcart = 'addcart13', header1 = header1, header2 = header2, about = list(about_list[0].values())[12])
    if itemname == 'item14':
        header1 = 'DESKTOP6'
        header2 = 899.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/cpu6.jpg', Buy = 'Buy14', addcart = 'addcart14', header1 = header1, header2 = header2, about = list(about_list[0].values())[13])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/cpu6.jpg', Buy = 'Buy14', addcart = 'addcart14', header1 = header1, header2 = header2, about = list(about_list[0].values())[13])
    if itemname == 'item15':
        header1 = 'DESKTOP7'
        header2 = 249.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/cpu7.jpg', Buy = 'Buy15', addcart = 'addcart15', header1 = header1, header2 = header2, about = list(about_list[0].values())[14])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/cpu7.jpg', Buy = 'Buy15', addcart = 'addcart15', header1 = header1, header2 = header2, about = list(about_list[0].values())[14])
    if itemname == 'item16':
        header1 = 'DESKTOP8'
        header2 = 619.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/cpu8.jpg', Buy = 'Buy16', addcart = 'addcart16', header1 = header1, header2 = header2, about = list(about_list[0].values())[15])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/cpu8.jpg', Buy = 'Buy16', addcart = 'addcart16', header1 = header1, header2 = header2, about = list(about_list[0].values())[15])
    if itemname == 'item17':
        header1 = 'MISC1'
        header2 = 34.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/per1.jpg', Buy = 'Buy17', addcart = 'addcart17', header1 = header1, header2 = header2, about = list(about_list[0].values())[16])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/per1.jpg', Buy = 'Buy17', addcart = 'addcart17', header1 = header1, header2 = header2, about = list(about_list[0].values())[16])
    if itemname == 'item18':
        header1 = 'MISC2'
        header2 = 39.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/per2.jpg', Buy = 'Buy18', addcart = 'addcart18', header1 = header1, header2 = header2, about = list(about_list[0].values())[17])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/per2.jpg', Buy = 'Buy18', addcart = 'addcart18', header1 = header1, header2 = header2, about = list(about_list[0].values())[17])
    if itemname == 'item19':
        header1 = 'MISC3'
        header2 = 119.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/per3.jpg', Buy = 'Buy19', addcart = 'addcart19', header1 = header1, header2 = header2, about = list(about_list[0].values())[18])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/per3.jpg', Buy = 'Buy19', addcart = 'addcart19', header1 = header1, header2 = header2, about = list(about_list[0].values())[18])
    if itemname == 'item20':
        header1 = 'MISC4'
        header2 = 179.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/per4.jpg', Buy = 'Buy20', addcart = 'addcart20', header1 = header1, header2 = header2, about = list(about_list[0].values())[19])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/per4.jpg', Buy = 'Buy20', addcart = 'addcart20', header1 = header1, header2 = header2, about = list(about_list[0].values())[19])
    if itemname == 'item21':
        header1 = 'MISC5'
        header2 = 349.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/per5.jpg', Buy = 'Buy21', addcart = 'addcart21', header1 = header1, header2 = header2, about = list(about_list[0].values())[20])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/per5.jpg', Buy = 'Buy21', addcart = 'addcart21', header1 = header1, header2 = header2, about = list(about_list[0].values())[20])
    if itemname == 'item22':
        header1 = 'MISC6'
        header2 = 79.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/per6.jpg', Buy = 'Buy22', addcart = 'addcart22', header1 = header1, header2 = header2, about = list(about_list[0].values())[21])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/per6.jpg', Buy = 'Buy22', addcart = 'addcart22', header1 = header1, header2 = header2, about = list(about_list[0].values())[21])
    if itemname == 'item23':
        header1 = 'MISC7'
        header2 = 99.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/per7.jpg', Buy = 'Buy23', addcart = 'addcart23', header1 = header1, header2 = header2, about = list(about_list[0].values())[22])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/per7.jpg', Buy = 'Buy23', addcart = 'addcart23', header1 = header1, header2 = header2, about = list(about_list[0].values())[22])
    if itemname == 'item24':
        header1 = 'MISC8'
        header2 = 43.99
        if var == 'PROFILE':
            return render_template('item.html', var = 'PROFILE', imgsrc = '../static/images/per8.jpg', Buy = 'Buy24', addcart = 'addcart24', header1 = header1, header2 = header2, about = list(about_list[0].values())[23])
        else:
            return render_template('item.html', var = 'LOGIN',imgsrc = '../static/images/per8.jpg', Buy = 'Buy24', addcart = 'addcart24', header1 = header1, header2 = header2, about = list(about_list[0].values())[23])

# sign-up page route and function
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    global var

    if request.method == 'GET':
        return render_template('signup.html')

    if request.method == 'POST':
        email = request.form['email-address']
        passwd = request.form['passwd']
        conn = connect(host='localhost', password='aadi', user='root', database='main')
        conn2 = connect(host='localhost', password='aadi', user='root', database='carts')
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
                cursor.execute('create table `%s`(Product varchar(255), Price float(10,2));', (email,))
                conn.commit()
                return render_template('home.html', var='LOGIN', button_var='SIGN UP')

# login page route and function
@app.route('/login', methods=['POST', 'GET'])
def login():
    global var, email

    if request.method == 'GET':
        return render_template('login.html', button_var='SIGN UP')

    if request.method == 'POST':
        email = request.form['email-address']
        passwd = request.form['passwd']
        conn = connect(host='localhost', user='root', password='aadi', database='main')
        cur = conn.cursor()

        cur.execute('SELECT Email_Address FROM profile WHERE Email_Address = %s;', (email,))
        rv = cur.fetchone()
        cur.execute('SELECT Password FROM profile WHERE Email_Address = %s;', (email,))
        rvp = cur.fetchone()
        try:
            if rv[0] == email and rvp[0] == passwd:
                var = 'PROFILE'
                return redirect(url_for('product'))
            else:
                return render_template('login.html'), email
        except TypeError:
            return render_template('error.html', error_message = 'Account not registered', btn_name = 'ac_not_reg')

# Profile page route and function
@app.route('/profile', methods=['POST', 'GET'])
def profile():
    global email, var

    if request.method == 'GET':
        return render_template('profile.html', account_var=email)
    if request.method == 'POST':
        currpass = request.form['current']
        newpass = request.form['new']
        conn = connect(host='localhost', user='root', password='aadi', database='main')
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
            conn2 = connect(host='localhost', user='root', password='aadi', database='carts')
            cur2 = conn2.cursor()
            cur2.execute('DELETE FROM `%s`', (email,))
            conn2.commit()
            return redirect(url_for('home'))

# cart's page function this route will lead you to the dashboard page
@app.route('/cart', methods=['GET', 'POST'])
def cart():
    global email, var, total, proname

    conn2 = connect(host='localhost', user='root', password='aadi', database='billing_info')
    conn3 = connect(host='localhost', user='root', password='aadi', database='carts')
    cur2 = conn2.cursor()
    cur3 = conn3.cursor()

    if request.method == 'GET':
        return redirect(url_for('dashboard'))

    if request.method == 'POST':

        if var == 'PROFILE':
            conn = connect(host='localhost', user='root', password='aadi', database='carts')
            conn1 = connect(host='localhost', user='root', password='aadi', database='billing_info')
            cur = conn.cursor()
            cur1 = conn1.cursor()

            cur1.execute('SELECT Expire_Date FROM billing_info WHERE Email_Address = %s', (email,))
            dates = cur1.fetchone()

            try:
                if datetime.datetime.strptime(str(dates[0]), '%Y-%m-%d') <= datetime.datetime.today():
                    cur1.execute('DELETE FROM billing_info WHERE Email_Address = %s', (email,))
                    conn1.commit()
                    return render_template('error.html', error_message = 'Your Credit Card Has Expired', btn_name = 'payment_error')
                else:
                    if 'addcart1' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item1'))
                    elif 'addcart2' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item2'))
                    elif 'addcart3' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item3'))
                    elif 'addcart4' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item4'))
                    elif 'addcart5' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item5'))
                    elif 'addcart6' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item6'))
                    elif 'addcart7' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item7'))
                    elif 'addcart8' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item8'))
                    elif 'addcart9' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item9'))
                    elif 'addcart10' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item10'))
                    elif 'addcart11' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item11'))
                    elif 'addcart12' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item12'))
                    elif 'addcart13' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item13'))
                    elif 'addcart14' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item14'))
                    elif 'addcart15' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item15'))
                    elif 'addcart16' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item16'))
                    elif 'addcart17' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item17'))
                    elif 'addcart18' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item18'))
                    elif 'addcart19' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item19'))
                    elif 'addcart20' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item20'))
                    elif 'addcart21' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item21'))
                    elif 'addcart22' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item22'))
                    elif 'addcart23' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item23'))
                    elif 'addcart24' in request.form:
                        cur.execute('INSERT INTO `%s`(Product, Price) VALUES (%s, %s);', (email, header1, header2))
                        conn.commit()
                        return redirect(url_for('products', itemname='item24'))

                    elif 'Buy1' in request.form:
                        proname = header1                
                        total = int(math.ceil(2399.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy2' in request.form:
                        proname = header1                
                        total = int(math.ceil(1399.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy3' in request.form:
                        proname = header1                
                        total = int(math.ceil(999.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy4' in request.form:
                        proname = header1                
                        total = int(math.ceil(459.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy5' in request.form:
                        proname = header1                
                        total = int(math.ceil(3699.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy6' in request.form:
                        proname = header1                
                        total = int(math.ceil(1299.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy7' in request.form:
                        proname = header1                
                        total = int(math.ceil(1899.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy8' in request.form:
                        proname = header1                
                        total = int(math.ceil(2999.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy9' in request.form:
                        proname = header1                
                        total = int(math.ceil(1349.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy10' in request.form:
                        proname = header1
                        total = int(math.ceil(1239.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy11' in request.form:
                        proname = header1
                        total = int(math.ceil(649.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy12' in request.form:
                        proname = header1
                        total = int(math.ceil(1799.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy13' in request.form:
                        proname = header1
                        total = int(math.ceil(199.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy14' in request.form:
                        proname = header1
                        total = int(math.ceil(899.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy15' in request.form:
                        proname = header1
                        total = int(math.ceil(249.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy16' in request.form:
                        proname = header1
                        total = int(math.ceil(619.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy17' in request.form:
                        proname = header1
                        total = int(math.ceil(34.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy18' in request.form:
                        proname = header1
                        total = int(math.ceil(39.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy19' in request.form:
                        proname = header1
                        total = int(math.ceil(119.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy20' in request.form:
                        proname = header1
                        total = int(math.ceil(179.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy21' in request.form:
                        proname = header1
                        total = int(math.ceil(349.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy22' in request.form:
                        proname = header1
                        total = int(math.ceil(79.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy23' in request.form:
                        proname = header1
                        total = int(math.ceil(99.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))
                    elif 'Buy24' in request.form:
                        proname = header1
                        total = int(math.ceil(43.99))
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        cur2.execute('SELECT Email_Address FROM billing_info')
                        ers = cur2.fetchall()
                        if any(email in i for i in ers):
                            return redirect(url_for('purchase'))
                        else:
                            return redirect(url_for('payment'))

                    elif 'buyall' in request.form:
                        proname = ''
                        if var == 'PROFILE':
                            cur2.execute('SELECT Email_Address FROM billing_info')
                            ers = cur2.fetchall()
                            if any(email in i for i in ers):
                                return redirect(url_for('purchase'))
                            else:
                                return redirect(url_for('payment'))
                if 'clearall' in request.form: 
                    if var == 'PROFILE':
                        cur3.execute('DELETE FROM `%s`', (email,))
                        conn3.commit()
                        return redirect(url_for('dashboard'))
            except TypeError:
                return redirect(url_for('payment'))
        else:
            return render_template('error.html', error_message = 'Please Login or Create an Account', btn_name = 'account_404')
            
# cart dashboard page route and function
@app.route('/dashboard')
def dashboard():
    global email, var, total

    conn = connect(host='localhost', user='root', password='aadi', database='carts')
    cur = conn.cursor()

    if var == 'PROFILE':
        cur.execute('SELECT * FROM `%s`', (email,))
        data = cur.fetchall()
        cur.execute('SELECT Price FROM `%s`', (email,))
        prs = cur.fetchall()
        total = int(math.ceil((float(sum(map(sum, prs))))))
        return render_template('cart.html', var='PROFILE', data=data, total = total)
    else:
        return render_template('error.html', error_message='Please Login or Create an Account', btn_name = 'account_404')

# payment registration page route and function (This page will only be shown at first purchase)
@app.route('/payment', methods=['POST', 'GET'])
def payment():
    global email

    conn = connect(host='localhost', user='root', password='aadi', database='billing_info')
    cur = conn.cursor()

    cur.execute('SELECT * FROM billing_info')
    crs = cur.fetchall()

    if request.method == 'GET':
        return render_template('payment.html')
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
                phoneno = request.form['Phone']
                city = request.form['City']
                zip_code = request.form['zip']
                noc = request.form['noc']
                creditno = request.form['creditno']
                expdate = request.form['expdate']
                try:
                    if datetime.datetime.strptime(expdate, '%Y-%m-%d') <= datetime.datetime.today():
                        return render_template('error.html', error_message = 'Credit Card has Expired Try Again', btn_name = 'payment_error')
                except ValueError:
                    return render_template('error.html', error_message = 'Date is Wrong, Try Again', btn_name = 'payment_error')  
                try:                  
                    if fname == "" or lname == "" or address == "" or city == "" or zip_code == "" or noc == "" or creditno == "" or expdate == "":
                        return render_template('error.html', error_message = 'Fields cannot be empty', btn_name = 'payment_error')
                    else:
                        try:
                            cur.execute(
                                'INSERT INTO billing_info VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                (fname, lname, email, address, phoneno, city, zip_code, noc, creditno, expdate,))
                            conn.commit()
                            return redirect(url_for('home'))
                        except IntegrityError:
                            return render_template('error.html', error_message = 'Credit Card Number Already Exists', btn_name = 'payment_error')
                except DatabaseError:
                    return render_template('error.html', error_message = 'Please sEnter a Valid Information', btn_name = "payment_error")
# purchase page route and function
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
                conn2 = connect(host='localhost', user='root', password='aadi', database='carts')
                conn3 = connect(host = 'localhost', user = 'root', password = 'aadi', database = 'revenue')
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

# Success page route and function after a successful purchase
@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        if 'success' in request.form:
            return redirect(url_for('product'))

# Error page route and function for multiple errors
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
        if 'payment_error' in request.form:
            return redirect(url_for('payment'))

# admin page route and function
@app.route('/admin', methods = ['GET', 'POST'])
def admin():
        
        email = 'admin@gmail.com'

        conn1 = connect(host = 'localhost', user = 'root', passwd = 'aadi', database = 'main')
        conn2 = connect(host = 'localhost', user = 'root', passwd = 'aadi', database = 'billing_info')
        conn3 = connect(host = 'localhost', user = 'root', passwd = 'aadi', database = 'carts')
        conn4 = connect(host = 'localhost', user = 'root', passwd = 'aadi', database = 'revenue')
    
        cur1 = conn1.cursor()
        cur2 = conn2.cursor()
        cur3 = conn3.cursor()
        cur4 = conn4.cursor()

        cur1.execute('SELECT * FROM profile')
        cur2.execute('SELECT * FROM billing_info')
        cur3.execute('SELECT * FROM `%s`', (email,))

        res1 = cur1.fetchall()
        res2 = cur2.fetchall()

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
                return render_template('admin.html', account_data = res1, billing_data = res2, revenue = res4, net = netres, gross = totalres)
            else:
                return render_template('admin_login.html')

app.run(host='0.0.0.0', port=8080, debug=True)