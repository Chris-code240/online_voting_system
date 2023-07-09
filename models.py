from flask import Flask, jsonify,json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,Boolean, String, LargeBinary,ForeignKey
import os

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app)

def startDB():
    db.drop_all()
    db.create_all()
class Party(db.Model):
    __tablename__ = "Party"
    id = Column(Integer(),primary_key=True)
    name = Column(String(),nullable=False,unique=True)
    acronym = Column(String(),nullable=False,unique=True)

    def __init__(self,name,acronym) -> None:
        self.name  = name
        self.acronym = acronym

    def getParty(self):
        return {"id":self.id,"name":self.name,"acronym":self.acronym,"aspirants":[a.getAspirant() for a in Aspirant.query.filter(Aspirant.party == self.name).all()]}
    
    def addParty(self):
        db.session.add(self)
        db.session.commit()
    
    def removeParty(self):
        db.session.delete(self)
        db.session.commit()


class Aspirant(db.Model):
    __tablename__ = "Aspirant"
    id = Column(Integer(),primary_key=True)
    firstname = Column(String(),nullable=False)
    lastname = Column(String(),nullable=False)
    voter_number = Column(String(12),ForeignKey('Voter.voter_id'),nullable=False)
    party = Column(String(),ForeignKey('Party.name'),nullable=False)
    post = Column(String(),nullable=False)
    votes = Column(String(),default="[]")

    def __init__(self,firstname,lastname,voter_number,party,post) -> None:
        self.voter_number = voter_number
        self.party = party
        self.post = post
        self.firstname = firstname
        self.lastname = lastname
    
    def getAspirant(self):
        return {"id":self.id,"voter_id":self.voter_number,"party":self.party,"firstname":self.firstname,"lastname":self.lastname,"votes":self.votes} 
    
    def addVote(self,voter_id):
        votes = json.loads(self.votes)
        votes.append(voter_id)
        self.votes = json.dumps(votes)
    
    def remoteVote(self,voter_id):
        votes = json.loads(self.votes)
        votes.remove(voter_id)
        self.votes = json.dumps(votes)


class Voter(db.Model):
    __tablename__ = "Voter"
    id = Column(Integer,primary_key=True)
    voter_id = Column(String(12),nullable=False,unique=True)
    first_name = Column(String(),nullable=False)
    last_name = Column(String(),nullable=False)
    voted = Column(Boolean(),default=False)

    def __init__(self,voter_id,firstname,last_name):
        self.voter_id = voter_id
        self.first_name = firstname
        self.last_name = last_name
    def adduser(self):
        db.session.add(self)
        db.session.commit()
    
    def removeUser(self):
        db.session.delete(self)
        db.session.commit()

    def getvoter(self):
        return {"id":self.id,"voter_id":self.voter_id,"firstname":self.first_name,"lastname":self.last_name}



        

