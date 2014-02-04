#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from imp import find_module, load_module
from sys import exit

class ByteBotPluginLoader:
    PLUGINS = {} 

    def __init__(self, plugins, plugin_path='plugins'):
        """
        plugins:        tupel with plugins
        plugin_path:    path to plugins
                        MUST NOT end with a trailing slash
        """
        plugin_path = plugin_path.replace('/', '.')
        for plugin in plugins:
            try:
                self.PLUGINS[plugin] = getattr(
                    __import__("%s.%s" % (plugin_path, plugin)).__dict__[plugin],
                    plugin.title()
                )
            except Exception, e:
                print("FATAL: Could not import plugin %s" % plugin)
                print(e)
                #exit(255)

    def runCommands(self, fn, args={}):
        pass