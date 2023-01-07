import random

RandomNumber = str(random.randint(1,6))
jordan_types = [('LOW'), ('MID'), ('HIGH')]

def get_response(message: str) -> str:
    p_message  = message.lower()
    
    if p_message == 'hello':
        return 'Hey!'
    
    if p_message == 'roll':
        return RandomNumber
    
    if p_message == '!help':
        return "`This is a help message that you can modify.`"
    
    if p_message == 'jordan':
        return jordan_types
    
    
    #if p_message = "/wtb"
        #return "
    