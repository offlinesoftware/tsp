from treelib import Tree

class JsonToTree:

    def next_id():
        return str(next(id_counter)) 

    def json_to_tree(data, parent=None, name="root"):
        node_id = next_id()

        tree.create_node(name, node_id, parent=parent)

        if isinstance(data, dict):
            for key, value in data.items():
                json_to_tree(value, node_id, key)

        elif isinstance(data, list):
            for i, item in enumerate(data):
                json_to_tree(item, node_id, f"[{i}]")

        else:
            leaf_id = next_id()
            tree.create_node(str(data), leaf_id, parent=node_id)