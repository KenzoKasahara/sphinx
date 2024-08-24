import time


def timeit(func):
    """
    関数の実行時間を計測するデコレータ
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 開始時間を記録
        result = func(*args, **kwargs)  # 関数の実行
        end_time = time.time()  # 終了時間を記録
        elapsed_time = end_time - start_time  # 経過時間を計算
        print(f"Function '{func.__name__}' executed in {elapsed_time:.6f} seconds")
        return result
    return wrapper
