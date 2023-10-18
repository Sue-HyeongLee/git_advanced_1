from typing import List

# Skeleton code for even_list
def even_list(int_list) :
  new_list = []
  for i in int_list:
    if i % 2== 0:
      new_list.append(i)
  return new_list


# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list):
  pass

def main():
  int_list = {1,2,3,4,5,6,7,8,9,10}
  even_int_list = even_list(int_list)
  output = sum_of_squares_of_even(even_int_list)
  print(output)

# Boilerplate code
if __name__ == "__main__":
  main()



