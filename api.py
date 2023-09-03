import flask
from flask import request, jsonify, make_response,render_template
import requests
import numpy as np
import time

data = []
grid = []
solvedjson = {}
lines = []

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.


def possible(y,x,n):
    global grid

    #this bit does a vertical search
    for i in range(0,9):
        if(grid[i][x] == n):
            return False
    
    #this bit does a horizontal search
    for j in range(0,9):
        if(grid[y][j] == n):
            return False

    # this bit does a search in 
    xsquare = (x//3)*3
    ysquare = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if(grid[i + ysquare][j + xsquare] == n):
                return False
    
    return True

def solvegrid():
    global grid
    global solvedjson

    for y in range(9):
        for x in range(9):
            if(grid[y][x] == 0):
                for n in range(1,10):
                    if(possible(y,x,n)):
                        grid[y][x] = n
                        solvegrid()
                        grid[y][x] = 0
                return
    
    # this code will print the grid
    for i in range(3):
        print(str(grid[i][0]) + " " + str(grid[i][1]) + " " + str(grid[i][2]) + "|" + str(grid[i][3]) + " " + str(grid[i][4]) + " " + str(grid[i][5]) + "|" + str(grid[i][6]) + " " + str(grid[i][7]) + " " + str(grid[i][8]))
    print("— — — — — — — — —")
    for i in range(3,6):
        print(str(grid[i][0]) + " " + str(grid[i][1]) + " " + str(grid[i][2]) + "|" + str(grid[i][3]) + " " + str(grid[i][4]) + " " + str(grid[i][5]) + "|" + str(grid[i][6]) + " " + str(grid[i][7]) + " " + str(grid[i][8]))
    print("— — — — — — — — —")
    for i in range(6,9):
        print(str(grid[i][0]) + " " + str(grid[i][1]) + " " + str(grid[i][2]) + "|" + str(grid[i][3]) + " " + str(grid[i][4]) + " " + str(grid[i][5]) + "|" + str(grid[i][6]) + " " + str(grid[i][7]) + " " + str(grid[i][8]))
    #input("more solutions?:")

    solvedjson = {
        "first":str(grid[0][0]) + str(grid[0][1]) + str(grid[0][2]) + str(grid[0][3]) + str(grid[0][4]) + str(grid[0][5]) + str(grid[0][6]) + str(grid[0][7]) + str(grid[0][8]),
        "second":str(grid[1][0]) + str(grid[1][1]) + str(grid[1][2]) + str(grid[1][3]) + str(grid[1][4]) + str(grid[1][5]) + str(grid[1][6]) + str(grid[1][7]) + str(grid[1][8]),
        "third":str(grid[2][0]) + str(grid[2][1]) + str(grid[2][2]) + str(grid[2][3]) + str(grid[2][4]) + str(grid[2][5]) + str(grid[2][6]) + str(grid[2][7]) + str(grid[2][8]),
        "fourth":str(grid[3][0]) + str(grid[3][1]) + str(grid[3][2]) + str(grid[3][3]) + str(grid[3][4]) + str(grid[3][5]) + str(grid[3][6]) + str(grid[3][7]) + str(grid[3][8]),
        "fifth":str(grid[4][0]) + str(grid[4][1]) + str(grid[4][2]) + str(grid[4][3]) + str(grid[4][4]) + str(grid[4][5]) + str(grid[4][6]) + str(grid[4][7]) + str(grid[4][8]),
        "sixth":str(grid[5][0]) + str(grid[5][1]) + str(grid[5][2]) + str(grid[5][3]) + str(grid[5][4]) + str(grid[5][5]) + str(grid[5][6]) + str(grid[5][7]) + str(grid[5][8]),
        "seventh":str(grid[6][0]) + str(grid[6][1]) + str(grid[6][2]) + str(grid[6][3]) + str(grid[6][4]) + str(grid[6][5]) + str(grid[6][6]) + str(grid[6][7]) + str(grid[6][8]),
        "eighth":str(grid[7][0]) + str(grid[7][1]) + str(grid[7][2]) + str(grid[7][3]) + str(grid[7][4]) + str(grid[7][5]) + str(grid[7][6]) + str(grid[7][7]) + str(grid[7][8]),
        "ninth":str(grid[8][0]) + str(grid[8][1]) + str(grid[8][2]) + str(grid[8][3]) + str(grid[8][4]) + str(grid[8][5]) + str(grid[8][6]) + str(grid[8][7]) + str(grid[8][8])
    }



# A route to return all of the available entries in our catalog.
@app.route('/api', methods=['GET','OPTIONS'])
def api_all():
    if request.method == 'OPTIONS': 
        return build_preflight_response()
    elif request.method == 'GET':
        global data
        global grid
        global solvedjson

        data = []
        grid = []
        solvedjson = {}
        lines = []


        lines.append(str(request.args.get('first')))
        lines.append(str(request.args.get('second')))
        lines.append(str(request.args.get('third')))
        lines.append(str(request.args.get('fourth')))
        lines.append(str(request.args.get('fifth')))
        lines.append(str(request.args.get('sixth')))
        lines.append(str(request.args.get('seventh')))
        lines.append(str(request.args.get('eighth')))
        lines.append(str(request.args.get('ninth')))

        for line in lines:
           nums = list(line)
           print(nums)
           numbers = [int(n) for n in nums] # Convert to integers
           data.append(numbers)

        grid = np.array(data)
        solvegrid()

        time.sleep(1)

        return build_actual_response(jsonify(solvedjson))

def build_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def build_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

app.run(host="0.0.0.0")