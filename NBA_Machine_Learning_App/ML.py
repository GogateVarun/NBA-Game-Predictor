import tensorflow as tf
import numpy as np 
import pickle

def run_models(input_dict):

    # To confirm the ML has the correct inputs 
    values = input_dict.values()
    keys = input_dict.keys()

    some_list= []
    for value in values:
        some_list.append(value)

   
    print("Here is the model input.....")
    model_input = np.array(some_list).reshape(1,-1)
    print(model_input)


    # Loading in the Trained Models and Scaler Objects
    ML_model = tf.keras.models.load_model('Models/nn_model_ML.h5')
    spread_model = tf.keras.models.load_model('Models/nn_model_spread.h5') 
    OU_model = tf.keras.models.load_model('Models/nn_model_OU.h5')

    ML_scaler = pickle.load(open('Models/scaler_ML.pkl','rb'))
    spread_scaler = pickle.load(open('Models/scaler_spread.pkl','rb'))
    OU_scaler = pickle.load(open('Models/scaler_OU.pkl','rb'))

    # Scaling the Inputs using the Scaler Objects
    ML_scaled = ML_scaler.transform(model_input)
    spread_scaled = spread_scaler.transform(model_input)
    OU_scaled = OU_scaler.transform(model_input)

    
    # Making Predictions with the Model
    print("HERE IS THE ML MODEL'S PREDICTION....")
    ML_prediction = ML_model.predict(ML_scaled)
    ML_output = str(ML_prediction[0][0])
    print(ML_output)

    print("HERE IS THE SPREAD MODEL'S PREDICTION....")
    spread_prediction = spread_model.predict(spread_scaled)
    spread_output = str(spread_prediction[0][0])
    print(spread_output)

    print("HERE IS THE OU MODEL'S PREDICTION....")
    OU_prediction = OU_model.predict(OU_scaled)
    OU_output = str(OU_prediction[0][0])
    print(OU_output)

    return {'ML_Output':ML_output,'Spread_Output':spread_output,'OU_Output':OU_output}