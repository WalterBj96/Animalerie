from flask import *
from bson import ObjectId

def init_routes(app,animal_collection, stock_collection, transaction_collection ):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    #ajouter animal
    @app.route('/ajouterAnimal', methods = ['GET', 'POST'])
    def ajouterAnimal():
        if request.method == 'POST':
            nom = request.form['nom']
            type = request.form['type']
            age = request.form['age']

            nouvelle_animal = {'nom': nom, 'type': type, 'age': age}
            animal_collection.insert_one(nouvelle_animal)
            return redirect(url_for('afficherAnimaux')) 
        return render_template('afficherAnimal.html')
        
    
    #afficher animal
    @app.route('/afficherAnimaux')
    def afficherAnimaux():
       animaux = animal_collection.find()
       return render_template('afficherAnimal.html', animaux = animaux)
    
    #ajouter stock
    @app.route('/ajouterStock>', methods = ['GET', 'POST'])
    def ajouterStock():
        if request.method == 'POST':
            quantite = request.form['quantite']
            prix = request.form['prix']
            valeur = int(prix) * int(quantite)

            nouveau_stock = {'quantite': quantite, 'prix': prix, 'valeur': valeur}
            stock_collection.insert_one(nouveau_stock)
            return redirect(url_for('afficherStock')) 
        return render_template('afficherStock.html')
       
    
    #afficher stock
    @app.route('/afficherStock')
    def afficherStock():
       stocks = stock_collection.find()
       return render_template('afficherStock.html', stocks = stocks)
    
     #Transaction
    @app.route('/enregistrerTransaction', methods = ['GET', 'POST'])
    def enregistrerTransaction():
        if request.method == 'POST':
            montant = request.form['montant']
            date = request.form['date']
            type = request.form['type']

            enregistrement = {'montant': montant, 'date': date, 'type': type}
            transaction_collection.insert_one(enregistrement)
            return redirect(url_for('afficherTransaction')) 
        return render_template('afficherTransaction.html')
        
     #afficher tansaction
    @app.route('/afficherTransaction')
    def afficherTransaction():
       transactions = transaction_collection.find()
       return render_template('afficherTransaction.html', transactions = transactions)
    