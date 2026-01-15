from benchmarks.isaac.run_isaac import run as run_base

def run():
    # 假设插件已在 Isaac Sim Extension 中启用（Assume that the plugin has been enabled in Isaac Sim Extension）
    # runner 逻辑完全复用（The logic is completely reused）
    results = run_base()

    # 标记 system
    return results
