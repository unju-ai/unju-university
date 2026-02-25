# Level 0: Initiation

**Duration:** 2 hours  
**Cost:** FREE  
**Format:** Self-paced with AI guide

## Welcome to unju University

You're about to learn how to build with AI agents, trade perpetual futures, and deploy smart contracts. This isn't theory—you'll ship real things.

## What You'll Do

1. **Create Your Wallet** (15 min)
   - Set up unju-wallet (non-custodial)
   - Fund with testnet tokens
   - Sign your first transaction

2. **Deploy Your First Agent** (30 min)
   - Create a simple trading agent
   - Connect to Hyperliquid testnet
   - Make a test trade

3. **Understand the Stack** (45 min)
   - How unju works
   - Agent architecture (MCP, LiveKit)
   - Smart wallets (ERC-4337)
   - The credits system

4. **Join the Community** (15 min)
   - Discord setup
   - Introduce yourself
   - Find your first project

5. **Next Steps** (15 min)
   - Choose your learning path
   - Meet your AI teacher
   - Plan your first week

## Lessons

### Lesson 1: Your First Wallet

**Goal:** Create a non-custodial wallet in 5 minutes

```bash
# Install unju CLI
npm install -g unju-cli

# Create wallet (local, no server)
unju wallet create

# This generates:
# - Your wallet address (your identity)
# - Recovery phrase (SAVE THIS!)
# - Virtual email (address@unju.ai)
```

**Why this matters:**
- Your wallet = your identity in Web3
- Non-custodial = you own your keys
- No email signup required

**Exercise:**
1. Create wallet
2. Save recovery phrase (write it down!)
3. Check balance: `unju wallet balance`

### Lesson 2: Get Testnet Funds

**Goal:** Fund your wallet with testnet tokens

```bash
# Get testnet ETH on Arbitrum Sepolia
unju faucet request

# Get testnet USDC
unju faucet usdc

# Check balance
unju wallet balance
# Should show: 1 ETH, 1000 USDC
```

**Why this matters:**
- Testing is free
- Learn without risk
- Ship to mainnet later

**Exercise:**
1. Request testnet ETH
2. Request testnet USDC
3. Verify balances

### Lesson 3: Deploy Your First Agent

**Goal:** Create a trading agent that monitors BTC price

```bash
# Create agent from template
unju agent create price-monitor --template=trading

# Configure
unju agent config set HYPERLIQUID_API testnet
unju agent config set ALERT_THRESHOLD 5  # 5% move

# Deploy
unju agent deploy

# Check status
unju agent status price-monitor
```

**What this agent does:**
- Monitors BTC price on Hyperliquid
- Alerts you on 5%+ moves
- Suggests long/short entries

**Why this matters:**
- Agents work 24/7
- No code required (yet)
- Foundation for trading strategies

**Exercise:**
1. Deploy price-monitor agent
2. Watch it run for 10 minutes
3. Check the logs: `unju agent logs price-monitor`

### Lesson 4: Make Your First Trade

**Goal:** Execute a small testnet trade

**Using the dashboard:**
1. Visit https://app.unju.ai
2. Connect your wallet (Sign in with Ethereum)
3. Navigate to "Trade"
4. Select BTC/USD
5. Enter position: $10, 2x leverage, LONG
6. Confirm and execute

**Using the CLI:**
```bash
# Long BTC with $10, 2x leverage
unju trade long BTC --size 10 --leverage 2

# Check position
unju positions list

# Close position
unju positions close BTC
```

**What happened:**
1. Your wallet signed a transaction
2. Position opened on Hyperliquid testnet
3. You're now long BTC with 2x leverage
4. P&L updates in real-time

**Why this matters:**
- This is REAL trading (just testnet)
- Same interface as mainnet
- Risk-free learning

**Exercise:**
1. Open a small long or short
2. Watch P&L for 5 minutes
3. Close the position
4. Check your realized P&L

### Lesson 5: Understand the Architecture

**The unju Stack:**

```
┌──────────────────────────────────────────┐
│  You (Human)                              │
│  - Set strategy                           │
│  - Define risk limits                     │
│  - Monitor results                        │
└─────────────┬────────────────────────────┘
              │
┌─────────────▼────────────────────────────┐
│  AI Agent Swarm                           │
│  - Monitor markets 24/7                   │
│  - Execute trades                         │
│  - Manage positions                       │
│  - Report to you                          │
└─────────────┬────────────────────────────┘
              │
┌─────────────▼────────────────────────────┐
│  unju Platform                            │
│  - Agent orchestration                    │
│  - Risk management                        │
│  - Wallet management (ERC-4337)           │
│  - Credits system                         │
└─────────────┬────────────────────────────┘
              │
┌─────────────▼────────────────────────────┐
│  Hyperliquid                              │
│  - Perpetual futures exchange             │
│  - On-chain settlement                    │
│  - Deep liquidity                         │
└───────────────────────────────────────────┘
```

