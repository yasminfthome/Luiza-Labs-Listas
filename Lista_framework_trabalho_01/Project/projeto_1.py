from re import I
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel


# DEFININDO NOSSAS APLICAÇÕES
app = FastAPI()

# TESTE
@app.get("/")
def home():
    return {"Status": "200",
    "Message": "Sejam bem vindos, está é uma api desenvolvida dentro do projeto luiza labs",
    "Data de finalização": "18/09/2022",
    "Autora": "Nicole Maia Argondizzi",
    "Email para duvidas": "nicolemaiaargondizzi02@gmail.com"}


# CRIANDO USUARIO, PRDUTO, CARRINHO
class Usuario(BaseModel):
    id_usuario: int
    nome: str
    email: str
    senha: str
    endereco: List[List[tuple]] = []

class Produto(BaseModel):
    id_produto: int
    nome: str
    descricao: str
    preco: float

class Carrinho(BaseModel):
    id_usuario: int
    produtos: List[list] = []
    preco_total: float
    quantidade_total: int

class Endereco(BaseModel):
    id_usuario: int
    id_endereco: int
    rua: str
    cep: str
    cidade: str
    estado: str
    


# BANCOS DE DADOS
db_usuarios: dict = {}
db_produtos: dict = {}
db_carrinhos: dict = {}


# CALCULA PREÇO DO CARRINHO
def preco_carrinho(id_usuario):
    valor = 0
    amount = 0
    for produto in db_carrinhos[id_usuario].produtos:
        valor += db_produtos[produto[0]].preco*produto[1]
        amount += produto[1]

    db_carrinhos[id_usuario].quantidade_total = amount
    db_carrinhos[id_usuario].preco_total = valor




# VISUALIZANDO OS BANCOS DE DADOS
@app.get("/usuarios")
def get_all_usuarios():
    return db_usuarios

@app.get("/produtos")
def get_all_produtos():
    return db_produtos

@app.get("/carrinhos")
def get_all_carrinhos():
    return db_carrinhos




# ADICIONANDO NOVOS ELEMENTOS AOS BANCOS DE DADOS
@app.post("/usuarios/")
def add_usuario(usuario: Usuario):
    for key in db_usuarios.keys():
        if usuario.id_usuario == key:
            return {"Status": 400, "Message": "O id deste usuario já está cadastrado"}
        elif usuario.email == db_usuarios[key].email:
            return {"Status": 400, "Message": "O email deste usuario já está cadastrado"}
    db_usuarios[usuario.id_usuario] = usuario
    return {"Status":200, "Message": "Usuario adicionado"}

@app.post("/produtos/")
def add_produto(produto: Produto):
    for key in db_produtos.keys():
        if produto.id_produto == key:
            return {"Status": 400, "Message": "O id deste produto já está cadastrado"}
    db_produtos[produto.id_produto] = produto
    return {"Status":200, "Message": "Produto adicionado"}

@app.post("/carrinhos/")
def add_carrinho(carrinho: Carrinho):
    db_carrinhos[carrinho.id_usuario] = carrinho
    return {"Status":200, "Message": "Carrinho adicionado"}

@app.post("/usuarios/enderecos/")
def add_endereco_usuario(endereco: Endereco):
    if endereco.id_usuario in db_usuarios.keys():
        for end in db_usuarios[endereco.id_usuario].endereco:
            if endereco.id_endereco == end[0][1]:
                return {"Status":400, "Message": "Endereço já está cadastrado"}
        db_usuarios[endereco.id_usuario].endereco.append([("id_endereco", endereco.id_endereco), ("Rua", endereco.rua), ("Cep", endereco.cep), 
                                    ("Cidade", endereco.cidade), ("Estado", endereco.estado)])
        return {"Status":200, "Message": "Endereço adicionado com sucesso"}
    else:
        return {"Status":404, "Message": "Usuario não está cadastrado"}


