'''
Test cases for the formatted_output module.
'''
import formatted_output

def test_first_line(capsys):

    
    # go about using input() like you normally would:
    formatted_output.formatted_output()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    for i in range(len(all_outputs)):
        match i:
            case 0:
                assert '  NO PARKING' in all_outputs[i], "The first line should include two spaces and all capital letters"
            case 1:
                assert '2:00 - 6:00 a.m.' in all_outputs[i], "The second line should be formatted correctly"

