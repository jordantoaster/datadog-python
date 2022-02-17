# datadog-python

## Setting Up Local Development Environment.

1. Setup a Datadog account.

2. Generate an API key on the Datadog UI and put it in the docker compose file, replacing ```<API KEY HERE>```

2. At the project root run ```docker-compose up --build```, this will create the Docker image and run the container. Unless manually stopped, it will run indefinitely run the Python script specified in the Docker file.

3. The metric should be avaliable on the datadog metric explorer if you search for ```example_metric```

## Notes

- I used a personal account on a free trail for the datadog account, on the eu site ```https://app.datadoghq.eu/```

- Datadog assumes it is interacting with the US site when validting API keys, which is why the ```DD_SITE``` is set explictly in the docker compose file for the agent.

- API keys are generated in the organisation settings for the account.
