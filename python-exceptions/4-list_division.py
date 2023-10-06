#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            division_result = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError):
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                division_result = 0
            elif not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                print("wrong type")
                division_result = 0
            else:
                print("division by 0")
                division_result = 0
        except IndexError:
            print("out of range")
            division_result = 0
        finally:
            result.append(division_result)
    return result
