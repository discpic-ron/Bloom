custom_extension = ".bl"
file_name = "" + custom_extension

def create_file(data):
  try:
    with open(file_name, 'w') as custom_file:
        custom_file.write(data)
    print(f"File '{file_name}' created successfully with custom format.")
  except IOError as e:
      print(f"An error occurred: {e}")

def read_file():
  try:
      with open(filename, 'r') as custom_file:
          content = custom_file.read()
      print(f"\nContents of '{file_name}':\n{content}")
  except FileNotFoundError:
      print(f"File '{file_name}' not found.")
