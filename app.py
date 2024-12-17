from flask import Flask,render_template,request,jsonify
import pickle

app=Flask(__name__)

with open('Car_price_prediction.pickle', 'rb') as f:
    loaded_model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        fuel_type_diesel = 1 if request.form['fuel-type'] == 'diesel' else 0
        fuel_type_gas = 1 if request.form['fuel-type'] == 'gas' else 0
        stroke=float(request.form['stroke'])
        bore=float(request.form['bore'])
        width=float(request.form['width'])
        city_mpg=float(request.form['city-mpg'])
        symboling=float(request.form['symboling'])
        highway_mpg=float(request.form['highway-mpg'])
        height=float(request.form['height'])
    
        input_features=[[fuel_type_diesel,fuel_type_gas,stroke,bore,width,city_mpg,symboling,highway_mpg,height]]

        #predict using the model
        prediction=loaded_model.predict(input_features)

        prediction_text = f"Predicted Car Price: ${round(prediction[0], 2)}"
        return render_template('index.html', prediction_text=prediction_text)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__== '__main__':
    app.run(debug=True,port=5001)
