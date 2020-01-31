from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo= PyMongo(app, uri="mongodb://localhost:27017/mars_data")

@app.route('/')
def home():
    scrape_data = mongo.db.mars_data.find()
    #scrape_data=mongo.db.collection.find_one()
    #scraper = mongo.db.collection.find()
    return render_template("index.html", sd=scrape_data)
    #return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    #mars_data = scrape_mars.scrape_info()
    #scrape_data= mongo.db.mars_data()
    data = scrape_mars.scrape()
    #mars.update({}, marsdata, upsert=True)
    mongo.db.mars_data.update({}, data, upsert=True)
    #mongo.db.collection.update({}, data, upsert=True)
    return redirect ("/")
    
if __name__ == "__main__":
    app.run(debug=True)
