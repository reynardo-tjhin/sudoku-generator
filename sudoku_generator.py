import random

# 17 is the absolute minimum number of clues in a standard sudoku.

def remove(ls):
    """function always removes last element of list"""
    new_ls = []
    for i in range(0, len(ls) - 1):
        new_ls.append(ls[i])
    return new_ls

def is_set(ls):
    """return True if the list has all different elements"""
    return len(set(ls)) == len(ls)

def check(ls):
    """return a new list that is a correct answer"""
    first_part_ls = []
    second_part_ls = []
    i = 0
    while i < len(ls):
        if i >= 0 and i <= 8:
            first_part_ls.append(ls[i])
        else:
            second_part_ls.append(ls[i])
        i += 1
    if len(set(first_part_ls)) != 9 and len(set(second_part_ls)) != 9:
        return False
    row7 = []
    row8 = []
    row9 = []
    j = 0
    while j < len(first_part_ls):
        if j >= 0 and j <= 2:
            row7.append(first_part_ls[j])
            row7.append(second_part_ls[j])
        elif j >= 3 and j <= 5:
            row8.append(first_part_ls[j])
            row8.append(second_part_ls[j])
        else:
            row9.append(first_part_ls[j])
            row9.append(second_part_ls[j])
        j += 1
    if len(set(row7)) == 6 and len(set(row8)) == 6 and len(set(row9)) == 6:
        return True
    return False

is_success = True
is_fail_new = True

