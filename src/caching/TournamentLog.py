from caching.fileio import save_as_json_to_file, load_json_from_file


class TournamentLog:
    def __init__(self, file_path: str):
        self.file = file_path

    def add_code(self, code: str):
        data = load_json_from_file(self.file)
        data.append(code)
        save_as_json_to_file(path=self.file, content=data, indent=4)

    def check_code(self, code: str) -> bool:
        return code in load_json_from_file(self.file)
