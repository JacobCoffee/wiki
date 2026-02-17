# PatchGuidelines

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

- Submit all patches to the [Jython Patch Tracker](http://bugs.jython.org)

- Follow the [CodingStandards](CodingStandards).

- The patch should be a single unified diff file, not several diffs or a tar or zip containing several diffs. The easiest way to produce this is with svn diff:

  1.  Make all the changes necessary to fix the bug or add the feature you\'re working on.

  2.  svn add any files that need to be added and svn rm any files that need to be removed.

  3.  Run \'svn diff \> patch_name.diff\' in the root of your checkout. If there are changes in your checkout that aren\'t part of the patch, just pass the files that should be included in the diff explicitly to svn diff.

  If you\'ve done it correctly, you\'ll be able to run \'patch -p0 \< patch_name.diff\' from the root of a clean checkout and the patch will apply without errors or any further input from the user.

- Name the patch after the functionality it adds or the bug it fixes. For example, a patch for [http://bugs.jython.org/issue1803250](http://bugs.jython.org/issue1803250), a bug pointing out the lack of the indicies method on the slice type, the patch could be called \'add_indicies_to_slice.patch\'

- If the patch is to fix a bug already in the bug tracker, include the bug number in your comment.

- Reciprocally, after you\'ve created the patch add a comment to the bug with the patch number.

- Be sure to run regrtest and the bugtests as described in the [JythonDeveloperGuide](JythonDeveloperGuide) and mention that in your comments.

- If the functionality changed by the patch isn\'t exercised by existing tests, new tests for the functionality should be included. See the unittests in Lib/test that are run by regrtest as examples of how to write a new test.

- Include a succinct message on your tracker entry that explains what the patch is about that can be used directly as a checkin message. Ideally, such a message explains the problem and describes the fix in a few lines.
