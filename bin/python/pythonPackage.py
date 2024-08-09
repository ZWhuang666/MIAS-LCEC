import os
import subprocess
import sys
import site

def find_python_site_packages():
    paths = []

    # 查找系统路径中的所有Python环境
    try:
        if os.name == 'nt':  # Windows
            result = subprocess.run(['where', 'python'], capture_output=True, text=True)
        else:  # Unix/Linux/MacOS
            result = subprocess.run(['which', '-a', 'python'], capture_output=True, text=True)
        
        if result.returncode == 0:
            python_executables = result.stdout.splitlines()
            for python in python_executables:
                try:
                    result = subprocess.run([python, '-c', 'import site; print(site.getsitepackages())'], capture_output=True, text=True)
                    if result.returncode == 0:
                        site_packages_paths = eval(result.stdout.strip())
                        paths.extend(site_packages_paths)
                except Exception as e:
                    print(f"Error finding site-packages for {python}: {e}")
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
                        try:
                            result = subprocess.run([python_path, '-c', 'import site; print(site.getsitepackages())'], capture_output=True, text=True)
                            if result.returncode == 0:
                                site_packages_paths = eval(result.stdout.strip())
                                paths.extend(site_packages_paths)
                        except Exception as e:
                            print(f"Error finding site-packages for {python_path}: {e}")
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
    site_packages_paths = find_python_site_packages()
    if site_packages_paths:
        write_paths_to_file(site_packages_paths, 'site_packages_paths.txt')
    else:
        print("No site-packages directories found.")
