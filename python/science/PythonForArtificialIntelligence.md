# PythonForArtificialIntelligence

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page attempts to collect information and links pertaining to the practice of AI and Machine Learning in python.

# General AI 

- **[AIMA](http://code.google.com/p/aima-python/)** - Python implementation of algorithms from Russell and Norvig\'s \'Artificial Intelligence: A Modern Approach\'

- **[pyDatalog](https://sites.google.com/site/pydatalog/)** - Logic Programming engine in Python

- **[SimpleAI](http://github.com/simpleai-team/simpleai)** - Python implementation of many of the artificial intelligence algorithms described on the book \"Artificial Intelligence, a Modern Approach\". It focuses on providing an easy to use, well documented and tested library.

- **[EasyAI](http://zulko.github.io/easyAI)** - Simple Python engine for two-players games with AI (Negamax, transposition tables, game solving).

# Machine Learning 

- **[GraphLab Create](https://dato.com/learn/userguide/)** - An end-to-end Machine Learning platform with a Python front-end and C++ core. It allows you to do data engineering, build ML models, and deploy them. Key design principles: out-of-core computation, fast and robust learning algorithms, easy-to-use Python API, and fast deployment of arbitrary Python objects.

- **[Feature Forge](https://github.com/machinalis/featureforge)** - A set of tools for creating and testing machine learning features, with a scikit-learn compatible API.

- **[Orange](http://orange.biolab.si/)** - Open source data visualization and analysis for novice and experts. Data mining through visual programming or Python scripting. Components for machine learning. Extensions for bioinformatics and text mining. Packed with features for data analytics.

- **[PyBrain](http://pybrain.org/)** - [PyBrain](./PyBrain.html) is a modular Machine Learning Library for Python. Its goal is to offer flexible, easy-to-use yet still powerful algorithms for Machine Learning Tasks and a variety of predefined environments to test and compare your algorithms.

- **[PyML](http://pyml.sourceforge.net/)** - PyML is an interactive object oriented framework for machine learning written in Python. PyML focuses on SVMs and other kernel methods. It is supported on Linux and Mac OS X.

- **[MlPy](https://mlpy.fbk.eu/)** - mlpy makes extensive use of [NumPy](NumPy) to provide fast N-dimensional array manipulation and easy integration of C code. The GNU Scientific Library ( GSL) is also required. It provides high level procedures that support, with few lines of code, the design of rich Data Analysis Protocols (DAPs) for preprocessing, clustering, predictive classification, regression and feature selection. Methods are available for feature weighting and ranking, data resampling, error evaluation and experiment landscaping.

- **[Milk](http://packages.python.org/milk/)** - Milk is a machine learning toolkit in Python. Its focus is on supervised classification with several classifiers available: SVMs (based on libsvm), k-NN, random forests, decision trees. It also performs feature selection. These classifiers can be combined in many ways to form different classification systems.

- **[SAMBO](https://sambo-optimization.github.io)** - a light toolbox for sequential and model-based optimization of black-box functions, including hyper-parameter optimization in ML.

- **[scikit-learn](http://scikit-learn.sourceforge.net/)** - scikit-learn is a Python module integrating classic machine learning algorithms in the tightly-knit world of scientific Python packages (numpy, scipy, matplotlib). It aims to provide simple and efficient solutions to learning problems that are accessible to everybody and reusable in various contexts: machine-learning as a versatile tool for science and engineering.

- **[Shogun](http://www.shogun-toolbox.org/)** - The machine learning toolbox\'s focus is on large scale kernel methods and especially on Support Vector Machines (SVM) . It provides a generic SVM object interfacing to several different SVM implementations, among them the state of the art OCAS, Liblinear, LibSVM, SVMLight, SVMLin and GPDT. Each of the SVMs can be combined with a variety of kernels. The toolbox not only provides efficient implementations of the most common kernels, like the Linear, Polynomial, Gaussian and Sigmoid Kernel but also comes with a number of recent string kernels. SHOGUN is implemented in C++ and interfaces to Matlab(tm), R, Octave and Python and is proudly released as Machine Learning Open Source Software

- **[MDP-Toolkit](http://mdp-toolkit.sourceforge.net/)** - Modular toolkit for Data Processing (MDP) is a Python data processing framework. From the user's perspective, MDP is a collection of supervised and unsupervised learning algorithms and other data processing units that can be combined into data processing sequences and more complex feed-forward network architectures. From the scientific developer's perspective, MDP is a modular framework, which can easily be expanded. The implementation of new algorithms is easy and intuitive. The new implemented units are then automatically integrated with the rest of the library. The base of available algorithms is steadily increasing and includes signal processing methods (Principal Component Analysis, Independent Component Analysis, Slow Feature Analysis), manifold learning methods (\[Hessian\] Locally Linear Embedding), several classifiers, probabilistic methods (Factor Analysis, RBM), data pre-processing methods, and many others.

- **[LibSVM](http://www.csie.ntu.edu.tw/~cjlin/libsvm/)** - LIBSVM is an integrated software for support vector classification, (C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution estimation (one-class SVM). It supports multi-class classification. A Python interface is available by by default.

- **[Weka](http://www.cs.waikato.ac.nz/ml/weka/)** - Weka is a collection of machine learning algorithms for data mining tasks. The algorithms can either be applied directly to a dataset or called from your own Java code. Weka contains tools for data pre-processing, classification, regression, clustering, association rules, and visualization. It is also well-suited for developing new machine learning schemes. See [here](http://weka.wikispaces.com/Using+WEKA+from+Jython) for a tutorial on using Weka from jython.

- **[Monte](http://montepython.sourceforge.net/)** - Monte (python) is a Python framework for building gradient based learning machines, like neural networks, conditional random fields, logistic regression, etc. Monte contains modules (that hold parameters, a cost-function and a gradient-function) and trainers (that can adapt a module\'s parameters by minimizing its cost-function on training data).

- **[SOM](http://paraschopra.com/sourcecode/SOM/index.php)** - Self-Organizing Maps is a form of machine learning technique which employs unsupervised learning. It means that you don\'t need to explicitly tell the SOM about what to learn in the input data. It automatically learns the patterns in input data and organizes the data into different groups.

- **[Yalign](https://github.com/machinalis/yalign)** - Yalign is a friendly tool for extracting parallel sentences from comparable corpora..

# Natural Language & Text Processing 

- **[NLTK](http://www.nltk.org/)** - Open source Python modules, linguistic data and documentation for research and development in natural language processing and text analytics, with distributions for Windows, Mac OSX and Linux.

- **[gensim](http://radimrehurek.com/gensim)** - Gensim is a Python framework designed to automatically extract semantic topics from documents, as naturally and painlessly as possible. Gensim aims at processing raw, unstructured digital texts ("plain text"). The unsupervised algorithms in gensim, such as Latent Semantic Analysis, Latent Dirichlet Allocation or Random Projections, discover hidden (latent) semantic structure, based on word co-occurrence patterns within a corpus of training documents. Once these statistical patterns are found, any plain text documents can be succinctly expressed in the new, semantic representation, and queried for topical similarity against other documents and so on.

- **[Quepy](https://github.com/machinalis/quepy)** - A python framework to transform natural language questions to queries in a database query language.

# Neural Networks 

- **[neurolab](http://code.google.com/p/neurolab/)** - Neurolab is a simple and powerful Neural Network Library for Python. Contains based neural networks, train algorithms and flexible framework to create and explore other networks. It has the following features: pure python + numpy; API like Neural Network Toolbox (NNT) from MATLAB; interface to use train algorithms from scipy.optimize; flexible network configurations and learning algorithms; and a variety of supported types of Artificial Neural Network and learning algorithms.

- **[ffnet](http://pypi.python.org/pypi/ffnet)** - ffnet is a fast and easy-to-use feed-forward neural network training solution for python. Many nice features are implemented: arbitrary network connectivity, automatic data normalization, very efficient (also parallel) training tools, network export to fortran code.

- **[FANN](http://leenissen.dk/fann/wp/)** - Fast Artificial Neural Network Library is a free open source neural network library, which implements multilayer artificial neural networks in C with support for both fully connected and sparsely connected networks. Cross-platform execution in both fixed and floating point are supported. It includes a framework for easy handling of training data sets. It is easy to use, versatile, well documented, and fast. Bindings to more than 15 programming languages are available. An easy to read introduction article and a reference manual accompanies the library with examples and recommendations on how to use the library. Several graphical user interfaces are also available for the library.

- **[bpnn.py](./arctrix(2e)com(2f)nas(2f)python(2f)bpnn(2e)py.html)** - Written by Neil Schemenauer, bpnn.py is used by an IBM [article](http://www.ibm.com/developerworks/library/l-neural/) entitled \"An introduction to neural networks\".

- **[PyAnn](http://pyann.sourceforge.net/)** - A Python framework to build artificial neural networks

- **[pyrenn](https://github.com/yabata/pyrenn)** - pyrenn is a recurrent neural network toolbox for python (and matlab). It is written in pure python and numpy and allows to create a wide range of (recurrent) neural network configurations for system identification. It is easy to use, well documented and comes with several examples.
