# import os
import string
from random import choice
from flask import render_template, request, redirect, abort
from app import app, db
from url.forms import UrlForm
from url.models import Url


@app.route("/", methods=['GET', 'POST'])
def index():
    def gen():
        chars = string.ascii_letters + string.digits
        length = 3
        code = ''.join(choice(chars) for x in range(length))
        print("verifying", code)
        exists = db.session.query(db.exists().where(Url.new == code)).scalar()
        if not exists:
            print("Your new code is:", code)
            return code
    code = gen()
    while code is None:
        code = gen()

    if request.method == 'POST' and code is not None:
        form = UrlForm(request.form)
        if form.validate():
            url = form.save_url(Url(new=code))
            db.session.add(url)
            db.session.commit()
            return render_template("success.html", code=code, old=url.old)
    else:
        form = UrlForm()
    return render_template("index.html", form=form)


@app.route('/<new>')
def redirect_to_old(new):
    new = Url.query.filter_by(new=new).first()
    if new is None:
        abort(404)
    else:
        new.hits = new.hits+1
        db.session.add(new)
        db.session.commit()
        return redirect(new.old)


@app.route("/stats")
@app.route("/stats/<int:page>")
def stats(page=1):
    stats = Url.query.order_by(Url.id.desc()).paginate(page, 10, False)
    return render_template("stats.html", stats=stats)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
