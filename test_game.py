from game import check_input, update_hidden_word, generate_word
import pytest


class TestGameModules:
   def test_generate_word(self):
      """
      Тест функции генерации слова
      """
      expected_words = [
        "skillfactory", 
        "testing", 
        "blackbox", 
        "pytest", 
        "unittest", 
        "coverage"
        ]
      result = generate_word()
      assert result.lower() in expected_words

   @pytest.mark.parametrize("args, expected_result", [
      (("A", "BBBBBB"), (False)),
      (("A", "AAAAAA"), (True))
      ])
   def test_check_input(self, args, expected_result):
      """
      Тест функции проверки введенной буквы
      """
      result = check_input(*args)
      assert result == expected_result
   
   def test_update_hidden_word(self):
      """
      Тест функции обновления скрытого слова
      """
      result = update_hidden_word("A", "ABBABBA", "_______")
      assert result == "A__A__A"
