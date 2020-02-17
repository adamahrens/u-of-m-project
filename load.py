import csv
import time
from geopy.geocoders import Nominatim

def process():
    data = []
    with open('park_coordinates.csv', newline='') as csvfile:
        parks = csv.reader(csvfile)
        next(parks)
        for row in parks:
            dictionary = {"abbv" : row[0], "name" : row[1], "longitude" : row[2], "latitude" : row[3] }
            data.append(dictionary)

        # Confirm data
        print(data)

        # Lookup State
        for park in data:
            long = park["longitude"]
            lat = park["latitude"]

            geolocator = Nominatim(user_agent="U of M Project")
            location = geolocator.reverse(f'{lat}, {long}')
            time.sleep(1)
            park["state"] = location.raw["address"]["state"]
            print(park)

        # Confirm data
        print(data)

        # Add region
        pacific_west = ["Washington", "Oregon", "California", "Nevada", "Idaho"]
        intermountain = ["Montana", "Wyoming", "Utah", "Colorado", "Arizona", "New Mexico", "Texas", "Oklahoma"]
        midwest = ["North Dakota", "South Dakota", "Nebraska", "Kansas", "Minnesota", "Iowa", "Missouri", "Arkansas", "Wisconsin", "Michigan", "Illinois", "Indiana", "Ohio"]
        south_east = ["Kentucky", "Tennessee", "Louisiana", "Mississippi", "Alabama", "Georgia", "Florida", "North Carolina", "South Carolina"]
        north_east = ["Maine", "Vermont", "New York", "Pennsylvania", "Massachusetts", "Rhode Island", "Connecticut", "New Jersey", "Delaware", "West Virginia", "Virginia", "Maryland"]
        alaska = ["Alaska"]
        hawaii = ["Hawaii"]
        samoa = ["American Samoa"]
        vi = ["United States Virgin Islands"]
        for park in data:
            state = park["state"]
            if state in pacific_west:
                park["region"] = "Pacific West"
            elif state in intermountain:
                park["region"] = "Intermountain"
            elif state in midwest:
                park["region"] = "Midwest"
            elif state in south_east:
                park["region"] = "South East"
            elif state in north_east:
                park["region"] = "North East"
            elif state in alaska:
                park["region"] = "Alaska"
            elif state in hawaii:
                park["region"] = "Hawaii"
            elif state in samoa:
                park["region"] = "American Samoa"
            elif state in vi:
                park["region"] = "Virgin Islands"
            else:
                print(f"Unknown state {state}")

        print(data)
