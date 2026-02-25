"""
Unju University Teacher Configs — maps teacher personas to AgentConfig objects.

These configs can be:
1. Imported directly into unju-agent runtime
2. Deployed as a template via the template system
3. Loaded from PlanetScale (when DB-driven)

Each teacher is a specialized agent with:
- Unique personality prompt (from prompt.md)
- Service tools matching their expertise
- Knowledge bases for their domain
- Voice configuration for audio/video lessons
"""

# This file generates AgentConfig-compatible dicts from teacher configs.
# Used by the unju-university template in unju-agent.

import yaml
from pathlib import Path

TEACHERS_DIR = Path(__file__).parent


def load_teacher_config(slug: str) -> dict:
    """Load a teacher's full config (YAML + prompt)."""
    teacher_dir = TEACHERS_DIR / slug
    config_path = teacher_dir / "config.yaml"
    prompt_path = teacher_dir / "prompt.md"

    if not config_path.exists():
        raise FileNotFoundError(f"Teacher config not found: {config_path}")

    with open(config_path) as f:
        config = yaml.safe_load(f)

    prompt = ""
    if prompt_path.exists():
        with open(prompt_path) as f:
            prompt = f.read()

    return {
        **config,
        "system_prompt": prompt,
    }


def teacher_to_agent_config(slug: str) -> dict:
    """Convert a teacher config to an AgentConfig-compatible dict."""
    tc = load_teacher_config(slug)
    voice = tc.get("voice", {})

    return {
        "slug": tc["slug"],
        "display_name": tc["display_name"],
        "role_tagline": f"Unju University — {tc['personality']['tagline']}",
        "system_prompt": tc["system_prompt"],
        "tools": tc.get("services", ["memory"]),
        "knowledge_bases": tc.get("knowledge_bases", []),
        "voice_config": {
            "provider": voice.get("provider", "elevenlabs"),
            "voice_id": voice.get("voice_id", "asteria"),
            "speed": voice.get("speed", 1.0),
        },
        "modalities": ["text", "voice"],
        "model": "gpt-4o",
        "accent_color": tc.get("accent_color", "#6B5BFF"),
        "is_official": True,
        "metadata": {
            "type": "teacher",
            "emoji": tc.get("emoji", "📚"),
            "tracks": tc.get("tracks", []),
            "teaching_style": tc["personality"].get("teaching_style", "conversational"),
            "escalation_triggers": tc.get("escalation_triggers", []),
        },
    }


ALL_TEACHERS = [
    "professor-perps",
    "dr-deploy",
    "agent-alpha",
    "builder-bob",
    "meta-mike",
]


def get_all_teacher_configs() -> list[dict]:
    """Get all teacher configs as AgentConfig-compatible dicts."""
    configs = []
    for slug in ALL_TEACHERS:
        try:
            configs.append(teacher_to_agent_config(slug))
        except Exception as e:
            print(f"Warning: failed to load teacher '{slug}': {e}")
    return configs


if __name__ == "__main__":
    import json
    for config in get_all_teacher_configs():
        print(f"\n{'='*60}")
        print(f"📚 {config['display_name']} ({config['slug']})")
        print(f"   {config['role_tagline']}")
        print(f"   Tools: {config['tools']}")
        print(f"   KBs: {config['knowledge_bases']}")
        print(f"   Voice: {config['voice_config']['voice_id']}")
        print(f"   Prompt: {len(config['system_prompt'])} chars")