**Key Concepts:**

1. **MCP (Model Context Protocol)**
   - How agents expose tools
   - Standard for AI-to-tool communication
   - unju-perps is an MCP server

2. **ERC-4337 (Account Abstraction)**
   - Smart contract wallets
   - Gas sponsorship (pay with credits)
   - Custom validation logic
   - Batch transactions

3. **Credits System**
   - 1 credit ≈ $1 in gas + fees
   - Buy once, use across platform
   - Simplified billing

4. **LiveKit**
   - Real-time agent communication
   - Voice/video for agents (optional)
   - Multi-modal interactions

**Exercise:**
1. Draw the stack from memory
2. Explain to someone (or rubber duck)
3. Identify which parts you want to learn more about

### Lesson 6: Join the Community

**Discord:**
1. Join: https://discord.gg/unju
2. Verify wallet (link in #start-here)
3. Post in #introductions:
   - What you're building
   - What you want to learn
   - Your background

**Telegram:**
1. Join: https://t.me/unju_university
2. Introduce yourself
3. Find study buddies

**Twitter:**
1. Follow: https://x.com/unju_ai
2. Share your first trade screenshot
3. Tag @unju_ai and use #UnjuUniversity

**Why this matters:**
- Learn faster with peers
- Get help when stuck
- Ship together

**Exercise:**
1. Introduce yourself in Discord
2. Find 2 people learning the same track
3. Schedule a call this week

### Lesson 7: Choose Your Path

**Pick 1-2 tracks to start:**

**🤖 AI Agent Mastery** → For: Automation enthusiasts, tool builders  
**📊 Perpetual Trading** → For: Traders, risk-takers, alpha hunters  
**🔐 Smart Contracts** → For: Protocol builders, security-minded  
**🏗️ Full-Stack Web3** → For: Product builders, UI/UX focused  
**🧠 Meta-Game** → For: Strategists, networkers, system thinkers

**Not sure? Take this quiz:**

1. **I want to build something that...**
   - A) Works while I sleep → AI Agents
   - B) Makes money from markets → Trading
   - C) Lives on-chain forever → Smart Contracts
   - D) People actually use → Full-Stack
   - E) Changes how people think → Meta-Game

2. **My strength is...**
   - A) Automation & systems → AI Agents
   - B) Risk & probability → Trading
   - C) Logic & security → Smart Contracts
   - D) UI & user experience → Full-Stack
   - E) Strategy & positioning → Meta-Game

3. **In 6 months, I want to have...**
   - A) An agent that runs my life → AI Agents
   - B) Profitable trading strategy → Trading
   - C) Deployed protocol → Smart Contracts
   - D) Live dApp with users → Full-Stack
   - E) Unique market position → Meta-Game

**Most people do 2-3 tracks.** That's ideal.

**Exercise:**
1. Pick your primary track
2. Pick your secondary track
3. Post in Discord: "Starting with [X] and [Y]"

## Graduation Requirements

To complete Level 0 (Initiation):

✅ Created wallet  
✅ Funded with testnet tokens  
✅ Deployed first agent  
✅ Made first trade  
✅ Joined community (Discord/Telegram)  
✅ Chosen learning tracks  

**Time to complete:** 2 hours (or less)

**Next step:**
```bash
# Enroll in Level 1
unju university enroll --level=1 --tracks=ai-agents,trading

# Cost: 10 credits ($100)
# Duration: 4 weeks
# Format: Hybrid (live + self-paced)
```

## Need Help?

**AI Teacher:** Professor Perps is available 24/7
```bash
unju chat "I'm stuck on [problem]"
```

**Human Support:**
- Discord: #support channel
- Office Hours: Tuesdays 2pm PT (esper)
- Email: support@unju.ai

**Common Issues:**

**Problem:** Wallet creation failed  
**Solution:** Make sure you're on latest CLI: `npm update -g unju-cli`

**Problem:** Testnet faucet not working  
**Solution:** Try again in 10 min (rate limits), or ask in Discord

**Problem:** Agent won't deploy  
**Solution:** Check logs: `unju agent logs [name] --tail=50`

**Problem:** Trade execution failed  
**Solution:** Check wallet balance, try smaller size

## What's Next?

**Level 1: Foundations** starts with:

**Week 1:** Deep dive into your primary track  
**Week 2:** Build your first real project  
**Week 3:** Ship to testnet  
**Week 4:** Go to mainnet (optional)

**Live sessions:**
- Mondays 6pm PT: Lecture + Q&A
- Wednesdays 6pm PT: Project workshop
- Fridays 12pm PT: Office hours

**Self-paced:**
- 5-10 hours of video content
- Hands-on exercises
- Weekly project milestones

**AI Teacher:**
- Available 24/7
- Reviews your code
- Answers questions
- Gives feedback

**Enroll:** https://university.unju.ai/level-1

---

**Congrats on completing Initiation!** 🎓

The hard part is starting. You did it.

Now keep going. 🚀
