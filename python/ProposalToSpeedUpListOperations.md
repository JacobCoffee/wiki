# ProposalToSpeedUpListOperations

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Abstract 

Operations on lists that insert/delete elements at the end of the list are not symmetric in CPython. Inserting/deleting from the end is O(1); inserting/deleting at the beginning is O(N). This proposal attempts to improve performance for remove operations at the front of the list to an O(1) operation by lazily releasing memory. Insertions are still tricky to make O(1), but they can be made to at least reclaim space from lazy removes.

## Motivation 

The author of the patch discovered the admonition against using pop(0) in the tutorial and had used it in some of his own programs, notably parsers.

Here are the proposed benefits:

- O(1) is faster than O(N) for some, presumably quite small, value of N.
- Performance benefits tend to compound. If you have P processes doing pop(0) in a loop on an N-element list, you are saving P \* N memmoves of size kN.
- The technique required to make O(1) work is simple at its core\--advance a pointer forward instead of moving the memory backward.
- Encouraging the use of pop(0) will lead to leaner Python programs that release memory earlier in the process.
- While not super common, there do exist programs today that pop from the top, either using pop itself or del, including programs in the standard library
- The language moratorium provides a good window for performance improvements in general (even if this one does not pass the litmus test for other reasons)

## Rationale 

The rationale for improving the speed of list removes should be fairly self-evident; the merits of the proposal then need to be measured against the tradeoffs required to gain that speed.

Many objections have been presented:

- The simplicity of the current implementation is important beyond the normal benefits of simplicity, since it is also a reference implementation for other ports of Python.

- People who got used to O(1) in one version of Python might have unpleasant surprises when they went to other versions.

- Alternatives to list already exist, such as deque and blist

- An O(1) solution would postpone the release of the memory from the orphaned pointers.

- An O(1) solution would slow down calls to list_resize, [PyList](./PyList.html)\_new, and list_dealloc.

- For small and medium sized lists, memmove()\'s penalty is usually drowned out by other operations on the list elements.

- The use case of popping elements off a large list is not that common (although this might be somewhat driven by the documented slowness)

- There may be third party code that relies on the current internal implementation

The objection on grounds of simplicity is the hardest to counter, except to say that the proposed patch is fairly small and non-invasive.

The objection that Python programmers will be \"spoiled\" by a fast implementation is a rather thin objection.

The alternatives to list, deque and blist, do not replicate all the features of list. Both come pretty close, though. Of course, the existence of alternatives to list does not justify keeping list itself crippled, as list is a data structure that many Python programmers naturally pick, without regard to performance, only to find out down the road that they are using list on larger and larger sets of data.

Postponing the release of memory after popping the first element off the list is wasteful, but in the alternative scenario, users would be avoiding pop(0) in the first place and needlessly tying up memory not only for the list pointers, but the list elements themselves (although they could set elements to None). The patch does limit the number of orphan pointers, and it does reclaim orphans when new elements gets inserted to the front of the list.

The changes to [PyList](./PyList.html)\_new and list_dealloc are small, and those methods only get called once during the lifetime of a list. The changes to list_resize would be the most likely to counteract other speedup gains.

Although memmove() is rarely the largest bottleneck in a Python program, every little speedup counts.

The assertion that current large Python programs today do not tend to pop elements off the top of the list is hard to verify for sure.

The patch does not break the public interface for third party extensions.

## Implementation 

[SteveHowell](SteveHowell) submitted the first draft of a fix, which you can find here.

[http://codereview.appspot.com/194083/show](http://codereview.appspot.com/194083/show)

For a small test program the patch produces a 100X speedup.
