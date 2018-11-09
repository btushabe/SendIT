from flask import Flask, jsonify, request
app = Flask(__name__)

# Empty list where parcels are to be POSTED OR GOT

parcels = []
users = []
    
# Creating the END POINT for USER can add a parcel order
 

@app.route('/api/v1/parcels', methods=['POST'])
def create_parcel_delivery_order():
    parcel = {
        'id': len(parcels)+1,
        'name': request.json['name'],
        'price':  request.json['price'],
        'pickup':request.json['pickup'],
        'destination':request.json['destination']
        }

    parcels.append(parcel)
    return jsonify({'parcel': parcel})




if __name__ == '__main__':
    app.run(debug=True)


