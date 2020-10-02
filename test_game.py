from game import check_input, update_hidden_word
import pytest

@pytest.mark.parametrize("args, expected_result", [
   (("A", "BBBBBB"), (False)),
   (("A", "AAAAAA"), (True))
])
def test_check_input(args, expected_result):
   result = check_input(*args)
   assert result == expected_result
   