"""A flask application"""

from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {'author':'Emmanuel Eni',
     'title':'Acquatic Life',
     'content':'first post in the second quarter of the year',
     'date_posted':'April 10,2023'},
     {
        'author':'Benjamin Asare',
     'title':'Daily Living',
     'content':'first post in the second quarter of the year',
     'date_posted':'January 24,2023' 
     },
     {
         'author':'Gifty Dantey',
     'title':'Temptations',
     'content':'first post in the second quarter of the year',
     'date_posted':'Feb 1,2023'
     }
]

@app.route('/')
def home():      
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html',posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
