class Node:
    def __init__(self):
        self.all_file = []
        self.child = []
class FileSysytem:
    def __init__(self):
        self.dirs = {'my_com': {'files' : [], 'a': {'files': []}, 'd': {'files': []}, 's': {'files': [], 'f': {'files': []}, 't': {'files': [], 'q': {'files': []}}}}}
        self.ls = []
        self.curr = self.dirs["my_com"]
        
    def mkdir_with_path(self, path, name):
        path_list = path.split("/")[1:]
        self.curr = self.dirs[path_list[0]]
        for pa in path_list[1:]:
            self.curr = self.curr[pa]
        self.curr[str(name)] = {'files': []}
    
    def mkdir_no_path(self, name):
        self.curr[str(name)] = {'files': []}
    
    def creat_file(self, path, name):
        path_list = path.split("/")[1:]
        self.curr = self.dirs[path_list[0]]
        for pa in path_list[1:]:
            self.curr = self.curr[pa]
        self.curr['files'].append(str(name))
        
    def remove_dir(self, path):
        path_list = path.split("/")[1:]
        name_of_dir = path_list[-1]
        path_list = path.split("/")[1:-1]
        self.curr = self.dirs[path_list[0]]
        for pa in path_list[1:]:
            self.curr = self.curr[pa]
        self.curr.pop(str(name_of_dir))
        
fs = FileSysytem()
fs.mkdir_with_path('/my_com/s/t/q', 'sddd')
fs.mkdir_no_path("!@$@#")
fs.creat_file('/my_com/s/t/q', 'CS')
fs.remove_dir('/my_com/s/t/q/!@$@#')