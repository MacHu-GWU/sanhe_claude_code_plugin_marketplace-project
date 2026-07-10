
.. image:: https://readthedocs.org/projects/sanhe-claude-code-plugin-marketplace/badge/?version=latest
    :target: https://sanhe-claude-code-plugin-marketplace.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/sanhe_claude_code_plugin_marketplace-project/actions/workflows/main.yml/badge.svg
    :target: https://github.com/MacHu-GWU/sanhe_claude_code_plugin_marketplace-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/sanhe_claude_code_plugin_marketplace-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/sanhe_claude_code_plugin_marketplace-project

.. image:: https://img.shields.io/pypi/v/sanhe-claude-code-plugin-marketplace.svg
    :target: https://pypi.python.org/pypi/sanhe-claude-code-plugin-marketplace

.. image:: https://img.shields.io/pypi/l/sanhe-claude-code-plugin-marketplace.svg
    :target: https://pypi.python.org/pypi/sanhe-claude-code-plugin-marketplace

.. image:: https://img.shields.io/pypi/pyversions/sanhe-claude-code-plugin-marketplace.svg
    :target: https://pypi.python.org/pypi/sanhe-claude-code-plugin-marketplace

.. image:: https://img.shields.io/badge/✍️_Release_History!--None.svg?style=social&logo=github
    :target: https://github.com/MacHu-GWU/sanhe_claude_code_plugin_marketplace-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/⭐_Star_me_on_GitHub!--None.svg?style=social&logo=github
    :target: https://github.com/MacHu-GWU/sanhe_claude_code_plugin_marketplace-project

------

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://sanhe-claude-code-plugin-marketplace.readthedocs.io/en/latest/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/sanhe_claude_code_plugin_marketplace-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/sanhe_claude_code_plugin_marketplace-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/sanhe_claude_code_plugin_marketplace-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/sanhe-claude-code-plugin-marketplace#files


Welcome to ``sanhe_claude_code_plugin_marketplace`` Documentation
==============================================================================
.. image:: https://sanhe-claude-code-plugin-marketplace.readthedocs.io/en/latest/_static/sanhe_claude_code_plugin_marketplace-logo.png
    :target: https://sanhe-claude-code-plugin-marketplace.readthedocs.io/en/latest/

This is a personal plugin marketplace created by an early adopter and power user of Claude Code. It contains hard-won patterns and redistributable components forged through production use—real-world solutions for enterprise AI applications and optimized development workflows. Not theoretical examples, but practical implementations battle-tested in actual use.


.. _install:

Install
------------------------------------------------------------------------------

Add this marketplace to your Claude Code ``.claude/settings.json`` (or ``~/.claude/settings.json`` for a global install), then enable whichever plugins you want:

.. code-block:: json

    {
        "extraKnownMarketplaces": {
            "sanhe-claude-code-plugin-marketplace": {
                "source": {
                    "source": "github",
                    "repo": "MacHu-GWU/sanhe_claude_code_plugin_marketplace-project",
                    "ref": "x.y.z"
                }
            }
        },
        "enabledPlugins": {
            "coding-agent-docs@sanhe-claude-code-plugin-marketplace": true,
            "doc-writing-styles@sanhe-claude-code-plugin-marketplace": true
        }
    }

Set ``ref`` to the latest tag (``x.y.z``) from `the releases page <https://github.com/MacHu-GWU/sanhe_claude_code_plugin_marketplace-project/releases>`_ to pick up marketplace catalog updates, then run ``/plugin marketplace update`` inside Claude Code.

``sanhe_claude_code_plugin_marketplace`` is also released on PyPI as a placeholder package, so if you need it as a Python dependency you can:

.. code-block:: console

    $ pip install sanhe-claude-code-plugin-marketplace

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade sanhe-claude-code-plugin-marketplace
