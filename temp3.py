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
            print(f"The {name}.txt created successfully")
        except:
            print("The path is not available")
            
    def file_txt_no_path(self, name):
        self.main_current["files"][str(name) + '.txt'] = []
        print(f"File '{name}.txt' created in the current directory.")
        
    def remove_file_txt(self, path):
        try:
            path_list = path.split("/")[1:]
            name_of_path = path_list[-1]
            self.curr = self.dirs[path_list[0]]
            for pa in path_list[1:-1]:
                self.curr = self.curr[pa]
            self.curr["files"].pop(name_of_path)
            print("The txt file removed")
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
      try:  
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
            file_txt.append(input_line)
        file_txt.pop()
      except:
          print("The path is not available")
          
    def append_text(self, path):
      try:  
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
            file_txt.append(input_line)
        file_txt.pop()
      except:  
        print("The path is not available")
        
    def edit_line(self, path, number_of_line: int, list_text_of_line: list):
      try:  
        path_list = path.split("/")[1:]
        name_of_txt = path_list[-1]
        dir_of_txt = path_list[1:-1]
        self.curr = self.dirs["my_com"]
        for pa in dir_of_txt:
            self.curr = self.curr[pa]
        file_txt = self.curr["files"][name_of_txt]
        text_of_line = ""
        for word in list_text_of_line:
            text_of_line += word
            text_of_line += " "
        file_txt[number_of_line - 1] = text_of_line[:-1]
        print("The edit successfully")
      except:
          print("The path is not available")
        
        
    def delete_line(self, path, number_of_line: int):
      try:  
        path_list = path.split("/")[1:]
        name_of_txt = path_list[-1]
        dir_of_txt = path_list[1:-1]
        self.curr = self.dirs["my_com"]
        for pa in dir_of_txt:
            self.curr = self.curr[pa]
        file_txt = self.curr["files"][name_of_txt]
        file_txt.pop(number_of_line - 1)
        print(f"The line of {number_of_line} has deleted")
      except:
          print("The path is not available")
        
    def veiw_of_text(self, path):
      try:  
        path_list = path.split("/")[1:]
        name_of_txt = path_list[-1]
        dir_of_txt = path_list[1:-1]
        self.curr = self.dirs["my_com"]
        for pa in dir_of_txt:
            self.curr = self.curr[pa]
        file_txt = self.curr["files"][name_of_txt]
        for line in file_txt:
            print(f"- {line}")
      except:
          print("The path is not available")
        
    def move_path(self, source_path, destination_path):
      try:  
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
        print("The mission of move path is completed")
      except:
          print("The path is not available")
        
    def copy_path(self, source_path, destination_path):
      try:  
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
        print("The mission of copy path is completed")
      except:
          print("The path is not available")
        
    def rename(self, path, new_name):
      try:
        path_list = path.split("/")[1:]
        before_name = path_list[-1]
        self.curr = self.dirs[path_list[0]]
        for pa in path_list[1:]:
            self.curr = self.curr[pa]
        parent = self.curr["Parent"]
        parent.pop(before_name)
        new_name_1 = ""
        for word in new_name:
            new_name_1 += word
            new_name_1 += " "
        new_name_1 = new_name_1[:-1]
        parent[new_name_1] = self.curr
        print(f"The name changed to {new_name_1}")
      except:
        print("The path is not available")
        
    def all_sub_directories(self):
        print("- folders:")
        for dirs_name in self.main_current.keys():
            if dirs_name  != "files" and dirs_name != "Parent":
                print(dirs_name, end= "   ")
        print("\n")
        print("- files:")
        for file in self.main_current["files"]:
            print(file, end= "   ")
        print("\n")    
        
        

