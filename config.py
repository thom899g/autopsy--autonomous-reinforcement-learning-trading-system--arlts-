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