# PyTorch Installation

## Introduction
In this page, we are about to learn [PyTorch](http://pytorch.org/), a framework for building and training neural networks. **PyTorch** in a lot of ways behaves like the arrays you learned from Numpy. All these arrays in PyTorch, after all, are just tensors. PyTorch takes these tensors and makes it simple to move them to GPUs for the faster processing needed when training neural networks. It also provides a module that automatically calculates gradients (for backpropagation!) and another module specifically for building neural networks. All together, PyTorch ends up being more coherent with Python and the Numpy/Scipy stack compared to TensorFlow and other frameworks.


## Installation instruction
1. Install PyTorch package is simple with **conda**. Open the JupyterLab and start a new **Terminal** (refer to [Anaconda installation instruction](https://monaen.github.io/DHLO-2021Spring/anaconda)).

2. Type <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch</code> in the **Terminal** and press enter.

3. After a while, conda will search for the usable pytorch and some dependent packages for your automatically and list all of them. You only have to check whether Pytorch is included in the list and type <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">y</code> to confirm the installation.

4. 
