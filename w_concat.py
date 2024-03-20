import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

all_words = []
with open(input_file, 'r') as file:
    for line in file:
        word = line.split(" ")
        all_words.append(word)

with open(input_file, 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines if line.strip()]

print(all_words)
print("\n")

full_words = []
new_word = ''
last_word = ''
start_times = []
end_times = []

for item in all_words:
    if len(item) == 5:
        start = item[0]
        end = item[2]
        separator = item[1]
        start_times.append(start)
        end_times.append(end)

        full_words.append(item[-1].strip())
        new_word = item[-1].strip()

    if len(item) == 4:
        end = item[2]
        end_times.pop()
        end_times.append(end)

        full_words.pop()
        last_word = item[-1].strip()
        new_word += last_word
        full_words.append(new_word)

print(start_times)
print(end_times)
print(full_words)

output_lines = []

for item1, item2, item3 in zip(start_times, end_times, full_words):
    output_lines.append(f"{item1} {separator} {item2} {item3}\n")

with open(output_file, 'w') as output_file:
    output_file.writelines(output_lines)

with open("full_words", "w") as file:
    for word in full_words:
        file.write(word + "\n")
