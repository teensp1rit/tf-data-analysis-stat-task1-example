import pandas as pd
import numpy as np


chat_id = 332487463 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    y = np.array([(i + 27 - np.random.exponential(1)) / 10 for i in x])
    return y.mean() # Ваш ответ
