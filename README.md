# MicroInfo Team code event

You made it. Your setup is complete. Congrats. 

Make sure your python version is > 3. Better would be > 3.6


## Getting started 

```
# lets collect all code we run to get the repro running

# thats what I already ran
mkdir MicroInfoTeam_code
cd MicroInfoTeam_code
git init

# if we want to do testing, this could help
pip install pytest

# setting up some nice pre-commit hooks, so the code never gets dirty
pip install pre-commit
pip install black

wget https://raw.githubusercontent.com/Finn-Lab/EukCC/master/.flake8
wget https://raw.githubusercontent.com/Finn-Lab/EukCC/master/.pre-commit-config.yaml
wget https://raw.githubusercontent.com/Finn-Lab/EukCC/master/pyproject.toml

pre-commit install
```