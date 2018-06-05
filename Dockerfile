FROM python
RUN pip install Flask requests statsmodels scipy

COPY api.py ./
CMD ["python","./api.py"]
