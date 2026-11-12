from treelib import Tree
from itertools import count
from service.logging import debug

class JsonTree:
    def __init__(self, file_data):
        self._file_data = file_data
        debug.log("\nNew JsonTree instance with file data:", file_data)
        self.tree = Tree()
        self.id_counter = count()
        self.build(file_data)
    
    def next_id(self):
        return str(next(self.id_counter)) 

    def build(self, data, parent=None, name="root"):
        node_id = self.next_id()

        self.tree.create_node(name, node_id, parent=parent)

        if isinstance(data, dict):
            for key, value in data.items():
                self.build(value, node_id, key)

        elif isinstance(data, list):
            for i, item in enumerate(data):
                self.build(item, node_id, f"[{i}]")

        else:
            leaf_id = self.next_id()
            self.tree.create_node(str(data), leaf_id, parent=node_id)


    def get(self):
        return self.tree.show(stdout=False)
