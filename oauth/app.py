"""GitHub OAuth proxy for Decap CMS."""

from __future__ import annotations

import os
from pathlib import Path

import httpx
from litestar import Litestar, get
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin
from litestar.openapi.spec import Contact, ExternalDocumentation, License, Server
from litestar.response import Redirect
from litestar.response.base import ASGIResponse

# Load .env from oauth/ or repo root if present
_env_file = Path(__file__).parent / ".env"
if not _env_file.is_file():
    _env_file = Path(__file__).parent.parent / ".env"
if _env_file.is_file():
    for line in _env_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())

CLIENT_ID = os.environ["GITHUB_CLIENT_ID"]
CLIENT_SECRET = os.environ["GITHUB_CLIENT_SECRET"]

AUTHORIZE_URL = "https://github.com/login/oauth/authorize"
TOKEN_URL = "https://github.com/login/oauth/access_token"

CALLBACK_HTML = """<!doctype html>
<html><body><script>
(function() {
  const token = "%s";
  const data = JSON.stringify({token: token, provider: "github"});

  // Step 1: Tell the parent we're starting auth
  window.opener.postMessage("authorizing:github", "*");

  // Step 2: Wait for parent to acknowledge, then send the token
  window.addEventListener("message", function(e) {
    window.opener.postMessage(
      "authorization:github:success:" + data,
      e.origin
    );
    window.close();
  }, false);
})();
</script></body></html>
"""


@get("/_health/")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@get("/auth")
async def auth() -> Redirect:
    return Redirect(f"{AUTHORIZE_URL}?client_id={CLIENT_ID}&scope=repo,user")


@get("/callback", media_type="text/html")
async def callback(code: str) -> ASGIResponse:
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            TOKEN_URL,
            json={"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "code": code},
            headers={"Accept": "application/json"},
        )
        resp.raise_for_status()
        token = resp.json()["access_token"]
    return ASGIResponse(body=(CALLBACK_HTML % token).encode(), media_type="text/html")


app = Litestar(
    route_handlers=[health, auth, callback],
    openapi_config=OpenAPIConfig(
        title="Python Wiki API",
        version="1.0.0",
        summary="GitHub OAuth proxy powering Decap CMS for the Python Wiki.",
        description=(
            "Provides the OAuth handshake between Decap CMS (running in the browser) "
            "and GitHub, so editors can authenticate and commit changes to the wiki "
            "repository without exposing client secrets.\n\n"
            "## Endpoints\n\n"
            "| Path | Purpose |\n"
            "|---|---|\n"
            "| `GET /auth` | Redirects the user to GitHub's OAuth authorize page |\n"
            "| `GET /callback` | Exchanges the authorization code for an access token "
            "and posts it back to Decap CMS via `postMessage` |\n"
            "| `GET /_health/` | Health check for load balancers and uptime monitors |\n"
        ),
        contact=Contact(
            name="Python Software Foundation",
            url="https://www.python.org/psf/",
            email="psf@python.org",
        ),
        license=License(name="MIT", identifier="MIT"),
        external_docs=ExternalDocumentation(
            description="Python Wiki source repository",
            url="https://github.com/python/wiki",
        ),
        servers=[
            Server(url="https://api.wiki.python.org", description="Production"),
            Server(url="http://localhost:8000", description="Local development"),
        ],
        render_plugins=[ScalarRenderPlugin(path="/")],
        path="/api",
    ),
)
