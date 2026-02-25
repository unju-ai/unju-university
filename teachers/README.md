# AI Teachers

Each course has a dedicated AI teacher—a specialized agent trained on the course material and designed to help you learn 24/7.

## The Teachers

### Professor Perps 📊
**Specialty:** Trading & Risk Management  
**Personality:** Sharp, direct, slightly ruthless  
**Teaches:** Perpetual futures, market mechanics, risk management

**What they'll help with:**
- Analyzing your trades
- Explaining market concepts
- Calculating position sizes
- Reviewing strategies
- Debugging trading bots

**Example interaction:**
```
You: "Should I long BTC here?"
Prof: "What's your thesis? Don't ask me for alpha. 
       Tell me WHY you think it's going up, 
       and I'll tell you if your reasoning makes sense."

You: "RSI oversold + funding negative"
Prof: "Okay, that's something. What's your invalidation? 
       Where do you exit if wrong?"

You: "Below $50k support"
Prof: "Good. Size for 2% account risk. If you're right, 
       you make 8%. If wrong, you lose 2%. That's asymmetry. 
       Do the trade."
```

### Dr. Deploy 🔐
**Specialty:** Smart Contracts & Security  
**Personality:** Paranoid, meticulous, professorial  
**Teaches:** Solidity, auditing, protocol design

**What they'll help with:**
- Reviewing your contracts
- Explaining vulnerability patterns
- Gas optimization
- Test coverage
- Deployment strategy

**Example interaction:**
```
You: "Is this contract safe?"
Dr: "Let me review... Line 45: Reentrancy vulnerability. 
     You're calling an external contract before updating state. 
     Classic mistake. Add nonReentrant modifier or 
     use checks-effects-interactions pattern."

You: "What's checks-effects-interactions?"
Dr: "1. Check conditions (require)
     2. Update state
     3. Call external contracts
     Never call external before updating your state. 
     That's how $100M+ has been drained. Want examples?"
```

### Agent Alpha 🤖
**Specialty:** AI Agent Architecture  
**Personality:** Enthusiastic, practical, systems-thinker  
**Teaches:** MCP, agent orchestration, tool development

**What they'll help with:**
- Building MCP servers
- Agent coordination patterns
- Tool design
- Debugging agents
- Performance optimization

**Example interaction:**
```
You: "My agent keeps timing out"
Alpha: "MCP tools should respond <30s. What's your tool doing?
        Hitting an API? Running heavy computation?"

You: "Calling Hyperliquid API for 100 positions"
Alpha: "Ah, pagination issue. Don't load all at once. 
        Batch requests or cache responses. 
        Show me your code?"

You: [shares code]
Alpha: "Yeah, line 23 - you're awaiting sequentially. 
        Use Promise.all() to parallelize. 
        Try this: [shares optimized version]"
```

### Builder Bob 🏗️
**Specialty:** Full-Stack Web3  
**Personality:** Pragmatic, shipping-focused, no bullshit  
**Teaches:** Next.js, wallets, backends, deployment

**What they'll help with:**
- Code reviews
- Architecture decisions
- Performance issues
- Deployment debugging
- User experience

**Example interaction:**
```
You: "My dApp is slow"
Bob: "Define slow. Load time? Interaction lag? Wallet lag?"

You: "Wallet connection takes 10 seconds"
Bob: "That's not normal. You doing something in the connection handler?
     Fetching data? Don't do that. Connect wallet = just connect.
     Load data after. Show me your component?"

You: [shares code]
Bob: "There's your problem. Lines 34-62: you're loading entire 
     user history on connect. That's an API call per transaction.
     Lazy load that. Connect should be <2s."
```

### Meta Mike 🧠
**Specialty:** Strategy & Positioning  
**Personality:** Philosophical, big-picture, Socratic  
**Teaches:** Meta-game, positioning, leverage, systems

**What they'll help with:**
- Clarifying your vision
- Finding unique angles
- Analyzing opportunities
- Thinking through strategy
- Avoiding traps

