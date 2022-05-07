def clean_inputs(input_dict):

    team = input_dict['home_away']
    # print(team)
    # print(type(team))

    # Use this loop to confirm the values carried over in the dict from app.py to see as the "before clean" view in terminal output
    for i in input_dict:
        print(input_dict[i])
        print(type(input_dict[i]))
    
    # Dropping unnecessary fields
    del input_dict['_id']
    del input_dict['home_away']

    # Converting string user inputs to floats to match ML inputs
    for keys in input_dict.keys():
        value = input_dict[keys]
        value = float(value)
        input_dict[keys] = value
 
    
    # HOME VS AWAY 
    # Need a column for home and a column for away, not combined (check ML)
    if team.lower() == 'home':
        input_dict['home'] = 1
        input_dict['away'] = 0
    else:
        input_dict['home'] = 0
        input_dict['away'] = 1
    
    # Isolating and confirming the values and the types
    values = input_dict.values()
    print(values)
    print(type(values))

    # Use this loop to confirm value types changed to floats
    for value in values:
        print(type(value))

    # Isolating and confirming the keys 
    keys = input_dict.keys()
    print(keys)
    print(type(keys))
        
    # for keys,values in enumerate(input_dict):
    #     print(keys)
    #     print(values)
    #     print(type(values))
    
    return input_dict 