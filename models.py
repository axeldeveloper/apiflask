from wsgi import db

class Tipos(db.Model):
    __tablename__ = 'Tipos'
    
    id = db.Column(db.Integer, primary_key=True)
    
    descricao = db.Column(db.String())

    def __init__(self, descricao):
        self.descricao = descricao


    def __repr__(self):
        return '<id {}>'.format(self.id)

class Estados(db.Model):
    __tablename__ = 'Estados'
    
    id = db.Column(db.Integer, primary_key=True)
    sigla = db.Column(db.String(2), nullable=False)
    nome = db.Column(db.String(100) , nullable=False)

    def __init__(self, sigla, nome ):
        self.sigla = sigla
        self.nome = nome


    def __repr__(self):
        return '<id {}>'.format(self.id)
