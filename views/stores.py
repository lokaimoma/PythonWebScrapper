from flask import Blueprint, render_template, redirect, url_for, request
from models import Store 
import json
from models.users import requires_admin, requires_login


stores_blueprint = Blueprint("stores", __name__)


@stores_blueprint.route('/')
@requires_login
def index():
    stores = Store.all()

    return render_template('stores/index.html', stores=stores)


@stores_blueprint.route('/new', methods=['GET', 'POST'])
@requires_admin
def new_store():

    if request.method == 'POST':
        name = request.form['name']
        url_prefix = request.form['url_prefix']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])

        Store(name, url_prefix, tag_name, query).save_to_mongo()

        return redirect(url_for('.index'))

    return render_template('stores/new_store.html')


@stores_blueprint.route('/edit/<string:store_id>', methods=['GET', 'POST'])
@requires_admin
def edit_store(store_id):
    store = Store.get_by_id(store_id)

    if request.method == 'POST':
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])

        store.tag_name = tag_name
        store.query = query
        store.update_mongo(store_id)

        return redirect(url_for('.index'))

    return render_template('stores/edit_store.html', store=store)
