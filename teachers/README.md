# AI Teachers

Teacher agents will be designed and slotted into courses later. This directory will hold their configs once ready.

## Architecture

Each course can have a dedicated AI teacher — a specialized agent with domain expertise, personality, and access to course materials.

### How Teachers Work

Teachers are specialized agents deployed via the unju-agent runtime. Each teacher has:

1. **Domain expertise** — Trained on specific course content
2. **Personality** — Unique teaching style (TBD by design)
3. **Tools** — Access to relevant MCP services
4. **Knowledge base** — Course materials and examples

### Teacher Template Structure

```
teacher-name/
├── config.yaml         # Agent config (name, tools, voice, etc.)
├── prompt.md           # System prompt
├── knowledge/          # Course content
└── examples/           # Code examples
```

### Interaction Modes

- **Chat** — Ask questions, get explanations
- **Code Review** — Submit code for feedback
- **Debug** — Share logs for troubleshooting
- **Discussion** — Strategic/conceptual conversations

### Ethics

- No hallucinations — say "I don't know" when unsure
- No shortcuts — make students think
- No financial advice
- Safety first — warn about security risks
- Honest, direct feedback

## Status

🟡 **Curriculum first, teachers later.** Courses and content are being built. Teacher agents will be designed by Esper and configured here when ready.
