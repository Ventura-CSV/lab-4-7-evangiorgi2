def main():
    numbers = []
    current_input = 0
    previous_input = 0
    while (current_input > previous_input):
        current_input = int(input('Enter a number'))
        if (current_input > previous_input):
            numbers.append(current_input)
            break
        else:   
            previous_input = current_input
        
            print(numbers)
            return numbers
        
        


if __name__ == '__main__':
    main()
