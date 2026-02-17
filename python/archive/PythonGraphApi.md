# PythonGraphApi

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# A Python Graph API? 

This wiki page is a resource for some brainstorming around the possibility of a Python Graph API in the form of an informational PEP, similar to [PEP 249, the Python DB API](http://www.python.org/peps/pep-0249.html). The goal would be, in other words, to define how a graph (or various kinds of graphs) would be expected to behave (possibly from different perspectives) in order to increase interoperability among graph algorithms. [The numeric array interface](http://numeric.scipy.org/array_interface.shtml), recently developed by the Numeric Python community to increase interoperability between array-handling software, illustrates the general idea.

A comp.lang.python thread discussing this (with some useful ideas) may be found [here](http://groups-beta.google.com/group/comp.lang.python/browse_thread/thread/cbca60cb36be39ed/313113af1aa077af).

This is not about plotting; for a definition of the kind of graph we\'re talking about, see [here](http://mathworld.wolfram.com/Graph.html).

If you have interest in this, please feel free to add your ideas here. If you\'d like to be named as a contributor in the case that some \"standard\" should emerge, please add your name to the list of contributors. (You might also want to create a user name and log in when doing changes, or possibly just state your name when you edit stuff, so one can see who did what.)

## A simple use-case 

Just to illustrate the point of this discussion, here is a simple example:

Let\'s say I have some special hardware that is able to search efficiently for complex patterns in byte sequences. I somehow use this to find various relationships between the genomes of different organisms, or between different genes in a given genome. This implicitly defines a graph, but I cannot put the graph explicitly in the form of a data structure that Python can manipulate, and, hence, I cannot use a ready-made graph library. So, I instead write an API to my system so that it can be probed and manipulated by other code *as if it were* a graph data structure.

Now, someone else might have written some nice graph code for, say, an approximated bipartite clique cover (or whatever) and I want to use that. In an ideal world, the clique partition code would be written using only an abstract notion of what a graph is (i.e. a *protocol* or *interface*/*API*) and I have implemented my hardware-based graph using the same graph notion/protocol. In this case I can simply write a small program that drops my hardware-based graph right into the clique partition code and it will work.

This ideal world scenario would only be possible, though, if some abstract graph notion or protocol is defined, so that both graph implementors and graph algorithm implementors can use it. The goal of this little project is, of course, to define such a protocol/API.

Note that the goal is *not* to implement a specific graph representation or a set of graph algorithms. The goal is only to mediate between developers of the two.

## Preliminary ideas 

### General thoughts 

Ideas so far include basing the API on the standard notion of using adjacency maps (such as dicts of neighbor lists), as described in [Guido\'s well-known essay](http://www.python.org/doc/essays/graphs.html) and used in [these examples by David Eppstein](http://www.ics.uci.edu/~eppstein/PADS), and using object adaptation (through the adapt() function, as described in [PEP 246](http://www.python.org/peps/pep-0246.html) and as used in [PyProtocols](http://peak.telecommunity.com/PyProtocols.html)) to allow access to graphs through various perspectives (such as adjacency maps, incidence maps, adjacency arrays, edge lists\...). This would also allow graphs implementations with completely different interfaces to be adapted to a standard interface, and thus be used by generic graph algorithms.

An example of an existing graph library for Python, written by István Albert, may be found [here](http://pygraphlib.sourceforge.net/). Note that this library is no longer maintained and its developers recommend using NetworkX instead (vide infra).

[Bulbflow](http://bulbflow.com) is an open-source Python persistence framework for graph databases. It uses Gremlin as the query language, and you can use it to connect to any Blueprints-enabled database, including [TinkeGraph](./TinkeGraph.html), Neo4j, OrientDB, Dex, [InfiniteGraph](./InfiniteGraph.html), and OpenRDF.

[NetworkX](http://networkx.lanl.gov) is another example of a graph library in Python.

[python-graph](http://code.google.com/p/python-graph/) a framework of generic graph classes and commonly used algorithms by Pedro Maitello. Under active development. The project aims to use pythonic conventions, and takes a modular approach to external dependancies.

[graph-tool](http://graph-tool.skewed.de) is an efficient python module for graph manipulation. It contains a comprehensive list of algorithms and network models, and integrates with [GraphViz](http://www.graphviz.org) for visualization. It is implemented in C++ with the [Boost Graph Library](http://www.boost.org/doc/libs/release/libs/graph), which makes it orders of magnitude faster than implementations based purely on python.

[py_graph](http://compbio.washington.edu/~zach/py_graph) is an example by Zach Frazier, partly inspired by Eppstein\'s example. No longer under development, the author recommends using NetworkX.

[kjbuckets](http://gadfly.sourceforge.net/kjbuckets.html) is a C extension and very fast, but imcomplete.

[pypes](http://cvs.zope.org/Packages/pypes/) appears never to have been released officially.

Bruno Preiss offers a very complete but somewhat unPythonic Graph type as part of an online [book on data structures in Python](http://www.brpreiss.com/books/opus7/html/page519.html). (Downloadable at the Opus7 package.)

[Nathan Denny\'s graph library](http://www.ece.arizona.edu/~denny/python_nest/graph_lib.py) appears to be a fairly simplistic implementation.

[Graphine](http://gitorious.org/projects/graphine/pages/Home) is a Python 3 graph implementation with support for bridge, directed, and undirected multigraphs.

[Pygr](http://www.bioinformatics.ucla.edu/pygr/) is billed as a \"Python graph database framework for bioinformatics\", and clearly aims to be more than just a graph library.

[Gato](http://gato.sourceforge.net/), the Graph Animation Toolkit, is a visual tool intended to teach graph algorithms. It contains a fully functional graph library.

[pynetwork](http://sourceforge.net/projects/pynetwork/)

[BOOST](http://boost.org/libs/graph/doc/python.html) - how about BOOST? it seems to be well developed and has already Python bindings

[pygraph](http://alpha-leonis.lids.mit.edu/nlp/pygraph/), Beracah Yankama\'s pure python a/cyclic tk grapher for tk contains spring and hierarchical node placement algorithms, along with some basic classes for creating nodes & edges.

[Graph::Easy](http://bloodgate.com/perl/graph/manual/overview.html) for perl allows flowcharts to be defined in plain text and then outputted in multiple formats which is quite handy for web applications and creating diagrams via wiki-like mechanisms.

One possible underlying technology for graphs would be adjacency matrices using [numarray](http://www.stsci.edu/resources/software_hardware/numarray). This approach would need to use sparse matrices to be practical for large graphs. The following library uses the numpy array and sparse scipy matrix for adjacency matrices: [Another Python Graph Library](http://sourceforge.net/projects/apythongraphlib/).

### Add your ideas here (Go wild, folks\...) 

\- I think that the graph representation should be a redundant one, that allows the fast traversals, quick node, edge and neighbour lookups as well as fast iterations over all nodes or all edges. This will of course come at the expense of storage and/or graph initialization efficieny. For example in the python graph representation mentioned above (modeled after LEDA) the nodes and the edges are stored in a separate dictionaries. Each edge_id maps to a tuple of the head_id and the tail_id (the nodes) that form the edge. (Edge_ids are automatically created as they are added.) At the same time each node_id maps to a tuple of two lists corresponding to incoming and outgoing edges. *(Istvan)*

\- IMO, one of the points of a standard interface is to let people choose their own representations. *(Magnus)*.

\- I believe that just as most people don\'t care how lists and dictionaries work behind the scenes they won\'t care (or want to have to deal with) picking a graph representation. The two representation that are listed in just about every computer science book, the adjacency matrix and the adjecency list representations are just about useless in the real world. These are what I would call a **node** centric view of the graph. It turns out in many probelms edges have far more utility.Graphs are a very rich methaphor and one rarely uses them in the stripped down version. What we need is a representation that is simple, fast and efficient enough in every case. *(Istvan)*

\- This is not about giving people a graph library, but letting people who write graph representations and people who write graph algorithms interoperate more easily, by giving them a common interface. If people want to use a ready-made library, that\'s fine. The point is that people (like me) might want to represent graphs completely differently from the \"textbook\" version (in fact, compact graph representations is what my current research is about). It\'s the same with the DB API; by fixing a standard API, people can write programs that use databases without having to worry about which database or database library they use. I\'ve added a use-case above to clear this up a bit. *(Magnus)*

\- To write **any** graph algorithm, you need a set of standard methods. As far as I know, there are only two ways of getting this - either agree on a fixed interface which implementations *must* follow (the DB API approach) or define an interface and require that implementations *can* be adapted to it (the adaptation approach). I don\'t like Andrew Dalke\'s suggestion of code-generating template systems, it seems to me that this would make writing algorithms far too hard, and where multiple graph representations are in use, result in code explosion (a well-known problem with C++ templates). My preference is for adaptation. It\'s ideal for this sort of thing, the only downside is that it isn\'t standard. But getting PEP 246 accepted would be easier with more use cases - avoiding its use is self-defeating. Better to lobby for its use, on the basis that we need it for this type of situation. *([PaulMoore](./PaulMoore.html))*

\- I share your view here. One possibility is to specify how a graph can be adapted to the (or one of) the standard interface(s) as part of the (hypothetical) Graph PEP, using adapter/factory functions. This can then be the same mechanism used by adapt(), but we don\'t have to require its use. (Or we could use it, of course\...)

\- On the other hand, it isn\'t really necessary for us (if we go down this road) to specify how such adaptation should be done. We could define the graph interface, and graph libraries could supply their own adapter functions or wrappers. *(Magnus)*

\- I also think that one important use case for a generalized graph api would be tree representations. Any standard graph representation should as a subset present a standard tree, with the classic algorithms being portable between them. (As a minimum, pre-, in-, and post-order traversal; preferably depth-first and breadth-first searches.) *(VanL)*

\- Andrew Dalke [suggests](http://groups.google.com/groups?selm=yyq0d.3041%24xA1.1224%40newsread3.news.pas.earthlink.net&output=gplain) using a template system that can transform code using a standard API into code using a custom API. This differs from a solution using object adaptation in that it works at the source level, and thus can have some performance advantages.

Perhaps we should try to keep the edge and node attributes/decorations separate from the GraphAPI. The API should specify that each node and edge store a pointer. The pointer would be set to an object that handles all decorations and manipulations of those decorations. The graph algorithms would work on the graph structure itself \-- not the decorations \-- and the user would need to interface those results to the decorations. *(dschult)*

\- I think that to be the most general the API should support hypergraphs, with regular graphs being a subclass. A hypergraph is defined by two sets of objects (a.k.a. nodes & edges). So if we have \'nodes\' A={a1,a2,a3} and \'edges\' B={B1,B2,B3} and then we make make a map d = {a1: (B1,B2), a2: (B2), a3: (B1,B2,B3)} Then G(A,B,d) is the hypergraph. The representation can be inverted too, so that B becomes the nodes and A the edges (if you start out with an incidence matrix with actors A down the rows and events they attend B across the columns the first form is the ties between the actors and the second is the ties between the This hypergraph has a As said before, a graph is a special case of a hypergraph where the number of points \'in\' each edge is 2 (i.e. len(d\[Bi\])=2 for all i); and of course, a directed graph is a special case of that where d\[Bi\]\[0\] is taken to be the sender and d\[Bi\]\[1\] the receiver.

As far as the API goes, it should be be both graph-theoretic and matrix-(uh?)-theoretic at once, because both representations are equally useful (though if I had to pick I\'d pick graph because that is what this API is for, networks, not matricies).

It has to support attributes on the nodes/edges \_with ease\_, to be able to support valued/signed graphs, as well as to provide a convienient hook for interfacing to other things (for example, colouring and labeling nodes/edges in generated diagrams)

The nodes/edges could be arbitrary python objects. Besides just allowing python\'s natural expressive freedom to be made full use of, this would solve the attributes problem with ease: An implementation wrinkle would be that the map would have to distinguish between seperate nodes/edges even though the actual items might have identical values, such as in the case of a signed graph where all edges are either -1 or +1 (perhaps index them when they get entered, and store them as (obj, index)?). This is basically dschult\'s suggestion, but I want to flesh out the bit about \"it\'s up to the user\...\"; for example, if a library was written to calculate various measures on the graph it would be important that the values of the edges are numeric. *(Nick)*

\- Also: +1 for standard API so that algorithms can be described in a standard way. Also: I see that the requirement about allowing \"Object\" has already been raised on usenet Also: I missed a type of graph, the multigraph, where more than one type of relation is defined. You can fake this with multiple separate graphs, and in many ways I prefer this (then you can attach descriptive data to each relation\...) but I can see that some algorithms might be more naturally expressed as operating on a multigraph. *(Nick)*

\- I second the notion of hypergraphs. I have a graph implementation that uses a base hypergraph class which contains Node, Edge, [NodeContainer](./NodeContainer.html), and [EdgeContainer](./EdgeContainer.html) classes, each of which can have its behavior modified via mixins. As examples, the modification from a hypergraph to a DAG is accomplished by subclassing Graph and mixing in a new edge container that raises an exception if an illegal edge insertion is attempted, the more implementation-centric question of storing nodes in a database backend is handled by exchanging the standard list-based [NodeContainer](./NodeContainer.html) with one that overrides add_node to a DB insertion operation, and the question of edge and node attributes is handled by simple keyword arguments which are passed to the base node and edge constructors, optionally made mandatory by subclassing Node or Edge. Please contact me if interested. *(Geremy)*

\- (Multigraphs are mentioned. - *Magnus*)

\- I\'m new here, so here goes: I would like to see a standard api for Graph *objects*, concentrating on two dimensional graphs. Hyper-graphs, multi-graphs, two-structures, etc shouldn\'t really be considered, imo, as they\'re much too esoteric and don\'t really map to many common usages (I\'m sure I\'ll get argument here from the graph researchers). Also, I don\'t want to define *what* a graph or a vertex or an edge actually is, other than the standard mathematical definition that an edge is some dort of a *relationship* between vertices.

The graph api should be graph-class agnositc. That is, it should not care if the graph is a connected, disconnected, directed, undirected, etc. It should only care about vertex and edge properties, other than adjacency, where a callback can be provided to account for the property\'s selection. I\'ll provide a proposal in the section below. *(jconnor)*

### Specifics 

*Put potential specifics here, that is, what functionality an API must cover. For now, it is completely permissible to have mutually exclusive items here, as nothing is anywhere near fixed yet.*

Static graphs:

- Node membership: Is a node part of the graph?
- Node iteration: Iterate over all the nodes.
- Edge membership: Is an edge part of the graph?
- Edge iteration: Iterate over all the edges.
- Adjacency iteration: Iterate over all the neighbors of a node.
- Incidence iteration: Iterate over all the edges incident to a node (out- and in-edges separately?)
- Node decoration: labels, weights, colors, capacities (can be done with external maps)
- Edge decoration: labels, weights, colors, capacities

*(dschult)* would add:

- Size of Graph: Report the number of edges in the graph.
- Order of Graph: Report the number of nodes in the graph.
- Degree of node: Report the number of neighbors for a node (or sum of edge weights incident on the node).

\"well this is tricky; the edges aren\'t neccessarily numbers, remember? *(nick)*\"

\- (I wasn\'t talking about numbers. \"The number of X\" means \"how many Xs\" there are. - *Magnus*)

\- Accessing incident edges based on their labels can also be useful (e.g. in FSAs). \"again tricky because it requires defining that a node/edge \"\"must\"\" have a label. Does this mean having `class LabeledGraph(Graph)`{.backtick}? *(nick)*\"

\- (The access here would, of course, only be available if the edges or labels do indeed have labels; not otherwise. - *Magnus*)

Dynamic graphs:

- Node addition

- Node deletion

- Edge addition

- Edge deletion

- Node decoration modification

- Edge decoration modification

- Edge contraction (Can\'t this be done using the add and delete above? Do we want to get this specialized? *(dschult)*)

- Node and edge hiding?

\- \"these all seem to revolve around the notion of a graph-update operation of some sort. So then the question is how to record what specific operation to perform? Also, do we just record which event comes before the others or do we attach a time to each? *(nick)*\"

\- (Not sure what you mean here. Why would we need to record anything like this? Why not simply modify the graph? That was the idea\... - *Magnus*)

\- It may be that a given representation only supports a subset of the given operations, and that subset might not necessarily be easy to predict. For example, even though it might seem that neighbor iteration and adjacency testing go hand in hand, for implicit graph representation they are quite separate. For such a representation, you can only check whether two given nodes are neighbors; to iterate over all the neighbors of a node, you\'d have to iterate over all the nodes in the graph.

Basic set operations (and more advanced operations, such as cartesian product) might be useful for graphs, but needn\'t be part of the standard.

Should there be separate functionality for directed and undirected graphs? Should all graphs be chain graphs (which allow both directed and undirected edges)? Should two-way directed edge be treated as an undirected edge (and vice versa)? \"Chain graphs are the most general, so we must have them. However, would they be a superset or simply next to normal graphs? *(nick)*\"

\- (Chain graphs are a generalization of both directed and undirected graphs. - *Magnus*)

\- How do we handle the proliferation of other graph classes (such as multigraphs, pseudographs, \...), all of which are only minor tweaks of the basic structure? How about more radical departures such as hypergraphs (which allow an arbitrary number of nodes per edge)? \"oops, didn\'t read this far. Well you know my answer: make every graph a hypergraph. *(Nick)*\"

\- One possibility would be to base the API definition on the [Graph eXchange Language](http://www.gupro.de/GXL) (GXL). It is derived from many separate graph representation languages and seems quite complete (it even supports hypergraphs and hierarchical graphs!), logical, and well-thought-out. The language itself consists of an XML and a UML notation, but it is based on a clearly defined [object model/ADT](http://www.gupro.de/GXL/GraphModel/graphModel.html), which we could adapt to a Python interface. I\'m not sure about how (or whether) they model graph modification (although I think there is some support for transformations of some kind) but that could probably be done as a simple, logical extension. We might not want to support *all* of the GXL model, of course. We might even want to define several layers of standard compliance, with Layer 0 being only the current de facto standard graph API, for example. *(Magnus)*

\- I think [GraphML](http://graphml.graphdrawing.org/) would be great to be supported for reading and writing graphs. *(Ralf)*

\- With the goal of designing an API for Python in mind, I would think one of the first decisions that needs to be made is whether to use multiple classes (ala Vertex, Edge, Graph) or just one (ala Graph); also, are those classes going to be \"Pythonic\" in that they provide various methods in terms of Python operators or not (let\'s call the \"not\" alternative \"Textbookish\")? It seems to me that without settling this first, discussing the details of the API further is moot. But maybe I am wrong? *(Peter)*

\- No, defining Vertex and Edge interfaces makes working with graphs just that much more difficult. That\'s the Java way, don\'t go there. *(Nick)*

\- Well, the \"Java way\" can also be the \"OO way\" and thus could also be the \"Python way\". Theoretically a Graph G is defined a set of vertices and a set of Edges. **G=(V,E)**. (Nick V.)

\- The only requirement on a vertex is that it can be represented in a set, which I think maps to supporting testing for equality and hashing. In Python, this does not require a dedicated Vertex class or interface.

I tend to prefer/develop graph implementations that support representing the nodes with arbitrary objects:

g=Graph()

some_object=[SomeObject](./SomeObject.html)(\*args1, \*\*kwds1 )

some_object2=[SomeObject](./SomeObject.html)(\*args2, \*\*kwds2)

g.add_vertex( some_object1 )

g.add_vertex( some_object2 )

new_edge=g.add_edge( some_object1, some_object2)

So that I do not have to maintain a mapping from the objects (that I care about) to some integers that uniquely label the nodes (which I don\'t care about). *(/David [McNamara](./McNamara.html))*

\- Proposal for Graph interface:

I think that algorithms should assume that a graph is immutable, so if it needs to add an artificial vertex or delete edges, etc, it should take care of all that accounting behind the scenes. As a result, I do not propose any interface that would alter the graph, though, perhaps, standard names may be in order (e.g. add_vertex(v))

- size(): return the \# of edges in the graph

- order(): return the \# of vertices in the graph

- edges(): return an iterable of all edges in the graph as tuples

- vertices(): return an iterable of all vertices in the graph

- is_adjacent(u, v): returns True iff *u* is adjacent to *v*

- adjacent_vertices(v): return an iterable of all vertices adjacent to *v*

- inbound_edges(v): return an iterable of all inbound edges incident to *v*

- outbound_edges(v): return an iterable of all outbound edges from *v*

- extrema_inbound_edge(v, cmp): return an inbound edge with an *extreme* property that is incident to *v* using the comparison callable, *cmp*, as a tuple (e.g. a minimal edge)

- extrema_outbound_edge(v, cmp): return an outbound edge with an *extreme* property that is incident to *v* using the comparison callable, *cmp*, as a tuple (e.g. a minimal edge)

Some notes:

1.  The calls size and order would be optional or could return None in the case that the graph is being computed on the fly.

2.  The calls edges and vertices would be optional or could return None in the case the graph is being computed on the fly.

3.  The iterable returned by adjacent_verticves would be ordered for certain classes of graph (e.g. ordered left to right for some trees).

4.  The \'edges\' would be returned as tuples, (*u*, *v*). And the tuples would be ordered in the case of directed graphs and unordred in the case of undirected graphs.

5.  The inbound/outbound edge calls would return identical results in the case of undirected graphs, and, potentially, different in the case of directed.

I would leave it to the graph implementors to provide a set of comparison callables that would be passed into a graph algorithm. Perhaps some standardization of names may be in order, but I don\'t see the need right now.

I believe that the majority of graph algorithms can be implemented with this interface. *(jconnor)*

# Vertices and Edges as Separate Objects 

1\. I think a **Vertex** and an **Edge** as objects are meaninful and useful. One should be able to create v1=Vertex(1) and v2=Vertex(2) and then e12=Edge(v1,v2). Then do G.add_edge(e12), which should be no different than doing G.add_vertex(v1); G.add_vertex(v2); G.add_edge(e12). In this respect this is a departure from the NetworkX idea of using integers as nodes and 2-tuples of integers as edges, having the user map back and forth between nodes and data.

2\. Whatever the repsentation used, the graph could expose a set of nodes and edges like graph.nodes and graph.edges. A new graph could be built from an existing set of nodes and edges: newG=Graph(G.nodes,G.edges). .nodes and .edges could be provided on-the-fly by property descriptors, regardless if a matrix or adj. list is used for internal representation. If the graph is connected, the graph could be exactly represented by G.edges

3\. A Vertex object would have an .id attribute that could uniquely identify it, and provide an [eq] and [hash] magic methods. This way it could be inserted into a set. It could also a have a label or reference to some data. Perhaps there could be a \"tag\" attribute which would be similar to what the Tk Canvas has. A tag could be anything like a color value, a \'visited\' flag.

4\. A Vertex object should not reference its edges. Edges should reference its vertices, because that is what an \'edge\' is \-- a relation between 2 vertices. So Edges will contain references to its nodes. An Edge object could have a \'from_vertex\' and a \'to_vertex\' attributes, a data attribute which could be the weight for example, and also a \"tag\" attribute like the Vertex.

5\. Providing a way to obtain edges to neighbour vertices in this scheme would ammount to an exhaustive search of the edges set. Therefore edges would be held in a nested dict like edges\[v1\]\[v2\]=edge12 . To quickly access the edges to neighbours of v1 would be G.edges\[v1\].values() (Nick V.)

6\. We must note that Edges and Vertices are defined as sets in standar graph theory, so, we must also think how to joind the graph data structure to the standard python (set) builtin data type. *(Jose Antonio Martin H.)*

7\. In a graph implementation of mine, I also have the possibility to specify generic n-edges (edges involving 3 or more vertexes) and for reification (specifying additional information about an edge) *(Stefano Borini)*

# Hypergraphs 

\- As far as hypergraphs are concerned, a hypergraph is equivalent to a bi-partite graph, with two different set of nodes. One represents the regular nodes, the other a set of edges (\<- these are not edges of the Graph itself, but separate Edge(s) created earlier. So it is probably not necessary to include a separate mechanism for hypergraphs. *(Nick V.)*

# GraphABC 

Matteo Dell\'Amico wrote [GraphABC](http://www.linux.it/~della/GraphABC/), a proposal for a graph Abstract Base Class. Please comment!

# Graph decoration 

\- The graph in itself contains just topology, but it would be nice to add data containers associated to the graph, to describe vertexes, edges, n-edges and the graph itself. *(Stefano Borini)*

= Graph databases =

Although not directly related to the graph API, but a storage shelf for descripted graphs would be useful as well. *(Stefano Borini)*

## The Principle of Least Surprise 

The API for sets (see [PEP 218](http://www.python.org/dev/peps/pep-0218/)) was initially designed by looking at the terminology used in two classic texts ([Aho, Hopcroft, and Ullman](http://www.amazon.com/Data-Structures-Algorithms-Alfred-Aho/dp/0201000237/) and [Sedgwick](http://www.amazon.com/Algorithms-Parts-1-5-Bundle-Fundamentals/dp/0201756080/)). Since most programmers learn about graphs from books like that, how about picking a couple of current data structures textbooks and using their terms and (implicit) APIs as a starting point? It might also short circuit otherwise-interminable arguments\-\--we agree in advance that if most books do X, the API should do X. Alternatively, we could just do whatever Magnus does in [his new book](http://www.amazon.com/Python-Algorithms-Mastering-Basic-Language/dp/1430232374/).

## Contributors 

(*Add your name to this list if you contribute.*)

- Magnus Lie Hetland

- Istvan Albert

- Paul Moore

- Van Lindberg

- Dan Schult

- Peter Froehlich

- Aric Hagberg

- Nick Guenther

- Nick Vatamaniuc

- Jose Antonio Martin H

- Beracah Yankama

- David [McNamara](./McNamara.html)

- Jason Connor

- Geremy Condra

- Matteo Dell\'Amico

- [Stefano Borini](StefanoBorini)

- Tomasz J. Kotarba

- Greg Wilson

(See also the Usenet discussion above for more contributors.)
