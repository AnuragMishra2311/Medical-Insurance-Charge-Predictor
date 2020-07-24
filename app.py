import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():

    
    
    age=int(request.form['age'])
    bmi=float(request.form['bmi'])
    child=int(request.form['children'])
    gender=int(request.form['gender'])
    smoker=int(request.form['smoker'])
    
    final_features=np.array([[age,bmi,child,gender,smoker]])
    prediction=model.predict(final_features)
    output=prediction[0]
    
    return render_template('index.html',prediction_text='Your Insurance cost will be around {} bucks 💵'.format(int(output))) 
        
if __name__=='__main__':
    app.run(debug=True)
    
