import os

# Create folder
folder = "My_Files"

if not os.path.exists(folder):
    os.mkdir(folder)

# Create 5 files automatically
for i in range(1, 6):

    file_name = f"file_{i}.txt"
    file_path = os.path.join(folder, file_name)

    with open(file_path, "w") as file:
        file.write(f"This is automatically created file {i}")

    print(f"{file_name} created successfully!")

print("All files created successfully!")

