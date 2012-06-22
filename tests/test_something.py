# -*- coding: utf-8 -*-

from unittest import TestCase

from main import app_factory
from config import Testing
from database import get_db

class SomethingTest(TestCase):

    def setUp(self):
        """docstring for setUp"""
        self.app = app_factory(Testing).test_client()
        self.db = get_db()

    def tearDown(self):
        """docstring for tearDown"""
        self.db = None

    def test_example(self):
        """Sample test"""
        response = self.app.get('/')
        self.assertIn("Hello, world!", response.data)