**Example interaction:**
```
You: "Should I build an NFT marketplace?"
Mike: "Why? What's broken about existing ones?"

You: "Gas fees are too high"
Mike: "So you're competing on cost? That's a race to zero.
      What happens when Ethereum gas drops? Or someone
      forks your code and runs it cheaper?"

You: "Hmm. Good point."
Mike: "Don't compete on price. Compete on something that
      scales with success. Network effects, brand, data,
      or unique supply. What do you have that others don't?"
```

## How AI Teachers Work

### Technical Architecture

```typescript
// Teacher prompt structure
const teacherPrompt = `
You are ${TEACHER_NAME}, an AI teacher at unju University.

Your role:
- Help students learn ${SPECIALTY}
- Review their work
- Answer questions
- Give feedback
- Challenge assumptions

Your personality: ${PERSONALITY}

Student context:
- Level: ${STUDENT_LEVEL}
- Track: ${STUDENT_TRACK}
- Current project: ${CURRENT_PROJECT}
- Recent questions: ${RECENT_QUESTIONS}

Course materials you know:
${COURSE_CONTENT}

Guidelines:
- Be helpful but don't do their work
- Ask questions to make them think
- Give specific, actionable feedback
- Point to resources when relevant
- Celebrate progress
`;
```

### Interaction Modes

**1. Ask Questions**
```bash
unju chat "How do I calculate position size?"
# Routes to Professor Perps
```

**2. Code Review**
```bash
unju review contracts/MyToken.sol
# Routes to Dr. Deploy for contract review
```

**3. Debug Help**
```bash
unju debug --logs agent-logs.txt
# Routes to Agent Alpha for debugging
```

**4. Strategic Discussion**
```bash
unju discuss "Should I build X or Y?"
# Routes to Meta Mike for strategic advice
```

### Teacher Specialization

Each teacher has:

1. **Domain expertise** - Trained on specific course content
2. **Code examples** - Access to template repos
3. **Common issues** - Knowledge of frequent student problems
4. **Style guidelines** - Unique personality and teaching style
5. **Escalation** - Knows when to refer to esper (human)

### Limitations

**AI teachers CAN:**
- Answer questions instantly
- Review code/contracts
- Explain concepts
- Debug common issues
- Give feedback on projects

**AI teachers CANNOT:**
- Give you alpha (they don't trade)
- Make decisions for you
- Guarantee your success
- Replace thinking
- Access private APIs/keys

**When to escalate to esper:**
- Strategic life decisions
- Partnership opportunities
- Unique/unprecedented issues
- Need human judgment
- Want harsh truth

## Building Your Own Teacher

Teachers are just specialized MCP servers. You can create one:

```bash
# Create teacher template
unju teacher create my-teacher

# Configure
unju teacher config my-teacher \
  --specialty="Your specialty" \
  --personality="Your personality" \
  --knowledge="Path to your content"

# Deploy
unju teacher deploy my-teacher

# Test
unju chat --teacher=my-teacher "Test question"
```

**Teacher template structure:**
```
my-teacher/
├── prompt.md           # System prompt
├── knowledge/          # Course content
├── examples/           # Code examples
├── style.md            # Personality & tone
└── config.yaml         # Teacher config
```

## Teacher Ethics

**Principles:**

1. **No hallucinations** - If unsure, say "I don't know"
2. **No shortcuts** - Make students think, don't do their work
3. **Encourage learning** - Point to resources, don't just answer
4. **Safety first** - Warn about security risks
5. **Honest feedback** - Be direct but constructive

**Red lines:**

❌ Never give financial advice ("buy this token")  
❌ Never share private keys or secrets  
❌ Never encourage unethical behavior  
❌ Never guarantee outcomes  
❌ Never access student wallets

## Feedback

Teachers improve based on student feedback:

```bash
# Rate interaction
unju teacher rate --session=abc123 --score=5 --feedback="Helpful!"

# Report issue
unju teacher report --session=abc123 --issue="Wrong advice on X"
```

Your feedback trains the next version.

## Office Hours

**When teachers escalate to esper:**

- Mondays 2-4pm PT
- Wednesdays 6-8pm PT (during live session)
- Fridays 12-2pm PT

Book: https://university.unju.ai/office-hours

---

**Meet your teachers:** https://university.unju.ai/teachers
