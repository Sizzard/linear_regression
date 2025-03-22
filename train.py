import matplotlib.pyplot as plt
from predict import estimate, getData


def show_plot(km, price, estimated):
    plt.scatter(km, price)
    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.plot(km, estimated, color="red")
    plt.show()


def algorithm(km, price):
    t0 = 0
    t1 = 0
    km_norm = (km - km.mean()) / km.std()
    m = len(km_norm)
    iterations = 10000
    learning_rate = 0.01
    estimated = []
    for _ in range(iterations):
        tmp0 = t0
        tmp1 = t1
        sum0 = 0
        sum1 = 0
        
        for i in range(m):
            error = (estimate(km_norm[i], tmp0, tmp1) - price[i])
            sum0 += (error)
            sum1 += (error * km_norm[i])
        
        d0 = (1 / m) * sum0
        d1 = (1 / m) * sum1

        t0 = tmp0 - (learning_rate * d0)
        t1 = tmp1 - (learning_rate * d1)
        if _ % 500 == 0 or _ == 1 or _ == 0:
            print(t0, t1)
            print(f"sum0 : {sum0}, sum1 : {sum1}")

    for mileage in km_norm:
        estimated.append(estimate(mileage, t0, t1))

    show_plot(km, price, estimated)

    return t0, t1


def writeThetas(t0, t1):
    with open("thetas.txt" , 'w') as file:
        file.write(f"{t0}\n{t1}")

def main():
    try:
        km, price = getData()
        t0, t1 = algorithm(km, price)
        writeThetas(t0, t1)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
