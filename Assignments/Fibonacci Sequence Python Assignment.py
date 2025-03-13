def fibonacci_sequence(num_of_iteration):
    first_value = 0
    second_value = 1
    fibonacci_list = [first_value, second_value]

    if num_of_iteration == 0:
        return fibonacci_list

    elif num_of_iteration == 1:
        fibonacci_list.append(second_value)
        return fibonacci_list
    else:
        fibonacci_list.append(second_value)
        third_value = first_value + second_value
        first_value = second_value
        second_value = third_value
        for i in range(2, num_of_iteration + 2):
            next_value = first_value + second_value
            fibonacci_list.append(next_value)
            first_value = second_value
            second_value = next_value
    return fibonacci_list

num_of_iteration = int(input(" Number of iterations: "))

fibonacci_list = fibonacci_sequence(num_of_iteration)
print(fibonacci_list)



