'''
11st December, 2022
'''

from math import prod

def main():
   with open("input.txt") as f:
      ls = f.read().split("\n\n")

   monkeys = {}
   modulo = 1
   for element in ls:
      line = element.split("\n")
      curr_monkey = {}
      for word in line:
         word = word.strip()
         if word.startswith("Monkey"):
            monkey_id = int(word.split(" ")[1][:-1])
         elif word.startswith("Starting items:"):
            curr_monkey["items"] = [int(x) for x in word.split(":")[1].split(",")]
         elif word.startswith("Operation:"):
            curr_monkey["operation"] = word.split(":")[1].strip()
         elif word.startswith("Test:"):
            curr_monkey["test"] = int(word.split(" ")[3].strip())
         elif word.startswith("If true:"):
            curr_monkey["true_target"] = int(word.split(" ")[5].strip())
         elif word.startswith("If false:"):
            curr_monkey["false_target"] = int(word.split(" ")[5].strip())
      curr_monkey["inspections"] = 0
      modulo *= curr_monkey["test"]
      monkeys[monkey_id] = curr_monkey

   for i in range(10000):
      for monkey_id, monkey in monkeys.items():
         items = monkey["items"]
         monkey["items"] = []
         for item in items:
            old_value = item
            operation = monkey["operation"].replace("old", str(old_value))
            if '=' in operation:
               expression = operation.split('=')[1].strip()
            else:
               expression = operation.strip()
            new_value = eval(expression) % modulo
            if new_value % monkey["test"] == 0:
               target_monkey = monkey["true_target"]
            else:
               target_monkey = monkey["false_target"]
            monkeys[target_monkey]["items"].append(new_value)
            monkey["inspections"] += 1

   max_inspections = sorted([monkey["inspections"] for monkey in monkeys.values()], reverse=True)
   result = max_inspections[0] * max_inspections[1]
   print(f"Result: {result}")

if __name__ == "__main__":
    main()