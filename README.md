# Control interface for ODMR and Rabi experiments

**Description:** This project is for study the quantum information present in NV defects with ODMR and Rabi pulses experiments.

**Machines used:**
+ Pulse Streamer 8/2 : https://www.swabianinstruments.com/pulse-streamer-8-2/
+ Moku Pro : https://www.liquidinstruments.com/products/hardware-platforms/mokupro/
+ Rohde & Schwarz SMB100A : 
    + Pycharm plugin : https://rohde-schwarz.github.io/RsSmbv_PythonDocumentation/getting_started.html
    + Python API : https://rsicpycharmplugin.readthedocs.io/en/latest/ 

# How to use

**Install conda on Linux**

    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    rm -rf ~/miniconda3/miniconda.sh

**[Install conda on Window](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)**

1. Download the miniconda installer: https://docs.conda.io/projects/miniconda/en/latest/

2. [Verify your installer hashes.](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#hash-verification) (Optional)

3. Double-click the .exe file and follow the instructions on the screen.

4. Add conda to env var with following code

        # à faire

5. Test conda installation

        conda list

**Install RsVISA (this module is for dectecting R&S instruments) :** 

+ [doc](https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/dl_application/application_notes/1dc02___rs_v/1DC02_2e_RS_VISA.pdf)
+ [Downloading page](https://www.rohde-schwarz.com/fr/applications/r-s-visa-note-d-application_56280-148812.html)

**Pull project**

    git clone https://github.com/vuthanhtung2412/ODMR-FOTON.git
    cd ODMR-FOTON

**Set up conda env**

    conda env create --name <ur-env-name> --file environment.yml

**Run the program**

    python main.py

# Demos

**First version**
![](demos/demos_basic.png)

**ODMR & Rabi version**

# Explain file structure

# Futures works:

Error handling non found machine 

Load frequency list to Rohde & Schwarz SMB100A 

Ensure every thing is loaded before execution

Moku integration

Rohde & Schwarz SMB100A List mode (load list of frequency)

Switch frequency when receive signal from the Pulse Streamer