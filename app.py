from flask import Flask,jsonify,request
from model.User import User
app = Flask(__name__)


@app.route('/users/<int:userid>', methods=['GET'])
def getUser(userid):
    try:
        results=User.getUser(userid)

        #print(results)
        message={"users":results}
        return jsonify(message),200
    except Exception as err:
        message={"message":"Error!!"}
        return jsonify(message),500

@app.route('/users') #define the api route
def getAllUsers():
    try:
        results=User.getAllUsers()

        message={"users":results}
        return jsonify(message)
    except Exception as err:
        message={"message":"Error!!"}
        return jsonify(message),500

@app.route('/users', methods=['POST'])
def insertUsers():
    try:
        userJSON=request.json
        #print(userJSON)
        count=User.insertUser(userJSON['username'],userJSON['email'],userJSON['role'],userJSON['password'])
        output={"message":str(count)+"records modified"}
        return jsonify(output),201
    except Exception as err:
        message={"message":"Error!!"}
        return jsonify(message),500


@app.route('/users/<int:userid>', methods=['PUT'])
def updateUser(userid):
    jsonBody=request.json
    email =jsonBody['email']
    count=User.updateUser(userid,email)

    if(count>0):        
        return '{"message": "User with '+str(userid)+ ' has been successfully updated!"}',200
    else:
        return '{"message": "User with '+str(userid)+ ' does not exist!"}',404
    


@app.route('/users/<int:userid>', methods=['DELETE'])
def deleteUser(userid):
 
    count=User.deleteUser(userid)
    
    if(count>0):        
        return '{"message": "User with '+str(userid)+ ' has been successfully deleted!"}',200
    else:
        return '{"message": "User with '+str(userid)+ ' does not exist!"}',404
    


if __name__ == '__main__':
    app.run(debug=True)
