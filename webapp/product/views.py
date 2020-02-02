from flask import Blueprint, current_app, render_template, request, redirect

from webapp.db import db
from webapp.product.models import Product
from webapp.utils import get_redirect_target

blueprint = Blueprint("product", __name__)


@blueprint.route("/")
def index():
    title = "Цветы в горшках"
    product_list = Product.query.all()
    return render_template("product/index.html", page_title=title, product_list=product_list)


@blueprint.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        description = form.get('description')
        price = form.get('price')
        kind = form.get('kind')
        if not description or price or kind:
            entry = Product(description = description, price=price, kind = kind)
            db.session.add(entry)
            db.session.commit()
            return redirect("admin/")
    return redirect(get_redirect_target())


@blueprint.route('/update/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        entry = Product.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
            return render_template('update.html', entry=entry)


@blueprint.route('/update', methods=['POST'])
def update():
    if not id or id != 0:
        entry = Product.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect("admin/")
    return "ошибка"


@blueprint.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entry = Product.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect(get_redirect_target())

@blueprint.route('/buy', methods=['POST'])
def buy():
    title = "Оформление заказа"
    return render_template("buy.html", page_title=title)
