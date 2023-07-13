class IOEngine:
    @staticmethod
    def read_text_file():
        with open('readme.txt') as f:
            lines = f.readlines()
            f.close()