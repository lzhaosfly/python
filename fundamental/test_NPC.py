import unittest

from NPC import NPC


class Test:
    def __init__(self, npc: NPC):
        self.npc = npc


class NPCTests(unittest.TestCase):
    def setUp(self):
        self.NPC = NPC("tester", 10, 10)

    def test_hp(self):
        """Test NPC hp"""
        self.assertEqual(self.NPC.hp, 10)
