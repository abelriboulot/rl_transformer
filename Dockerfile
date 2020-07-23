FROM pytorch/pytorch:1.5-cuda10.1-cudnn7-runtime

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN apt-get update
RUN apt-get install -y -f git

# instructions for transformers
RUN git clone https://github.com/huggingface/transformers
RUN pip install transformers/.

# Install production dependencies.
RUN pip install Flask gunicorn torch nltk html2text

# Execute gunicorn with 8 threads
CMD exec gunicorn --bind :$PORT --workers 1 --threads 1 --timeout 0 app:app