# ADICIONAR PRODUTOS AO CARRINHO
@app.post("/carrinhos/{id_usuario}/{id_produto}/{quantidade}")
def add_produto_carrinho(id_usuario: int, id_produto: int, quantidade: int):
    if id_usuario in db_carrinhos.keys():
        add = False
        for produto in db_carrinhos[id_usuario].produtos:
            if id_produto == produto[0]:
                produto[1] += quantidade
                add = True
        if not add:
            db_carrinhos[id_usuario].produtos.append([id_produto, quantidade])
        
        preco_carrinho(id_usuario)

        return {"Status":200, "Message": f"Produto adicionado ao carrinho associado no usuario {id_usuario}"}
    else:
        return {"Status":404, "Message": f"Não há nenhum carrinho associado ao usuario {id_usuario}"}
    
@app.delete("/carrinhos/{id_usuario}/{id_produto}/{quantidade}")
def remove_produto_carrinho(id_usuario: int, id_produto: int, quantidade: int):
    if id_usuario in db_carrinhos.keys():
        remove = False
        for i, produto in enumerate(db_carrinhos[id_usuario].produtos):
            if id_produto == produto[0]:
                produto[1] -= quantidade
                remove = True
                if produto[1] <= 0:
                    db_carrinhos[id_usuario].produtos.pop(i)
        if not remove:
            return {"Status":404, "Message": f"Produto não está presente no carrinho associado ao usuario {id_usuario}"}

        preco_carrinho(id_usuario)
        return {"Status":200, "Message": f"Produto removido do carrinho associado no usuario {id_usuario}"}
    else:
        return {"Status":404, "Message": f"Não há nenhum carrinho associado ao usuario {id_usuario}"}






# CONSULTANDO USUARIOS, PRODUTOS E PRODUTOS
@app.get("/usuarios/{id_usuario}/")
def get_usuario_by_id(id_usuario: int):
    if id_usuario in db_usuarios.keys():
        return db_usuarios[id_usuario]
    return {"Status": 404, "Message": "O usuario não foi encontrado"}

@app.get("/usuarios/{nome}/")
def get_usuario_by_name(nome: str):
    for key in db_usuarios.keys():
        if db_usuarios[key].nome.split()[0] == nome:
            return db_usuarios[key]
    return {"Status": 404, "Message": "O usuario não foi encontrado"}

@app.get("/usuarios/enderecos/{id_usuario}/")
def get_enderecos_usuario_by_id(id_usuario: int):
    if id_usuario in db_usuarios.keys():
        return db_usuarios[id_usuario].endereco
    return {"Status": 404, "Message": "O usuario não foi encontrado"}




# REMOVENDO USUARIOS, PRODUTOS E ENDERECOS
@app.delete("/usuarios/{id_usuario}/")
def remove_usuario_by_id(id_usuario: int):
    try:
        del db_usuarios[id_usuario]
        return {"Status":200, "Message": "Usuario deletado com sucesso"}
    except Exception as erro:
        return {"Status":404, "Message": "Usuario não está cadastrado", "Erro": erro}

@app.delete("/produtos/{id_produto}/")
def remove_produto_by_id(id_produto: int):
    try:
        del db_produtos[id_produto]
        for key in db_carrinhos:
            for i, prod in db_carrinhos[key]["produtos"]:
                if id_produto == prod[0]:
                    db_carrinhos[key]["produtos"].pop(i)
        return {"Status":200, "Message": "Produto deletado com sucesso"}
    except Exception as erro:
        return {"Status":404, "Message": "Produto não está cadastrado"}

@app.delete("/carrinhos/{id_usuario}")
def remove_carrinho_by_id(id_usuario: int):
    try:
        del db_carrinhos[id_usuario]
        return {"Status":200, "Message": "Produto deletado com sucesso"}
    except Exception as erro:
        return {"Status":404, "Message": "Produto não está cadastrado"}

@app.delete("/usuarios/{id_usuario}/{id_endereco}")
def remove_endereco_usuario(id_usuario: int, id_endereco: int):
    if id_usuario in db_usuarios.keys():
        for i, end in enumerate(db_usuarios[id_usuario].endereco):
            if id_endereco == end[0][1]:
                db_usuarios[id_usuario].endereco.pop(i)
                return {"Status":200, "Message": "Endereço deletado com sucesso"}
            return {"Status":404, "Message": "Endereço não está cadastrado nesse usuario"}
    else:
        return {"Status":404, "Message": "Usuario não está cadastrado"}