while is_fail_new:
    index = 0
    while True:
        try:
            index += 1
            numbers = [1,2,3,4,5,6,7,8,9]

            mid_box = []

            for i in range(0,9):
                random_index = random.randint(0, len(numbers) - 1)
                mid_box.append(numbers[random_index])
                numbers.pop(random_index)

            column4 = []
            for i in range(0,3):
                column4.append(mid_box[i])

            column5 = []
            for i in range(3,6):
                column5.append(mid_box[i])

            column6 = []
            for i in range(6,9):
                column6.append(mid_box[i])

            row4 = []
            for i in range(0,3):
                row4.append(mid_box[3 * i])
            
            row5 = []
            for i in range(0,3):
                row5.append(mid_box[3 * i + 1])

            row6 = []
            for i in range(0,3):
                row6.append(mid_box[3 * i + 2])

            row1 = []
            row2 = []
            row3 = []
            row7 = []
            row8 = []
            row9 = []

            column1 = []
            column2 = []
            column3 = []
            column7 = []
            column8 = []
            column9 = []

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in range(0,3):
                numbers.remove(mid_box[i])
            random_index = random.randint(0, len(numbers) - 1)
            r3c4 = numbers[random_index]
            column4.append(r3c4)
            row3.append(r3c4)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in range(3,6):
                numbers.remove(mid_box[i])
            if r3c4 in numbers:
                numbers.remove(r3c4)
            random_index = random.randint(0, len(numbers) - 1)
            r3c5 = numbers[random_index]
            column5.append(r3c5)
            row3.append(r3c5)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in range(6,9):
                numbers.remove(mid_box[i])
            if r3c4 in numbers:
                numbers.remove(r3c4)
            if r3c5 in numbers:
                numbers.remove(r3c5)
            random_index = random.randint(0, len(numbers) - 1)
            r3c6 = numbers[random_index]
            column6.append(r3c6)
            row3.append(r3c6)

            box2 = []
            box2.append(r3c4)
            box2.append(r3c5)
            box2.append(r3c6)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in range(0,4):
                numbers.remove(column4[i])
            random_index = random.randint(0, len(numbers) - 1)
            r7c4 = numbers[random_index]
            column4.append(r7c4)
            row7.append(r7c4)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in range(0,4):
                numbers.remove(column5[i])
            if r7c4 in numbers:
                numbers.remove(r7c4)
            random_index = random.randint(0, len(numbers) - 1)
            r7c5 = numbers[random_index]
            column5.append(r7c5)
            row7.append(r7c5)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in range(0,4):
                numbers.remove(column6[i])
            if r7c4 in numbers:
                numbers.remove(r7c4)
            if r7c5 in numbers:
                numbers.remove(r7c5)
            random_index = random.randint(0, len(numbers) - 1)
            r7c6 = numbers[random_index]
            column6.append(r7c6)
            row7.append(r7c6)

            box8 = []
            box8.append(r7c4)
            box8.append(r7c5)
            box8.append(r7c6)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in column4:
                numbers.remove(i)
            for i in box2:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r2c4 = numbers[random_index]
            column4.append(r2c4)
            box2.append(r2c4)
            row2.append(r2c4)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in column5:
                numbers.remove(i)
            for i in box2:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r2c5 = numbers[random_index]
            column5.append(r2c5)
            box2.append(r2c5)
            row2.append(r2c5)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in column6:
                numbers.remove(i)
            for i in box2:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r2c6 = numbers[random_index]
            column6.append(r2c6)
            box2.append(r2c6)
            row2.append(r2c6)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in column4:
                numbers.remove(i)
            for i in box8:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r8c4 = numbers[random_index]
            column4.append(r8c4)
            box8.append(r8c4)
            row8.append(r8c4)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in column5:
                numbers.remove(i)
            for i in box8:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r8c5 = numbers[random_index]
            column5.append(r8c5)
            box8.append(r8c5)
            row8.append(r8c5)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in column6:
                numbers.remove(i)
            for i in box8:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r8c6 = numbers[random_index]
            column6.append(r8c6)
            box8.append(r8c6)
            row8.append(r8c6)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in column4:
                numbers.remove(i)
            for i in box2:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r1c4 = numbers[random_index]
            column4.append(r1c4)
            box2.append(r1c4)
            row1.append(r1c4)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in column5:
                numbers.remove(i)
            for i in box2:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r1c5 = numbers[random_index]
            column5.append(r1c5)
            box2.append(r1c5)
            row1.append(r1c5)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in column6:
                numbers.remove(i)
            for i in box2:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r1c6 = numbers[random_index]
            column6.append(r1c6)
            box2.append(r1c6)
            row1.append(r1c6)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in column4:
                numbers.remove(i)
            for i in box8:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r9c4 = numbers[random_index]
            column4.append(r9c4)
            box8.append(r9c4)
            row9.append(r9c4)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in column5:
                numbers.remove(i)
            for i in box8:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r9c5 = numbers[random_index]
            column5.append(r9c5)
            box8.append(r9c5)
            row9.append(r9c5)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in column6:
                numbers.remove(i)
            for i in box8:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r9c6 = numbers[random_index]
            column6.append(r9c6)
            box8.append(r9c6)
            row9.append(r9c6)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row4:
                numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r4c3 = numbers[random_index]
            row4.append(r4c3)
            column3.append(r4c3)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row5:
                numbers.remove(i)
            if r4c3 in numbers:
                numbers.remove(r4c3)
            random_index = random.randint(0, len(numbers) - 1)
            r5c3 = numbers[random_index]
            row5.append(r5c3)
            column3.append(r5c3)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row6:
                numbers.remove(i)
            if r4c3 in numbers:
                numbers.remove(r4c3)
            if r5c3 in numbers:
                numbers.remove(r5c3)
            random_index = random.randint(0, len(numbers) - 1)
            r6c3 = numbers[random_index]
            row6.append(r6c3)
            column3.append(r6c3)

            box4 = []
            box4.append(r4c3)
            box4.append(r5c3)
            box4.append(r6c3)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row4:
                numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r4c7 = numbers[random_index]
            row4.append(r4c7)
            column7.append(r4c7)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row5:
                numbers.remove(i)
            if r4c7 in numbers:
                numbers.remove(r4c7)
            random_index = random.randint(0, len(numbers) - 1)
            r5c7 = numbers[random_index]
            row5.append(r5c7)
            column7.append(r5c7)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row6:
                numbers.remove(i)
            if r4c7 in numbers:
                numbers.remove(r4c7)
            if r5c7 in numbers:
                numbers.remove(r5c7)
            random_index = random.randint(0, len(numbers) - 1)
            r6c7 = numbers[random_index]
            row6.append(r6c7)
            column7.append(r6c7)

            box6 = []
            box6.append(r4c7)
            box6.append(r5c7)
            box6.append(r6c7)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row4:
                numbers.remove(i)
            for i in box4:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r4c2 = numbers[random_index]
            row4.append(r4c2)
            box4.append(r4c2)
            column2.append(r4c2)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row5:
                numbers.remove(i)
            for i in box4:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r5c2 = numbers[random_index]
            row5.append(r5c2)
            box4.append(r5c2)
            column2.append(r5c2)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row6:
                numbers.remove(i)
            for i in box4:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r6c2 = numbers[random_index]
            row6.append(r6c2)
            box4.append(r6c2)
            column2.append(r6c2)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row4:
                numbers.remove(i)
            for i in box6:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r4c8 = numbers[random_index]
            row4.append(r4c8)
            box6.append(r4c8)
            column8.append(r4c8)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row5:
                numbers.remove(i)
            for i in box6:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r5c8 = numbers[random_index]
            row5.append(r5c8)
            box6.append(r5c8)
            column8.append(r5c8)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row6:
                numbers.remove(i)
            for i in box6:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r6c8 = numbers[random_index]
            row6.append(r6c8)
            box6.append(r6c8)
            column8.append(r6c8)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row4:
                numbers.remove(i)
            for i in box4:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r4c1 = numbers[random_index]
            row4.append(r4c1)
            box4.append(r4c1)
            column1.append(r4c1)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row5:
                numbers.remove(i)
            for i in box4:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r5c1 = numbers[random_index]
            row5.append(r5c1)
            box4.append(r5c1)
            column1.append(r5c1)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row6:
                numbers.remove(i)
            for i in box4:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r6c1 = numbers[random_index]
            row6.append(r6c1)
            box4.append(r6c1)
            column1.append(r6c1)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row4:
                numbers.remove(i)
            for i in box6:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r4c9 = numbers[random_index]
            row4.append(r4c9)
            box6.append(r4c9)
            column9.append(r4c9)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row5:
                numbers.remove(i)
            for i in box6:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r5c9 = numbers[random_index]
            row5.append(r5c9)
            box6.append(r5c9)
            column9.append(r5c9)

            numbers = [1,2,3,4,5,6,7,8,9]
            for i in row6:
                numbers.remove(i)
            for i in box6:
                if i in numbers:
                    numbers.remove(i)
            random_index = random.randint(0, len(numbers) - 1)
            r6c9 = numbers[random_index]
            row6.append(r6c9)
            box6.append(r6c9)
            column9.append(r6c9)

            is_fail = False
        
        except ValueError:
            is_fail = True
        
        finally:
            if is_fail == False:
                break

    # print("First Part Success!")

    ######################################################################################
    ######################################################################################
    ########################## HERE IS THE SECOND STEP ###################################
    ######################################################################################
    ######################################################################################

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row1:
        numbers.remove(i)
    for i in column1:
        if i in numbers:
            numbers.remove(i)
    r1c1 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row1:
        numbers.remove(i)
    for i in column2:
        if i in numbers:
            numbers.remove(i)
    r1c2 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row1:
        numbers.remove(i)
    for i in column3:
        if i in numbers:
            numbers.remove(i)
    r1c3 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row1:
        numbers.remove(i)
    for i in column7:
        if i in numbers:
            numbers.remove(i)
    r1c7 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row1:
        numbers.remove(i)
    for i in column8:
        if i in numbers:
            numbers.remove(i)
    r1c8 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row1:
        numbers.remove(i)
    for i in column9:
        if i in numbers:
            numbers.remove(i)
    r1c9 = numbers

    ls_solution = []
    stack = []
    stack_copy = []
    i = 0
    while i < len(r1c1):
        stack.append(r1c1[i])
        j = 0
        while j < len(r1c2):
            stack.append(r1c2[j])
            k = 0
            while k < len(r1c3):
                stack.append(r1c3[k])
                l = 0
                while l < len(r1c7):
                    stack.append(r1c7[l])
                    m = 0
                    while m < len(r1c8):
                        stack.append(r1c8[m])
                        n = 0
                        while n < len(r1c9):
                            stack.append(r1c9[n])
                            stack_copy = list(stack)
                            ls_solution.append(stack_copy)
                            stack = remove(stack)
                            n += 1
                        stack = remove(stack)
                        m += 1
                    stack = remove(stack)
                    l += 1
                stack = remove(stack)
                k += 1
            stack = remove(stack)
            j += 1
        stack = remove(stack)
        i += 1

    new_ls_solution = []
    i = 0
    while i < len(ls_solution):
        if is_set(ls_solution[i]):
            new_ls_solution.append(ls_solution[i])
        i += 1

    idx = 0
    while idx < len(new_ls_solution):

        box1 = []
        box3 = []

        r1c1 = new_ls_solution[idx][0]
        box1.append(r1c1)
        row1.append(r1c1)
        column1.append(r1c1)

        r1c2 = new_ls_solution[idx][1]
        box1.append(r1c2)
        row1.append(r1c2)
        column2.append(r1c2)

        r1c3 = new_ls_solution[idx][2]
        box1.append(r1c3)
        row1.append(r1c3)
        column3.append(r1c3)

        r1c7 = new_ls_solution[idx][3]
        box3.append(r1c7)
        row1.append(r1c7)
        column7.append(r1c7)

        r1c8 = new_ls_solution[idx][4]
        box3.append(r1c8)
        row1.append(r1c8)
        column8.append(r1c8)

        r1c9 = new_ls_solution[idx][5]
        box3.append(r1c9)
        row1.append(r1c9)
        column9.append(r1c9)

        numbers = [1,2,3,4,5,6,7,8,9]
        for i in row2:
            numbers.remove(i)
        for i in column1:
            if i in numbers:
                numbers.remove(i)
        for i in box1:
            if i in numbers:
                numbers.remove(i)
        r2c1 = numbers

        numbers = [1,2,3,4,5,6,7,8,9]
        for i in row2:
            numbers.remove(i)
        for i in column2:
            if i in numbers:
                numbers.remove(i)
        for i in box1:
            if i in numbers:
                numbers.remove(i)
        r2c2 = numbers

        numbers = [1,2,3,4,5,6,7,8,9]
        for i in row2:
            numbers.remove(i)
        for i in column3:
            if i in numbers:
                numbers.remove(i)
        for i in box1:
            if i in numbers:
                numbers.remove(i)
        r2c3 = numbers

        numbers = [1,2,3,4,5,6,7,8,9]
        for i in row2:
            numbers.remove(i)
        for i in column7:
            if i in numbers:
                numbers.remove(i)
        for i in box3:
            if i in numbers:
                numbers.remove(i)
        r2c7 = numbers

        numbers = [1,2,3,4,5,6,7,8,9]
        for i in row2:
            numbers.remove(i)
        for i in column8:
            if i in numbers:
                numbers.remove(i)
        for i in box3:
            if i in numbers:
                numbers.remove(i)
        r2c8 = numbers

        numbers = [1,2,3,4,5,6,7,8,9]
        for i in row2:
            numbers.remove(i)
        for i in column9:
            if i in numbers:
                numbers.remove(i)
        for i in box3:
            if i in numbers:
                numbers.remove(i)
        r2c9 = numbers

        ls_solution = []
        stack = []
        stack_copy = []
        i = 0
        while i < len(r2c1):
            stack.append(r2c1[i])
            j = 0
            while j < len(r2c2):
                stack.append(r2c2[j])
                k = 0
                while k < len(r2c3):
                    stack.append(r2c3[k])
                    l = 0
                    while l < len(r2c7):
                        stack.append(r2c7[l])
                        m = 0
                        while m < len(r2c8):
                            stack.append(r2c8[m])
                            n = 0
                            while n < len(r2c9):
                                stack.append(r2c9[n])
                                stack_copy = list(stack)
                                ls_solution.append(stack_copy)
                                stack = remove(stack)
                                n += 1
                            stack = remove(stack)
                            m += 1
                        stack = remove(stack)
                        l += 1
                    stack = remove(stack)
                    k += 1
                stack = remove(stack)
                j += 1
            stack = remove(stack)
            i += 1

        second_new_ls_solution = []
        i = 0
        while i < len(ls_solution):
            if is_set(ls_solution[i]):
                second_new_ls_solution.append(ls_solution[i])
            i += 1
        
        if len(second_new_ls_solution) == 0:
            idx += 1
            continue

        r2c1 = second_new_ls_solution[0][0]
        box1.append(r2c1)
        row2.append(r2c1)
        column1.append(r2c1)

        r2c2 = second_new_ls_solution[0][1]
        box1.append(r2c2)
        row2.append(r2c2)
        column2.append(r2c2)

        r2c3 = second_new_ls_solution[0][2]
        box1.append(r2c3)
        row2.append(r2c3)
        column3.append(r2c3)

        r2c7 = second_new_ls_solution[0][3]
        box3.append(r2c7)
        row2.append(r2c7)
        column7.append(r2c7)

        r2c8 = second_new_ls_solution[0][4]
        box3.append(r2c8)
        row2.append(r2c8)
        column8.append(r2c8)

        r2c9 = second_new_ls_solution[0][5]
        box3.append(r2c9)
        row2.append(r2c9)
        column9.append(r2c9)

        numbers = [1,2,3,4,5,6,7,8,9]
        for i in row3:
            numbers.remove(i)
        for i in column1:
            if i in numbers:
                numbers.remove(i)
        for i in box1:
            if i in numbers:
                numbers.remove(i)
        r3c1 = numbers

        if len(r3c1) == 0:
            idx += 1
            continue

        numbers = [1,2,3,4,5,6,7,8,9]
        for i in row3:
            numbers.remove(i)
        for i in column2:
            if i in numbers:
                numbers.remove(i)
        for i in box1:
            if i in numbers:
                numbers.remove(i)
        r3c2 = numbers

        if len(r3c2) == 0:
            idx += 1
            continue

        numbers = [1,2,3,4,5,6,7,8,9]
        for i in row3:
            numbers.remove(i)
        for i in column3:
            if i in numbers:
                numbers.remove(i)
        for i in box1:
            if i in numbers:
                numbers.remove(i)
        r3c3 = numbers

        if len(r3c3) == 0:
            idx += 1
            continue

        numbers = [1,2,3,4,5,6,7,8,9]
        for i in row3:
            numbers.remove(i)
        for i in column7:
            if i in numbers:
                numbers.remove(i)
        for i in box3:
            if i in numbers:
                numbers.remove(i)
        r3c7 = numbers

        if len(r3c7) == 0:
            idx += 1
            continue

        numbers = [1,2,3,4,5,6,7,8,9]
        for i in row3:
            numbers.remove(i)
        for i in column8:
            if i in numbers:
                numbers.remove(i)
        for i in box3:
            if i in numbers:
                numbers.remove(i)
        r3c8 = numbers

        if len(r3c8) == 0:
            idx += 1
            continue

        numbers = [1,2,3,4,5,6,7,8,9]
        for i in row3:
            numbers.remove(i)
        for i in column9:
            if i in numbers:
                numbers.remove(i)
        for i in box3:
            if i in numbers:
                numbers.remove(i)
        r3c9 = numbers

        if len(r3c9) == 0:
            idx += 1
            continue

        # only when all ifs are not passed
        break

    if len(r3c1) == 0 or len(r3c2) == 0 or len(r3c3) == 0 or \
        len(r3c7) == 0 or len(r3c8) == 0 or len(r3c9) == 0:
        # print("Second Part Fail!")
        is_fail_new = True
        continue

    # print("Second Part Success!")

    ######################################################################################
    ######################################################################################
    ########################## HERE IS THE THIRD STEP ####################################
    ######################################################################################
    ######################################################################################

    ls_solution = []
    stack = []
    stack_copy = []
    i = 0
    while i < len(r3c1):
        stack.append(r3c1[i])
        j = 0
        while j < len(r3c2):
            stack.append(r3c2[j])
            k = 0
            while k < len(r3c3):
                stack.append(r3c3[k])
                l = 0
                while l < len(r3c7):
                    stack.append(r3c7[l])
                    m = 0
                    while m < len(r3c8):
                        stack.append(r3c8[m])
                        n = 0
                        while n < len(r3c9):
                            stack.append(r3c9[n])
                            stack_copy = list(stack)
                            ls_solution.append(stack_copy)
                            stack = remove(stack)
                            n += 1
                        stack = remove(stack)
                        m += 1
                    stack = remove(stack)
                    l += 1
                stack = remove(stack)
                k += 1
            stack = remove(stack)
            j += 1
        stack = remove(stack)
        i += 1

    third_new_ls_solution = []
    i = 0
    while i < len(ls_solution):
        if is_set(ls_solution[i]):
            third_new_ls_solution.append(ls_solution[i])
        i += 1

    idx = 0
    r3c1 = third_new_ls_solution[idx][0]
    box1.append(r3c1)
    row3.append(r3c1)
    column1.append(r3c1)

    r3c2 = third_new_ls_solution[idx][1]
    box1.append(r3c2)
    row3.append(r3c2)
    column2.append(r3c2)

    r3c3 = third_new_ls_solution[idx][2]
    box1.append(r3c3)
    row3.append(r3c3)
    column3.append(r3c3)

    r3c7 = third_new_ls_solution[idx][3]
    box3.append(r3c7)
    row3.append(r3c7)
    column7.append(r3c7)

    r3c8 = third_new_ls_solution[idx][4]
    box3.append(r3c8)
    row3.append(r3c8)
    column8.append(r3c8)

    r3c9 = third_new_ls_solution[idx][5]
    box3.append(r3c9)
    row3.append(r3c9)
    column9.append(r3c9)

    # print("Third Part Success!")

    ######################################################################################
    ######################################################################################
    ########################## HERE IS THE FOURTH STEP ###################################
    ######################################################################################
    ######################################################################################

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row7:
        numbers.remove(i)
    for i in column1:
        if i in numbers:
            numbers.remove(i)
    r7c1 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row7:
        numbers.remove(i)
    for i in column2:
        if i in numbers:
            numbers.remove(i)
    r7c2 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row7:
        numbers.remove(i)
    for i in column3:
        if i in numbers:
            numbers.remove(i)
    r7c3 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row7:
        numbers.remove(i)
    for i in column7:
        if i in numbers:
            numbers.remove(i)
    r7c7 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row7:
        numbers.remove(i)
    for i in column8:
        if i in numbers:
            numbers.remove(i)
    r7c8 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row7:
        numbers.remove(i)
    for i in column9:
        if i in numbers:
            numbers.remove(i)
    r7c9 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row8:
        numbers.remove(i)
    for i in column1:
        if i in numbers:
            numbers.remove(i)
    r8c1 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row8:
        numbers.remove(i)
    for i in column2:
        if i in numbers:
            numbers.remove(i)
    r8c2 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row8:
        numbers.remove(i)
    for i in column3:
        if i in numbers:
            numbers.remove(i)
    r8c3 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row8:
        numbers.remove(i)
    for i in column7:
        if i in numbers:
            numbers.remove(i)
    r8c7 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row8:
        numbers.remove(i)
    for i in column8:
        if i in numbers:
            numbers.remove(i)
    r8c8 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row8:
        numbers.remove(i)
    for i in column9:
        if i in numbers:
            numbers.remove(i)
    r8c9 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row9:
        numbers.remove(i)
    for i in column1:
        if i in numbers:
            numbers.remove(i)
    r9c1 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row9:
        numbers.remove(i)
    for i in column2:
        if i in numbers:
            numbers.remove(i)
    r9c2 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row9:
        numbers.remove(i)
    for i in column3:
        if i in numbers:
            numbers.remove(i)
    r9c3 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row9:
        numbers.remove(i)
    for i in column7:
        if i in numbers:
            numbers.remove(i)
    r9c7 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row9:
        numbers.remove(i)
    for i in column8:
        if i in numbers:
            numbers.remove(i)
    r9c8 = numbers

    numbers = [1,2,3,4,5,6,7,8,9]
    for i in row9:
        numbers.remove(i)
    for i in column9:
        if i in numbers:
            numbers.remove(i)
    r9c9 = numbers

    if len(r7c1) == 0 or len(r7c2) == 0 or len(r7c3) == 0 or len(r7c7) == 0 or len(r7c8) == 0 or len(r7c9) == 0 or \
        len(r8c1) == 0 or len(r8c2) == 0 or len(r8c3) == 0 or len(r8c7) == 0 or len(r8c8) == 0 or len(r8c9) == 0 or \
        len(r9c1) == 0 or len(r9c2) == 0 or len(r9c3) == 0 or len(r9c7) == 0 or len(r9c8) == 0 or len(r9c9) == 0:
        # print("Fourth Part Fails!")
        is_fail_new = True
        continue

    is_fail_new = False
    # print("Fourth Part Success!")

    ls_solution = []
    stack = []
    stack_copy = []
    i = 0
    while i < len(r7c1):
        stack.append(r7c1[i])
        j = 0
        while j < len(r7c2):
            stack.append(r7c2[j])
            k = 0
            while k < len(r7c3):
                stack.append(r7c3[k])
                l = 0
                while l < len(r8c1):
                    stack.append(r8c1[l])
                    m = 0
                    while m < len(r8c2):
                        stack.append(r8c2[m])
                        n = 0
                        while n < len(r8c3):
                            stack.append(r8c3[n])
                            o = 0
                            while o < len(r9c1):
                                stack.append(r9c1[o])
                                p = 0
                                while p < len(r9c2):
                                    stack.append(r9c2[p])
                                    q = 0
                                    while q < len(r9c3):
                                        stack.append(r9c3[q])
                                        r = 0
                                        while r < len(r7c7):
                                            stack.append(r7c7[r])
                                            s = 0
                                            while s < len(r7c8):
                                                stack.append(r7c8[s])
                                                t = 0
                                                while t < len(r7c9):
                                                    stack.append(r7c9[t])
                                                    u = 0
                                                    while u < len(r8c7):
                                                        stack.append(r8c7[u])
                                                        v = 0
                                                        while v < len(r8c8):
                                                            stack.append(r8c8[v])
                                                            w = 0
                                                            while w < len(r8c9):
                                                                stack.append(r8c9[w])
                                                                x = 0
                                                                while x < len(r9c7):
                                                                    stack.append(r9c7[x])
                                                                    y = 0
                                                                    while y < len(r9c8):
                                                                        stack.append(r9c8[y])
                                                                        z = 0
                                                                        while z < len(r9c9):
                                                                            stack.append(r9c9[z])
                                                                            stack_copy = list(stack)
                                                                            # if check(stack_copy):
                                                                            ls_solution.append(stack_copy)
                                                                            stack = remove(stack)
                                                                            z += 1
                                                                        stack = remove(stack)
                                                                        y += 1
                                                                    stack = remove(stack)
                                                                    x += 1
                                                                stack = remove(stack)
                                                                w += 1
                                                            stack = remove(stack)
                                                            v += 1
                                                        stack = remove(stack)
                                                        u += 1    
                                                    stack = remove(stack)
                                                    t += 1
                                                stack = remove(stack)
                                                s += 1
                                            stack = remove(stack)
                                            r += 1
                                        stack = remove(stack)
                                        q += 1
                                    stack = remove(stack)
                                    p += 1
                                stack = remove(stack)
                                o += 1
                            stack = remove(stack)
                            n += 1
                        stack = remove(stack)
                        m += 1
                    stack = remove(stack)
                    l += 1
                stack = remove(stack)
                k += 1
            stack = remove(stack)
            j += 1
        stack = remove(stack)
        i += 1

    new_ls = []
    idx = 0
    while idx < len(ls_solution):
        if check(ls_solution[idx]):
            new_ls.append(ls_solution[idx])
        idx += 1

    if len(new_ls) == 0:
        # print("Last Part Failed :(")
        is_fail_new = True
        continue

    is_fail_new = False
    # print("Last Part Success!")

    r7c1 = new_ls[0][0]
    r7c2 = new_ls[0][1]
    r7c3 = new_ls[0][2]
    r8c1 = new_ls[0][3]
    r8c2 = new_ls[0][4]
    r8c3 = new_ls[0][5]
    r9c1 = new_ls[0][6]
    r9c2 = new_ls[0][7]
    r9c3 = new_ls[0][8]
    r7c7 = new_ls[0][9]
    r7c8 = new_ls[0][10]
    r7c9 = new_ls[0][11]
    r8c7 = new_ls[0][12]
    r8c8 = new_ls[0][13]
    r8c9 = new_ls[0][14]
    r9c7 = new_ls[0][15]
    r9c8 = new_ls[0][16]
    r9c9 = new_ls[0][17]

