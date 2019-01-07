# Run the Service

The service can be run a standalone microservice or can be embedded into
a larger component. This page describes the former.

You may run this service without any further dependency. From your virtual
environment, run the following command:

```
$ chaosplatform-scheduler run
```

You should pass the settings as follows:


```
$ chaosplatform-scheduler run --env-path=.env
```

Read the [settings][] documentation to know what values can be set.

[settings]: ./settings.md


## Dependencies

While this service may be executed as-is, it requires a Redis server to connect
to as it will place jobs into a queue on the Redis server.

Set the connection information in the `.env` file you pass to the
`chaosplatform-scheduler` call.

A great way to run locally is by using a docker instance as follows:

`
$ docker run --rm --name redis -p 6379:6379 redis
`

