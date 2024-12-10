def main():
    #getting camel case from user
    camel_case = input('camelCase: ')

    #printing...
    print('Camel case: ' + camel_case)

    #using function to define and transform camel to snake
    snake_case = transform_camel_case(camel_case)

    #printing again...
    print('Snake case ' + snake_case)

#transforming camel to snake using isupper to detect uppercase letter per character in camel case, then formatting
def transform_camel_case(camel_case):

    #set snake_case = nothing so we can add to it
    snake_case = ''

    #for every character in camel_case, we check if upper. if so, we add the "_" and add the lowercase letter
    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()

        #else we just add the lowercase letter
        else:
            snake_case += char

    #then we return that string
    return snake_case

#and call main
main()


