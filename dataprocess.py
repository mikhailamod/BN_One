import json

def total_genre(json_array, genreDict):
    for object in json_array:
        songs = object["songs"]
        for song in songs:
            tags = song["tags"]
            for genre in tags:
                genreDict[genre] = genreDict[genre] + 1

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
    

    with open(filename) as json_file:
        data = json.load(json_file)
        total_genre(data, genres)
        print(genres)

if __name__ == "__main__":
    main()