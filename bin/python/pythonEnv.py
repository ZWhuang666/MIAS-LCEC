import os
import subprocess

def find_python_executables():
    paths = []
    
    # 查找系统路径中的所有Python环境
    try:
        if os.name == 'nt':  # Windows
            result = subprocess.run(['where', 'python'], capture_output=True, text=True)
        else:  # Unix/Linux/MacOS
            result = subprocess.run(['which', '-a', 'python'], capture_output=True, text=True)
        
        if result.returncode == 0:
            paths.extend(result.stdout.splitlines())
    except Exception as e:
        print(f"Error finding system Python: {e}")

    # 查找Anaconda/Miniconda环境中的Python
    try:
        result = subprocess.run(['conda', 'env', 'list'], capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.splitlines()
            for line in lines:
                if line.startswith('#'):
                    continue
                parts = line.split()
                if len(parts) > 1 and os.path.exists(parts[-1]):
                    python_path = os.path.join(parts[-1], 'bin', 'python' if os.name != 'nt' else 'python.exe')
                    if os.path.exists(python_path):
                        paths.append(python_path)
    except Exception as e:
        print(f"Error finding conda environments: {e}")

    return paths

def write_paths_to_file(paths, file_path):
    try:
        with open(file_path, 'w') as f:
            for path in paths:
                f.write(path + '\n')
        print(f"Paths written to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    python_paths = find_python_executables()
    if python_paths:
        write_paths_to_file(python_paths, 'python_paths.txt')
    else:
        print("No Python executables found.")
