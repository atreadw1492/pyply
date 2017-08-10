


import pandas
import collections
import functools


def lapply(OBJECT, func, keys = None):
    """
    
    lapply(OBJECT, func, keys = None)
    
    Based off R's lapply function.  Takes a list, tuple, or dict
       as input, along with a function.  The function is applied to every element
       in this object.
       
    lapply returns a dict.  The keys of the dict are either the value of input 'keys'
    parameter or a default index.
       """
    if is_list(OBJECT) or is_tuple(OBJECT):
    
        mapped = [func(x) for x in OBJECT]
        keys = keys if keys is not None else range(len(mapped))
        
        result = {key : val for key,val in zip(keys , mapped)}
                  
        return result

    elif is_dict(OBJECT):

        keys = OBJECT.keys() if keys is None else keys
        
        mapped = [func(x) for x in OBJECT.items()]
        
        result = {key : val for key,val in zip(keys , mapped)}       
                  
        return result
        
    else:
        
        raise Exception("Only lists, tuples, and dicts supported")
        

def sapply(LIST , func, return_type = list):
    
    """sapply(LIST , func)
    
    Based off R's sapply function.  Takes a list, tuple, or dict
       as input, along with a function.  The function is applied to every element
       in this object.
       
    sapply returns a list.
       """
    if return_type == list:
        return [func(x) for x in LIST]
    elif return_type == tuple:
        return tuple(func(x) for x in LIST)
    else:
        raise Exception("return_type must be list or tuple")
        



def mode(OBJECT):
    
    """stats_mode(OBJECT)
        
        Computes simple statistical mode of a list or tuple. """
    
    if not is_list(OBJECT) and not is_tuple(OBJECT):
        
        raise Exception("Input must be a list or tuple")
        
    
    counter = collections.Counter(OBJECT)
    max_count = max(counter.values())
    
    result = [key for key,val in counter.items() if val == max_count]

    if len(result) == 1:
        return result[0]
    
    return sorted(result)
    


def rapply(OBJECT, func, keys = None , _type = None):
    
    
    """
    
    rapply(func , OBJECT, keys = None , _type = None)
    
    Based off R's rapply function.  Takes a list, tuple, or dict
       as input, along with a function.  The function is applied to each element
       in this object that has type = _type (the input parameter).
       
    For example, this can apply a function to all integers in a list of mixed types.
       
    rapply returns a dict, list, or tuple depending on the input.  
    
    If a dict is returned, the keys are either the value of input 'keys'
    parameter or a default index."""
    
    
    if is_list(OBJECT) or is_tuple(OBJECT):
        
        result = [x for x in OBJECT if type(x) == _type]
        
        return sapply(result , func)
        
    elif is_dict(OBJECT):

        keys = OBJECT.keys() if keys is None else keys

        result = {key : val for key,val in zip(keys, OBJECT)}
                  
        result = {key : val for key,val in result.items() if type(val) == _type}

        return lapply(result , func, keys)
                  
                  
    else:
        
        raise Exception("Only lists, tuples, and dicts supported")
        
        
def flatten(LIST):
    
    """flatten(LIST , recursive = True)
       
       Flattens a list of lists. """
       
    if LIST == []:
        return []
    
    if is_list(LIST[0]):
        
        return flatten(LIST[0]) + flatten(LIST[1:])
    
    return LIST[:1] + flatten(LIST[1:])
            

    


def split(df,field):
    
    """
       split(df,field)
       
       Based of R's split function.  
       This splits a data frame into a list of subset data frames, split """
    
    unique_field_values = list(set(field))
    
    temp = {key : df[df[field] == key] for key in unique_field_values}
    
    return collections.OrderedDict(temp)

    
def unsplit(df_list):
    """unsplit(df_list)
    
       Based off R's unsplit function.
       Appends a list of data frames and outputs a single data frame."""
    return functools.reduce(lambda x,y: x.append(y) , df_list)    
    
def is_tuple(x):
    if type(x) == tuple:
        return True
    return False

def is_list(x):
    if type(x) == list:
        return True
    return False
    
def is_dict(x):
    if type(x) == dict:
        return True
    return False

def is_int(x):
    if type(x) == int:
        return True
    return False

def is_float(x):
    if type(x) == float:
        return True
    return False

def is_str(x):
    if type(x) == str:
        return True
    return False
    
def is_DataFrame(x):
    if type(x) == pandas.core.frame.DataFrame:
        return True
    return False
    
def ifelse(EXPR , flow1 , flow2):
    
    """ifelse(EXPR , flow1 , flow2) 
       
       Based off R's ifelse function.
       
       Single-line, functional version of if / else.
    """
    
    if EXPR:
        return flow1
    return flow2
    
  
def switch(EXPR , *args,**kwargs):
    
    """
       switch(EXPR , *args,**kwargs)
       
       Based off switch function from R and other languages.
       
       switch offers a condensed version of a series of if / else 
       statements.  
       
       See github page for examples.
       """
    
    if is_int(EXPR):
        if is_list(args[0]) or is_tuple(args[0]):
            return args[0][EXPR]
        else:
            return args[EXPR]
        
    elif is_str(EXPR):
      
        return kwargs[EXPR]

    
    else:
        
        raise Exception("'EXPR' must be an int or str")
    
    
    
    
    
    
    
    
    
    
    