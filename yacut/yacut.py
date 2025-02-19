from flask import flash, redirect, render_template

from . import app
from .forms import LinkForm
from .models import URLMap
from settings import INVALID_SYMBOLS


@app.route('/', methods=('GET', 'POST'))
def index_view():
    form = LinkForm()
    link = None
    if form.validate_on_submit():
        urlmap = URLMap()
        short = form.custom_id.data
        if not short:
            short = urlmap.get_unique_short()
        if URLMap.query.filter_by(short=short).first():
            flash(
                'Предложенный вариант короткой ссылки уже существует.',
                'rejected'
            )
            return render_template('index.html', form=form)
        if not urlmap.is_valid_short(short):
            flash(
                INVALID_SYMBOLS, 'rejected'
            )
            return render_template('index.html', form=form)
        link = URLMap.create(
            original=form.original_link.data,
            short=short,
            validate=False
        ).short_link()
    return render_template('index.html', form=form, link=link)


@app.route('/<string:short>', methods=('GET',))
def redirect_short_link(short):
    url_map = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url_map.original)
