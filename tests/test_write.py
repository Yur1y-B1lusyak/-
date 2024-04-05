import os
import pytest
from main import write_file

@pytest.mark.parametrize('lines, expected', [
    ({'line1\n', 'line2\n', 'line3\n'}, ['line1\n', 'line2\n', 'line3\n']),
    ({'line2\n', 'line3\n', 'line4\n'}, ['line2\n', 'line3\n', 'line4\n']),
])

def test_write_file(tmp_path, lines, expected):
    file_path = tmp_path / 'test_file.txt'
    write_file(file_path, lines)
    with open(file_path, 'r') as file:
        assert file.readlines() == expected