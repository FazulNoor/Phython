FROM gitpod/workspace-full

COPY requirements.txt .
RUN pipenv shell
RUN pipenv install -r requirements.txt
RUN python -m ipykernel install --user --name=Phython
