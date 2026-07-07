# -*- coding: utf-8 -*-

from sanhe_claude_code_plugin_marketplace import api


def test():
    _ = api


if __name__ == "__main__":
    from sanhe_claude_code_plugin_marketplace.tests import run_cov_test

    run_cov_test(
        __file__,
        "sanhe_claude_code_plugin_marketplace.api",
        preview=False,
    )
