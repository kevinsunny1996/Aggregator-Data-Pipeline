FROM public.ecr.aws/lambda/python:3.9.2022.10.24.15

# copy function code
COPY src/ ${LAMBDA_TASK_ROOT}

# install the dependencies onto the folder
COPY requirements.txt .

RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# set the cmd to your handler 
CMD [ "app.lambda_handler" ]
