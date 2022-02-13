FROM jupyter/scipy-notebook:python-3.8.8

RUN conda install -c conda-forge imbalanced-learn

ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"

WORKDIR /home/jovyan/work




