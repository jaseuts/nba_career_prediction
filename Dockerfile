FROM jupyter/scipy-notebook:python-3.8.8

RUN conda install -c conda-forge imbalanced-learn

ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"

WORKDIR /home/jovyan/work
<<<<<<< HEAD




>>>>>>> a15a054 (jason trained  default logistic regression with SOMTE oversampled data)
=======
>>>>>>> 05a0cfa (jason tidied up the project folder)
