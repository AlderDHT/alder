# -*- coding: utf-8 -*-
'''
Test database compression functions
'''
# Import alder libs
import alder.db

# Import python libs
import os
import random
import shutil
import unittest
import tempfile


class TestCompress(unittest.TestCase):
    '''
    Cover compression possibilities
    '''
    def test_compress_no_changes(self):
        '''
        Run a scale db execution with the given db kwargs
        '''
        entries = 100
        w_dir = tempfile.mkdtemp()
        root = os.path.join(w_dir, 'db_root')
        db = alder.db.DB(root)
        data = {1:1}
        for num in xrange(entries):
            key = str(num)
            db.insert(key, data)
        db.compress('', 0)
        for num in xrange(entries):
            key = str(num)
            pull_data = db.get(key)
            self.assertEqual(data, pull_data)
        shutil.rmtree(w_dir)

    def test_compress_no_changes_depth(self):
        '''
        Run a scale db execution with the given db kwargs
        '''
        entries = 100
        w_dir = tempfile.mkdtemp()
        root = os.path.join(w_dir, 'db_root')
        db = alder.db.DB(root)
        data = {1:1}
        key = 'foo/bar'
        for num in xrange(entries):
            db.insert(key, data)
        db.compress('foo', 0)
        for num in xrange(entries):
            pull_data = db.get(key)
            self.assertEqual(data, pull_data)
        shutil.rmtree(w_dir)

    def test_compress_changes(self):
        '''
        Compress a db with removed keys
        '''
        entries = 100
        w_dir = tempfile.mkdtemp()
        root = os.path.join(w_dir, 'db_root')
        db = alder.db.DB(root)
        rands = set()
        data = {1:1}
        for num in xrange(entries):
            key = str(num)
            db.insert(key, data)
        for _ in xrange(entries):
            rands.add(random.randint(0, entries - 1))
        for key in rands:
            db.rm(str(key))
        db.compress('', 0)
        for num in xrange(entries):
            key = str(num)
            pull_data = db.get(key)
            if num in rands:
                self.assertIsNone(pull_data)
            else:
                self.assertEqual(data, pull_data)
        shutil.rmtree(w_dir)

    def test_compress_changes_depth(self):
        '''
        Run a scale db execution with the given db kwargs
        '''
        entries = 100
        w_dir = tempfile.mkdtemp()
        root = os.path.join(w_dir, 'db_root')
        db = alder.db.DB(root)
        data = {1:1}
        key = 'foo/bar'
        ids = []
        rm_ids = set()
        for num in xrange(entries):
            ids.append(db.insert(key, data)['id'])
        for _ in xrange(entries):
            rm_ids.add(ids[random.randint(0, entries - 1)])
        for rm_id in rm_ids:
            db.rm(key, rm_id)
        db.compress('foo', 0)
        for num in xrange(entries):
            pull_data = db.get(key)
            self.assertEqual(data, pull_data)
        shutil.rmtree(w_dir)
