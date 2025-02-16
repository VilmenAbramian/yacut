from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import LinkForm
from .models import URLMap
from settings import INVALID_SYMBOLS


@app.route('/', methods=('GET', 'POST'))
def index_view():
    form = LinkForm()
    if form.validate_on_submit():
        urlmap = URLMap()
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = urlmap.get_unique_short_id()
        if URLMap.query.filter_by(short=custom_id).first():
            flash(
                f'Имя {custom_id} уже занято!',
                'rejected'
            )
            return render_template('index.html', form=form)
        if not urlmap.is_valid_short_id(custom_id):
            flash(
                INVALID_SYMBOLS, 'rejected'
            )
            return render_template('index.html', form=form)
        link = URLMap(
            original=form.original_link.data,
            short=custom_id,
        )
        db.session.add(link)
        db.session.commit()
        flash(
            url_for(
                'redirect_short_link', short_id=custom_id, _external=True), 'complete_link'
        )
    return render_template('index.html', form=form)


@app.route('/<string:short_id>', methods=('GET',))
def redirect_short_link(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url_map.original)


if __name__ == '__main__':
    app.run()