# print(f"""
# {r1c1} {r1c2} {r1c3} | {r1c4} {r1c5} {r1c6} | {r1c7} {r1c8} {r1c9}
# {r2c1} {r2c2} {r2c3} | {r2c4} {r2c5} {r2c6} | {r2c7} {r2c8} {r2c9}
# {r3c1} {r3c2} {r3c3} | {r3c4} {r3c5} {r3c6} | {r3c7} {r3c8} {r3c9}
# ------+-------+-------
# {r4c1} {r4c2} {r4c3} | {mid_box[0]} {mid_box[3]} {mid_box[6]} | {r4c7} {r4c8} {r4c9}
# {r5c1} {r5c2} {r5c3} | {mid_box[1]} {mid_box[4]} {mid_box[7]} | {r5c7} {r5c8} {r5c9}
# {r6c1} {r6c2} {r6c3} | {mid_box[2]} {mid_box[5]} {mid_box[8]} | {r6c7} {r6c8} {r6c9}
# ------+-------+-------
# {r7c1} {r7c2} {r7c3} | {r7c4} {r7c5} {r7c6} | {r7c7} {r7c8} {r7c9}
# {r8c1} {r8c2} {r8c3} | {r8c4} {r8c5} {r8c6} | {r8c7} {r8c8} {r8c9}
# {r9c1} {r9c2} {r9c3} | {r9c4} {r9c5} {r9c6} | {r9c7} {r9c8} {r9c9}
# """)