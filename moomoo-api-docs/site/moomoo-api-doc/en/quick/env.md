



# <a href="#9771" class="header-anchor">#</a> Environment Setup



Notice

Ways of building programming environment are different for different
programming languages.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





## <a href="#4372" class="header-anchor">#</a> Python Environment

### <a href="#5781" class="header-anchor">#</a> Environment Requirement

- Operating system requirements:
  - 32-bit or 64-bit operating system of Windows 7/10
  - 64-bit operating system of Mac 10.11 and above
  - 64-bit operating system of CentOS 7 and above
  - 64-bit operating system of Ubuntu 16.04 and above
- Python version requirements:
  - Python 3.6 or above

### <a href="#4184" class="header-anchor">#</a> Environment Building

#### <a href="#4404" class="header-anchor">#</a> 1. Install Python

To avoid running failures due to environmental problems, we recommend
Python version 3.8.

Download page:
<a href="https://www.python.org/downloads/" target="_blank"
rel="noopener noreferrer">Download Python</a>

Tips

Two methods are provided to switch to a Python 3.8 environment:

- Method 1  
  Add the installation path of Python 3.8 to the environment variable
  path.

- Method 2  
  If you are using PyCharm, you can switch the Project Interpreter to
  specified Python environment in *Settings*.

![pycharm-switch-python](/moomoo-api-doc/assets/img/pycharm-switch-python.ca0405aa.png)

After the installation, execute the following command to see if the
installation is successful:  
`python -V` (Windows) or `python3 -V` (Linux/Mac)

#### <a href="#3184" class="header-anchor">#</a> 2. Install PyCharm (Optional)

We recommend that using
<a href="https://www.jetbrains.com/pycharm/download/" target="_blank"
rel="noopener noreferrer">PyCharm</a> as your Python IDE.

#### <a href="#6927" class="header-anchor">#</a> 3. Install TA-Lib (Optional)

TA-Lib is a functional library widely used in program trading for
technical analysis of market data. It provides a variety of technical
analysis functions to facilitate our quantitative investment.

Installation method: directly use pip installation in cmd  
`$ pip install TA-Lib`



提示

- Installation of TA-Lib is not necessary, you can skip this step











## <a href="#9075" class="header-anchor">#</a> C# Environment

### <a href="#5781-2" class="header-anchor">#</a> Environment Requirement

- Operating system requirements:
  - 32-bit or 64-bit operating system of Windows 7 and above
  - 64-bit operating system of Mac 10.11 and above
  - 64-bit operating system of CentOS 7 and above
  - 64-bit operating system of Ubuntu 16.04 and above
- The official SDK compilation environment is **Visual Studio 2013**
  **+** **.Net Framework 4.5** or **Visual Studio 2017** **+** **.NET
  Core 2.1**.
- If you need a later version of the Visual Studio environment, you can
  upgrade FTAPI4Net.sln, and recompile from the source code.

### <a href="#4184-2" class="header-anchor">#</a> Environment Building

#### <a href="#6305" class="header-anchor">#</a> 1. Install .NET Framework or .NET Core

<a href="https://dotnet.microsoft.com/download/dotnet-framework/"
target="_blank" rel="noopener noreferrer">.NET Framework</a> or
<a href="https://dotnet.microsoft.com/download/dotnet-core"
target="_blank" rel="noopener noreferrer">.NET Core</a>, you can choose one of them to install.

#### <a href="#2488" class="header-anchor">#</a> 2. Install Visual Studio development environment (optional)

We recommend using
<a href="https://visualstudio.microsoft.com/" target="_blank"
rel="noopener noreferrer">Visual Studio</a> as the C \# IDE.





## <a href="#9961" class="header-anchor">#</a> Java Environment

### <a href="#5781-3" class="header-anchor">#</a> Environment Requirement

- Operating system requirements:
  - 32-bit or 64-bit operating system of Windows 7 and above
  - 64-bit operating system of Mac 10.11 and above
  - 64-bit operating system of CentOS 7 and above
  - 64-bit operating system of Ubuntu 16.04 and above
- If you need a later version of JDK, you can set up your own
  compilation environment and recompile from the source code.

### <a href="#4184-3" class="header-anchor">#</a> Environment Building

#### <a href="#1742" class="header-anchor">#</a> 1. Install JDK

We recommend installing *OpenJDK 8*.

#### <a href="#2374" class="header-anchor">#</a> 2. Install IntelliJ IDEA development environment (optional)

