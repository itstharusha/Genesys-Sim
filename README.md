
# GENESYS – Generative Economy Simulation System

**A synthetic economy where AI companies compete, evolve, and win.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js&logoColor=white)](https://nextjs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LLM Powered](https://img.shields.io/badge/LLM-Groq%20%7C%20OpenRouter-purple)](https://groq.com)

**GENESYS** is a full-stack, multi-agent simulation platform that creates a living digital economy.  
AI-driven companies are generated in realistic industries, autonomously reason about strategy using large language models, manage capital & resources, compete for market share, earn revenue, pay costs — and either grow, adapt, or go bankrupt.

The system demonstrates **emergent behavior**: aggressive companies risk early failure, conservative ones survive longer, innovation-focused ones build long-term dominance.

### Full-Stack Highlights

- **Backend** — Realistic Python simulation engine with LLM-powered company decisions  
- **Frontend** — Modern Next.js 15 dashboard (App Router + shadcn/ui + Tailwind + Recharts)  
- **Real-time** — Polling / WebSocket-ready updates of companies, capital, strategies & LLM reasoning  
- **Beautiful UX** — Premium SaaS-style interface (inspired by Vercel, Linear, Supabase)

### Key Features

- Procedurally generated industries (SaaS, EV, Fintech, HealthTech, etc.)
- Autonomous AI companies with capital, talent, strategies & unique names
- **Live LLM strategy evolution** — companies adapt pricing/R&D/marketing every few cycles with natural-language reasoning
- Full economic loop: revenue, costs, profit/loss, capital flow, market share competition
- Bankruptcy & survival mechanics
- Real-time dashboard: KPIs, capital evolution charts, sortable company table, cycle timeline
- Console + web output with detailed LLM reasoning
- JSON snapshots for replay & analysis

### Demo (Console + Dashboard)
<img width="1913" height="924" alt="Screenshot 2026-01-12 222906" src="https://github.com/user-attachments/assets/ee09f067-6fdb-4f8a-a587-bbdeed2f55bc" />
<img width="1743" height="922" alt="Screenshot 2026-01-12 222726" src="https://github.com/user-attachments/assets/4a7359d8-8e37-4c5c-8299-2fc4b75dc11f" />
<img width="1916" height="922" alt="Screenshot 2026-01-12 222751" src="https://github.com/user-attachments/assets/cd99e8a6-3ba6-4bbe-bf4c-44d90e8c2953" />
<img width="1909" height="923" alt="Screenshot 2026-01-12 222805" src="https://github.com/user-attachments/assets/c0d724fd-9eb6-4eee-a9ed-3b32d0683302" />
<img width="1915" height="919" alt="Screenshot 2026-01-12 222821" src="https://github.com/user-attachments/assets/6bfa0e40-6e41-4403-920b-73d1c65e56e8" />
<img width="1916" height="914" alt="Screenshot 2026-01-12 222840" src="https://github.com/user-attachments/assets/288b80a8-67a3-44d3-aada-4bfda1b8994a" />


**Console excerpt** (real run):

```text
Cycle 03 ─────────────────────────────────────────────────────────────
VortexForge Vehicles → LLM evolved to Profit Focused (R&D:20%, Mkt:10%)
Reasoning: Given the current loss and low revenue growth, we need to prioritize profitability...

NovaVentures Payments → LLM evolved to Aggressive Growth (R&D:25%, Mkt:35%)
Reasoning: We're at a good market position but need to grow further...
```

**Dashboard** (Next.js frontend):

-   Overview: KPIs + live capital evolution chart
-   Companies: sortable/filterable table + detail sheet with reasoning history
-   Timeline: vertical cycle log with expandable LLM explanations

_(Add screenshots & 30–60s video demo here later)_

### Architecture

text

```
User → Next.js Dashboard (frontend)
       ↓ (polling / WebSocket)
FastAPI / Python Backend (optional bridge) ←→ SimulationEngine
                                           ↓
MarketWorld → industries, companies, economy
       ↓
CompanyAgent → holds state & acts each cycle
       ↓
StrategyAgent → LLM reasoning & strategy mutation
       ↓
LLMClient → Groq / OpenRouter
       ↓
MemoryStore → logs, snapshots, history
```

### Tech Stack

**Backend**

-   Python 3.10+
-   Custom agent simulation
-   OpenAI-compatible LLM client (Groq recommended)
-   python-dotenv, tqdm, numpy, pandas

**Frontend**

-   Next.js 15 (App Router) + TypeScript
-   shadcn/ui + Tailwind CSS
-   Recharts (charts)
-   @tanstack/react-table (companies table)
-   @tanstack/react-query (data fetching + polling)
-   lucide-react icons

### Quick Start (Local Development)

1.  **Clone the repository**

Bash

```
git clone https://github.com/YOUR_USERNAME/genesys.git
cd genesys
```

2.  **Backend Setup**

Bash

```
# Python virtual env
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install backend deps
pip install -r requirements.txt
```

3.  **Frontend Setup**

Bash

```
# Go to frontend folder (adjust path if different)
cd frontend

# Install Node dependencies
npm install

# OR with pnpm (recommended)
pnpm install
```

4.  **Configure LLM (free tier)**

Create .env in **root** (backend):

env

`# Groq (fastest & generous free tier) LLM_PROVIDER=groq LLM_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxx LLM_BASE_URL=https://api.groq.com/openai/v1 LLM_MODEL=llama-3.1-8b-instant`

5.  **Run Backend**

Bash

```
# In root folder
python main.py
```

6.  **Run Frontend Dashboard**

Bash

```
# In frontend folder
npm run dev
# or
pnpm dev
```

Open [http://localhost:3000/dashboard](http://localhost:3000/dashboard?referrer=grok.com)

### Project Structure

text

```
genesys/
├── main.py                     # Backend entry point
├── config/
│   └── config.py
├── core/
│   ├── engine.py
│   ├── world.py
│   ├── memory.py
│   └── llm_client.py
├── agents/
│   ├── company_agent.py
│   └── strategy_agent.py
├── generators/
│   ├── industry_generator.py
│   └── company_generator.py
├── frontend/                   # Next.js dashboard
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── types/
├── data/
│   └── simulations/
├── .env.example
├── requirements.txt
└── README.md
```

### Roadmap

-   WebSocket real-time updates (instead of polling)
-   Company post-mortem reports (LLM-generated)
-   Mergers & acquisitions logic
-   Saved simulation gallery
-   Export simulation animation/video
-   Mobile-responsive dashboard improvements

### Contributing

Pull requests welcome! For major changes, please open an issue first.

### License

MIT License — see the LICENSE file for details.

### Acknowledgments

Powered by free-tier LLMs — Groq & OpenRouter.

Created in 2026 by Tharusha
