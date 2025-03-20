def getThetas():
    with open("thetas.txt", 'r') as file:
        data = file.read()
        thets = data.split('\n')
        thet0 = float(thets[0])
        thet1 = float(thets[1])
        return thet0, thet1

def estimate(mileage: int, thet0: float, thet1: float) -> int:
    result = thet0 + (thet1 * mileage)
    return result

def main():
    try:
        str = input("Mileage : ")
        mileage = int(str)
        thet0, thet1 = getThetas()
        result = estimate(mileage, thet0, thet1)
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
