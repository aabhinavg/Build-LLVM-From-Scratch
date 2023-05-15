import subprocess
import shutil
import sys

# Check if a command is available
def is_command_available(command):
    return shutil.which(command) is not None

# Install required packages using pip
def install_packages(packages):
    subprocess.check_call([sys.executable, "-m", "pip", "install", *packages])

# Check and install required dependencies
def check_and_install_dependencies():
    print(f"Checking Dependencies")
    dependencies = ['git', 'cmake']

    missing_dependencies = [dep for dep in dependencies if not is_command_available(dep)]

    if missing_dependencies:
        print(f"Missing dependencies: {', '.join(missing_dependencies)}")
        install_packages(['git', 'cmake'])

# Step 1: Check and install dependencies
check_and_install_dependencies()

# Step 2: Clone LLVM Source Code
subprocess.run(['git', 'clone', 'https://github.com/llvm/llvm-project.git'])

# Step 3: Prepare the Build Directory
subprocess.run(['mkdir', 'llvm-build'])
subprocess.run(['cd', 'llvm-build'])

# Step 4: Run CMake (your architecture mine is mac that's why macOS M1-specific configuration)
subprocess.run(['cmake', '-G', 'Unix Makefiles','-DCMAKE_BUILD_TYPE=Release', '-DLLVM_ENABLE_PROJECTS=clang', '-DLLVM_TARGETS_TO_BUILD=AArch64', '-DCMAKE_OSX_ARCHITECTURES=arm64', 'llvm-project/llvm'])

# Step 5: Build LLVM
subprocess.run(['cmake', '--build', '.'])

# Step 6: Verify the Build
try:
    version = subprocess.check_output(['./bin/llvm-config', '--version'])
    print(f"LLVM Version: {version.decode('utf-8').strip()}")
except subprocess.CalledProcessError:
    print("LLVM build failed.")

