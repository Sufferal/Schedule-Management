import os
from google.cloud import vision_v1p3beta1 as vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

coordinates = []
words = []


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
text = detect_text(image_path)
#print(words)
#print(coordinates)

avg_x_all = []
avg_y_all = []
coords = []

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
    coords.append((avg_x, avg_y))
    #print(f"Average coordinates for {words[i]}: (x: {avg_x}, y: {avg_y})")


# Calculate rows
rows = []
current = 0
avg_y_all.sort()
avg_x_all.sort()

for i in range(len(avg_y_all)):
    isRow = False
    if i == 0:
        current = avg_y_all[i]

    if len(rows) > 0:
        if abs(current - avg_y_all[i]) > 0.5 * current or abs(current - avg_y_all[i]) > 0.5 * rows[0]:
            rows.append(current)
            current = avg_y_all[i]
            continue
    else:
        if abs(current - avg_y_all[i]) > 0.5 * current:
            rows.append(current)
            current = avg_y_all[i]
            continue

    current *= i
    current += avg_y_all[i]
    current /= (i + 1)

print(avg_x_all)
print(avg_y_all)
print(coords)
