import json
import random

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
            if fog < 4:
                read_dict["<4"] = read_dict["<4"]+1
            elif fog >= 4 and fog < 5:
                read_dict["4<x<5"] = read_dict["4<x<5"]+1
            elif fog >= 5 and fog < 7:
                read_dict["5<x<7"] = read_dict["5<x<7"]+1
            else:
                read_dict[">7"] = read_dict[">7"]+1

def count_dupes(json_array, dict):
    for object in json_array:
        songs = object["songs"]
        for song in songs:
            field = song["num_dupes"]
            if field < 20:
                dict["<20"] = dict["<20"]+1
            elif field >= 20 and field < 30:
                dict["20<x<30"] = dict["20<x<30"]+1
            elif field >= 30 and field < 50:
                dict["30<x<50"] = dict["30<x<50"]+1
            else:
                dict[">50"] = dict[">50"]+1

def count_words(json_array, dict):
    for object in json_array:
        songs = object["songs"]
        for song in songs:
            field = song["num_words"]
            if field < 200:
                dict["<200"] = dict["<200"]+1
            elif field >= 200 and field < 300:
                dict["200<x<300"] = dict["200<x<300"]+1
            elif field >= 300 and field < 400:
                dict["300<x<400"] = dict["300<x<400"]+1
            else:
                dict[">400"] = dict[">400"]+1

def count_sentiment(json_array, dict):
    for object in json_array:
        songs = object["songs"]
        for song in songs:
            field = song["sentiment"]["compound"]
            if field < -0.05:
                dict["negative"] = dict["negative"]+1
            elif field >= -0.05 and field < 0.05:
                dict["neutral"] = dict["neutral"]+1
            else:
                dict["positive"] = dict["positive"]+1

def count_grammy(json_array, dict):
    for object in json_array:
        songs = object["songs"]
        for song in songs:
            field = song["WonGrammy"]
            if field == True:
                dict["True"] = dict["True"]+1
            else:
                dict["False"] = dict["False"]+1

def split_data(json_array, testarr, trainarr):
    for jsonobject in json_array:
        testObjectToAdd = {
            "songs" : [],
            "year" : jsonobject["year"]
        }

        trainObjectToAdd = {
            "songs" : [],
            "year" : jsonobject["year"]
        }

        songs = jsonobject["songs"]
        arr = []
        for i in range(100):
            arr.append(i+1)
        # We choose 20 random chart rankings per year as test data.
        test_indices = random.sample(arr, 20)
        for song in songs:
            if song["pos"] in test_indices:
                testObjectToAdd["songs"].append(song)
            else:
                trainObjectToAdd["songs"].append(song)
        testarr.append(testObjectToAdd)
        trainarr.append(trainObjectToAdd)



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
        "<4": 0,
        "4<x<5" : 0,
        "5<x<7" : 0,
        ">7" : 0
    }

    dupes = {
        "<20": 0,
        "20<x<30" : 0,
        "30<x<50" : 0,
        ">50" : 0
    }

    numWords = {
        "<200": 0,
        "200<x<300" : 0,
        "300<x<400" : 0,
        ">400" : 0
    }

    sentiment = {
        "negative": 0,
        "neutral" : 0,
        "positive" : 0
    }

    wonGrammy = {
        "True": 0,
        "False" : 0
    }

    with open(filename) as json_file:
        data = json.load(json_file)
        #total_genre(data, genres)
        #total_readability(data, readability)
        #total_difficulty(data, difficulty)
        #count_dupes(data, dupes)
        #count_words(data, numWords)
        #count_sentiment(data, sentiment)
        test = []
        train = []

        split_data(data, test, train)
        with open("testdata.json", "w+") as writefile:
            json.dump(test, writefile)
        with open("traindata.json", "w+") as writefile:
            json.dump(train, writefile)

if __name__ == "__main__":
    main()