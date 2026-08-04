.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.4.7 (2026-08-04)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Miscellaneous**

- Bump the pinned ``doc-writing-styles`` plugin ref from ``v0.1.4`` to ``v0.1.5``


0.4.6 (2026-08-02)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Miscellaneous**

- Bump the pinned ``dot-claude`` plugin ref from ``v0.1.1`` to ``v0.2.1``
- Bump the pinned ``doc-writing-styles`` plugin ref from ``v0.1.3`` to ``v0.1.4``
- Bump the pinned ``lesson-smith`` plugin ref from ``v0.2.2`` to ``v0.2.3``


0.4.5 (2026-07-31)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Miscellaneous**

- Bump the pinned ``coding-agent-docs`` plugin ref from ``v0.1.2`` to ``v0.1.4``
- Bump the pinned ``lesson-smith`` plugin ref from ``v0.2.1`` to ``v0.2.2``


0.4.4 (2026-07-29)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Miscellaneous**

- Bump the pinned ``doc-writing-styles`` plugin ref from ``v0.1.2`` to ``v0.1.3``


0.4.3 (2026-07-25)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Miscellaneous**

- Bump the pinned ``coding-agent-docs`` plugin ref from ``v0.1.1`` to ``v0.1.2``


0.4.2 (2026-07-23)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Miscellaneous**

- Bump the pinned ``lesson-smith`` plugin ref from ``v0.1.1`` to ``v0.2.1``


0.4.1 (2026-07-22)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the ``dot-claude`` plugin to the marketplace catalog


0.3.1 (2026-07-22)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the ``lesson-smith`` plugin to the marketplace catalog

**Miscellaneous**

- Document how to install this marketplace via ``extraKnownMarketplaces`` and ``enabledPlugins`` in Claude Code's ``settings.json``, and clarify that the PyPI package is a placeholder for those who need it as a Python dependency


0.2.1 (2026-07-09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the ``doc-writing-styles`` plugin to the marketplace catalog

**Bugfixes**

- Fix ``git-subdir`` plugin source URLs to use the full ``https://github.com/...`` form instead of the ``owner/repo`` shorthand, which could cause SSH-based clone failures (``Host key verification failed`` / ``Permission denied (publickey)``) on machines without SSH configured

**Miscellaneous**

- Update the ``coding-agent-docs`` plugin description for clarity
- Document how to pin a marketplace's own ``ref`` version in ``extraKnownMarketplaces``, and record the SSH-vs-HTTPS URL pitfall in the ``maintain-claude-plugins`` reference guide


0.1.1 (2026-07-09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- First release
- Add the central marketplace catalog (``.claude-plugin/marketplace.json``) listing ``coding-agent-docs`` as the first published plugin
- Add the ``maintain-claude-plugins`` skill, documenting the split-repo plus central-marketplace workflow and providing the ``plugin_release.py`` script for discovering, validating, and tagging plugin releases