We recommend using
<a href="https://www.jetbrains.com/idea/" target="_blank"
rel="noopener noreferrer">IntelliJ IDEA</a> as the Java IDE.





### <a href="#738" class="header-anchor">#</a> C++ Environment

### <a href="#5781-4" class="header-anchor">#</a> Environment Requirement

- Operating system requirements:
  - Windows:
    - 32-bit or 64-bit operating system of Windows 7 and above.
    - the official SDK compilation environment is *Visual Studio 2013*.
      If you need a later version of the VS environment, it is
      recommended upgrading FTAPI.sln.
  - MacOS:
    - 64-bit operating system is required.
    - the official SDK compilation environment is *MacOS Mojave,Xcode
      11*. Other versions need to upgrade the Xcode project file.
  - Linux:
    - 64-bit operating system is required.
    - the official SDK compilation environment is *CentOS 7 (gcc 4.8.5)*
      and *Ubuntu 16.04 (gcc 5.4.0)*.
- unofficial environment:
  - you need to compile the FTAPI and Protobuf with source codes in the
    `/FTAPI4CPP/Src` directory.





## <a href="#6584" class="header-anchor">#</a> JS Environment

### <a href="#5781-5" class="header-anchor">#</a> Environment Requirement

- Operating system requirements:
  - 32-bit or 64-bit operating system of Windows 7 and above
  - 64-bit operating system of Mac 10.11 and above
  - 64-bit operating system of CentOS 7 and above
  - 64-bit operating system of Ubuntu 16.04 and above
- We recommend Chrome 70 and above.

### <a href="#4184-4" class="header-anchor">#</a> Environment building

#### <a href="#4710" class="header-anchor">#</a> 1. Install Node.js

Node.js is an open source, cross-platform JavaScript running environment
based on Chrome kernel. Click
<a href="https://nodejs.org/zh-cn/download/" target="_blank"
rel="noopener noreferrer">here</a> to download.

#### <a href="#3161" class="header-anchor">#</a> 2. Install Visual Studio Code (optional)

We recommend using
<a href="https://code.visualstudio.com/" target="_blank"
rel="noopener noreferrer">Visual Studio Code</a> as the JavaScript IDE.













- Python
- Proto
- C#
- Java
- C++
- JavaScript





## <a href="#4372-2" class="header-anchor">#</a> Python Environment

### <a href="#5781-6" class="header-anchor">#</a> Environment Requirement

- Operating system requirements:
  - 32-bit or 64-bit operating system of Windows 7/10
  - 64-bit operating system of Mac 10.11 and above
  - 64-bit operating system of CentOS 7 and above
  - 64-bit operating system of Ubuntu 16.04 and above
- Python version requirements:
  - Python 3.6 or above

### <a href="#4184-5" class="header-anchor">#</a> Environment Building

#### <a href="#4404-2" class="header-anchor">#</a> 1. Install Python

To avoid running failures due to environmental problems, we recommend
Python version 3.8.

Download page:
<a href="https://www.python.org/downloads/" target="_blank"
rel="noopener noreferrer">Download Python</a>

Tips

Two methods are provided to switch to a Python 3.8 environment:

- Method 1  
  Add the installation path of Python 3.8 to the environment variable
  path.

- Method 2  
  If you are using PyCharm, you can switch the Project Interpreter to
  specified Python environment in *Settings*.

![pycharm-switch-python](/moomoo-api-doc/assets/img/pycharm-switch-python.ca0405aa.png)

After the installation, execute the following command to see if the
installation is successful:  
`python -V` (Windows) or `python3 -V` (Linux/Mac)

#### <a href="#3184-2" class="header-anchor">#</a> 2. Install PyCharm (Optional)

We recommend that using
<a href="https://www.jetbrains.com/pycharm/download/" target="_blank"
rel="noopener noreferrer">PyCharm</a> as your Python IDE.

#### <a href="#6927-2" class="header-anchor">#</a> 3. Install TA-Lib (Optional)

TA-Lib is a functional library widely used in program trading for
technical analysis of market data. It provides a variety of technical
analysis functions to facilitate our quantitative investment.

Installation method: directly use pip installation in cmd  
`$ pip install TA-Lib`



提示

- Installation of TA-Lib is not necessary, you can skip this step











## <a href="#9075-2" class="header-anchor">#</a> C# Environment

