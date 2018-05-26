# -----------------------------------------------------------------------------
# File          :data.py
#
# Author        :Sreenidhin C C.
# Date          :6-June-2018.
# Description   :Inputs to be given to the parser/Lexer.
# -----------------------------------------------------------------------------

# ######################### Dictionary of Variables  ##########################
data = {
    "a": "5",
	"b": "6",
	"name": "test",
	"c": {"v_a": [ { "el": 1 }, { "el": 2 },] },
	"value": "a",
	"list": ["a", "b", "c"]
}


# ###################### Input Code strings for Parser  #######################

operation_A = "if (@a > @b) return 1 else if (@a < @b) return 2 else return 3"

operation_B = "if (@c.v_a[1] == 2) return 1 else return 2"

operation_C = "if (@name in @list) return 1 else return 2"

operation_D = "if (@name == 'test') return 1 else return 2"
