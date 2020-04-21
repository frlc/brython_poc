from browser.html import INPUT, LABEL, BR, FORM
from browser import document


def login_form():
    form = FORM(id="meu-forme", action="#", method="GET", target="_blank")
    form <= LABEL('seu nome', For='nome', name="nome")
    form <= INPUT(id='nome')
    form <= BR()
    form <= LABEL('sua senha', For='senha', senha="senha")
    form <= INPUT(id='senha', type='password', required=True)
    form <= BR()
    form <= INPUT(id='submit', type='submit')

    return form
