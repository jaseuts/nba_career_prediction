FROM jupyter/scipy-notebook:python-3.8.8

RUN conda install -c conda-forge imbalanced-learn

<<<<<<< HEAD
ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"
=======
ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"

WORKDIR /home/jovyan/work




>>>>>>> a15a054 (jason trained  default logistic regression with SOMTE oversampled data)
