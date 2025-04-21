from typing import Optional
from fastapi import FastAPI , Request
import mysql.connector
import json
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()#snaana Instance mel fastapi mteena

#Hnee faza mtaa security , mele5er el fast api maykhalich eli yji yebaath alih des requetes donc ena zedt el serveur mtaa el angular lel origins w kotlou trustih
origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/dessert/info")
def gets(id:int):
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "testDB")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM dessert where id_dish = {id}")
    #ena fel resultat eli bech yraja7ouli el api nhebou yrajaali json w assemi el attributs mte3ou houma assemi les attributs mte3i eli f table mtaa el SQL
    row_headers=[x[0] for x in mycursor.description] #EL CODE hedha dima yetaawed donc copy paste w mataabech rouhek
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json_data
@app.get("/dish/info")
def gets(id:int):
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "testDB")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM dish where id_dish = {id}")
    #ena fel resultat eli bech yraja7ouli el api nhebou yrajaali json w assemi el attributs mte3ou houma assemi les attributs mte3i eli f table mtaa el SQL
    row_headers=[x[0] for x in mycursor.description] #EL CODE hedha dima yetaawed donc copy paste w mataabech rouhek
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json_data
@app.get("/salade/info")
def gets(id:int):
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "testDB")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM salade where id_dish = {id}")
    #ena fel resultat eli bech yraja7ouli el api nhebou yrajaali json w assemi el attributs mte3ou houma assemi les attributs mte3i eli f table mtaa el SQL
    row_headers=[x[0] for x in mycursor.description] #EL CODE hedha dima yetaawed donc copy paste w mataabech rouhek
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json_data
@app.get("/menu")
def getM():
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "testDB")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM menu")
    #ena fel resultat eli bech yraja7ouli el api nhebou yrajaali json w assemi el attributs mte3ou houma assemi les attributs mte3i eli f table mtaa el SQL
    row_headers=[x[0] for x in mycursor.description] #EL CODE hedha dima yetaawed donc copy paste w mataabech rouhek
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json_data

@app.post("/salade/del")
async def dels(request:Request):
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "testDB")#Connectiw ala el BD mteena
    mycursor = mydb.cursor()#snaana cursor ala el db 
    body = json.loads(await request.body())#khdhina el body mtaa el requete post mteena w radineh objet json
    #executina instruction mtaa insert w ki hachtna b variable mel body il suffit naamlou {body['{esm_el_attribut}']}
    mycursor.execute(f"DELETE from salade where id_dish = {body['id']}")
    mydb.commit()#commit bech nsajlou fel BD
    return {"done"}
@app.post("/dish/del")
async def dels(request:Request):
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "testDB")#Connectiw ala el BD mteena
    mycursor = mydb.cursor()#snaana cursor ala el db 
    body = json.loads(await request.body())#khdhina el body mtaa el requete post mteena w radineh objet json
    #executina instruction mtaa insert w ki hachtna b variable mel body il suffit naamlou {body['{esm_el_attribut}']}
    mycursor.execute(f"DELETE from dish where id_dish = {body['id']}")
    mydb.commit()#commit bech nsajlou fel BD
    return {"done"}
@app.post("/dessert/del")
async def dels(request:Request):
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "testDB")#Connectiw ala el BD mteena
    mycursor = mydb.cursor()#snaana cursor ala el db 
    body = json.loads(await request.body())#khdhina el body mtaa el requete post mteena w radineh objet json
    #executina instruction mtaa insert w ki hachtna b variable mel body il suffit naamlou {body['{esm_el_attribut}']}
    mycursor.execute(f"DELETE from dessert where id_dish = {body['id']}")
    mydb.commit()#commit bech nsajlou fel BD
    return {"done"}
#dima ki bech tesna3 endpoint ykoun e syntax fel forma hedhi:
#@app.{naw3_el_requete}("/{esm_el_endpoint}") (anwe3 les requetes ykoun ya get ya post)
#def {esm_el_fonction}({les parametres mteek }) (les parametres mteek yajmou ykounou query params benesba lel get w fel post tajem thot param type mte3ou request hedha tajem tekhou menou el data eli fel body )
@app.post("/add")
async def add(request:Request):
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "testDB")#Connectiw ala el BD mteena
    mycursor = mydb.cursor()#snaana cursor ala el db 
    body = json.loads(await request.body())#khdhina el body mtaa el requete post mteena w radineh objet json
    #executina instruction mtaa insert w ki hachtna b variable mel body il suffit naamlou {body['{esm_el_attribut}']}
    mycursor.execute(f"INSERT INTO `{body['type']}` ( `nom_dish`, `desc_dish`, `price_dish` , `img_dish`) VALUES ( '{body['nom']}', '{body['desc']}', '{body['price']}'  , '{body['img']}');")
    mydb.commit()#commit bech nsajlou fel BD
    return {"done"}

@app.post("/gerant/login")
async def login(request:Request):
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "testDB")#Connectiw ala el BD mteena
    mycursor = mydb.cursor()#snaana cursor ala el db 
    body = json.loads(await request.body())#khdhina el body mtaa el requete post mteena w radineh objet json
    #executina instruction mtaa insert w ki hachtna b variable mel body il suffit naamlou {body['{esm_el_attribut}']}
    mycursor.execute(f"SELECT * from gerant where username = '{body['username']}' and password = '{body['password']}' ")
    row_headers=[x[0] for x in mycursor.description] #EL CODE hedha dima yetaawed donc copy paste w mataabech rouhek
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json_data


    
@app.get("/salade")#hedhi GET
def gets():#ken nheb naadi query param juste fi west el () nekteb b syntax hedha {esm_el_var}:{type} [EX : gets(id:int) ======> donc fel requete ki naamel get l http://127.0.0.1:8000/gets?id=4 el variable id mte3i fi west el code bech tkoun el valeur mte3ha 4]
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "testDB")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM salade")
    #ena fel resultat eli bech yraja7ouli el api nhebou yrajaali json w assemi el attributs mte3ou houma assemi les attributs mte3i eli f table mtaa el SQL
    row_headers=[x[0] for x in mycursor.description] #EL CODE hedha dima yetaawed donc copy paste w mataabech rouhek
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json_data
@app.get("/dessert")
def gets():
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "testDB")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM dessert")
    row_headers=[x[0] for x in mycursor.description] 
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json_data
@app.get("/dish")
def gets():
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "testDB")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM dish")
    row_headers=[x[0] for x in mycursor.description] 
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json_data
