import random
from data import data,vs

# set initial score tobe 0 
score = 0

# fetches the data from data file
def get_data():
    random_data = random.choice(data)
    name = random_data["name"]
    description = random_data["description"] 
    country = random_data["country"]
    follower = random_data["follower_count"]
    return name,description,country,follower

while True:
    # getting hold of data by calling the function
    name1,description1,country1,follower1 = get_data()
    
    print(f"Compare A: {name1}, {description1}, from {country1}")
    print(vs)
    while True:
        name2,description2,country2,follower2 = get_data()
        if name1 != name2:
            break
    print(f"Compare B: {name2}, {description2}, from {country2}")  
     
    # taking input from user 'A' or 'B' as their answere 
    ask_ans = input("type here :").upper()

    if follower1 > follower2:
        real_ans = "A"
    else:
        real_ans = "B"

    # here if user gives the right answere loop continues 
    if real_ans == ask_ans :
        score += 1
        print("that's right, score is",score)

    # if user gives any wrong answere, game stops by showing final score    
    else:
        print("that's wrong,score is",score,"\ngame ended")
        break

