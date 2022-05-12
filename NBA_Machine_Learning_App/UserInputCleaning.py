def clean_inputs(input_dict):

    team = input_dict['home_away']
    
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

    return input_dict 