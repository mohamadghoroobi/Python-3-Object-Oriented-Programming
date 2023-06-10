input_strings = ["1", "5", "28", "131", "3"]

output_integers = []
for num in input_strings:
    output_integers.append(int(num))

print(output_integers)

output_integers_comp = [int(num) for num in input_strings]

print(output_integers_comp)

output_integers_if = [int(num) for num in input_strings if len(num) < 3]

print(output_integers_if)
