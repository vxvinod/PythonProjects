import csv
import os
from _datetime import datetime

class DirectoyFileTracker:

    def __init__(self, directory):
        self.directory = directory
        self.file_list = []

    def get_all_files(self, file_path):
        print("Inside get all files")
        for path, _, files in os.walk(file_path):
            for file in files:
                yield os.path.join(path, file)
    def get_file_metadata(self, file_path):
        stat = os.stat(file_path)
        print(stat.st_size)
        return {
            "file_name": os.path.basename(file_path),
            "file_size_kb": round(stat.st_size/1024,2),
            "last_modified": datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
            "file_type": os.path.splitext(file_path)[1],
            "file_path": file_path
        }
    def scan(self, file_path):
        files = list(self.get_all_files(file_path))
        print(files)
        for path in files:
            meta = self.get_file_metadata(path)
            if meta:
                self.file_list.append(meta)
        return True


    def write_csv_report(self, output_file='file_report.csv'):
        if not self.file_list:
            print("No files to write")
        field_names = ["file_name", "file_size_kb", "last_modified", "file_type", "file_path"]
        with open(output_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(self.file_list)
        print("Output file written")


if __name__ == "__main__":
    print("test")
    file_path = "C:\\aws\\AUTOMATION_VM_LINUX_11"
    dft = DirectoyFileTracker(file_path)
    dft.scan(file_path)
    dft.write_csv_report()