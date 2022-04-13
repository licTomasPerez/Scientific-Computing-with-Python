### We start by defining the rectangle class alongside its nested methods, which all instances of said class will inherit.
class Rectangle: 
  ### All rectangles are uniquely defined by a width and a height. Then, a method for defining a rectangle is going to take these attributes.
  def __init__(self, w,h): 
    self.width = w
    self.height = h
  
  ### Next we define the set_width and set_height methods. With these methods, the user can adjust the rectangle's dimensions.
  def set_width(self, x):
    self.width = x

  def set_height(self, x):
    self.height = x

  ### Next we define the get_perimeter, get_perimeter and get_diagonal. With these methods defined, the user can garner knowledge and access to information about the rectangle.
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  
  ### Now we get to work with the get_picture method. Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.". So we'll have to introduce some control cutoffs.  
  picture = "Too big for picture."
  def get_picture(self):
    if self.width < 50 and self.height < 50:
      draw_width = "*" * self.width
      picture = (draw_width + "\n") * self.height
    return picture
  
  ### Onwards to the get_amount_inside method. Here we take another shape (square or rectangle) as an argument and return the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

  def get_amount_inside(self, rectangle):
    if (self.width < rectangle.width or self.height < rectangle.height):
      return 0
    width_mult = int(self.width / rectangle.width)
    height_mult = int(self.height / rectangle.height)

    return width_mult * height_mult

  def __repr__(self):
   return f"Rectangle(width={self.width}, height={self.height})"
    
class Square(Rectangle):
  ### All squares are rectangles. So an instance of an square will also be an instance of a rectangle. We need to make explicit this classes hierarchy.

  def __init__(self, side):
    super().__init__(side, side) ## with this super() we make explicit the hierarchies. 

  ## Now the rectangle will be characterized by a unique user-input number
  def set_side(self, x):
    self.width = x
    self.height = x
  def set_width(self, x):
    self.set_side(x)
  def set_height(self, x):
    self.set_side(x)

  def __repr__(self):
    return f"Square(side={self.width})"