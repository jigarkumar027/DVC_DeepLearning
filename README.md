# DVC - DL

## commands -

### create a new env 
```bash
conda create --prefix ./env python==3.8 -y
```

### activate new env
```bash
source activate ./env
```
### create and run requirement.txt
```bash
touch requirements.txt
pip install -r requirement.txt
```
### init git 
```bash
git init
```

### init DVC
```bash
dvc init
```

### create some dir and files 
here i am showing some of the file, rest you can look above in repo
```bash
mkdir -p src/utils config
touch src/__init__.py src/utils/__init__.py params.yaml config/config.yaml setup.py .gitignore
```
