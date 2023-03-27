from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "my top secret key rhymes with 123" # this key is needed to access session

@app.route('/') # default page route
def counter():
    if 'counter' in session: # either increment or create counter, which user can reset
        session['counter'] += 1
    else:
        session['counter'] = 1
    
    if 'user_visits' in session: # either increment or create user visits, which user can NOT reset
        session['user_visits'] += 1
    else:
        session['user_visits'] = 1

    return render_template('index.html')

@app.route('/destroy_session') 
def destroy_session():
    session.pop('counter') # will reset counter but NOT user_visits
    return redirect('/')

@app.route('/add_visits', methods=['POST']) # will add values to the counter
def add_visits():
    if request.form['count_inc'] == "": # ignore an empty form
        return redirect('/')
    session['counter'] += int(request.form['count_inc']) - 1 # need the -1 as the counter will add 1 upon redirect
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True, port = 8000) # default port 5000 is used on the mac