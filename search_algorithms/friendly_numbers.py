from tqdm import tqdm

friendly_sum = lambda n: sum(i for i in range(1, n) if n % i == 0)
friendly_numbers = lambda num1, num2: friendly_sum(num1) == num2 and friendly_sum(num2) == num1
def friendly_main():
    num1, num2 = int(input("first value: ")), int(input("second value: "))
    while num2 < num1: num1, num2 = int(input("first value: ")), int(input("second value: "))
    friends = [(i, j) for i in tqdm(range(num1, num2)) for j in range(i+1, num2+1) if friendly_numbers(i, j)]
    print([x[0] for x in friends], [x[1] for x in friends])

friendly_main()