# -*- coding: utf-8 -*-
# =============================================================================
# Project       : Rubik's Cube Analysis
# Module name   : Cube
# File name     : cube.py
# File type     : Python script (Python 3 or higher)
# Purpose       : Cube object definition for the Rubik's Cube Analysis project
# Author        : QuBi (nitrogenium@outlook.fr)
# Creation date : August 8th, 2024
# -----------------------------------------------------------------------------
# Best viewed with space indentation (2 spaces)
# =============================================================================

# =============================================================================
# EXTERNALS
# =============================================================================
import json



# =============================================================================
# CLASS DEFINITION
# =============================================================================
class Cube :
  
  """
  CUBE object
  
  The Cube object is a representation of an arbitrary sized Rubik's Cube.
  It implements:
  - a state variable representing the current state of the cube
  - move methods reproducing the legal moves


  """

  def __init__(self, size = 3) :
    self.size = size
    self.state = [n for n in range(1, (6*size*size)+1)]   # State variable following the convention in '/resources/numbering__SxS.drawio'

    self._loadMoveDescriptor()




  # ---------------------------------------------------------------------------
  # METHOD: Cube._loadMoveDescriptor()                                [PRIVATE]
  # ---------------------------------------------------------------------------
  def _loadMoveDescriptor(self) -> None :
    """
    Loads the JSON file that describes how all faces are affected by each move
    on the Rubik's Cube.

    It is much clearer to have this info stored in a separate file as it would
    make the code very messy for bigger sizes.
    """
    
    moveDescriptorFile = f"./src/moveDescriptor__{self.size}x{self.size}.json"

    with open(moveDescriptorFile, "r") as fileHandler :
      self.moveDescriptor = json.load(fileHandler)



  # ---------------------------------------------------------------------------
  # METHOD: Cube.move()
  # ---------------------------------------------------------------------------
  def move(self, sequence: str) -> None :
    """
    Performs the sequence of moves described in the 'sequence' string.
    """
    
    if (self.size == 2) :
      for s in sequence :
        if (s == "R") :
          tmp = self.state[0]
          self.state[0] = self.state[1]
          self.state[1] = self.state[2]
          self.state[2] = self.state[3]
          self.state[3] = tmp

          tmp = self.state[0]
          self.state[0] = self.state[1]
          self.state[1] = self.state[2]
          self.state[2] = self.state[3]
          self.state[3] = tmp


    else :
      print("[ERROR] This size is not supported.")



  # ---------------------------------------------------------------------------
  # METHOD: Cube.shuffle()
  # ---------------------------------------------------------------------------
  def shuffle(self) :
    """
    Shuffles the Rubik's Cube using a random combination of legal moves.
    """
    
    print("[ERROR] The shuffle function is not supported.")



  # ---------------------------------------------------------------------------
  # METHOD: Cube._circShift()
  # ---------------------------------------------------------------------------
  def _circShift(self, ) :
    """
    TODO
    """

    pass




# =============================================================================
# UNIT TESTS
# =============================================================================
if (__name__ == "__main__") :
  
  C = Cube(2)


