FROM jupyter/scipy-notebook:python-3.8.8

WORKDIR /home/jovyan/work

ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"
