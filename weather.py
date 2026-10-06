def main():
    day1 = [26,26,25,25,24,22,21,21,20]
    day2 = [19,19,18,17,17,16,16,16,15,24,23,21,21,20,19,19]
    day3 = [17,18,19,19,18,19,20,19,20,23,14,18,17,19,19,19]

    print("Today")
    max_temperature(day1)
    min_temperature(day1)
    print()

    print("Tomorrow")
    max_temperature(day2)
    min_temperature(day2)
    print()

    print("Day after tommorrow")
    max_temperature(day3)
    min_temperature(day3)
    print()

def max_temperature(temperatures):
    highest_temp = temperatures[0]
    for hour in temperatures:
        if hour > highest_temp:
            highest_temp = hour
    print(f"High {highest_temp}°")
    # TO-DO: Find and print the highest temperature in the list

def min_temperature(temperatures):
    lowest_temp = temperatures[0]
    for hour in temperatures:
        if hour > lowest_temp:
            lowest_temp = hour
    print(f"Low {lowest_temp}°")
    # TO-DO: Find and print the lowest temperature in the list

if __name__ =="__main__":
    main()
