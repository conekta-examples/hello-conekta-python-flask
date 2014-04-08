import os
from flask import Flask
from flask import render_template
from flask import request
import conekta

app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/index')
@app.route('/subscribe')
def index():
    return render_template('subscribe.html')

@app.route('/subscriptions', methods=["POST"])
def subscription_create():
    conekta.api_key = '1tv5yJp3xnVZ7eK67m4h'

    plan = conekta.Plan.find('gold-plan')

    customer = conekta.Customer.create({
        'name':request.form['name'],
        'email':request.form['email'],
        'cards':[request.form['token_id']],
        'plan':plan.id
    })

    return render_template('subscribed_successfully.html', plan_name=plan.name, customer_id=customer.id)

@app.route('/charge')
def charge():
    return render_template('charge.html')

@app.route('/charges', methods=["POST"])
def charge_create():
    conekta.api_key = '1tv5yJp3xnVZ7eK67m4h'

    charge = conekta.Charge.create({
        'amount':request.form['amount'],
        'currency':'MXN',
        'description':request.form['description'],
        'card':request.form['token_id']
    })

    return render_template('charged_successfully.html', charge=charge)

