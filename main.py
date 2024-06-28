def main():
    flag=1
    numbers = []
    previous_input = int(100)
    current_input = int(input('Enter a number: '))
    
    while (flag):
        
        if ( current_input > previous_input):
            flag=0
            print(numbers, end=' ')
            break
        else:
            numbers.append(current_input)
            previous_input = current_input
            current_input = int(input('Enter a number: '))
            continue
            
            


            
        
        
    return numbers

if __name__ == '__main__':
    main()
