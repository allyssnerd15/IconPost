from flask import redirect, render_template, url_for, flash, request
from loja import db, app

from .forms import AddProduto



@app.route('/')
def home():
    pagina = request.args.get('pagina', 1, type=int)
    produtos = AddProduto.query.filter(AddProduto.amount_per_package > 0).paginate(pagina=pagina,per_page=4)
    prod = addproduto.query.all()
    return render_template('produtos/index.html', produtos=produtos, prod=prod)


@app.route('/addproduto', methods=['GET', 'POST'])
def addproduto():
    form = AddProduto(request.form)
    return render_template('produtos/addproduto.html', title="Cadastro de produtos", form=form)


@app.route('/addproduto/<int:id>')
def get_produto(id):
    produto = addproduto.query.filter_by(produto_id=id)
    return render_template('produtos/index.html', produto=produto)



@app.route('/addproduto/<int:id>')
def pagina_unica(id):
    produto = addproduto.query.get_or_404(id)
    return render_template('produtos/pagina_unica.html', produto=produto)