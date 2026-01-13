# generators/industry_generator.py
"""
Generates industry definitions with economic characteristics.
"""
import random
from typing import Dict, List

INDUSTRY_TEMPLATES = [
    {
        "name": "SaaS Productivity",
        "description": "Cloud-based tools for teams (CRM, project mgmt, collab)",
        "growth_rate_mean": 0.18,   # monthly growth potential
        "volatility": 0.09,
        "capital_intensity": "low",
        "barriers": "medium",       # switching costs, network effects
        "customer_type": "B2B"
    },
    {
        "name": "Electric Vehicles",
        "description": "Manufacturing & charging infrastructure for EVs",
        "growth_rate_mean": 0.12,
        "volatility": 0.15,
        "capital_intensity": "very_high",
        "barriers": "high",
        "customer_type": "B2C + B2G"
    },
    {
        "name": "Fintech Payments",
        "description": "Digital wallets, cross-border payments, neobanks",
        "growth_rate_mean": 0.15,
        "volatility": 0.11,
        "capital_intensity": "medium",
        "barriers": "regulatory + trust",
        "customer_type": "B2C + B2B"
    },
    {
        "name": "HealthTech Telemedicine",
        "description": "Remote care, AI diagnostics, wearables integration",
        "growth_rate_mean": 0.14,
        "volatility": 0.08,
        "capital_intensity": "medium",
        "barriers": "regulatory + data privacy",
        "customer_type": "B2C + B2B"
    }
]


def generate_industries(num_industries: int = 3) -> List[Dict]:
    """Randomly select and slightly randomize industry params"""
    if num_industries > len(INDUSTRY_TEMPLATES):
        num_industries = len(INDUSTRY_TEMPLATES)

    selected = random.sample(INDUSTRY_TEMPLATES, num_industries)

    for industry in selected:
        # Add some randomness to make each simulation unique
        industry["growth_rate"] = random.gauss(
            industry["growth_rate_mean"],
            industry["volatility"]
        )
        industry["demand"] = 100.0  # normalized market size (will grow/shrink)

    return selected