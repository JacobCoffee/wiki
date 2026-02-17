"""GitHub OAuth proxy for Decap CMS."""

from __future__ import annotations

import os

import httpx
from litestar import Litestar, get
from litestar.response import Redirect

CLIENT_ID = os.environ["GITHUB_CLIENT_ID"]
CLIENT_SECRET = os.environ["GITHUB_CLIENT_SECRET"]

AUTHORIZE_URL = "https://github.com/login/oauth/authorize"
TOKEN_URL = "https://github.com/login/oauth/access_token"

CALLBACK_HTML = """<!doctype html>
<html><body><script>
(function() {
  const token = "%s";
  window.opener.postMessage(
    "authorization:github:success:" + JSON.stringify({token: token, provider: "github"}),
    document.referrer
  );
  window.close();
})();
</script></body></html>
"""


@get("/_health/")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@get("/auth")
async def auth() -> Redirect:
    return Redirect(f"{AUTHORIZE_URL}?client_id={CLIENT_ID}&scope=repo,user")


@get("/callback")
async def callback(code: str) -> str:
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            TOKEN_URL,
            json={"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "code": code},
            headers={"Accept": "application/json"},
        )
        resp.raise_for_status()
        token = resp.json()["access_token"]
    return CALLBACK_HTML % token


app = Litestar(route_handlers=[health, auth, callback])
