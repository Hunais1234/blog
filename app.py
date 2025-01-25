from flask import Flask,render_template,request,redirect,jsonify
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='blogs'
)

@app.route('/')
def index():
    return render_template('main.html')
@app.route('/about')
def about_page():
    return render_template('about.html')
@app.route('/blog')
def blog_page():
    return render_template('blog.html')
@app.route('/post')
def posts_page():
    return render_template('post.html')
@app.route('/service')
def service_page():
    return render_template('service.html')
@app.route('/main')
def main_page():
    return render_template('main.html')
@app.route('/contact')
def contact_page():
    return render_template('contact.html')
@app.route('/help')
def help_page():
    return render_template('help.html')
@app.route('/login')
def login_page():
    return render_template('login.html')
@app.route('/forget')
def forget_page():
    return render_template('forget.html')
@app.route('/signup')
def signup_page():
    return render_template('signup.html')
@app.route('/reset')
def reset_page():
    return render_template('reset.html')
@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    contact = request.form['contact']
    password = request.form['password']
    
    cursor = db.cursor()
    query = "INSERT INTO register (username, email, contact, password) VALUES (%s, %s, %s, %s)"
    values = (username, email, contact, password)
    cursor.execute(query, values)
    db.commit()
    
    return render_template('login.html')

    
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    cursor = db.cursor()
    query = "SELECT * FROM register WHERE username=%s AND password=%s"
    values = (username, password)
    cursor.execute(query, values)
    user = cursor.fetchone()  # Fetch one record (if exists)
    
    if user:
        return render_template('post.html')
    else:
        return render_template('login.html')

@app.route('/forget', methods=['POST'])
def forget():
    email = request.form['email']
    new_contact = request.form['contact']
    new_password = request.form['password']
    
    cursor = db.cursor()
    query = "UPDATE register SET contact=%s, password=%s WHERE email=%s"
    values = (new_contact, new_password, email)
    cursor.execute(query, values)
    db.commit()

    return render_template('login.html',user=(email, new_contact, new_password))

@app.route('/contact', methods=['POST'])
def contact():
    try:
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        
        cursor = db.cursor()
        query = "INSERT INTO contact (fname, lname, email, phone, message) VALUES (%s, %s, %s, %s, %s)"
        values = (fname, lname, email, phone, message)
        cursor.execute(query, values)
        db.commit()
        
        return render_template('main.html')
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while sending your message."

@app.route('/email', methods=['POST'])
def subscribe_email():
    try:
        # Retrieve the email from the form
        email = request.form['email']
        
        # Create a cursor object
        cursor = db.cursor()
        
        # Define the SQL query to insert the email into the 'mail' table
        query = "INSERT INTO mail (email) VALUES (%s)"
        values = (email,)
        
        # Execute the query
        cursor.execute(query, values)
        
        # Commit the transaction
        db.commit()
        
        # Optionally, handle cases where the email is already subscribed (e.g., primary key constraints)
        
        # Render a template or redirect
        return render_template('blog.html', email=email)
    
    except pymysql.MySQLError as e:
        # Handle database errors
        print(f"Database error: {e}")
        return "An error occurred while processing your subscription."
    
    except Exception as e:
        # Handle other errors
        print(f"Error: {e}")
        return "An unexpected error occurred."
    image_storage = {}


if __name__ == '__main__':
    app.run()


