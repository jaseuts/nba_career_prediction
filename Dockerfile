FROM jupyter/scipy-notebook:python-3.8.8

RUN conda install -c conda-forge imbalanced-learn

<<<<<<< HEAD
ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"
=======
ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"

WORKDIR /home/jovyan/work




>>>>>>> a15a054ea3b80b4ab0ae7c9e65f3a8131871dd23
