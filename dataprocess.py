import json
import math
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
            field = song["wonGrammy"]
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

def printDict(dict, name):
    print("Data for " + name)
    total = 0
    for key in dict:
        total += dict[key]
    for key in dict:
        perc = round_up(dict[key]/total, 2)
        print(key + ": " + str(dict[key]) + ", percentage: " + str(perc))
    print()

def printDictPercOnly(dict, name):
    print("Data for " + name)
    total = 0
    for key in dict:
        total += dict[key]
    for key in dict:
        perc = round_up(dict[key]/total, 2)
        print(perc)
    print()

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def num_words_prob(json_array, dict):
    for obj in json_array:
        songs = obj["songs"]
        for song in songs:
            sent = song["sentiment"]["compound"]
            grammy = song["wonGrammy"]
            readability = song["fog_index"]
            if (sent < -0.05) and grammy == False and (readability >= 7):
                if song["num_words"] < 200:
                    dict["lt200"] = dict["lt200"] + 1
                elif 200 <= song["num_words"] < 300:
                    dict["gt200"] = dict["gt200"] +1
                elif 300 <= song["num_words"] < 400:
                    dict["gt300"] = dict["gt300"] +1
                else:
                    dict["gt400"] = dict["gt400"] +1

def num_dupes_prob(data, dict):
    for obj in data:
        songs = obj["songs"]
        for song in songs:
            numWords = song["num_words"]
            if (numWords >= 400):
                if song["num_dupes"] < 20:
                    dict["lt20"] +=1
                elif 20 <= song["num_dupes"] < 30:
                    dict["lt30"] += 1
                elif 30 <= song["num_dupes"] < 50:
                    dict["lt50"] += 1
                else:
                    dict["gt50"] += 1

def genre_prob(data, dict):
    for obj in data:
        songs = obj["songs"]
        for song in songs:
            numWords = song["num_words"]
            if (numWords >= 400):
                tags = song["tags"]
                for genre in tags:
                    dict[genre] += 1


def main():
    filename = "traindata.json"

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

    numWordsProb = {
        "lt200": 0,
        "gt200": 0,
        "gt300": 0,
        "gt400": 0
    }

    numDupesProb = {
        "lt20": 0,
        "lt30": 0,
        "lt50": 0,
        "gt50": 0
    }

    with open(filename) as json_file:
        data = json.load(json_file)
        # total_genre(data, genres)
        # total_readability(data, readability)
        # total_difficulty(data, difficulty)
        # count_dupes(data, dupes)
        # count_words(data, numWords)
        # count_sentiment(data, sentiment)
        # count_grammy(data, wonGrammy)
        # num_words_prob(data, numWordsProb)
        # num_dupes_prob(data, numDupesProb)
        genre_prob(data, genres)
        printDictPercOnly(genres, "Genre prob")
        #print(genres)

        # printDict(genres, "Genres")
        # printDict(readability, "Readability")
        # printDict(difficulty, "Difficulty")
        # printDict(dupes, "Number of Duplicates")
        # printDict(numWords, "Number of Words")
        # printDict(sentiment, "Sentiment")
        # printDict(wonGrammy, "Grammy Winners")

        # test = []
        # train = []

        # split_data(data, test, train)
        # with open("testdata.json", "w+") as writefile:
        #     json.dump(test, writefile)
        # with open("traindata.json", "w+") as writefile:
        #     json.dump(train, writefile)

if __name__ == "__main__":
    main()