#!/user/bin/env python3
# Sebstian Lemm


import random



def trial(class_size):
    """trial to see if birthday is true"""
    birth_date = [False] * 365
    for i in range(class_size):
        individual_birthday = random.randint(0, 364) 
        if birth_date[individual_birthday]:
            return True
        else:
            birth_date[individual_birthday] = True 
    return False 

def expiriment(num_trials, size_of_class):
    """expirement loop"""
    success = 0 
    for i in range(num_trials):
        if trial(size_of_class):
            success += 1 
            
    return success 


#print in threshhold function
def threshhold():
    num_trials = 100000
    thresh_input = int(input(f"What threshold would you like?(enter as a percent):"))
    while thresh_input < 1 or thresh_input > 100:
        print(f"This is not a valid percent")
        thresh_input = int(input(f"What threshold would you like?(enter as a percent):"))
    
    for i in range(2, thresh_input):
        success = expiriment(num_trials, i)
        class_size = 30 
            
        prob_success = success / num_trials
        percent = prob_success * 100
        x = success / class_size
        y = x / 100000 
        z = y * 100
            
        if thresh_input >= percent:
            print(f"For {i} people, the probababilty of a shared birthday was {success} / 100000 or {percent:.2f}%")
        else:
            break
           
            
    if success > thresh_input:
        print(f"To achieve at least {thresh_input}% probability of a collision, need {i} people in the room")

    threshhold()



threshhold() 
