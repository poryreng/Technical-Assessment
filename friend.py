import json
from math import radians, sin, cos, acos

def calcDistance(lat1, long1, lat2, long2):
    # convert latitude and longitude from degrees to radians to suit the formula
    lat1 = radians(lat1)
    long1 = radians(long1)
    lat2 = radians(lat2)
    long2 = radians(long2)

    long3 = long2 - long1

    # great circle distance formula, calculates the central angle between 2 points on a sphere
    # multiplied by 6371(earths radius) to get the distance between the 2 points
    distance = acos((sin(lat1) * sin(lat2)) + (cos(lat1) * cos(lat2) * cos(long3))) * 6371
    return distance

# co-ords of stephens green
sgreen_lat = 53.337839
sgreen_long = -6.259520

# empty list to store friend's data
friend_list = []
with open("friends.txt", "r") as file:
    for line in file:
        friends = json.loads(line)
        # changes the longitude and latitude from string to float
        friends_lat = float(friends["latitude"])
        friends_long = float(friends["longitude"])

        distance = calcDistance(sgreen_lat, sgreen_long,friends_lat, friends_long)

        #checks if friends are within 100km from stephens green
        if distance <= 100:
            # appends a string of friend data in a specific format
            friend_list.append(f"Id: {friends['user_id']}, Name: {friends['name']}, {distance:.2f}km away")

# function to get the user Id from friend's data in the list
def getUserID(friend_data):
    return int(friend_data.split(":")[1].split(",")[0])

# sorts the friend list by User Id in ascending order
sorted_friend_list = sorted(friend_list, key=getUserID)

# prints output
for friend in sorted_friend_list:
    print(friend)

# Output of the code:
# Id: 4, Name: Ian Kehoe, 10.41km away
# Id: 5, Name: Nora Dempsey, 23.12km away
# Id: 6, Name: Theresa Leaon, 23.90km away
# Id: 8, Name: Eoin Ahearn, 83.72km away
# Id: 11, Name: Richard Finnegan, 38.00km away
# Id: 12, Name: Christina MacFarlane, 41.65km away
# Id: 13, Name: Olive Ahearn, 62.03km away
# Id: 15, Name: Michael Ahearn, 43.52km away
# Id: 17, Name: Patricia Cahill, 96.28km away
# Id: 23, Name: Eoin Rosan, 82.86km away
# Id: 24, Name: Rose Leaon, 89.19km away
# Id: 26, Name: Stephen MacFarlane, 98.70km away
# Id: 29, Name: Oliver Ahearn, 72.22km away
# Id: 30, Name: Nick Leaon, 82.64km away
# Id: 31, Name: Alan Behan, 44.10km away
# Id: 39, Name: Lisa Ahearn, 38.16km away
