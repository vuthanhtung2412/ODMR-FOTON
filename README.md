# Control interface for ODMR and Rabi experiments

**Description:** This project is for study the quantum information present in NV defects with ODMR and Rabi pulses experiments.

**Machines used:**
+ Pulse Streamer 8/2 : https://www.swabianinstruments.com/pulse-streamer-8-2/
+ Moku Pro : https://www.liquidinstruments.com/products/hardware-platforms/mokupro/
+ Rohde & Schwarz SMB100A : 
    + Pycharm plugin : https://rohde-schwarz.github.io/RsSmbv_PythonDocumentation/getting_started.html
    + Python API : https://rsicpycharmplugin.readthedocs.io/en/latest/ 

## How to use

**Install conda**

    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    rm -rf ~/miniconda3/miniconda.sh

**Set up conda env**

    conda env create --name <ur-env-name> --file environment.yml

**Run the program**

    python main.py

## Demos

**First version**
![](demos/demos_basic.png)

**ODMR & Rabi version**

## Futures works:

Error handling non found machine 

Load frequency list to Rohde & Schwarz SMB100A 

Ensure every thing is loaded before execution

Moku integration

Rohde & Schwarz SMB100A List mode (load list of frequency)