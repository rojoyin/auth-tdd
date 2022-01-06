Implementation guide:

https://santoshk.dev/posts/2021/tdd-approach-to-creating-an-authentication-system-with-fastapi-part-1/

For testing: located at root of project run
```bash
$ pytest -q
```

For hotreaload uvicorn
```bash
$ uvicorn main:app --reload
```

SwaggerUI
```url
http://localhost:8000/docs
```

OpenAPI
```url
http://127.0.0.1:8000/openapi.json
```

Environment variable
copy the .env-sample contents into .env file and change the entries accordingly
