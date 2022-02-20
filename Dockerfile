FROM jupyter/scipy-notebook:python-3.8.8

RUN conda install -c conda-forge imbalanced-learn
RUN conda install xgboost
RUN conda install lime
RUN conda install -c conda-forge hyperopt
RUN conda install graphviz

ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"

WORKDIR /home/jovyan/work
