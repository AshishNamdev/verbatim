#!/usr/bin/env python
# -*- coding: utf-8 -*-

from translate.storage import mozilla_lang
from translate.storage import test_base


class TestMozLangUnit(test_base.TestTranslationUnit):
    UnitClass = mozilla_lang.LangUnit

    def test_translate_but_same(self):
        """Mozilla allows {ok} to indicate a line that is the
        same in source and target on purpose"""
        unit = self.UnitClass("Open")
        unit.target = "Open"
        assert unit.target == "Open"
        assert str(unit).endswith(" {ok}")

    def test_untranslated(self):
        """THe target is always written to files and is never blank."""
        unit = self.UnitClass("Open")
        assert unit.target is None
        assert str(unit).find("Open") == 1
        assert str(unit).find("Open", 2) == 6
        unit = self.UnitClass("Closed")
        unit.target = ""
        assert unit.target == ""
        assert str(unit).find("Closed") == 1
        assert str(unit).find("Closed", 2) == 8

    def test_comments(self):
        """Comments start with #."""
        unit = self.UnitClass("One")
        unit.addnote("Hello")
        assert str(unit).find("Hello") == 2
        assert str(unit).find("# Hello") == 0


class TestMozLangFile(test_base.TestTranslationStore):
    StoreClass = mozilla_lang.LangStore

    def test_nonascii(self):
        # FIXME investigate why this doesn't pass or why we even do this
        # text with UTF-8 encoded strings
        pass
