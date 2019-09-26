import json

def total_genre(json_array, genreDict):
    for object in json_array:
        songs = object["songs"]
        for song in songs:
            tags = song["tags"]
            for genre in tags:
                genreDict[genre] = genreDict[genre] + 1

def total_readability(json_array, read_dict):
    for object in json_array:
        songs = object["songs"]
        for song in songs:
            fog = song["fog_index"]
            if fog < 3:
                read_dict["x<3"] = read_dict["x<3"]+1
            elif fog >= 3 and fog < 5:
                read_dict["3<x<5"] = read_dict["3<x<5"]+1
            elif fog >= 5 and fog < 7:
                read_dict["5<x<7"] = read_dict["5<x<7"]+1
            else:
                read_dict[">=7"] = read_dict[">=7"]+1

def total_difficulty(json_array, read_dict):
    for object in json_array:
        songs = object["songs"]
        for song in songs:
            fog = song["fog_index"]
            if fog < 25:
                read_dict["<25"] = read_dict["<25"]+1
            elif fog >= 3 and fog < 5:
                read_dict["25>x>50"] = read_dict["25>x>50"]+1
            elif fog >= 5 and fog < 7:
                read_dict["50>x>75"] = read_dict["50>x>75"]+1
            else:
                read_dict[">75"] = read_dict[">75"]+1

def main():
    filename = "cleandata.json"

    genres = {"rock" : 0,
            "alternative/indie" : 0,
            "electronic/dance" : 0,
            "soul" : 0,
            "classical/soundtrack" : 0,
            "pop" : 0,
            "hip-hop/rnb" : 0,
            "disco" : 0,
            "swing" : 0,
            "folk" : 0,
            "country" : 0,
            "jazz" : 0,
            "religious" : 0,
            "blues" : 0,
            "reggae" : 0
    }

    readability = {
        "x<3" : 0,
        "3<x<5" : 0,
        "5<x<7" : 0,
        ">=7" : 0
    }

    difficulty = {
        "<25": 0,
        "25<x<50" : 0,
        "50<x<75" : 0,
        ">75" : 0
    }



    with open(filename) as json_file:
        data = json.load(json_file)
        total_genre(data, genres)
        total_readability(data, readability)
        total_difficulty(data, difficulty)
        print(difficulty)

if __name__ == "__main__":
    main()