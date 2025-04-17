import json
class LogAnalyzer:

    def __init__(self):
        self.file_content = None
        self.log_levels_count = {}
    def read_log(self, file_path):
        with open(file_path, 'r') as file:
            self.file_content = file.readlines()

    def print_content(self):
        print(self.file_content)

    def extract_count_from_log_file(self):
        for line in self.file_content:
            if line.startswith('['):
                log_level = line.split(']')[0][1:]
                self.log_levels_count[log_level] = self.log_levels_count.get(log_level, 0) + 1

    def save_to_json(self, out_file='log_count.json'):
        with open(out_file, 'w') as file:
            json.dump(self.log_levels_count, file, indent=2)

if __name__ == '__main__':
    la = LogAnalyzer()
    la.read_log('server.log')
    la.extract_count_from_log_file()
    print(la.log_levels_count)
    la.save_to_json()