import os

# Check whether index.html exists
assert os.path.exists("index.html"), "index.html does not exist"

# Read the HTML file
with open("index.html", "r", encoding="utf-8") as file:
    html = file.read().lower()

# Required elements
required_elements = [
    "<html",
    "<head",
    "<title",
    "<form",
    'name="name"',
    'name="email"',
    'name="course"',
    'name="roll"',
    "<button"
]

# Check each element
for element in required_elements:
    assert element in html, f"Missing required element: {element}"

print("All HTML tests passed successfully!")