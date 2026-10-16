
with open("missing_records.txt") as f:  # Intentional missing-file error.
    content = f.read()
    print(content)
