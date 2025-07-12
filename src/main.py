# -*- coding: utf-8 -*-
# =============================================================================
# Project       : Rubik's Cube Analysis
# Module name   : -
# File name     : main.py
# File type     : Python script (Python 3 or higher)
# Purpose       : entry point
# Author        : QuBi (nitrogenium@outlook.fr)
# Creation date : Saturday, 26 October 2024
# -----------------------------------------------------------------------------
# Best viewed with space indentation (2 spaces)
# =============================================================================

# =============================================================================
# Description
# =============================================================================
# Notations
#
# ----
# Misc
# ---- 
# 
#



# =============================================================================
# External libs
# =============================================================================
import cube

C = cube.Cube(2)

for n in range(10) :
  print(C.state)
  C.move("R")
  


