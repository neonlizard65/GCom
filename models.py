from connection import db
from dataclasses import dataclass

@dataclass
class Manager(db.Model):
    __tablename__ = "Manager"

    id: int
    fio: str
    password: str
    
    id = db.Column(db.Integer, primary_key = True)
    fio = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable = False)
    
    
@dataclass
class User(db.Model):
    __tablename__ = "User"

    id: int
    name: str
    password: str
    address: str
    number: str
    balance: float
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable = False)
    address = db.Column(db.String)
    number = db.Column(db.String)
    address = db.Column(db.String)
    balance = db.Column(db.Float)
    
    
@dataclass
class Dogovor(db.Model):
    __tablename__ = "Dogovor"
    
    id: int
    path: str
    
    id = db.Column(db.Integer, primary_key = True)
    path = db.Column(db.String)
   
@dataclass 
class Tariff(db.Model):
    __tablename__ = "Tariff"
    
    id: int
    type: str
    name: str
    price: int
    speed: int
    tv: bool
    video: bool
    
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    tv = db.Column(db.Boolean)
    video = db.Column(db.Boolean)
    
@dataclass  
class Request(db.Model):
    __tablename__ = "Request"
    
    id: int
    clientid: int
    tariffid: int
    managerid: int
    date: str  
    handled: bool
    additional: str
    
    id = db.Column(db.Integer, primary_key = True)
    clientid = db.Column(db.Integer, db.ForeignKey("User.id", ondelete="CASCADE"), nullable=False)
    tariffid = db.Column(db.Integer, db.ForeignKey("Tariff.id", ondelete="CASCADE"), nullable=False)
    managerid = db.Column(db.Integer, db.ForeignKey("Manager.id", ondelete="CASCADE"))
    date = db.Column(db.DateTime)
    handled = db.Column(db.Boolean)
    additional = db.Column(db.String)