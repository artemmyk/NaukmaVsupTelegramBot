FROM python:3.10
RUN python -m pip install --upgrade pip
RUN pip install pipenv

COPY ./ ./

RUN pipenv install

CMD ["pipenv", "shell"]
CMD ["pipenv", "run", "bot"]