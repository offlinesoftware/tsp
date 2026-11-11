import subprocess

class ProcessRunner:
    def run_process(command):
        result = subprocess.run(
            command.split(), 
            capture_output=True, 
            text=True,
            shell=True
        )
        return result