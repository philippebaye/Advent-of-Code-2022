import sys

if "SAMPLE" in sys.argv:
    # interpreted content of day11_input_sample.txt
    MONKEYS_COUNT = 4

    monkeys_items = [[79, 98], [54, 65, 75, 74], [79, 60, 97], [74]]
    monkeys_operations = [lambda x: x * 19, lambda x: x + 6, lambda x: x * x, lambda x: x + 3]

    monkeys_test_divisible = [23, 19, 13, 17]
    throw_to_monkey_when_test_is_true = [2, 2, 1, 0]
    throw_to_monkey_when_test_is_false = [3, 0, 3, 1]
else:
    # interpreted content of day11_sample.txt
    MONKEYS_COUNT = 8

    monkeys_items = [[65, 58, 93, 57, 66], [76, 97, 58, 72, 57, 92, 82], [90, 89, 96], [72, 63, 72, 99], [65], [97, 71], [83, 68, 88, 55, 87, 67], [64, 81, 50, 96, 82, 53, 62, 92]]
    monkeys_operations =  [lambda old: old * 7, lambda old: old + 4, lambda old: old * 5, lambda old: old * old, lambda old: old + 1, lambda old: old + 8, lambda old: old + 2, lambda old: old + 5]

    monkeys_test_divisible = [19, 3, 13, 17, 2, 11, 5, 7]
    throw_to_monkey_when_test_is_true = [6, 7, 5, 0, 6, 7, 2, 3]
    throw_to_monkey_when_test_is_false = [4, 5, 1, 4, 2, 3, 1, 0]


# inspected items realized by each monkey, initialized with 0
monkeys_inspections_count = [ 0 ] * MONKEYS_COUNT


# Important to determine where to throw item is divisible test remainder.
# So, in place of use real value, it's possible to use the remainder result of multiplication of all divisors
# This multiplication can be used as Modulo. Then the items are in a limited range of value, avoiding performance problems
def multiply_elements(elements:[]) -> int:
    result = 1
    for element in elements:
        result *= element
    return result

modulo = multiply_elements(monkeys_test_divisible)


#=============================================
# Monkey do all actions with its current items
#=============================================
def do_monkey_actions(monkey_number:int):
    for old_item in monkeys_items[monkey_number]:
        # an other item inspected by monkey
        monkeys_inspections_count[monkey_number] += 1

        # calculate new item value
        new_item = monkeys_operations[monkey_number](old_item)
        new_item = new_item % modulo

        # throw item to good monkey
        if not (new_item % monkeys_test_divisible[monkey_number]):
            new_monkey_number = throw_to_monkey_when_test_is_true[monkey_number]
        else:
            new_monkey_number = throw_to_monkey_when_test_is_false[monkey_number]
        monkeys_items[new_monkey_number].append(new_item)
        ##print(f"{new_item}->monkey {new_monkey_number}")
    
    monkeys_items[monkey_number] = []


#=============================
# Process all the 10000 rounds
#=============================
ROUNDS = 10_000
for round in range(ROUNDS):
    for monkey_number in range(MONKEYS_COUNT):
        do_monkey_actions(monkey_number)
    ##print(f"monkeys items: {monkeys_items}")

print(f"---------------------------------")
print(f"inspections count for each monkey: {monkeys_inspections_count}")

first, second = sorted(monkeys_inspections_count, reverse=True)[:2]
print(f"monkey business: {first * second}")
