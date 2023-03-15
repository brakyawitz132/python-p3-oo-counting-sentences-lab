#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value

  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")
  
  value = property(get_value, set_value)

  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")

  def is_exclamation(self):
    return self.value.endswith("!")

  def count_sentences(self):
    no_q = self.value.replace("?", ".")
    only_period = no_q.replace("!", ".")
    return len([i for i in only_period.split(".") if i])
