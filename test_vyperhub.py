# test_vyperhub.py
"""
Tests for VyperHub module.
"""

import unittest
from vyperhub import VyperHub

class TestVyperHub(unittest.TestCase):
    """Test cases for VyperHub class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VyperHub()
        self.assertIsInstance(instance, VyperHub)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VyperHub()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
