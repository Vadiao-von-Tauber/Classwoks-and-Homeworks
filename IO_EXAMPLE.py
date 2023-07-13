# https://www.pythontutorial.net/python-basics/python-read-text-file/


class IOEngine:
    @staticmethod
    def read_text_file():
        # 'README01.txt
        # 'README02.txt
        # 'README03.txt

        # README01 open
        # README02 open
        # README03 open


        # README03 close
        # README02 close
        # README01 close

        with open('README01.txt') as f:
            lines = f.readlines()
            f.close()

            with open('README02.txt') as ff:
                lines = ff.readlines()

                with open('README03.txt') as fff:
                    lines = fff.readlines()

                    #fff.close()
                #ff.close()
            #f.close()