flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]

# for flowers in flowers:
#     print(flowers)

seperator = " | "
output = seperator.join(flowers)  # All items must be Strings, Ints + Strings do not work
print(output)

print(",".join(flowers))