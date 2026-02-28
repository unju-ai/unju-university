# Teachers

Teachers are **dynamic** — a teacher slot can be filled by a human, an AI agent, or both, switching fluidly per session.

## Teacher Types

| Type | Description | Delivery |
|------|-------------|----------|
| **Human (live)** | Real person streaming via LiveKit/RTMP | Live video/voice, chat |
| **AI (live)** | Agent streaming via LiveKit + RTMP egress | Live video/voice, chat |
| **AI (async)** | Agent available for 1:1 chat/review | Text, voice, code review |
| **Hybrid** | Human streams live, AI handles Q&A/review between sessions | Both |

## How It Works

Each **course** defines:
- Curriculum (lessons, projects, assessments)
- Required tools/services
- Knowledge base

Each **session** has a teacher assignment:
- Who's teaching (human ID or agent config)
- Mode (live stream, 1:1 chat, async review)
- Schedule (if live)

The same course can have:
- A human streaming Monday's live session
- An AI handling Tuesday's practice/review
- Both co-teaching Wednesday's workshop

## Teacher Config

```yaml
# Per-session teacher assignment
session:
  course: "trading-101"
  lesson: 3
  teacher:
    type: "human"          # human | ai | hybrid
    human_id: "esper"      # if human/hybrid
    agent_config: null      # if ai/hybrid — references agent template
    mode: "livestream"      # livestream | chat | async
    stream_targets:         # optional RTMP destinations
      - platform: "tiktok"
        stream_key: "..."
      - platform: "youtube"
        stream_key: "..."
```

## AI Teacher Capabilities

When an AI fills the teacher slot:
- Full access to course knowledge base
- LiveKit room for voice/video
- RTMP egress for streaming to TikTok/YouTube
- MCP tools relevant to the course (defi, code review, etc.)
- Memory of student progress

## Human Teacher Capabilities

When a human fills the teacher slot:
- LiveKit room (camera + screen share)
- RTMP egress for multi-platform streaming
- AI co-pilot available (answers chat, generates overlays)
- Student interaction tools (polls, Q&A queue)
- Session recording + clip generation

## Status

🟡 **Teacher system designed. Configs added per course when ready.**
