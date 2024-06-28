def main():
    
    numbers = []
    previous_input = 0
    current_input = 0
    while (current_input < previous_input):
        current_input = int(input('Enter a number'))
        numbers.append(current_input)
        print(numbers)
        if (current_input > previous_input):
            print(numbers, end='')
            break
        else:
            previous_input = current_input


            return numbers
        
        


if __name__ == '__main__':
    main()
