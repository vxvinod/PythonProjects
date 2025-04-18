

class LogRotator:

    def __init__(self, file):
        self.file = file

    def rotate_logs(self):
        with open(self.file, 'r') as file:
            for line in file:
                date = line.split()[1]
                if date:
                    file_name = f"server_{date}.log"
                    with open(file_name, 'a') as f:
                        f.write(line)









if __name__ == '__main__':
    lr = LogRotator('server.log')
    lr.rotate_logs()