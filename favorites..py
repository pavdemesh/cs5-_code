import csv

# For counting favorites
counts = {}

# Open CSV file
with open("Favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over CSV file
    for row in reader:
        # print(row["genres"])

        # Force title to lowercase
        title = row["title"].lower()

        # Add title to counts
        # if title in counts:
        #     counts[title] += 1
        # else:
        #     counts[title] = 1
        counts[title] = counts.get(title, 0) + 1
# Print counts

# x = sorted(counts.items())
# print(type(x))

for title, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
    print(title, count, sep=" | ")
