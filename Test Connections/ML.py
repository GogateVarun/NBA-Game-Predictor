import tensorflow as tf
import numpy as np 
import pickle

def run_models(input_dict):

    # To confirm the ML has the correct inputs 
    values = input_dict.values()
    print("Here are the values ...... ")
    print(values)
    print(type(values))

    some_list= []
    for value in values:
        print(type(value))
        some_list.append(value)


    keys = input_dict.keys()
    print(keys)
    print(type(keys))
    # 

    print("Here is the model input.....")
    model_input = np.array(some_list).reshape(1,-1)
    print(model_input)

    ML_model = tf.keras.models.load_model('nn_model_ML.h5')
    spread_model = tf.keras.models.load_model('nn_model_spread.h5') 
    OU_model = tf.keras.models.load_model('nn_model_OU.h5')

    ML_scaler = pickle.load(open('scaler_ML.pkl','rb'))
    spread_scaler = pickle.load(open('scaler_spread.pkl','rb'))
    OU_scaler = pickle.load(open('scaler_OU.pkl','rb'))

    ML_scaled = ML_scaler.transform(model_input)
    spread_scaled = spread_scaler.transform(model_input)
    OU_scaled = OU_scaler.transform(model_input)


  
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


    # TO-DO...
    
    # Need to update HTML inputs to reflect inputs to ML models / Merge new code to HTML
        # Once we make an array of the user inputs we can drop  
        # the ones we dont need for each model since they each  
        # take a different number of inputs
        # THIS MEANS UPDATING HTML,APP.JS,AND APP.PY TO REFLECT THIS
    
    # Figure out how to return outputs to JavaScript file 

    # Figure out Visualizations / create them 
        # Are we creating anohter HTML file to display figures and predictions?
        # Line graph of last 1o guesses
        # 3 Gauges of prediction
        # GIF of whether you should bet on it or not (determine a threshold)

    # Import in rest of models

    # Improve ML accuracy 

    # Host project on cloud if we have time

    # Presentation stuff 

    return {'ML_Output':ML_output,'Spread_Output':spread_output,'OU_Output':OU_output}