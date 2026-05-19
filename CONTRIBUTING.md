# Contributing

Thanks for improving this local LLM + SearxNG agent. The project is meant to stay local-first and understandable.

## Good contributions

- Better configuration via environment variables or CLI flags.
- Safer handling of web-search snippets before they are sent to the local LLM.
- Tests for search-trigger detection, response parsing, and error handling.
- Documentation for Ollama, LM Studio, Jan, and Podman setups.
- Container setup fixes that do not expose SearxNG publicly by default.

## Boundaries

- Do not add hosted/cloud LLM defaults. Local endpoints should remain the default.
- Do not add telemetry, prompt logging, analytics, or remote callbacks.
- Do not commit API keys, model provider tokens, private prompts, or local machine paths.
- Do not bind SearxNG to public interfaces without a clear security discussion.

## Development setup

```bash
cd llm_web_agent
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd ..
python3 -m pytest -q
```

If you only changed documentation, run at least:

```bash
python3 -m py_compile llm_web_agent/*.py
```

## Pull request checklist

- [ ] I ran `python3 -m pytest -q` or explained why it was not applicable.
- [ ] Defaults remain local-first.
- [ ] No credentials, tokens, prompt logs, or private paths were added.
- [ ] Any new network behavior is documented.
