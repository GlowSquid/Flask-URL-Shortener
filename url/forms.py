import wtforms
from wtforms import validators
# from flask_wtf.recaptcha import RecaptchaField


class UrlForm(wtforms.Form):
    old = wtforms.StringField('', validators=[validators.DataRequired(' If URL\'s were that short, would you even be here?')])
    # recaptcha = RecaptchaField()

    def save_url(self, url):
        self.populate_obj(url)
        if not "http" in url.old:
            url.old = "http://" + url.old
        if not "." in url.old:
            url.old = url.old + ".com/"
        return url
