# OAuth API Reference

The OAuth proxy lives in `oauth/app.py` and handles the GitHub OAuth handshake for Decap CMS. Three routes, one module, no database.

When running locally (`make oauth-serve`), [Litestar](https://litestar.dev/) auto-generates interactive API docs at [http://localhost:8000/api](http://localhost:8000/api) via the Scalar UI plugin. In production, the same docs are at [api.wiki.python.org/api](https://api.wiki.python.org/api).

## Endpoints

| Method | Path | What it does |
|--------|------|-------------|
| `GET` | `/auth` | Redirects the user to GitHub's OAuth authorize page |
| `GET` | `/callback?code=...` | Exchanges the authorization code for a token, posts it back to the CMS via `postMessage` |
| `GET` | `/_health/` | Returns `{"status": "ok"}` for load balancers |

## Module reference

```{eval-rst}
.. automodule:: app
   :members: health, auth, callback
   :show-inheritance:
```
