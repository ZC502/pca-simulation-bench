from benchmarks.isaac.run_isaac import run as run_base

def run():
    # 假设插件已在 Isaac Sim Extension 中启用
    # runner 逻辑完全复用
    results = run_base()

    # 标记 system
    return results
