import copy

MONKEYS_COUNT = 8

monkeys_items = [[65, 58, 93, 57, 66], [76, 97, 58, 72, 57, 92, 82], [90, 89, 96], [72, 63, 72, 99], [65], [97, 71], [83, 68, 88, 55, 87, 67], [64, 81, 50, 96, 82, 53, 62, 92]]
monkeys_operations =  [lambda old: old * 7, lambda old: old + 4, lambda old: old * 5, lambda old: old * old, lambda old: old + 1, lambda old: old + 8, lambda old: old + 2, lambda old: old + 5]

monkeys_test_divisible = [19, 3, 13, 17, 2, 11, 5, 7]
throw_to_monkey_when_test_is_true = [6, 7, 5, 0, 6, 7, 2, 3]
throw_to_monkey_when_test_is_false = [4, 5, 1, 4, 2, 3, 1, 0]

monkeys_inspections_count = [ 0 ] * MONKEYS_COUNT


def multuply_all_element(elements:[]):
    result = 1
    for element in elements:
        result *= element
    return result

modulo = multuply_all_element(monkeys_test_divisible)

def monkey_action(monkey_number:int):
    for old_item in monkeys_items[monkey_number]:
        monkeys_inspections_count[monkey_number] += 1
        new_item = monkeys_operations[monkey_number](old_item)
        #new_item = new_item // 3
        new_item = new_item % modulo
        if not (new_item % monkeys_test_divisible[monkey_number]):
            new_monkey_number = throw_to_monkey_when_test_is_true[monkey_number]
        else:
            new_monkey_number = throw_to_monkey_when_test_is_false[monkey_number]
        monkeys_items[new_monkey_number].append(new_item)
        #print(f"{new_item}->monkey {new_monkey_number}")
    
    monkeys_items[monkey_number] = []


ROUNDS = 10_000
for round in range(ROUNDS):
    for monkey_number in range(MONKEYS_COUNT):
        monkey_action(monkey_number)
    #print(monkeys_items)
    print(f"round: {round}")

print(f"---------------------------------")
print(f"inspections count : {monkeys_inspections_count}")

first, second = sorted(monkeys_inspections_count, reverse=True)[:2]

print(f"multiplication: {first * second}")
# inspections count : [44, 328, 52, 279, 323, 303, 286, 41]
# multiplication: 105944