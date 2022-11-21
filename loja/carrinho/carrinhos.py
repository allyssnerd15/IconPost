from flask import redirect, render_template, session, url_for, flash, request
from loja import db, app
from loja.produtos.models import Produtos


@app.route('/addCart', methods=['POST'])
def AddCart(id):
    try:
        produto_id = request.form.get('produto_id')
        amount_per_package = request.form.get('amount_per_package')
        produto = Produtos.query.filter_by(id=produto_id).first()
        if produto_id and amount_per_package and request.method == "POST":
            DicItens = {produto_id: {'Nome': produto.name, 'Preço': produto.price}}
            if 'loja' in session:
                print(session['loja'])
            else:
                session['loja'] = DicItens
                return redirect(request.referrer)
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)