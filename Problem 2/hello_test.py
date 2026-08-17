'''
Test cases for the hello module.
'''
import hello 

def test_hello(capsys):
    # go about using input() like you normally would:
    hello.hello_world()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    print(all_outputs)
    assert 'Hello World!' in all_outputs