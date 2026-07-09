.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


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
