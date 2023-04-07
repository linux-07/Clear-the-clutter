import os

files = os.listdir("Clutter")
i = 1
for file in files:
  if file.endswith(".png"):
    os.rename(f"Clutter/{file}", f"Clutter/{i}.png")
    i = i + 1

print("Renamed successfully!")
