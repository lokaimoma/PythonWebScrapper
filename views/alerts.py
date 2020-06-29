from models import Alert, Item
from flask import Blueprint, render_template, request, redirect, url_for, session
from models.users import requires_login

alerts_blueprint = Blueprint("alerts", __name__)

@alerts_blueprint.route('/')
@requires_login
def index():
    alerts = Alert.find_many_by("user_email", session['email'])
    for a in alerts:
        item1 = Item.find_only_one("_id", a.item_id)
        item1.calc()
        a.price = item1.price
        a.update_mongo(a._id)

    return render_template('alerts/index.html', alerts = alerts)


@alerts_blueprint.route('/new', methods=['GET', 'POst'])
@requires_login
def create_new():
    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        price_limit = float(request.form['price_limit'])

        Alert.new_alert(name, url, price_limit)

        return redirect(url_for('.index'))

    return render_template('alerts/create_new.html')


@alerts_blueprint.route('/remove/<string:alert_id>')
@requires_login
def remove_alert(alert_id):
    alert = Alert.get_by_id(alert_id)

    if alert.user_email == session['email']:

        alert.remove_from_mongo(alert_id)

    return redirect(url_for('.index'))

@alerts_blueprint.route('/edit/<string:alert_id>', methods=['GET', 'POST'])
@requires_login
def edit_alert(alert_id):
    alert = Alert.get_by_id(alert_id)

    if alert.user_email == session['email']:
        if request.method == 'POST':
            price_limit = request.form['price_limit']

            alert.price_limit = price_limit

            alert.update_mongo(alert._id)

            return redirect(url_for('.index'))

    return render_template('alerts/edit_alert.html', alert=alert)
