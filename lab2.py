def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    x = input()
    y = x.split(",")
    y = list(map(float, y))    
    # print(y)
    return y

def calc_average(list):
    print("calc_average")
    total = sum(list)
    count = len(list)
    print("Temperature reading (average) :" + str(total/count))

def find_min_max(list):
    print("find_min_max")
    minimum = min(list)
    maximum = max(list)
    print([minimum, maximum])

def sort_temperature(list):
    print("sort_temperature")
    

def calc_median_temperature():
    print("calc_median_temperature")

def main():
    list = get_user_input()
    calc_average(list)
    find_min_max(list)
    sort_temperature(list)

if __name__ == "__main__":
    main()