"""Tests for the GitHub OAuth proxy."""

from __future__ import annotations

from unittest.mock import patch

import pytest
from litestar.status_codes import HTTP_200_OK, HTTP_302_FOUND
from litestar.testing import AsyncTestClient


@pytest.fixture()
def _env(monkeypatch):
    monkeypatch.setenv("GITHUB_CLIENT_ID", "test-client-id")
    monkeypatch.setenv("GITHUB_CLIENT_SECRET", "test-client-secret")


@pytest.fixture()
async def client(_env):
    # Import after env vars are set so module-level os.environ reads work
    import importlib

    import app as app_module

    importlib.reload(app_module)

    async with AsyncTestClient(app=app_module.app) as client:
        yield client


async def test_health(client):
    resp = await client.get("/_health/")
    assert resp.status_code == HTTP_200_OK
    assert resp.json() == {"status": "ok"}


async def test_auth_redirects_to_github(client):
    resp = await client.get("/auth", follow_redirects=False)
    assert resp.status_code == HTTP_302_FOUND
    location = resp.headers["location"]
    assert "github.com/login/oauth/authorize" in location
    assert "client_id=test-client-id" in location
    assert "scope=repo,user" in location


async def test_callback_exchanges_code_for_token(client):
    mock_response = type("Response", (), {
        "json": lambda self: {"access_token": "gho_test_token_123"},
        "raise_for_status": lambda self: None,
    })()

    async def mock_post(*args, **kwargs):
        return mock_response

    with patch("app.httpx.AsyncClient") as mock_client_cls:
        mock_instance = mock_client_cls.return_value.__aenter__.return_value
        mock_instance.post = mock_post

        resp = await client.get("/callback?code=test-auth-code")
        assert resp.status_code == HTTP_200_OK
        assert "gho_test_token_123" in resp.text
        assert "postMessage" in resp.text
        assert "authorization:github:success:" in resp.text