fs = FileSysytem()
fs.mkdir_with_path("/my_com", "a")
fs.mkdir_no_path("b")
fs.mkdir_with_path("/my_com/a", "x")
fs.change_dir("/my_com/a/x")
fs.change_dir("cd")
fs.creat_file_txt("/my_com", "40313016")
fs.file_txt_no_path("40000")
fs.remove_file_txt("/my_com/a/40000.txt")
fs.dirs["my_com"]["files"]["40313016.txt"] = ["a", "b", "c"]
fs.edit_line("/my_com/40313016.txt", 2, "B")
fs.move_path("/my_com/a/x", "/my_com/b") 
fs.mkdir_with_path("/my_com/b", 'L')
fs.mkdir_with_path("/my_com/b/L", "F")
fs.mkdir_with_path("/my_com/b/L", "R")
fs.creat_file_txt("/my_com/b/L", "Q")
fs.mkdir_with_path("/my_com/b/L/F", "U")
fs.rename("/my_com/b/L", ["ASSD"])
class Terminal:
    def __init__(self, file_system: FileSysytem):
        self.file_system = file_system
        
    def handling_of_terminal(self):
        order_in_terminal = [""]

        while order_in_terminal[0] != "end":
            try:
                order_in_terminal = input(">>  ").split(" ")
                if order_in_terminal[0] == "mkdir":
                    if len(order_in_terminal) == 2:
                        name = order_in_terminal[1]
                        self.file_system.mkdir_no_path(name)
                    else:
                        path = order_in_terminal[1]
                        name = order_in_terminal[2]
                        self.file_system.mkdir_with_path(path, name)
                        
                if order_in_terminal[0] == "cd":
                    if len(order_in_terminal) == 1:
                        self.file_system.change_dir("")
                    else:
                        path = order_in_terminal[1]
                        if "/" in order_in_terminal[1]:
                            self.file_system.change_dir(path)
                        else:
                            self.file_system.switch_to_sub_directories(path)
                        
                if order_in_terminal[0] == "rm":
                    if order_in_terminal[1].endswith(".txt"):
                        path = order_in_terminal[1]
                        self.file_system.remove_file_txt(path)                        
                    else:
                        path = order_in_terminal[1]
                        self.file_system.remove_dir(path)
                        
                if order_in_terminal[0] == "touch":
                    if len(order_in_terminal) == 2:
                        name = order_in_terminal[1]
                        self.file_system.file_txt_no_path(name)
                    else:
                        path = order_in_terminal[1]
                        name = order_in_terminal[2]
                        self.file_system.creat_file_txt(path, name)
                        
                if order_in_terminal[0] == "newfiletxt":
                    path = order_in_terminal[1]
                    self.file_system.write_new_file_txt(path)
                    
                if order_in_terminal[0] == "appendtxt":
                    path = order_in_terminal[1]
                    self.file_system.append_text(path)
                    
                if order_in_terminal[0] == "editline":
                    path = order_in_terminal[1]
                    number_of_line = int(order_in_terminal[2])
                    text_of_line = order_in_terminal[3:]
                    self.file_system.edit_line(path, number_of_line, text_of_line)
                    
                if order_in_terminal[0] == "deline":
                    path = order_in_terminal[1]
                    number_of_line = int(order_in_terminal[2])
                    self.file_system.delete_line(path, number_of_line)
                    
                if order_in_terminal[0] == "cat":
                    path = order_in_terminal[1]
                    self.file_system.veiw_of_text(path)
                    
                if order_in_terminal[0] == "mv":
                    source_path = order_in_terminal[1]
                    destination_path = order_in_terminal[2]
                    self.file_system.move_path(source_path, destination_path)
                    
                if order_in_terminal[0] == "cp":
                    source_path = order_in_terminal[1]
                    destination_path = order_in_terminal[2]
                    self.file_system.copy_path(source_path, destination_path)
                    
                if order_in_terminal[0] == "rename":
                    path = order_in_terminal[1]
                    new_name = order_in_terminal[2:]
                    self.file_system.rename(path, new_name)
                    
                if order_in_terminal[0] == "ls":
                    self.file_system.all_sub_directories()
                    
            except:
                print("The command is not correct")



# Start of Terminal

terminal = Terminal(fs)
terminal.handling_of_terminal()


















