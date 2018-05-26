# -----------------------------------------------------------------------------
# File          :main.py
#
# Author        :Sreenidhin C C.
# Date          :6-June-2018.
# Description   :Dynamic  Binder Implementation using python PLY package
#                (Build and Parse codes)
# -----------------------------------------------------------------------------

#       -------------------------- Imports  ---------------------------

from dynamicbinder.parser import build_parser
from data import *

#     ----------------Function to pass args to Parser  ----------------
def get_parser(*args):
  for arg in args:
    s = arg
    result = parser.parse(s)
    print(result)



parser = build_parser()

get_parser(operation_A, operation_B, operation_C, operation_D)

#      ------------------------------ End  -----------------------------
