def line_count():
  file = open("file.txt", "r")
  num_lines = len(file.readlines())
  file.close()
  return num_lines