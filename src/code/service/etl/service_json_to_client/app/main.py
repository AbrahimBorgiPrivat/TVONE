import importlib
import os
from pathlib import Path

from libraries.utils import runtime


def run_runner(module_path: str, runtime_json_path: Path) -> None:
    print(f"\n[main] Running {module_path} using {runtime_json_path}")
    module = importlib.import_module(module_path)
    if not hasattr(module, "main"):
        raise AttributeError(f"Module {module_path} has no 'main' function")

    runtime_vars = runtime.load_runtime_vars(JSON_PATH=runtime_json_path)
    print(runtime_vars)
    module.main(runtime_vars)
    print(f"[main] Completed: {runtime_json_path.name}")


if __name__ == "__main__":
    current_dir = Path(__file__).resolve().parent
    runtime_base = current_dir.parent / "runtime_definitions" / "json_to_client" / "runtime"
    runner_module = os.getenv("RUNNER_MODULE", "libraries.runners.runners")
    runtime_files_env = os.getenv("RUNTIME_FILES", "seasons.json")
    runtime_files = [filename.strip() for filename in runtime_files_env.split(",") if filename.strip()]

    for filename in runtime_files:
        runtime_json = runtime_base / filename
        if not runtime_json.exists():
            print(f"[main] Warning: {runtime_json} not found, skipping.")
            continue
        run_runner(runner_module, runtime_json)

    print("\n[main] All runtime files processed successfully.")
