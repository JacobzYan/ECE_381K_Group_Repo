# Used to automate generating several datasets at once
import subprocess


def run_command(command):
    try:
        # Run the command and capture the output
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

        # Accessing the output
        output = result.stdout.strip()  # Strip to remove any leading/trailing whitespace
        error = result.stderr.strip()

        if output:
            return output
        if error:
            print("Error:")
            print(error)
            return -1

    except subprocess.CalledProcessError as e:
        print(f"Command '{e.cmd}' failed with exit code {e.returncode}.")
        print(f"Error: {e.stderr.strip()}")
        return -1




batch_name = 'Large_'

# -------------------------------------------------------------------
id_filenames = ['train_identity.csv', 'test_identity.csv']
trans_filenames = ['train_identity.csv', 'test_identity.csv']
combined_filenames = ['combined_train.csv', 'combined_test.csv']
formatted_filenames = ['formatted_train.csv', 'formatted_test.csv']




for i in range(2):
    output = run_command(['python', 'Combine_Datasets.py', trans_filenames[i], id_filenames[i], batch_name+combined_filenames[i]])
    if output != -1:
        print('Combination successful')

    output = run_command(['python', 'Fill_Datset_NA.py', batch_name+combined_filenames[i], batch_name+formatted_filenames[i]])
    if output != -1:
        print('Combination successful')

