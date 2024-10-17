from flask import Flask,render_template,redirect,request
import sqlite3 as sql

app=Flask(__name__)


conn=sql.connect('airline.db')
c=conn.cursor()


@app.route('/')
def home():
    return render_template('intropage.html')


@app.route('/book_a_flight',methods=['GET','POST'])
def bood_a_flight():
    if request=='POST':
        From=request.form['from']
        To=request.form['to']
        Passengers=request.form['passenger']
        q='SELECT * FROM TABLE_NAME WHERE FROM=? AND TO=? AND PASSENGERS=?' #change the table name
        c.execute(q,(From,To,Passengers))
        table=c.fetchall()
        return render_template('intropage',tables=table)
    return render_template('intropage')


@app.route('/manage',methods=['GET','POST'])
def manage():
    if request=='POST':
        refno=request.form['reference_number']
        lastname=request.form['last_name']   #also we need to add the username of the user so i will modify later
        q='DELETE TABLE_NAME WHERE REFERENCE_NUMBER=?'
        c.execute(q,refno)
        val=c.fetchall()
        if len(val)==0:
            return redirect('No_Payment_Has_Done.html') #go to the page showing the you havnt done the payment
        return redirect('message.html') #message showing flight has been cancelled
    return render_template('intropage')


@app.route('/flight_status',methods=['GET','POST'])
def flight_status():
    if request=='POST':
        From=request.form['from']
        To=request.form['to']
        date=request.form['date']
        q='SELECT * FROM TABLE_NAME WHERE FROM=? AND TO=?' #change the table name
        c.execute(q,(From,To))
        val=c.fetchall()
        return render_template('intropage',table=val)
    return render_template('intropage')


if __name__=='__main__':
    app.run(debug=True)

