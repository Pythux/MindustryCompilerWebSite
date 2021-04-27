
# deploy to heroku

in this directory:

```sh
heroku login
heroku container:login
```

## push the image

```sh
heroku container:push web --app mindustry-compiler
```

## run the pushed image

```sh
heroku container:release web --app mindustry-compiler
```
