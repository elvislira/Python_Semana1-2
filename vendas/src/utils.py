import time


# Decorator para medir tempo de execução
def log_time(func):
    def wrapper(*args, **kwargs):
        tempo_inicial = time.time()
        result = func(*args, **kwargs)
        print(f'\n⏱️ Tempo de execução de {func.__name__}: {time.time() - tempo_inicial:.4f}s')
        
        return result
    return wrapper
