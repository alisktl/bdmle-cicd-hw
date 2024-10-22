FROM python:3.9

WORKDIR /app

COPY README.md pyproject.toml pdm.lock ./
RUN python3 -m pip install --upgrade pip setuptools wheel pdm
RUN pdm lock --check \
    && pdm -v export --without-hashes -f requirements -o requirements.txt \
    && python3 -m pip install --no-cache-dir -r requirements.txt

COPY dist/ /tmp/dist/
RUN python3 -m pip install --no-cache-dir /tmp/dist/*.whl

COPY src/bdmle_cicd_hw/task.py /app/
CMD ["python3", "task.py", "23", "107"]