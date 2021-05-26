from months import Months
from birthday import Birthday
from sweepstakes import Sweepstakes
from family import Family
from my_node import My_Node

if __name__ == '__main__':
  my_months = Months()
  print(len(my_months.months_in_year))
  print(my_months.months_in_year)
  print(my_months.months_in_year[2])

  my_birthday = Birthday()
  print(len(my_birthday.locations))
  print(my_birthday.locations)
  my_birthday.locations.add('Japan')
  my_birthday.locations.add('Africa')
  my_birthday.locations.add('Europe')
  print(my_birthday.locations)
  for destination in my_birthday.locations:
      print(destination)

  my_winner = Sweepstakes()
  my_winner.choosing_winner()

  the_fam = Family()
  print(the_fam.First_Name)

  the_node = My_Node(77)
  the_node.insert(75)
  the_node.insert(60)
  the_node.insert(20)
  the_node.insert(100)
  the_node.PrintTree()
  print(the_node)
