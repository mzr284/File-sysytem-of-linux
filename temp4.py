import copy

class FileSysytem:
    def __init__(self):
        self.dirs = {'my_com': {'files': {}, "Parent": None}}
        self.main_current = self.dirs["my_com"]
        self.curr = self.dirs["my_com"]
        
    def switch_to_sub_directories(self, name_of_sub_directory):
        try:
            self.main_current = self.main_current[name_of_sub_directory]
        except:
            print(f"The folder with title : {name_of_sub_directory} is not found")
            
    def switch_to_sub_directories_curr(self, name_of_sub_directory):
        try:
            self.curr = self.curr[name_of_sub_directory]
        except:
            print(f"The folder with title : {name_of_sub_directory} is not found")
            
    def change_dir_nesbi(self, order_path):
        try:
            order_list = order_path.split("/")[1:]
            for pa in order_list:
                self.switch_to_sub_directories(pa)
        except:
            print("The path is not available")
            
    def change_curr_nesbi(self, order_path):
        order_list = order_path.split("/")[1:]
        self.curr = self.main_current
        for pa in order_list:
            self.switch_to_sub_directories_curr(pa)
            
    def change_dir(self, order_path):
        if "/" in order_path:
            try:
                if "/my_com" in order_path:
                    order_list = order_path.split("/")[1:]
                    self.curr = self.dirs[order_list[0]]
                    for pa in order_list[1:]:
                        self.curr = self.curr[pa]
                    self.main_current = self.curr
                else:
                    self.change_dir_nesbi(order_path)
            except:
                print("The path is not available")
        else:
            if self.main_current["Parent"] != None:
                self.main_current = self.main_current["Parent"]
            else:
                print("you are is already in the root, if you return to parent you can't go up!")
                
    def return_to_parent_for_main_curent(self):
        self.main_current = self.main_current["Parent"]
            
    def change_curr(self, order_path):
        if "/my_com" in order_path:
            try:
                order_list = order_path.split("/")[1:]
                self.curr = self.dirs[order_list[0]] 
                for pa in order_list[1:]:
                    self.curr = self.curr[pa]
            except:
                print("The path is not available")
        else:
            self.change_curr_nesbi(order_path)
            
    def return_to_parent(self):    # for self.curr
        self.curr = self.curr["Parent"]
            
    def mkdir_with_path(self, path, name):
        self.change_curr(path)
        self.curr[str(name)] = {'files': {}, "Parent": self.curr}
        print("The dir created successfully")
            
    def mkdir_no_path(self, name):
        self.main_current[str(name)] = {'files': {}, "Parent": self.curr}
        print("The dir created successfully")
        
    def is_sub_directory(self, path):
        while self.main_current != None:
            if self.main_current == path:
                return 1
            else:
                self.return_to_parent_for_main_curent()
        return 0
    
    def remove_dir(self, path):
        main_current = self.main_current
        self.change_curr(path)
        name_of_dir = path.split("/")[-1]
        if self.is_sub_directory(self.curr):
            self.main_current = self.dirs["my_com"]
            print("you have been transfered to the root")
        else:
            self.main_current = main_current
        self.return_to_parent()
        self.curr.pop(str(name_of_dir))
        print("The dir remove successfully")
        
    def creat_file_txt(self, path, name):
        self.change_curr(path)
        self.curr['files'][str(name) + '.txt'] = []
        print(f"The {name}.txt created successfully")
                
    def file_txt_no_path(self, name):
        self.main_current["files"][str(name) + '.txt'] = []
        print(f"File '{name}.txt' created in the current directory.")
        
    def remove_file_txt(self, path):
        name_of_file = path.split("/")[-1]
        new_path = path.replace(f"/{name_of_file}", '')
        self.change_curr(new_path)
        self.curr["files"].pop(name_of_file)
        print("The txt file removed")

    def write_new_file_txt(self, path):
        name_of_file = path.split("/")[-1]
        new_path = path.replace(f"/{name_of_file}", '')
        self.change_curr(new_path)
        file_txt = self.curr["files"][name_of_file]
        file_txt.clear()
        input_line = ""
        while input_line != "exit":
            input_line = input()
            file_txt.append(input_line)
        file_txt.pop()
        print("The overwrite successfully")
        
    def append_text(self, path):
        name_of_file = path.split("/")[-1]
        new_path = path.replace(f"/{name_of_file}", '')
        self.change_curr(new_path)
        file_txt = self.curr["files"][name_of_file]
        input_line = ""
        while input_line != "exit":
            input_line = input()
            file_txt.append(input_line)
        file_txt.pop()
        print("The append text is successfully")
      
    def edit_line(self, path, number_of_line: int, list_text_of_line: list):  
        name_of_file = path.split("/")[-1]
        new_path = path.replace(f"/{name_of_file}", '')
        self.change_curr(new_path)
        file_txt = self.curr["files"][name_of_file]
        text_of_line = ""
        for word in list_text_of_line:
            text_of_line += word
            text_of_line += " "
        file_txt[number_of_line - 1] = text_of_line[:-1]
        print("The edit successfully")
        
    def delete_line(self, path, number_of_line: int): 
        name_of_file = path.split("/")[-1]
        new_path = path.replace(f"/{name_of_file}", '')
        self.change_curr(new_path)
        file_txt = self.curr["files"][name_of_file]
        file_txt.pop(number_of_line - 1)
        print(f"The line of {number_of_line} has deleted")
        
    def veiw_of_text(self, path):
        name_of_file = path.split("/")[-1]
        new_path = path.replace(f"/{name_of_file}", '')
        self.change_curr(new_path)
        file_txt = self.curr["files"][name_of_file]
        for line in file_txt:
            print(f"- {line}")
        
    def move(self, source_path, destination_path):
        if not source_path.endswith(".txt"):
            name_of_source = source_path.split("/")[-1]
            self.change_curr(source_path)
            folder_moved = self.curr
            parent_of_source_path = folder_moved["Parent"]
            self.change_curr(destination_path)
            self.curr[name_of_source] = folder_moved
            self.curr[name_of_source]['Parent'] = self.curr
            parent_of_source_path.pop(name_of_source)
            print("The mission of move path is completed")
        else:
            name_of_file = source_path.split("/")[-1]
            new_source_path = source_path.replace(f"/{name_of_file}", '')
            self.change_curr(new_source_path)
            file_txt_moved = self.curr["files"][name_of_file]
            self.curr["files"].pop(name_of_file)
            self.change_curr(destination_path)
            self.curr["files"][name_of_file] = file_txt_moved
            print("The mission of move file txt is completed")
        
    def copy(self, source_path, destination_path):
        if not source_path.endswith(".txt"):
            name_of_source = source_path.split("/")[-1]
            self.change_curr(source_path)
            folder_copyed = copy.deepcopy(self.curr)
            self.change_curr(destination_path)
            self.curr[name_of_source] = folder_copyed
            self.curr[name_of_source]["Parent"] = self.curr
            print("The mission of copy path is completed")
        else:
            name_of_file = source_path.split("/")[-1]
            new_source_path = source_path.replace(f"/{name_of_file}", '')
            self.change_curr(new_source_path)
            file_txt_copyed = copy.deepcopy(self.curr["files"][name_of_file])
            self.change_curr(destination_path)
            self.curr["files"][name_of_file] = file_txt_copyed
            print("The mission of copy file txt is completed")

    def rename(self, path, new_name):
        if not path.endswith(".txt"):
            before_name = path.split("/")[-1]
            self.change_curr(path)
            parent = self.curr["Parent"]
            parent.pop(before_name)
            new_name_1 = ""
            for word in new_name:
                new_name_1 += word
                new_name_1 += " "
            new_name_1 = new_name_1[:-1]
            parent[new_name_1] = self.curr
            print(f"The name of folder changed to {new_name_1}")
        else:
            before_name = path.split("/")[-1]
            new_path = path.replace(f"/{before_name}", '')
            self.change_curr(new_path)
            text_of_file = self.curr["files"][before_name]
            self.curr["files"].pop(before_name)
            new_name_1 = ""
            for word in new_name:
                new_name_1 += word
                new_name_1 += " "
            new_name_1 = new_name_1[:-1]
            self.curr["files"][new_name_1 + ".txt"] = text_of_file
            print(f"The name of file changed to {new_name_1}")
        
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
        
