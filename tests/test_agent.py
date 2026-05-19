import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENT_DIR = ROOT / "llm_web_agent"
sys.path.insert(0, str(AGENT_DIR))

spec = importlib.util.spec_from_file_location("agent", AGENT_DIR / "agent.py")
agent = importlib.util.module_from_spec(spec)
spec.loader.exec_module(agent)


def test_search_type_detects_text_keywords():
    assert agent.get_search_type("latest Python release") == agent.SearchType.TEXT
    assert agent.get_search_type("what happened in Berlin today") == agent.SearchType.TEXT


def test_search_type_detects_image_keywords_first():
    assert agent.get_search_type("show me image of a cat") == agent.SearchType.IMAGE


def test_search_type_none_for_regular_prompt():
    assert agent.get_search_type("write a short haiku") == agent.SearchType.NONE
    assert agent.get_search_type("") == agent.SearchType.NONE


def test_remove_think_tags_case_insensitive_and_multiline():
    text = "Before <think>hidden\nreasoning</think> After"
    assert agent.remove_think_tags(text) == "Before  After"
    assert agent.remove_think_tags("<THINK>secret</THINK>Visible") == "Visible"
