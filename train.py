import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from predict import estimate
from predict import getThetas


def getDataSet(filepath: str) -> any:
    df = pd.read_csv(filepath)
    return df.iloc[:, 1], df.iloc[:, 0]


# def compute_theta0(price, km, th0: float, th1: float, learning_rate: float):
#     error = 0
#     for idx, _ in enumerate(km):
#         error += float(estimate(km[idx], th0, th1) - price[idx])
#     summation = (error / km.size)
#     return th0 - summation * learning_rate


# def compute_theta1(price, km, th0: float, th1: float, learning_rate: float):
#     error = 0
#     for idx, _ in enumerate(km):
#         error += float(estimate(km[idx], th0, th1) - price[idx]) * km[idx]
#     summation = (error / km.size)
#     return th1 - summation * learning_rate


# def compute_alt_0(th0, errors, learning_rate):
#     return th0 - (learning_rate / len(errors)) * sum(errors)


# def compute_alt_1(th1, km, errors, learning_rate):
#     res = np.dot(errors, km)
#     res = (learning_rate / len(errors)) * res
#     return th1 - res


def compute_errors(price, estimated) -> any:
    return [estimated[idx] - price[idx] for idx in range(len(price))]


def compute_estimated(km, th0, th1) -> any:
    return [th0 + th1 * km[idx] for idx in range(len(km))]


# def show_plot(price, km, th0: float, th1: float):
#     x_pred = estimate(km, th0, th1)
#     print(np.column_stack((km, x_pred)))
#     plt.xlabel(km.name)
#     plt.ylabel(price.name)
#     plt.scatter(km, price, label='Data Points')
#     plt.plot(km, x_pred, color='red')
#     plt.show()


# def real_polyfit(price, km):
#     coefficients = np.polyfit(price, km, 1)
#     print(coefficients)
#     p = np.poly1d(coefficients)
#     plt.scatter(price, km, label='Data Points')
#     plt.plot(price, p(price), label='Linear Fit', color='red')
#     plt.legend()
#     plt.show()

# def algorithm():
#     price, km = getDataSet('data.csv')
#     tmp0, tmp1 = getThetas()
#     learning_rate = 0.0000000001
#     print(tmp0, tmp1)
#     for _ in range(1500):
#         estimated = compute_estimated(km, tmp0, tmp1)
#         errors = compute_errors(price, estimated)
#         tmp0 = compute_theta0(price, km, tmp0, tmp1, learning_rate)
#         tmp1 = compute_theta1(price, km, tmp0, tmp1, learning_rate)
#         tmp0 = compute_alt_0(tmp0, errors, learning_rate)
#         tmp1 = compute_alt_1(tmp1, km, errors, learning_rate)
#         print(f"0 = {tmp0}")
#         print(f"1 = {tmp1}")
#     print(estimated)
#     print(tmp0)
#     print(tmp1)

#     show_plot(price, km, tmp0, tmp1)


price, temp = getDataSet("set.csv")

temp = np.array(temp)

price = np.array(price)


def calc_thet1(thet1: float, learning_rate: float, errors: list) -> float:

    res = 0
    for idx, _ in enumerate(errors):
        res += errors[idx] * temp[idx]
    res = res / len(errors)
    print(f"res : {res}")
    res = res * learning_rate
    thet1 = thet1 - res

    return thet1


def algorithm():
    thet0 = 0
    thet1 = 0
    learning_rate = 0.0001
    iterations = 5000
    estimated = [0, 0, 0]
    errors = [0, 0, 0]
    cost_history = []
    for _ in range(iterations):
        # estimated[0] = estimate(temp[0], thet0, thet1)
        # estimated[1] = estimate(temp[1], thet0, thet1)
        # estimated[2] = estimate(temp[2], thet0, thet1)
        estimated = compute_estimated(temp, thet0, thet1)
        print(f"Iteration : {_} : {estimated}")
        # for idx, _ in enumerate(estimated):
        #     errors[idx] = estimated[idx] - price[idx]
        errors = compute_errors(price, estimated)
        print("errors : ", errors)
        thet0 = thet0 - (sum(errors) / len(errors)) * learning_rate
        thet1 = calc_thet1(thet1, learning_rate, errors)

        print(thet0, thet1)
        guessed = estimate(88, thet0, thet1)
        print(f"Prix d'une glace quand il fait 88 degree : {guessed}")
        cost = sum(e**2 for e in errors) / (2 * len(errors))
        cost_history.append(cost)

    plt.plot(range(iterations), cost_history, color='blue')
    plt.xlabel("Itérations")
    plt.ylabel("Coût J(θ)")
    plt.title("Évolution de la fonction de coût")
    plt.show()
    print("estimated : ", estimated)

    pred = thet0 + thet1 * temp
    print(pred)
    plt.scatter(temp, price)
    plt.plot(temp, pred, color='r')
    plt.show()


def main():
    try:
        algorithm()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