# for example:     

fs = FileSysytem()
fs.mkdir_with_path("/my_com", "a")
fs.mkdir_no_path("b")
fs.mkdir_with_path("/my_com/a", "x")
fs.change_dir("/my_com/a/x")
fs.change_dir("cd")
fs.change_dir("cd")
fs.creat_file_txt("/my_com", "40313016")
fs.file_txt_no_path("40000")
fs.dirs["my_com"]["files"]["40313016.txt"] = ["a", "b", "c"]
fs.edit_line("/my_com/40313016.txt", 2, "B")
fs.move("/my_com/a/x", "/my_com/b")
fs.mkdir_with_path("/my_com/b", 'L')
fs.mkdir_with_path("/my_com/b/L", "F")
fs.mkdir_with_path("/my_com/b/L", "R")
fs.creat_file_txt("/my_com/b/L", "Q")
fs.mkdir_with_path("/my_com/b/L/F", "U")
fs.rename("/my_com/b/L", ["ASSD"])
fs.copy('/my_com/40313016.txt', "/my_com/b")

############################

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
                    self.file_system.move(source_path, destination_path)
                    
                if order_in_terminal[0] == "cp":
                    source_path = order_in_terminal[1]
                    destination_path = order_in_terminal[2]
                    self.file_system.copy(source_path, destination_path)
                    
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


















