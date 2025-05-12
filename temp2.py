import copy
class FileSysytem:
    def __init__(self):
        self.dirs = {'my_com': {'files': {}}}
        self.main_current = self.dirs["my_com"]
        self.curr = self.dirs["my_com"]
        
    def mkdir_with_path(self, path, name):
        try:
            path_list = path.split("/")[1:]
            self.curr = self.dirs[path_list[0]]
            for pa in path_list[1:]:
                self.curr = self.curr[pa]
            self.curr[str(name)] = {'files': {}, "Parent": self.curr}
        except:
            print("The path is not available")
            
    def mkdir_no_path(self, name):
        self.curr = self.main_current
        self.main_current[str(name)] = {'files': {}, "Parent": self.curr}
        
    def switch_to_sub_directories(self, name_of_sub_directory):
        try:
            self.main_current = self.main_current[name_of_sub_directory]
        except:
            print(f"The folder with title:{name_of_sub_directory} is not found")
            
    def remove_dir(self, path):
        try:
            path_list = path.split("/")[1:]
            name_of_dir = path_list[-1]
            path_list = path.split("/")[1:-1]
            self.curr = self.dirs[path_list[0]]
            for pa in path_list[1:]:
                self.curr = self.curr[pa]
            self.curr.pop(str(name_of_dir))
        except:
            print("The path is not available")
            
    def creat_file_txt(self, path, name):
        try:
            path_list = path.split("/")[1:]
            self.curr = self.dirs[path_list[0]]
            for pa in path_list[1:]:
                self.curr = self.curr[pa]
            self.curr['files'][str(name) + '.txt'] = []
        except:
            print("The path is not available")
            
    def file_txt_no_path(self, name):
        self.main_current["files"][str(name) + '.txt'] = []
        print(f"File '{name}.txt' created in the current directory.")

    def remove_file_txt(self, path, name):
        try:
            path_list = path.split("/")[1:]
            self.curr = self.dirs[path_list[0]]
            for pa in path_list[1:]:
                self.curr = self.curr[pa]
            self.curr["files"].pop(str(name) + ".txt")
        except:
            print("The path is not available")
        
    def change_dir(self, order_path):
        if "/" in order_path:
            try:
                order_list = order_path.split("/")[1:]
                self.curr = self.dirs[order_list[0]]
                for pa in order_list[1:]:
                    self.curr = self.curr[pa]
                self.main_current = self.curr
            except:
                print("The path is not available")
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
        
    def move_path(self, source_path, destination_path):
        name_of_source = source_path.split("/")[-1]
        source_path_list = source_path.split("/")[1:]
        self.curr = self.dirs[source_path_list[0]]
        for pa in source_path_list[1:]:
            self.curr = self.curr[pa]
        folder_moved = self.curr
        parent_of_source_path = folder_moved["Parent"]
        destination_path_list = destination_path.split("/")[1:]
        self.curr = self.dirs[destination_path_list[0]]
        for pa in destination_path_list[1:]:
            self.curr = self.curr[pa]
        self.curr[name_of_source] = folder_moved
        self.curr[name_of_source]['Parent'] = self.curr
        parent_of_source_path.pop(name_of_source)
        
    def copy_path(self, source_path, destination_path):
        name_of_source = source_path.split("/")[-1]
        source_path_list = source_path.split("/")[1:]
        self.curr = self.dirs[source_path_list[0]]
        for pa in source_path_list[1:]:
            self.curr = self.curr[pa]
        folder_copyed = copy.deepcopy(self.curr)
        destination_path_list = destination_path.split("/")[1:]
        self.curr = self.dirs[destination_path_list[0]]
        for pa in destination_path_list[1:]:
            self.curr = self.curr[pa]
        self.curr[name_of_source] = folder_copyed
        self.curr[name_of_source]["Parent"] = self.curr
        
    def rename(self, path, new_name):
        path_list = path.split("/")[1:]
        before_name = path_list[-1]
        self.curr = self.dirs[path_list[0]]
        for pa in path_list[1:]:
            self.curr = self.curr[pa]
        parent = self.curr["Parent"]
        parent.pop(before_name)
        parent[new_name] = self.curr
        
    def all_sub_directories(self):
        for dirs_name in self.main_current.keys():
            print(dirs_name, end= "     ")
        
        

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
fs.move_path("/my_com/a/x", "/my_com/b") 
fs.rename("/my_com/b", "B")
fs.rename("/my_com/B", "C")
fs.mkdir_with_path("/my_com/C", 'L')
fs.mkdir_with_path("/my_com/C/L", "F")
fs.mkdir_with_path("/my_com/C/L", "R")
fs.creat_file_txt("/my_com/C/L", "Q")
fs.mkdir_with_path("/my_com/C/L/F", "U")

# Start of Terminal

order_in_terminal = ""

while order_in_terminal != "end":
    try:
        order_in_terminal = input(">>  ").split(" ")
        if order_in_terminal[0] == "mkdir":
            if len(order_in_terminal) == 2:
                name = order_in_terminal[1]
                fs.mkdir_no_path(name)
    except:
        print("The command is not correct")




















