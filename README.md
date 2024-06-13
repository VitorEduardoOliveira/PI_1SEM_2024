# Alimenta Ação


Projeto Integrador do 3º semestre da FATEC Araras

# Objetivo 
O projeto consiste no desenvolvimento de um site de doação para Instituições, onde o usuario acessará e terá contato com as ONGs cadastradas e poderá ajudar doando quantias monetárias.

## Tecnologias utilizadas

Esse projeto foi desenvolvido com as seguintes ferramentas:

<div><img height="50em" align="center"style="padding:15px;"
  <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/></a> 
  <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/></a> 
  <a href="https://www.mongodb.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg" alt="mongodb" width="40" height="40"/></a> 
  <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a> 
  <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/></a>



## Documentos
[Documentação](https://github.com/VitorEduardoOliveira/PI_1SEM_2024/tree/main/Documenta%C3%A7%C3%A3o/Documentação_P.I_1_SEM_2024.pdf)

## Para rodar esse projeto você precisa realizar a seguinte instrução
No ambiente Linux:
```console
git clone https://github.com/VitorEduardoOliveira/PI_1SEM_2024.git
cd Alimenta-Ação/
cd Projeto_AlimentaAcao/
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py test
pip install coverage
coverage run --source='.' manage.py test
coverage html
python manage.py runserver
```
No ambiente Windows:
```console
git clone https://github.com/VitorEduardoOliveira/PI_1SEM_2024.git
cd Alimenta-Ação/
cd Projeto_AlimentaAcao/
python -m venv env
cd env
cd Scripts
activate.bat
cd ..
cd ..
pip install -r requirements.txt
cd Alimenta-Ação/
cd Projeto_AlimentaAcao/
python manage.py migrate
python manage.py test
pip install coverage
coverage run --source='.' manage.py test 
coverage html
python manage.py runserver
```

## Integrantes do Projeto
- [Miran Romeiro](https://github.com/miranromeiro)
- [Thiago Cesar Alvarez ](https://github.com/Alvarez-T)
- [Vitor Eduardo de Oliveira](https://github.com/VitorEduardoOliveira)
- [Wesley Gustavo Kilian](https://github.com/WesleyGustavoKilian)
- [William Fonseca Geralde](https://github.com/William-Fonseca-Geralde)
