# Securing Reset Operations in NISQ Quantum Computers

Code and Supplementary Material

Allen Mi, Shuwen Deng, and Jakub Szefer

September 2022

## How-To-Run

The project is developed under `x86-64` Linux. The system dependencies are as follows:

- `conda`: Anaconda or Miniconda, for managing the appropriate Python virtual environment

To install the Python dependencies, run

```
conda env create -f requirements.yml
```

at the root directory of the folder, followed by

```
conda activate sec-rst
```

to activate the virtual environment.

Navigate to the `credentials/` directory and copy `provider.template.json` as `provider.json`. Enter your IBM Quantum provider details in `provider.json`.

### Project structure

- `credentials/`: template for IBM Quantum provider specifications
- `experiments/`: saved experiment and result checkpoints
- `figures/`: project figures, including figures used in the publication
- `notebooks/`: Jupyter Notebooks containing project source code
- `scripts/`: utility scripts
- `COPYING': A copy of the GPLv3 license
- `README.md`: this Markdown file
- `requirements.yml`: `conda` virtual environment specifications
