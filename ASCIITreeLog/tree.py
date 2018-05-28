
class TreeNode(object):
    """"""
    def __init__(self, name, time, docs):
        self.name = name
        self.time = time
        self.docs = docs
        self.childs = []
        self.parent = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return "TreeNode[{}]".format(self.name)

    def add_child(self, child):
        assert isinstance(child, TreeNode)
        self.childs.append(child)
        if child.parent != self:
            child.set_parent(self)

    def set_parent(self, parent):
        assert isinstance(parent, TreeNode)
        self.parent = parent
        if self not in parent.childs:
            parent.add_child(self)

    def get_root(self):
        if self.parent == None:
            return self
        else:
            return self.parent.get_root()
    