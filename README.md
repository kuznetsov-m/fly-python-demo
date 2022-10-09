# fly.io python app demo

`flyctl auth login`

`flyctl launch`

`flyctl deploy`

`flyctl secrets set DATABASE_URL=postgres://example.com/mydb`

`cat .env | fly secrets import` [source](https://community.fly.io/t/how-are-you-managing-cert-files-with-fly/2984/8)

## fly.toml
Remove: ...

Add:

```
[build]
  builder = "heroku/buildpacks:latest"
```

## Procfile
`web: python main.py`

# Notes

Error: `Error failed to fetch an image or build from source: failed building options: failed probing "personal": context deadline exceeded`

[Solution 1](https://community.fly.io/t/failed-to-fetch-an-image-or-build-from-source-failed-building-options-failed-probing-personal-context-deadline-exceeded/7140/7): `fly wireguard reset`

[Solution 2](https://community.fly.io/t/deployments-not-working-error-connecting-to-docker/3992/54?page=3): `fly agent stop; fly agent start`


# Links
- https://www.youtube.com/watch?v=CedAzHw1k5I
