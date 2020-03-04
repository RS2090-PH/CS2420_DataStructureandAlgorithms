import unittest
from linkedbst import LinkedBST

class UnitTests(unittest.TestCase):
    def test_preorder_traversal(self):
        t1 = LinkedBST()
        t1.add("W") #root
        t1.add("U")
        t1.add("T")
        t1.add("V")
        t1.add("Y")
        t1.add("X")
        t1.add("Z")
        s1 = ""
        for node in t1.preorder():
            s1 = s1 + node + " "
        s2 = "W U T V Y X Z "
        self.assertEqual(s1, s2)

    def test_preorder_traversal_left_to_right(self):
        t1 = LinkedBST()
        t1.add("W") #root
        t1.add("U")
        t1.add("T")
        t1.add("V")
        t1.add("Y")
        t1.add("X")
        t1.add("Z")
        s1 = ""
        for node in t1.preorder():
            s1 = s1 + node + " "
        s2 = "Z X Y V T U W "
        self.assertNotEqual(s1, s2)

    def test_preorder_traversal_not_inorder(self):
        t1 = LinkedBST()
        t1.add("W") #root
        t1.add("U")
        t1.add("T")
        t1.add("V")
        t1.add("Y")
        t1.add("X")
        t1.add("Z")
        s1 = ""
        for node in t1.preorder():
            s1 = s1 + node + " "
        s2 = "T U V W X Y Z "
        self.assertNotEqual(s1, s2)

    def test_preorder_traversal_not_postorder(self):
        t1 = LinkedBST()
        t1.add("W") #root
        t1.add("U")
        t1.add("T")
        t1.add("V")
        t1.add("Y")
        t1.add("X")
        t1.add("Z")
        s1 = ""
        for node in t1.preorder():
            s1 = s1 + node + " "
        s2 = "T V U X Z Y W "
        self.assertNotEqual(s1, s2)

    def test_preorder_traversal_not_levelorder(self):
        t1 = LinkedBST()
        t1.add("W") #root
        t1.add("U")
        t1.add("T")
        t1.add("V")
        t1.add("Y")
        t1.add("X")
        t1.add("Z")
        s1 = ""
        for node in t1.preorder():
            s1 = s1 + node + " "
        s2 = "W U Y T V X Z "
        self.assertNotEqual(s1, s2)

    def test_inorder_traversal(self):
        t1 = LinkedBST()
        t1.add("W") #root
        t1.add("U")
        t1.add("T")
        t1.add("V")
        t1.add("Y")
        t1.add("X")
        t1.add("Z")
        s1 = ""
        for node in t1.inorder():
            s1 = s1 + node + " "
        s2 = "T U V W X Y Z "
        self.assertEqual(s1, s2)

    def test_inorder_traversal_not_preorder(self):
        t1 = LinkedBST()
        t1.add("W") #root
        t1.add("U")
        t1.add("T")
        t1.add("V")
        t1.add("Y")
        t1.add("X")
        t1.add("Z")
        s1 = ""
        for node in t1.inorder():
            s1 = s1 + node + " "
        s2 = "W U T V Y X Z "
        self.assertNotEqual(s1, s2)

    def test_inorder_traversal_not_postorder(self):
        t1 = LinkedBST()
        t1.add("F") #root
        t1.add("E")
        t1.add("D")
        t1.add("C")
        t1.add("B")
        t1.add("A")
        s1 = "C D E A B F "
        for node in t1.inorder():
            s1 = s1 + node + " "
        s2 = "C E D F A B "
        self.assertNotEqual(s1, s2)

    def test_inorder_traversal_not_postorder(self):
        t1 = LinkedBST()
        t1.add("W") #root
        t1.add("U")
        t1.add("T")
        t1.add("V")
        t1.add("Y")
        t1.add("X")
        t1.add("Z")
        s1 = ""
        for node in t1.inorder():
            s1 = s1 + node + " "
        s2 = "T V U X Z Y W "
        self.assertNotEqual(s1, s2)

    def test_postorder_traversal(self):
        t1 = LinkedBST()
        t1.add("W") #root
        t1.add("U")
        t1.add("T")
        t1.add("V")
        t1.add("Y")
        t1.add("X")
        t1.add("Z")
        s1 = ""
        for node in t1.postorder():
            s1 = s1 + node + " "
        s2 = "T V U X Z Y W "
        self.assertEqual(s1, s2)

    def test_postorder_traversal_not_preorder(self):
        t1 = LinkedBST()
        t1.add("W") #root
        t1.add("U")
        t1.add("T")
        t1.add("V")
        t1.add("Y")
        t1.add("X")
        t1.add("Z")
        s1 = ""
        for node in t1.postorder():
            s1 = s1 + node + " "
        s2 = "W U T V Y X Z "
        self.assertNotEqual(s1, s2)

    def test_postorder_traversal_not_inorder(self):
        t1 = LinkedBST()
        t1.add("W") #root
        t1.add("U")
        t1.add("T")
        t1.add("V")
        t1.add("Y")
        t1.add("X")
        t1.add("Z")
        s1 = ""
        for node in t1.postorder():
            s1 = s1 + node + " "
        s2 = "T U V W X Y Z "
        self.assertNotEqual(s1, s2)

    def test_postorder_traversal_not_levelorder(self):
        t1 = LinkedBST()
        t1.add("W") #root
        t1.add("U")
        t1.add("T")
        t1.add("V")
        t1.add("Y")
        t1.add("X")
        t1.add("Z")
        s1 = ""
        for node in t1.postorder():
            s1 = s1 + node + " "
        s2 = "W U Y T V X Z "
        self.assertTrue(s1 != s2)

    def test_levelorder_traversal(self):
        t1 = LinkedBST()
        t1.add("W") #root
        t1.add("U")
        t1.add("T")
        t1.add("V")
        t1.add("Y")
        t1.add("X")
        t1.add("Z")
        s1 = ""
        for node in t1.levelorder():
            s1 = s1 + node + " "
        s2 = "W U Y T V X Z "
        self.assertEqual(s1, s2)

    def test_levelorder_traversal_not_preorder(self):
        t1 = LinkedBST()
        t1.add("W") #root
        t1.add("U")
        t1.add("T")
        t1.add("V")
        t1.add("Y")
        t1.add("X")
        t1.add("Z")
        s1 = ""
        for node in t1.levelorder():
            s1 = s1 + node + " "
        s2 = "W U T V Y X Z "
        self.assertNotEqual(s1, s2)

    def test_levelorder_traversal_not_postorder(self):
        t1 = LinkedBST()
        t1.add("W") #root
        t1.add("U")
        t1.add("T")
        t1.add("V")
        t1.add("Y")
        t1.add("X")
        t1.add("Z")
        s1 = ""
        for node in t1.levelorder():
            s1 = s1 + node + " "
        s2 = "T V U X Z Y W "
        self.assertNotEqual(s1, s2)

    def test_levelorder_traversal_not_inorder(self):
        t1 = LinkedBST()
        t1.add("W") #root
        t1.add("U")
        t1.add("T")
        t1.add("V")
        t1.add("Y")
        t1.add("X")
        t1.add("Z")
        s1 = ""
        for node in t1.levelorder():
            s1 = s1 + node + " "
        s2 = "T U V W X Y Z "
        self.assertNotEqual(s1, s2)
