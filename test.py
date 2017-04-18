#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from gittle import Gittle

def increment_bundle_number(plistfile,bundleVersion,repo):
    os.system('/usr/libexec/PlistBuddy -c "Set:CFBundleVersion %s" %s' % (bundleVersion,plistfile))
    repo.stage(plistfile)
    repo.commit(name="Samy Pesse", email="samy@friendco.de", message="This is a commit")

    repo.push()


if __name__ == '__main__':
    xctest_plist_file = os.getcwd() + "/xcstest/Info.plist"
    repo = Gittle(os.getcwd(),origin_uri='https://github.com/Cpplu11/xcstest.git')
    print(xctest_plist_file)
    increment_bundle_number(xctest_plist_file, 11, repo)

