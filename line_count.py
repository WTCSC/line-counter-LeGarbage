def line_count():
  #Opens file
  file = open("file.txt", "r")
  #Splits the file into a list of individual lines, then returns the length of that list
  num_lines = len(file.readlines())
  #Closes the file
  file.close()
  return num_lines