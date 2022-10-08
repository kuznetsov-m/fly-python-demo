# fly.io python app demo

`flyctl auth login`

`flyctl launch`

`flyctl deploy`

`flyctl secrets set DATABASE_URL=postgres://example.com/mydb`

## fly.toml
Remove: ...

Add:

```
[build]
  builder = "heroku/buildpacks:latest"
```

# Notes

Error: `Error failed to fetch an image or build from source: failed building options: failed probing "personal": context deadline exceeded`

[Solution](https://community.fly.io/t/failed-to-fetch-an-image-or-build-from-source-failed-building-options-failed-probing-personal-context-deadline-exceeded/7140/7): `fly wireguard reset`


# Links
- https://www.youtube.com/watch?v=CedAzHw1k5I