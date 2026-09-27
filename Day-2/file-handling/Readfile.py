""" with open("text.txt", "r") as text_file:
  content = text_file.read()
  print(content)  """

with open("React.txt", "r") as text_file:
  for line in text_file:
    print(line.strip())



