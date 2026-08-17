'''
Test cases for the formated output module.
'''
import drive


'''
If students get weird os erros, they need to validate that they are only calling
input() twice in their code.  If they call input() more than twice, then the test case breaks.
'''
def test_six( monkeypatch, capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["25.0", "3.1599"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    # monkeypatch.setattr('builtins.input', lambda : "2")
    # go about using input() like you normally would:
    drive.drive()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    assert '2.53 9.48 63.20' in all_outputs, "The output is not formatted as expected make sure the answer appears in one line with one space between each number"

def test_seven( monkeypatch, capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["30.0", "3.8999"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    # monkeypatch.setattr('builtins.input', lambda : "2")
    # go about using input() like you normally would:
    drive.drive()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    assert '2.60 9.75 65.00' in all_outputs, "The output is not formatted as expected make sure the answer appears in one line with one space between each number"

def test_eight( monkeypatch, capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["15.0", "6.4999"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    # monkeypatch.setattr('builtins.input', lambda : "2")
    # go about using input() like you normally would:
    drive.drive()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    assert '8.67 32.50 216.66' in all_outputs, "The output is not formatted as expected make sure the answer appears in one line with one space between each number"

def test_nine( monkeypatch, capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["45.0", "5.8999"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    # monkeypatch.setattr('builtins.input', lambda : "2")
    # go about using input() like you normally would:
    drive.drive()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    assert '2.62 9.83 65.55' in all_outputs, "The output is not formatted as expected make sure the answer appears in one line with one space between each number"

def test_ten( monkeypatch, capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["37.0", "4.7999"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    # monkeypatch.setattr('builtins.input', lambda : "2")
    # go about using input() like you normally would:
    drive.drive()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    assert '2.59 9.73 64.86' in all_outputs, "The output is not formatted as expected make sure the answer appears in one line with one space between each number"

