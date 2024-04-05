from main import main

def test_same_lines(tmp_path, file1, file2):
    same_file = tmp_path / "same.txt"
    diff_file = tmp_path / "diff.txt"

    main(file1, file2)

    with open(same_file, 'r') as file:
        same_lines = set(file.readlines())
    with open(diff_file, 'r') as file:
        diff_lines = set(file.readlines())

    assert same_lines == {"line2\n", "line3\n"}
    assert diff_lines == {"line1\n", "line4\n"}
