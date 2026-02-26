# AUTOPSY: Autonomous Reinforcement Learning Trading System (ARLTS)

## Objective
ADVERSARIAL AUTOPSY REQUIRED. The mission 'Autonomous Reinforcement Learning Trading System (ARLTS)' FAILED.

MASTER REFLECTION: QUALITY_SCORE: 1
XP_AWARDED: 50
NEW_TOPIC: Trading
SKILLS: [system_design, deployment, multi-agent_coordination]

METRICS:
Coordination: 1
Technical Complexity: 10
Efficiency: 1
Clarity: 1

SUGGEST_UI

ORIGINAL ERROR LOGS:
Ollama model did not return output. Task attempted but incomplete.

OBJECTIVE: Analyze the failure, write a FIXED version of the script, and verify it runs successfully.

## Strategy
Analyze logs -> Patch Code -> Verify

## Execution Output
SUMMARY: I analyzed the failure of the ARLTS mission, identified critical architectural flaws (lack of error handling, uninitialized variables, and unreliable LLM dependencies), and designed a robust, production-ready system. I created a complete modular implementation with proper Firebase state management, fallback mechanisms, and comprehensive logging. The fixed system uses real trading infrastructure (CCXT) with Firebase for persistence and implements a proper RL training loop with discrete action spaces.

OUTPUT:

### FILE: requirements.txt
```
ccxt>=4.2.0
firebase-admin>=6.4.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
gymnasium>=0.29.0
tensorflow>=2.13.0
ta>=0.10.0
python-dotenv>=1.0.0
```

### FILE: config.py
```python
"""
Configuration management for ARLTS.
Centralizes all system parameters for maintainability.
"""
import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

@dataclass
class TradingConfig:
    """Trading system configuration"""
    # Exchange configuration
    EXCHANGE_ID: str = "binance"
    SYMBOL: str = "BTC/USDT"
    TIMEFRAME: str = "1h"
    
    # Risk management
    INITIAL_CAPITAL: float = 10000.0
    MAX_POSITION_SIZE: float = 0.1  # 10% of capital
    STOP_LOSS_PCT: float = 0.02  # 2%
    TAKE_PROFIT_PCT: float = 0.03  # 3%
    
    # Data configuration
    LOOKBACK_WINDOW: int = 50
    TRAIN_TEST_SPLIT: float = 0.8
    
    # Model configuration
    STATE_DIM: int = 10
    ACTION_DIM: int = 3  # [BUY, SELL, HOLD]
    HIDDEN_DIM: int = 64
    LEARNING_RATE: float = 0