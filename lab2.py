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
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j+1]:
                list[j] , list [j+1] = list [j+1] , list[j]
    print(list)
    
    return(list)
    

def calc_median_temperature(sorted):
    print("calc_median_temperature")
    if len(sorted)%2 != 0:
        middle = len(sorted)//2 
        sorted_list = sorted[middle] 
        print("Median number is " + str(sorted_list))
    
    elif len(sorted)%2 == 0:
        middle1 = len(sorted)//2 - 1
        middle2 = len(sorted)//2

        print("Median number is " + str((sorted[middle1]+ sorted[middle2])/2))

def main():
    list = get_user_input()
    calc_average(list)
    find_min_max(list)
    sorted = sort_temperature(list)
    calc_median_temperature(sorted)

if __name__ == "__main__":
    main()