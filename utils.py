from pydantic import BaseModel

class Test_Tool(BaseModel):
  nr_1: float = 0
  nr_2: float = 0

  # First test function

  def add_numbers(self):

    nr_1 = self.nr_1
    nr_2 = self.nr_2

    new_nr = nr_1 + nr_2

    return new_nr
