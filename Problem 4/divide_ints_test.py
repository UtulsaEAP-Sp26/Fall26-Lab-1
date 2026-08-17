'''
Test cases for the formated output module.
'''
import divide_ints


'''
If students get weird os erros, they need to validate that they are only calling
input() twice in their code.  If they call input() more than twice, then the test case breaks.
'''
def test_three(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["2000", "2"])
    monkeypatch.setattr('builtins.input', lambda : next(inputs, '\n'))
    #monkeypatch.setattr('builtins.input', lambda : "2")
    # go about using input() like you normally would:
    divide_ints.divide_ints()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    assert '1000 500 250' in all_outputs, "The output is not formatted as expected make sure the answer appears in one line with one space between each number"

def test_four(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["100", "4"])
    monkeypatch.setattr('builtins.input', lambda : next(inputs, '\n'))
    #monkeypatch.setattr('builtins.input', lambda : "2")
    # go about using input() like you normally would:
    divide_ints.divide_ints()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    assert '25 6 1' in all_outputs, "The output is not formatted as expected make sure the answer appears in one line with one space between each number"

def test_five(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["8000", "-2"])
    monkeypatch.setattr('builtins.input', lambda : next(inputs, '\n'))
    #monkeypatch.setattr('builtins.input', lambda : "2")
    # go about using input() like you normally would:
    divide_ints.divide_ints()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    assert '-4000 2000 -1000' in all_outputs, "The output is not formatted as expected make sure the answer appears in one line with one space between each number"
    