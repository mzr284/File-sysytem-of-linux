class FileSysytem:
    def __init__(self):
        self.dirs = {'my_com': {'files': {}}}
        self.ls = []
        self.main_current = self.dirs["my_com"]
        self.curr = self.dirs["my_com"]
        
    def mkdir_with_path(self, path, name):
        path_list = path.split("/")[1:]
        self.curr = self.dirs[path_list[0]]
        for pa in path_list[1:]:
            self.curr = self.curr[pa]
        self.curr[str(name)] = {'files': {}, "Parent": self.curr}

    def mkdir_no_path(self, name):
        self.curr = self.main_current
        self.main_current[str(name)] = {'files': {}, "Parent": self.curr}

    def remove_dir(self, path):
        path_list = path.split("/")[1:]
        name_of_dir = path_list[-1]
        path_list = path.split("/")[1:-1]
        self.curr = self.dirs[path_list[0]]
        for pa in path_list[1:]:
            self.curr = self.curr[pa]
        self.curr.pop(str(name_of_dir))

    def creat_file_txt(self, path, name):
        path_list = path.split("/")[1:]
        self.curr = self.dirs[path_list[0]]
        for pa in path_list[1:]:
            self.curr = self.curr[pa]
        self.curr['files'][str(name) + '.txt'] = []

    def file_txt_no_path(self, name):
        self.main_current["files"][str(name) + '.txt'] = []
        print(f"File '{name}.txt' created in the current directory.")

    def remove_file_txt(self, path, name):
        path_list = path.split("/")[1:]
        self.curr = self.dirs[path_list[0]]
        for pa in path_list[1:]:
            self.curr = self.curr[pa]
        self.curr["files"].pop(str(name) + ".txt")

    def change_dir(self, order_path):
        if "/" in order_path:
            order_list = order_path.split("/")[1:]
            self.curr = self.dirs[order_list[0]]
            for pa in order_list[1:]:
                self.curr = self.curr[pa]
            self.main_current = self.curr
        else:
            self.main_current = self.main_current["Parent"]
            self.curr = self.main_current
    
    def write_new_file_txt(self, path):
        path_list = path.split("/")[1:]
        name_of_txt = path_list[-1]
        dir_of_txt = path_list[1:-1]
        self.curr = self.dirs["my_com"]
        for pa in dir_of_txt:
            self.curr = self.curr[pa]
        file_txt = self.curr["files"][name_of_txt]
        file_txt.clear()
        input_line = ""
        while input_line != "exit":
            input_line = input()
            new_line = [input_line]
            file_txt.append(new_line)
        file_txt.pop()
        
    def append_text(self, path):
        path_list = path.split("/")[1:]
        name_of_txt = path_list[-1]
        dir_of_txt = path_list[1:-1]
        self.curr = self.dirs["my_com"]
        for pa in dir_of_txt:
            self.curr = self.curr[pa]
        file_txt = self.curr["files"][name_of_txt]
        input_line = ""
        while input_line != "exit":
            input_line = input()
            new_line = [input_line]
            file_txt.append(new_line)
        file_txt.pop()
        
    def edit_line(self, path, number_of_line: int, text_of_line):
        path_list = path.split("/")[1:]
        name_of_txt = path_list[-1]
        dir_of_txt = path_list[1:-1]
        self.curr = self.dirs["my_com"]
        for pa in dir_of_txt:
            self.curr = self.curr[pa]
        file_txt = self.curr["files"][name_of_txt]
        file_txt[number_of_line - 1] = list(text_of_line)
        
    def delete_line(self, path, number_of_line: int):
        path_list = path.split("/")[1:]
        name_of_txt = path_list[-1]
        dir_of_txt = path_list[1:-1]
        self.curr = self.dirs["my_com"]
        for pa in dir_of_txt:
            self.curr = self.curr[pa]
        file_txt = self.curr["files"][name_of_txt]
        file_txt.pop(number_of_line - 1)
        
    def veiw_of_text(self, path):
        path_list = path.split("/")[1:]
        name_of_txt = path_list[-1]
        dir_of_txt = path_list[1:-1]
        self.curr = self.dirs["my_com"]
        for pa in dir_of_txt:
            self.curr = self.curr[pa]
        file_txt = self.curr["files"][name_of_txt]
        for line in file_txt:
            print(line[0])
        
        

fs = FileSysytem()
fs.mkdir_with_path("/my_com", "a")
fs.mkdir_no_path("b")
fs.mkdir_with_path("/my_com/a", "x")
fs.change_dir("/my_com/a/x")
fs.change_dir("cd")
fs.creat_file_txt("/my_com", "40313016")
fs.file_txt_no_path("40000")
fs.remove_file_txt("/my_com/a", "40000")
fs.dirs["my_com"]["files"]["40313016.txt"] = [["a"], ["b"], ["c"]]
fs.edit_line("/my_com/40313016.txt", 2, "B")
fs.veiw_of_text("/my_com/40313016.txt")
