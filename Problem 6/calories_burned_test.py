'''
Test cases for the formated output module.
'''
import calories_burned


'''
If students get weird os erros, they need to validate that they are only calling
input() twice in their code.  If they call input() more than twice, then the test case breaks.
'''
def test_eleven( monkeypatch, capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["49", "155","148","60"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    # monkeypatch.setattr('builtins.input', lambda : "2")
    # go about using input() like you normally would:
    calories_burned.calculate_calories_burned()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    assert 'Calories: 736.21 calories' in all_outputs, "The output is not formatted as expected make sure the answer appears in one line as Calories: <answer> calories"

def test_twelve( monkeypatch, capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["25", "130", "120", "45"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    # monkeypatch.setattr('builtins.input', lambda : "2")
    # go about using input() like you normally would:
    calories_burned.calculate_calories_burned()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    assert 'Calories: 349.81 calories' in all_outputs, "The output is not formatted as expected make sure the answer appears in one line as Calories: <answer> calories"
