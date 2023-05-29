import os
def print_docs(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isdir(file_path):
            print("Папка:", filename)
            print_docs(file_path)
        else:
            print("Файл:", filename)
directory = r"C:\Users\ReQZ2JZ\Desktop\disk 2"
print_docs(directory)