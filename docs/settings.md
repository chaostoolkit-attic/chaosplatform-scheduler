# Server settings

The service is configured via environment variables which must be present in
the shell where you are running it from, or from a simple [.env][dotenv] file.

[dotenv]: https://pypi.org/project/python-dotenv/

You will find an example of such file in the repository.

## Configuration Keys

| Key                       | Default           | Required | Description                                        | 
|---------------------------|-------------------|----------|----------------------------------------------------|
| GRPC_LISTEN_ADDR          | "0.0.0.0:50058" | Yes      | The address to bind the GRPC server to             |
| QUEUE_NAME              | "chaosplatform"       | Yes      | The name of the queue holding the scheduled jobs          |
| REDIS_HOST | "127.0.0.1" | Yes      | The address of Redis server to connect to |
| REDIS_PORT            | 6379 | Yes      | The port of the Redis server to connect to |
