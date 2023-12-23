import os
import pandas as pd
from PIL import Image

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

COORDINATE_THRESHOLD = 1

coordinates = []
words = []
word_coord = dict()


def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    texts.pop(0)

    for text in texts:
        vertices = [
            (vertex.x, vertex.y) for vertex in text.bounding_poly.vertices
        ]
        coordinates.append(vertices)
        words.append(text.description)

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    document = response.full_text_annotation

    return document.text

image_path = 'images/test.png'

with Image.open(image_path) as img:
    IMAGE_WIDTH, IMAGE_HEIGHT = img.size

WORD_THRESHOLD = IMAGE_WIDTH * 0.05

text = detect_text(image_path)

avg_x_all = []
avg_y_all = []
avg_coords = []

# Calculate the average coordinates for each word
for i in range(len(words)):
    # Convert coordinates to integers
    x_coordinates = [int(coord[0]) for coord in coordinates[i]]
    y_coordinates = [int(coord[1]) for coord in coordinates[i]]

    # Calculate the average x and y coordinates
    avg_x = sum(x_coordinates) / len(x_coordinates)
    avg_y = sum(y_coordinates) / len(y_coordinates)
    avg_y_all.append(avg_y)
    avg_x_all.append(avg_x)
    avg_coords.append((avg_x, avg_y))

    word_coord[(avg_x, avg_y)] = words[i]

    # print(f"Average coordinates for {words[i]}: (x: {avg_x}, y: {avg_y})")


# Calculate rows
rows = []
current = 0
avg_y_all.sort()
avg_x_all.sort()
sorted_coords = sorted(avg_coords, key=lambda coord: coord[1])
count = 0

for i in range(len(avg_y_all)):
    isRow = False
    if i == 0:
        current = avg_y_all[i]
        count += 1

    if len(rows) > 0:
        if abs(current - avg_y_all[i]) > COORDINATE_THRESHOLD * current or abs(
                current - avg_y_all[i]) > COORDINATE_THRESHOLD * rows[0]:
            rows.append(current)
            current = avg_y_all[i]
            count = 1
            continue
    else:
        if abs(current - avg_y_all[i]) > COORDINATE_THRESHOLD * current:
            rows.append(current)
            current = avg_y_all[i]
            count = 1
            continue

    current *= count
    current += avg_y_all[i]
    count += 1
    current /= count

    if i == len(avg_y_all) - 1:
        rows.append(current)

table = []
# print(sorted_coords)
# print(word_coord)


# Combine words that are close on the x-axis and below the word threshold
# combined_table = []
# current_row = []
# current_x = None
# current_y = None
# previous_x = None
#
# for i in range(len(sorted_coords)):
#     try:
#         coord = sorted_coords[i]
#     except:
#         break
#
#     if i == 0:
#         current_x = coord[0]
#         current_y = coord[1]
#         previous_x = coord[0]
#         continue
#
#     if abs(current_x - coord[0]) <= WORD_THRESHOLD:
#         new_coord = ((current_x + coord[0])/2, (current_y + coord[1])/2)
#         sorted_coords[i] = (new_coord[0], new_coord[1])
#         sorted_coords.pop(i - 1)
#
#         word_coord[new_coord] = word_coord[(current_x, current_y)] + " " + word_coord[coord]
#         word_coord.pop((current_x, current_y))
#
#         previous_x = current_x
#
#     elif abs(previous_x - coord[0]) <= WORD_THRESHOLD:
#         new_coord = ((previous_x + coord[0])/2, (current_y + coord[1])/2)
#         sorted_coords[i] = (new_coord[0], new_coord[1])
#         sorted_coords.pop(i - 1)
#
#         word_coord[new_coord] = word_coord[(current_x, current_y)] + " " + word_coord[coord]
#         word_coord.pop((current_x, current_y))
#
#         previous_x = coord[0]
#
#     current_x = coord[0]
#     current_y = coord[1]
#
# print(sorted_coords)
# print(word_coord)


# Coordinates separation
for i in range(len(rows)):
    for j in range(len(sorted_coords)):
        if abs((sorted_coords[j][1] - rows[i])) > COORDINATE_THRESHOLD * rows[0]:
            table.append(sorted_coords[0:j])
            for z in range(j):
                sorted_coords.pop(0)
            break
        if j == len(sorted_coords) - 1:
            table.append(sorted_coords[0:j + 1])
            sorted_coords = []
            break

for i in range(len(table)):
    table[i].sort(key=lambda coord: coord[0])
    # print(table[i])

sorted_table = dict()

for i in range(len(table)):
    sorted_table[i] = []
    for j in range(len(table[i])):
        sorted_table[i].append(word_coord[table[i][j]])

print(sorted_table)

df = pd.DataFrame.from_dict(sorted_table, orient='index')

# Save the DataFrame to an Excel file
excel_path = 'output.xlsx'
df.to_excel(excel_path, index=False)

print(f"Excel file saved at: {excel_path}")
