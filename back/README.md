
# deploy to heroku

in this directory:

```sh
heroku login
heroku container:login
```

## push first version

```sh
heroku container:push web --app mindustry-compiler
```

## new version

```sh
heroku container:release web
```
