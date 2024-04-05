from main import read_file

def test_read_file(file1):
    expected = {'line1\n', 'line2\n', 'line3\n'}
    assert read_file(file1) == expected