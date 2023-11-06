import subprocess


# Define the command to run the tests
test_command = ["python", "-m", "unittest", "issue1"]
test_issue1_command = ['python', '-m', 'doctest', '-o', 'NORMALIZE_WHITESPACE', '-v', 'issue1.py']
test_issue2_command = list('pytest test_issue2.py'.split())
test_issue3_command = list('python -m unittest test_issue3.py'.split())
test_issue4_command = list('pytest test_issue4.py'.split())
test_commands = [test_issue1_command, test_issue2_command, test_issue3_command, test_issue4_command]
for i, test_command in zip(range(1,5), test_commands):
    process = subprocess.Popen(test_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    if stderr:
        with open(f'result{i}.txt', 'w') as file:
            file.write(f"Test Error: {stderr}")
    else:
        with open(f'result{i}.txt', 'w') as file:
            file.write(f"Test Output:\n{stdout}")
