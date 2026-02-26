# Content Pipeline

## The Funnel

```
TikTok/YouTube Short (60s)
  → "Want to learn more? Link in bio"
    → Landing Page (email capture)
      → Level 0: Free Initiation (2 hours)
        → Level 1: Foundations ($100)
          → Level 2: Specialization ($250)
            → Level 3: Mastery ($500)
```

## Content Types

### 1. Hook Videos (60s) — Faceless AI
- One concept, one lesson
- AI-generated visuals + TTS narration
- Produced autonomously by Saraswati (content creator agent)
- Styles: cinematic, anime, minimal, neon, documentary
- Posted to TikTok, YouTube Shorts, Instagram Reels

### 2. Tutorial Videos (5-15 min)
- Step-by-step walkthroughs
- Can be human (livestream recording) or AI-generated
- Screen recordings with voice

### 3. Deep Dives (30-60 min)
- Full course lessons
- Human teachers livestreaming or AI agents in LiveKit rooms
- Case studies, live coding sessions

## Production Pipeline (Faceless Videos)

```
Topic → Script → Voice (ElevenLabs TTS) → Visuals (Gemini AI) → Assembly (FFmpeg) → Post
```

### Script Format
- [0:00-0:02] Hook — stop the scroll
- [0:02-0:07] Problem — why should they care
- [0:07-0:40] Content — the actual value
- [0:40-0:55] Payoff — the insight or lesson
- [0:55-1:00] CTA — follow, link in bio, etc.

### Autonomous Agent (Saraswati)
Saraswati handles the full pipeline:
1. `create_video_script` — structured scenes with narration + visual prompts
2. `generate_video_assets` — TTS audio + AI images per scene (parallel)
3. `assemble_video` — FFmpeg with Ken Burns, captions, transitions
4. `generate_batch_scripts` — plan content calendar (5-10 videos at once)
5. `regenerate_scene` — tweak individual scenes without redoing everything

### Voice Options
- nova — warm, confident (female)
- asteria — clear, professional (female)
- orion — deep, authoritative (male)
- echo — energetic, dynamic (male)
- shimmer — soft, mystical (female)

### Visual Styles
- cinematic — dramatic lighting, film quality
- anime — vibrant, illustrated
- minimal — clean, geometric
- neon — cyberpunk, glowing
- documentary — photorealistic

## Content Strategy

### Volume Game
- Target: 3-5 videos/day per niche
- Batch production: plan 10, produce 10, post over 3-5 days
- A/B test hooks — same content, different first 2 seconds

### Content Angles
- Listicles ("5 things...")
- Myths busted ("You've been told X, but...")
- Mini-tutorials ("How to X in 60 seconds")
- Story-driven ("This person did X and...")
- Hot takes ("Unpopular opinion: ...")

### Platform-Specific
- **TikTok**: 30-90s, vertical 9:16, trending sounds optional
- **YouTube Shorts**: 30-60s, vertical 9:16, SEO title matters
- **Instagram Reels**: 30-90s, vertical 9:16, carousel follow-up

## Metrics
- Views → Watch time → Link clicks → Signups → Enrollments → Completion → Revenue
- Target: 1% of views → signup, 20% signup → Level 0, 10% Level 0 → Level 1