### <a href="#5781-7" class="header-anchor">#</a> Environment Requirement

- Operating system requirements:
  - 32-bit or 64-bit operating system of Windows 7 and above
  - 64-bit operating system of Mac 10.11 and above
  - 64-bit operating system of CentOS 7 and above
  - 64-bit operating system of Ubuntu 16.04 and above
- The official SDK compilation environment is **Visual Studio 2013**
  **+** **.Net Framework 4.5** or **Visual Studio 2017** **+** **.NET
  Core 2.1**.
- If you need a later version of the Visual Studio environment, you can
  upgrade MMAPI4Net.sln, and recompile from the source code.

### <a href="#4184-6" class="header-anchor">#</a> Environment Building

#### <a href="#6305-2" class="header-anchor">#</a> 1. Install .NET Framework or .NET Core

<a href="https://dotnet.microsoft.com/download/dotnet-framework/"
target="_blank" rel="noopener noreferrer">.NET Framework</a> or
<a href="https://dotnet.microsoft.com/download/dotnet-core"
target="_blank" rel="noopener noreferrer">.NET Core</a>, you can choose one of them to install.

#### <a href="#2488-2" class="header-anchor">#</a> 2. Install Visual Studio development environment (optional)

We recommend using
<a href="https://visualstudio.microsoft.com/" target="_blank"
rel="noopener noreferrer">Visual Studio</a> as the C \# IDE.





## <a href="#9961-2" class="header-anchor">#</a> Java Environment

### <a href="#5781-8" class="header-anchor">#</a> Environment Requirement

- Operating system requirements:
  - 32-bit or 64-bit operating system of Windows 7 and above
  - 64-bit operating system of Mac 10.11 and above
  - 64-bit operating system of CentOS 7 and above
  - 64-bit operating system of Ubuntu 16.04 and above
- If you need a later version of JDK, you can set up your own
  compilation environment and recompile from the source code.

### <a href="#4184-7" class="header-anchor">#</a> Environment Building

#### <a href="#1742-2" class="header-anchor">#</a> 1. Install JDK

We recommend installing *OpenJDK 8*.

#### <a href="#2374-2" class="header-anchor">#</a> 2. Install IntelliJ IDEA development environment (optional)

We recommend using
<a href="https://www.jetbrains.com/idea/" target="_blank"
rel="noopener noreferrer">IntelliJ IDEA</a> as the Java IDE.





### <a href="#738-2" class="header-anchor">#</a> C++ Environment

### <a href="#5781-9" class="header-anchor">#</a> Environment Requirement

- Operating system requirements:
  - Windows:
    - 32-bit or 64-bit operating system of Windows 7 and above.
    - the official SDK compilation environment is *Visual Studio 2013*.
      If you need a later version of the VS environment, it is
      recommended upgrading MMAPI.sln.
  - MacOS:
    - 64-bit operating system is required.
    - the official SDK compilation environment is *MacOS Mojave,Xcode
      11*. Other versions need to upgrade the Xcode project file.
  - Linux:
    - 64-bit operating system is required.
    - the official SDK compilation environment is *CentOS 7 (gcc 4.8.5)*
      and *Ubuntu 16.04 (gcc 5.4.0)*.
- unofficial environment:
  - you need to compile the MMAPI and Protobuf with source codes in the
    `/MMAPI4CPP/Src` directory.





## <a href="#6584-2" class="header-anchor">#</a> JS Environment

### <a href="#5781-10" class="header-anchor">#</a> Environment Requirement

- Operating system requirements:
  - 32-bit or 64-bit operating system of Windows 7 and above
  - 64-bit operating system of Mac 10.11 and above
  - 64-bit operating system of CentOS 7 and above
  - 64-bit operating system of Ubuntu 16.04 and above
- We recommend Chrome 70 and above.

### <a href="#4184-8" class="header-anchor">#</a> Environment building

#### <a href="#4710-2" class="header-anchor">#</a> 1. Install Node.js

Node.js is an open source, cross-platform JavaScript running environment
based on Chrome kernel. Click
<a href="https://nodejs.org/zh-cn/download/" target="_blank"
rel="noopener noreferrer">here</a> to download.

#### <a href="#3161-2" class="header-anchor">#</a> 2. Install Visual Studio Code (optional)

We recommend using
<a href="https://code.visualstudio.com/" target="_blank"
rel="noopener noreferrer">Visual Studio Code</a> as the JavaScript IDE.















