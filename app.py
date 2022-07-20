from flask import Flask, request, redirect
from flask import render_template, url_for
import csv

app = Flask(__name__)  # instantiate the class
print(__name__)


@app.route("/")  # route decorator pwd
def my_home():
    #print(url_for('static', filename='favicon.ico'))
    return render_template('index.html')  # render template


@app.route("/<string:page_name>") # using variable rules <variable> to make the page dynamic
def html_page(page_name):
    return render_template(page_name)

# functions
def write_to_file(data): # func write to database file
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

# functions
def write_to_csv(data):
    with open('database.csv',  newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message]) # pass it as a row

#GET - browser wants us to get information
# POST - means the browser wants us to save information
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() # write dict to variable
            write_to_csv(data) # write to database using func write_to_file
            return redirect('/thankyou.html')
        except:
            return  'did not save to database' # catch the error or error handling
    else:
        return 'something went wrong. Try again'