import tensorflow as tf
import numpy as np 

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
    model_input = np.array(some_list)
    print(model_input)

    OU_model = tf.keras.models.load_model('nn_model_OU.h5')
    print("HERE IS THE MODELS PREDICTION....")
    predict = OU_model.predict(model_input)
    print(predict)

    #OU_model.summary()

    # TO-DO...
    
    # Need to update HTML inputs to reflect inputs to ML models / Merge new code to HTML
        # Once we make an array of the user inputs we can drop  
        # the ones we dont need for each model since they each  
        # take a different number of inputs
        # THIS MEANS UPDATING HTML,APP.JS,AND APP.PY TO REFLECT THIS
    
    # Figure out how to return outputs to JavaScript file 

    # Figure out Visualizations / create them 
        # Are we creating anohter HTML file to display figures and predictions?

    # Import in rest of models

    # Improve ML accuracy 

    # Host project on cloud if we have time

    # Presentation stuff 










    

    return 'The 3 outputs'