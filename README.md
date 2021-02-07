**Build-LLVM-From-Scratch**
- Hello all llvm developers and fresher who want to learn LLVM.
- This repository will just give a keen idea of what is LLVM and its uses along with buildin process of it.

**About LLVM**
- [LLVM](https://llvm.org/) abbrevation is Low Level Virtual Machine.LLVM is a framework which is used to developed new language and improve existing     one.
- It consist of tools which is helping industry in language creation,creating a compiler, transferring the output code to multiple platforms and           architectures along with generation of architecture-specific optimizations.
- LLVM also consist of libraries, and header files which are used in process of converting binaries in to intermediate representations and converts it     into object files. Tools include an assembler, disassembler, bitcode analyzer, and bitcode optimizer. It also contains basic regression tests.
- The main advatnage of the LLVM project is that it provide a [SSA-based](https://en.wikipedia.org/wiki/Static_single_assignment_form)  (static single     assignment) compilation strategy.

**Building LLVM And Clang**
 - ***In Unix/Linux System***</br>
    - [Click here to see the requirement before initiating](https://llvm.org/docs/GettingStarted.html#requirements)
    - Required pyhton to run test suite. [Click Here](https://www.python.org/downloads/).
    - Build process require CMAKE. [Click Here](https://cmake.org/download/)   </br>
   
 - ***Steps Required***
    - Go to the directory where you want your llvm project to be their.
    - Clone the repository by using  command
            - git clone https://github.com/llvm/llvm-project.git (if git is not their install it by giving command sudo apt-get install git).
            - Now use the following command 
            - cd llvm-project ; mkdir build ; cd build;
            - cmake ../llvm -G -DCMAKE_BUILD_TYPE=RELEASE -DLLVM_TARGET_TO_BUILD="x86"
            - make -j   </br>
            
      Note this will build both llvm and clang both in debug mode.
      
 - ***In Windows***</br>
    - **Requirements**
      - Hardware
        - Any system that can adequately run Visual Studio 2017 is fine. The LLVM source tree and object files, libraries and executables will consume           approximately 3GB.</br>
        
      - Software
      
        - Need Visual Studio, Cmake[Click Here to Download](https://cmake.org/).
        - Required Python [Click Here To Download](https://www.python.org/).(version 3.6 or greater than 3.6)
        - Required [GnuWin32](http://gnuwin32.sourceforge.net/).
        
      - Steps Required
       
       - Get the Source Code
            - With the distributed files:
            - cd <where-you-want-llvm-to-live>
            - gunzip --stdout llvm-VERSION.tar.gz | tar -xvf - (or use WinZip)
            - cd llvm
            - With git access:
                - Note: some regression tests require Unix-style line ending (\n).
                - cd <where-you-want-llvm-to-live>
                - git clone https://github.com/llvm/llvm-project.git llvm
                - cd llvm

                        
        
    
    
      
            
            



