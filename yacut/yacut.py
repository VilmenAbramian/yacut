from flask import flash, redirect, render_template

from . import app
from .forms import LinkForm
from .models import URLMap


@app.route('/', methods=('GET', 'POST'))
def index_view():
    form = LinkForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    try:
        return render_template(
            'index.html',
            form=form,
            link=URLMap.create(
                original=form.original_link.data,
                short=form.custom_id.data,
            ).short_link()
        )
    except (ValueError, RuntimeError) as error:
        flash(str(error))
        return render_template('index.html', form=form)


@app.route('/<string:short>', methods=('GET',))
def redirect_short_link(short):
    url_map = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url_map.original)
