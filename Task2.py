def change_to_10(num: str, sys_num: int):
    sys_letters = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for i in range(10):
        sys_letters[f"{i}"] = i
    result = 0
    for element in num:
        result = sys_letters[element] + result * sys_num
    return result


def change_from_10_to_new(number: int, new_sys: int) -> str:
    sys_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    for i in range(10):
        sys_letters[i] = str(i)
    new_num = ''
    # if number < new_sys:
    # return sys_letters[number]
    quotient = number
    while quotient >= new_sys:
        rem_of_dev = quotient % new_sys
        quotient = quotient // new_sys
        new_num = sys_letters[rem_of_dev] + new_num
    new_num = sys_letters[quotient] + new_num
    return new_num


def change_num_to_new(x: str, new_system: int):
    x_pos = x.find('x')
    system_number = int(x[x_pos + 1:])
    number = x[:x_pos]
    return change_from_10_to_new(change_to_10(number, system_number), new_system)


while True:
    inp_num = input("Please, enter number: ")
    inp_sys = int(input("Please, enter system number: "))
    num_in_new_sys = change_num_to_new(inp_num, inp_sys)
    print(num_in_new_sys)
    if input("Do you want to enter again? (Yes/No): ") != "Yes":
        break
