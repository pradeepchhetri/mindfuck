#!/usr/bin/env python

import os
import pytest
import mindfuck

def load_from_file(brainfuck_code):
    cwd = os.path.dirname(__file__)
    fpath = os.path.join(cwd, 'data/%s' % brainfuck_code)
    with open(fpath, 'r') as f:
        return f.read()

def test_hello_world(capfd):
    code = load_from_file("helloworld.bf")
    mindfuck.eval(code)
    output, error = capfd.readouterr()
    assert output=="Hello World!\n"

def test_foobar(capfd):
    code = load_from_file("foobar.bf")
    mindfuck.eval(code)
    output, error = capfd.readouterr()
    assert output!="foobar"
