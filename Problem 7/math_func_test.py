'''
Test cases for the formated output module.
'''
import math_func


'''
If students get weird os erros, they need to validate that they are only calling
input() twice in their code.  If they call input() more than twice, then the test case breaks.
'''
def test_thirteen( monkeypatch, capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["5.0","1.5","3.2"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    # monkeypatch.setattr('builtins.input', lambda : "2")
    # go about using input() like you normally would:
    math_func.math_func()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    assert '172.47 361.66 3.50 13.13' in all_outputs, "The output is not formatted as expected make sure the answer appears in one line with one space between each number"

def test_fourteen( monkeypatch, capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["3.7", "-3","5"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    # monkeypatch.setattr('builtins.input', lambda : "2")
    # go about using input() like you normally would:
    math_func.math_func()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    assert '693.44 0.00 6.70 26.33' in all_outputs, "The output is not formatted as expected make sure the answer appears in one line with one space between each number"
