from pathlib import Path
class Loader:
    _base_dir = Path(__file__).resolve().parent.parent
    _prompt_path = _base_dir/"prompts"/"planner"
    @staticmethod
    def load(filename:str)->str:
        return  (Loader._prompt_path/filename).read_text(encoding="utf-8")