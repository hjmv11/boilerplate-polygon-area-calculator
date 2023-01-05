#import math module to use sqrt
import math

class Rectangle:
  #Rectangle object sets width & height at instantiation
  def __init__(self, width, height):
    self.name = 'Rectangle'
    self.width = width
    self.height = height

  #String output when Rectangle object printed
  def __str__(self):
    output = ''
    output+= self.name + '(width=' + str(self.width) + ', height=' + str(self.height) + ')'
    return output

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perim = self.width * 2 + self.height* 2
    return perim

  def get_diagonal(self):
    diag = math.sqrt(pow(self.width, 2) + pow(self.height, 2))
    return diag

  def get_picture(self):
    output = ''
    #if width or height greater than 50 show message
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    else:
      i = 0
      #height is the number of rows, width is number of asterisks  
      for i in range(0,self.height):
        output += ('*' * self.width) + '\n' 
      return output

  def get_amount_inside(self, shape):
    #floor division to get whole number 
    amount = self.get_area() // shape.get_area()
    return amount 

  

  
  
    



#Square extends Rectangle 
class Square(Rectangle):
  #Square object also sets width & height at instantiation
  def __init__(self, length):
    self.name = 'Square'
    self.width = length
    self.height = length

  def __str__(self):
    output = ''
    output += self.name + '(side=' + str(self.width) + ')'
    return output

  def set_side(self, side):
    self.width = side
    self.height = side
    
  #Sqaure.set_width() different from Rectangle.set_width(), same for height, sets both 
  def set_width(self, width):
    self.width= width
    self.height = width

  def set_height(self, height):
    self.height = height
    self.width = height

  
