import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from predict import estimate
from predict import getThetas


def getDataSet(filepath: str) -> any:
    df = pd.read_csv(filepath)
    return df.iloc[:, 1], df.iloc[:, 0]


def compute_theta0(df0, df1, th0: float, th1: float, learning_rate: float):
    summation = 0
    for idx, _ in enumerate(df1):
        summation += (estimate(df1[idx], th0, th1) - df0[idx])
    summation = (1 / len(df1)) * summation
    tmp_th0 = summation * learning_rate
    return tmp_th0


def compute_theta1(df0, df1, th0: float, th1: float, learning_rate: float):
    summation = 0
    for idx, _ in enumerate(df1):
        summation += (estimate(df1[idx], th0, th1) - df0[idx]) * df0[idx]
    summation = (1 / len(df1)) * summation
    tmp_th1 = summation * learning_rate
    return tmp_th1


def show_plot(df0, df1, th0: float, th1: float):
    x_pred = df0
    print(x_pred)
    plt.xlabel(df0.name)
    plt.ylabel(df1.name)
    plt.scatter(df0, df1)
    plt.plot(df0, x_pred, color='r')
    # plt.show()


def real_polyfit(df0, df1):
    coefficients = np.polyfit(df0, df1, 1)
    print(coefficients)
    p = np.poly1d(coefficients)
    plt.scatter(df0, df1, label='Data Points')
    plt.plot(df0, p(df0), label='Linear Fit', color='red')
    plt.legend()
    plt.show()

def algorithm():
    df0, df1 = getDataSet('data.csv')
    real_polyfit(df0, df1)
    tmp_th0, tmp_th1 = getThetas()
    learning_rate = 0.1
    tmp_th0 = compute_theta0(df0, df1, tmp_th0, tmp_th1, learning_rate)
    tmp_th1 = compute_theta1(df0, df1, tmp_th0, tmp_th1, learning_rate)
    print(tmp_th0)
    print(tmp_th1)
    guessed = tmp_th0 + tmp_th1 * 200000
    print(guessed)


    show_plot(df0, df1, tmp_th0, tmp_th1)


def main():
    try:
        algorithm()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
