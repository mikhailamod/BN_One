# script for messing around and testing

import random

def main():
    arr = []
    for i in range(100):
        arr.append(i+1)
    newarr = random.sample(arr, 20)

    # for each item in json, check if pos is in newarr, then add to testjson, else add to train json


if __name__ == "__main__":
    main()