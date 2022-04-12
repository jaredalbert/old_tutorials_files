import logging
#import Employee

logger = logging.getLogger(__name__)

logging.basicConfig(filename = 'test_1.log', level = logging.INFO, format = '%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    """add function"""
    return x + y

def subtract(x,y):
    """subtract function"""
    return x-y

def multiply (x,y):
    """multiply function"""
    return x*y

def divide (x, y):
    """division function"""
    try:
        result = x /y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result

num_1 = 10
num_2 = 5
num_3 = 0

add_result = add(num_1, num_2)
error_result = divide(num_2, num_3)
logger.debug('add: {} + {} = {}'.format(num_1, num_2, add_result) )   


    
