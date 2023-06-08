from flask import Flask
from flask import request, jsonify, make_response,Response,Request
import requests
import json
from requests.exceptions import RequestException
from flask_ngrok import run_with_ngrok
from flask_cors import CORS, cross_origin
import pandas as pd
import sqlite3
import constant as constant
import service as service
app = Flask(__name__)


'''movies = {
    "1": {
        "movie_id": "7",
        "title": "Movie 7",
        "Release_Date": "2022-12-04",
        "Duration": "120",
        "Genre":"Drama",
        "Director": "1",
        "Cast":"Actor myano Shiho",
        "Showtime_ID":"1"
    },
    "2": {
        "movie_id": "8",
        "title": "Movie 8",
        "Release_Date": "2022-02-04",
        "Duration": "120",
        "Genre":"Drama",
        "Director": "1",
        "Cast":"Actor Kudo shinichi",
        "Showtime_ID":"1"
    }
}
@app.route('/api/movies', methods = ['GET','POST'])
def api_book():
    if request.method == 'GET':
        return make_response(jsonify(movies),200)
    elif request.method == 'POST':
        content = request.json
        Movie_id = content['movie_id']
        movies[Movie_id] = content

        movie_object = movies.get(Movie_id,{})
        return make_response(jsonify(movie_object), 201)'''
@app.route('/movies', methods=['GET'])
def get_movies():
    try:
        response = requests.get('http://127.0.0.1:3000/movies')
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        
        try:
            movies = response.json()
            return jsonify(movies)
        except json.JSONDecodeError:
            print(response.content)
            return jsonify({'error': 'Invalid JSON response'}), 500

    except RequestException as e:
        return jsonify({'error': str(e)}), 500
if __name__ == "__main__":
    app.run(debug=True)
    
