import os
import pytest

@pytest.fixture(autouse=True)
def file1(tmp_path):
    file_path = os.path.join(tmp_path, 'file1.txt')
    with open(file_path, 'w') as file:
        lines = ['line1\n',
                 'line2\n',
                 'line3\n']
        file.writelines(lines)
    return file_path

@pytest.fixture(autouse=True)
def file2(tmp_path):
    file_path = os.path.join(tmp_path, 'file2.txt')
    with open(file_path, 'w') as file:
        lines = ['line2\n',
                 'line3\n',
                 'line4\n']
        file.writelines(lines)
    return file_path