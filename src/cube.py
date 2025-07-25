# -*- coding: utf-8 -*-
# =============================================================================
# Project       : Rubik's Cube Analysis
# Module name   : Cube
# File name     : cube.py
# File type     : Python script (Python 3.9 or higher)
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

    Notation specification follows the one described here: https://kewbz.co.uk/
    which can go up to Rubik's Cubes of size 7x7:
    
    SIMPLE MOVES (2x2 and above)
    - F / F'
    - R / R'
    - U / U'
    - B / B'
    - L / L'
    - D / D'
    
    DOUBLE SLICE MOVES (4x4 and above)
    - Fw / Fw'
    - Rw / Rw'

    TRIPLE SLICE MOVES (5x5 and above)
    - 3Fw / 3Fw'
    - 3Rw / 3Rw'
    - ...

    Note: most of the moves above can be doubled:
    - F2
    - Fw2
    - 3Fw2
    - 4Fw2
    - ...

    However, the counter-clockwise version cannot be doubled (not necessary)

    For readability, the sequence can be separated using whitespaces:
    - move("F U' L2")
    
    See: 
    - https://kewbz.co.uk/en-fr/blogs/notations-1/5x5-notation
    - https://kewbz.co.uk/en-fr/blogs/notations-1/6x6-notation
    - https://kewbz.co.uk/en-fr/blogs/notations-1/7x7-notations
    """
    
    seq = self._moveParser(sequence)

    for moveId in sequence :
      for subMove in self.moveDescriptor[moveId]["perm"] :
        pass



  # ---------------------------------------------------------------------------
  # METHOD: Cube._moveParser()
  # ---------------------------------------------------------------------------
  def _moveParser(self, sequence: str) -> list[str] :
    """
    Performs the sequence of moves described in the 'sequence' string.
    """

    




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
  
  print("[INFO] Library 'cube.py' called as main: running unit tests...")

  assert(cpu._asmReaderConsumeSpace("nop")      == "nop")
  assert(cpu._asmReaderConsumeSpace(" nop")     == "nop")
  assert(cpu._asmReaderConsumeSpace(" nop  ")   == "nop  ")
  assert(cpu._asmReaderConsumeSpace(" ,123 ")   == ",123 ")
  assert(cpu._asmReaderConsumeSpace("  ;456  ") == ";456  ")
  print("- Unit test passed: 'cpu._asmReaderConsumeSpace()'")



  C = Cube(2)
  C.move("LRUL'R'")

