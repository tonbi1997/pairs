import pickle

def main():
    with open("shipGPS.pickle", mode="rb") as f:
        hoge = pickle.load(f)
    print(hoge)
if __name__ == '__main__':
    main()