# main.py
from core.engine import SimulationEngine

if __name__ == "__main__":
    engine = SimulationEngine(num_cycles=12)
    engine.run(verbose=True)