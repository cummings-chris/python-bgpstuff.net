#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bgpstuff
import unittest


class ClientTest(unittest.TestCase):
    def setUp(self):
        self.client = bgpstuff.Client()

    def test_get_route(self):
        self.client.get_route("8.8.8.8")
        self.assertEqual("8.8.8.0/24", self.client.route)
        with self.assertRaises(ValueError):
            self.client.get_route("10.0.0.0")

    def test_get_origin(self):
        self.client.get_origin("8.8.8.8")
        self.assertEqual(15169, self.client.origin)
        with self.assertRaises(ValueError):
            self.client.get_route("10.0.0.0")

    def test_get_as_path(self):
        self.client.get_as_path("8.8.8.8")
        self.assertEqual(15169, self.client.as_path[-1])

    def test_get_roa(self):
        self.client.get_roa("1.1.1.1")
        self.assertEqual("VALID", self.client.roa)
        with self.assertRaises(ValueError):
            self.client.get_route("10.0.0.0")

    def test_get_roa(self):
        self.client.get_as_name(15169)
        self.assertEqual("GOOGLE", self.client.as_name)
        with self.assertRaises(ValueError):
            self.client.get_route("hi")

    def test_get_totals(self):
        self.client.get_totals()
        self.assertGreater(self.client.total_v4, 800000)
        self.assertGreater(self.client.total_v6, 100000)

    def tearDown(self):
        self.client._close_session()
