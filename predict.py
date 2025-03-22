import numpy as np
import pandas as pd


def getDataSet(filepath: str) -> any:
    df = pd.read_csv(filepath)
    return df


def getData():
    df = getDataSet("data.csv")
    km = df.iloc[:, 0]
    price = df.iloc[:, 1]
    km = np.array(km)
    price = np.array(price)
    return km, price


def getThetas():
    with open("thetas.txt", 'r') as file:
        data = file.read()
        thets = data.split('\n')
        t0 = float(thets[0])
        t1 = float(thets[1])
        return t0, t1

def estimate(mileage, t0, t1):
    result = t0 + (t1 * mileage)
    return result

def main():
    try:
        str = input("Mileage : ")
        mileage = int(str)
        t0, t1 = getThetas()
        km, _ = getData()
        km = np.append(km, mileage)
        km_norm = (km - km.mean()) / km.std()
        mileage = km_norm[-1]
        result = estimate(mileage, t0, t1)
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
