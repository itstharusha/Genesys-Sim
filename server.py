"""
Flask API server for GeneSys Simulation
Exposes REST endpoints to run and monitor simulations
"""
import os
import json
from flask import Flask, jsonify, request
from flask_cors import CORS

# Load .env before importing anything else
from dotenv import load_dotenv
load_dotenv()

# Now import core modules
from core.engine import SimulationEngine
from core.world import MarketWorld

app = Flask(__name__)
CORS(app)

# Global simulation state
simulation_state = {
    "engine": None,
    "is_running": False,
    "current_cycle": 0,
    "total_cycles": 0,
    "companies": [],
    "market_data": None,
    "history": {
        "cycle": [],
        "company": [],
        "capital": [],
        "market_share": []
    }
}


@app.route("/api/health", methods=["GET"])
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok", "message": "GeneSys Sim API running"})


@app.route("/api/simulation/status", methods=["GET"])
def get_simulation_status():
    """Get current simulation status"""
    return jsonify({
        "is_running": simulation_state["is_running"],
        "current_cycle": simulation_state["current_cycle"],
        "total_cycles": simulation_state["total_cycles"],
        "progress": (
            simulation_state["current_cycle"] / simulation_state["total_cycles"] * 100
            if simulation_state["total_cycles"] > 0
            else 0
        )
    })


@app.route("/api/simulation/run", methods=["POST"])
def run_simulation():
    """Start a new simulation"""
    try:
        data = request.json or {}
        num_cycles = data.get("num_cycles", 12)
        
        if simulation_state["is_running"]:
            return jsonify({"error": "Simulation already running"}), 400
        
        # Reset state
        simulation_state["is_running"] = True
        simulation_state["current_cycle"] = 0
        simulation_state["total_cycles"] = num_cycles
        simulation_state["companies"] = []
        simulation_state["history"] = {
            "cycle": [],
            "company": [],
            "capital": [],
            "market_share": []
        }
        
        # Create and run engine
        simulation_state["engine"] = SimulationEngine(num_cycles=num_cycles)
        engine = simulation_state["engine"]
        
        # Run simulation step by step for live updates
        for cycle in range(1, num_cycles + 1):
            simulation_state["current_cycle"] = cycle
            
            # Run cycle
            engine.current_cycle = cycle
            engine.memory.state.cycle = cycle
            engine.world.update_market_conditions()
            
            # Get companies data
            alive = engine.world.get_all_alive_companies()
            companies_data = []
            
            for agent in alive:
                d = agent.data
                strategy = d.get("strategy", {})
                # Ensure strategy has a focus field
                if not isinstance(strategy, dict):
                    strategy = {}
                if "focus" not in strategy:
                    strategy["focus"] = "Growth"
                
                companies_data.append({
                    "name": d["name"],
                    "capital": d["capital"],
                    "market_share": d["market_share"],
                    "last_profit": d.get("last_profit", 0),
                    "last_revenue": d.get("last_revenue", 0),
                    "strategy": strategy,
                    "industry": d.get("industry", "Unknown")
                })
                
                # Update history
                simulation_state["history"]["cycle"].append(cycle)
                simulation_state["history"]["company"].append(d["name"])
                simulation_state["history"]["capital"].append(d["capital"])
                simulation_state["history"]["market_share"].append(d["market_share"])
            
            simulation_state["companies"] = sorted(
                companies_data,
                key=lambda x: x["capital"],
                reverse=True
            )
            simulation_state["market_data"] = {
                "economic_growth": engine.world.market_conditions.get("economic_growth", 0),
                "tech_innovation": engine.world.market_conditions.get("tech_innovation", 0),
                "market_volatility": engine.world.market_conditions.get("market_volatility", 0)
            }
        
        simulation_state["is_running"] = False
        
        return jsonify({
            "message": "Simulation completed",
            "cycles": num_cycles,
            "companies": len(simulation_state["companies"])
        })
    
    except Exception as e:
        simulation_state["is_running"] = False
        return jsonify({"error": str(e)}), 500


@app.route("/api/simulation/data", methods=["GET"])
def get_simulation_data():
    """Get latest simulation data"""
    return jsonify({
        "companies": simulation_state["companies"],
        "market_data": simulation_state["market_data"],
        "history": simulation_state["history"],
        "current_cycle": simulation_state["current_cycle"],
        "total_cycles": simulation_state["total_cycles"]
    })


@app.route("/api/companies", methods=["GET"])
def get_companies():
    """Get list of all companies"""
    return jsonify({
        "companies": simulation_state["companies"],
        "count": len(simulation_state["companies"])
    })


@app.route("/api/companies/<name>", methods=["GET"])
def get_company(name):
    """Get specific company details"""
    company = next(
        (c for c in simulation_state["companies"] if c["name"].lower() == name.lower()),
        None
    )
    if company:
        return jsonify(company)
    return jsonify({"error": "Company not found"}), 404


@app.route("/api/market", methods=["GET"])
def get_market_data():
    """Get current market conditions"""
    return jsonify(simulation_state["market_data"] or {})


@app.route("/api/history", methods=["GET"])
def get_history():
    """Get simulation history"""
    return jsonify(simulation_state["history"])


if __name__ == "__main__":
    port = int(os.getenv("FLASK_PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
