# generators/company_generator.py
"""
Generates realistic AI-driven companies within an industry.
"""
import random
import uuid
from typing import Dict, List, Any

from config.config import (
    INITIAL_CAPITAL_RANGE,
    INITIAL_TALENT_POOL,
    DEFAULT_COMPANIES_PER_INDUSTRY
)


def generate_company_name(industry_name: str) -> str:
    """Generate plausible startup-style names"""
    prefixes = ["Neo", "Quantum", "Apex", "Vortex", "Nexus", "Pulse", "Strato", "Helix", "Nova", "Zenith"]
    suffixes = ["Labs", "Tech", "AI", "Solutions", "Systems", "Ventures", "Dynamics", "Forge", "Core", "Edge"]

    return f"{random.choice(prefixes)}{random.choice(suffixes)} {industry_name.split()[-1]}"


def generate_companies(industry: Dict[str, Any], num_companies: int = DEFAULT_COMPANIES_PER_INDUSTRY) -> List[
    Dict[str, Any]]:
    """
    Create list of company dicts for one industry.
    Each company is a dict with state that will evolve during simulation.
    """
    companies = []

    for _ in range(num_companies):
        company_id = str(uuid.uuid4())[:8]  # short unique id for logging

        company = {
            "id": company_id,
            "name": generate_company_name(industry["name"]),
            "industry": industry["name"],
            "capital": random.uniform(*INITIAL_CAPITAL_RANGE),
            "talent": INITIAL_TALENT_POOL + random.randint(-3, 5),  # slight variation
            "market_share": random.uniform(5.0, 35.0) / num_companies,  # rough initial split
            "health": 1.0,  # 0.0 = dead/bankrupt
            "strategy": None,  # to be filled by strategy agent
            "age_months": 0,
            "alive": True
        }

        companies.append(company)

    # Normalize initial market shares to sum ≈100% per industry
    total_share = sum(c["market_share"] for c in companies)
    if total_share > 0:
        for c in companies:
            c["market_share"] = (c["market_share"] / total_share) * 100.0

    return companies