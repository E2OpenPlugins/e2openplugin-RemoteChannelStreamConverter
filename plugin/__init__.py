# -*- coding: utf-8 -*-
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
from os import environ as os_environ
import gettext


def localeInit():
	gettext.bindtextdomain("RemoteChannelStreamConverter", resolveFilename(SCOPE_PLUGINS, "Extensions/RemoteChannelStreamConverter/locale"))


def _(txt):
	t = gettext.dgettext("RemoteChannelStreamConverter", txt)
	if t == txt:
		print("[RemoteChannelStreamConverter] fallback to default translation for", txt)
		t = gettext.gettext(txt)
	return t


localeInit()
language.addCallback(localeInit)
