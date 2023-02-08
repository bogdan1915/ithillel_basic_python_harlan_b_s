while True:
    try:
        a = int(input('Please enter an integer number: '))
        print('Next number for number ',a,'is ',a+1,'\n' 'Previous number for number ',a,'is ',a-1)
        break
    except ValueError:
        print('not an integer')





