#!/usr/bin/env python3

from flask import  make_response
from flask_restful import Resource
from config import app, api
from native_species import species

class Species(Resource):
    def get(self):
        animals = [animal for animal in species()]

        if animals:
            response = make_response(
                animals, 
                200
                )
            
            return response

api.add_resource(Species, '/species')


if __name__ == '__main__':
    app.run(port=5555, debug=True)

