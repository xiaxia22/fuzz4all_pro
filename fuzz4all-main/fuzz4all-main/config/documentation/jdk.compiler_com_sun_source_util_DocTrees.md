# Class DocTrees

**Source:** `jdk.compiler\com\sun\source\util\DocTrees.html`

### Class Description

```java
public abstract class
DocTrees

extends
Trees
```

Provides access to syntax trees for doc comments.

**Since:** 1.8

---

### Field Details

*No entries found.*

### Constructor Details

#### public DocTrees()

*No description found.*

---

### Method Details

#### public static
DocTrees
instance​(
JavaCompiler.CompilationTask
task)

Returns a DocTrees object for a given CompilationTask.

**Parameters:**
- task

- the compilation task for which to get the Trees object

**Returns:**
- the DocTrees object

**Throws:**
- IllegalArgumentException

- if the task does not support the Trees API.

---

#### public static
DocTrees
instance​(
ProcessingEnvironment
env)

Returns a DocTrees object for a given ProcessingEnvironment.

**Parameters:**
- env

- the processing environment for which to get the Trees object

**Returns:**
- the DocTrees object

**Throws:**
- IllegalArgumentException

- if the env does not support the Trees API.

---

#### public abstract
BreakIterator
getBreakIterator()

Returns the break iterator used to compute the first sentence of
documentation comments.
Returns

null

if none has been specified.

**Returns:**
- the break iterator

**Since:**
- 9

---

#### public abstract
DocCommentTree
getDocCommentTree​(
TreePath
path)

Returns the doc comment tree, if any, for the Tree node identified by a given TreePath.
Returns

null

if no doc comment was found.

**Parameters:**
- path

- the path for the tree node

**Returns:**
- the doc comment tree

---

#### public abstract
DocCommentTree
getDocCommentTree​(
Element
e)

Returns the doc comment tree of the given element.
Returns

null

if no doc comment was found.

**Parameters:**
- e

- an element whose documentation is required

**Returns:**
- the doc comment tree

**Since:**
- 9

---

#### public abstract
DocCommentTree
getDocCommentTree​(
FileObject
fileObject)

Returns the doc comment tree of the given file. The file must be
an HTML file, in which case the doc comment tree represents the
entire contents of the file.
Returns

null

if no doc comment was found.
Future releases may support additional file types.

**Parameters:**
- fileObject

- the content container

**Returns:**
- the doc comment tree

**Since:**
- 9

---

#### public abstract
DocCommentTree
getDocCommentTree​(
Element
e,

String
relativePath)
throws
IOException

Returns the doc comment tree of the given file whose path is
specified relative to the given element. The file must be an HTML
file, in which case the doc comment tree represents the contents
of the <body> tag, and any enclosing tags are ignored.
Returns

null

if no doc comment was found.
Future releases may support additional file types.

**Parameters:**
- e

- an element whose path is used as a reference
- relativePath

- the relative path from the Element

**Returns:**
- the doc comment tree

**Throws:**
- IOException

- if an exception occurs

**Since:**
- 9

---

#### public abstract
DocTreePath
getDocTreePath​(
FileObject
fileObject,

PackageElement
packageElement)

Returns a doc tree path containing the doc comment tree of the given file.
The file must be an HTML file, in which case the doc comment tree represents
the contents of the

<body>

tag, and any enclosing tags are ignored.
Any references to source code elements contained in

@see

and

{@link}

tags in the doc comment tree will be evaluated in the
context of the given package element.
Returns

null

if no doc comment was found.

**Parameters:**
- fileObject

- a file object encapsulating the HTML content
- packageElement

- a package element to associate with the given file object
representing a legacy package.html, null otherwise

**Returns:**
- a doc tree path containing the doc comment parsed from the given file

**Throws:**
- IllegalArgumentException

- if the fileObject is not an HTML file

**Since:**
- 9

---

#### public abstract
Element
getElement​(
DocTreePath
path)

Returns the language model element referred to by the leaf node of the given

DocTreePath

, or

null

if unknown.

**Parameters:**
- path

- the path for the tree node

**Returns:**
- the element

---

#### public abstract
List
<
DocTree
> getFirstSentence​(
List
<? extends
DocTree
> list)

Returns the list of

DocTree

representing the first sentence of
a comment.

**Parameters:**
- list

- the DocTree list to interrogate

**Returns:**
- the first sentence

**Since:**
- 9

---

#### public abstract
DocSourcePositions
getSourcePositions()

Returns a utility object for accessing the source positions
of documentation tree nodes.

**Specified by:**
- getSourcePositions

in class

Trees

**Returns:**
- the utility object

---

#### public abstract void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

DocTree
t,

DocCommentTree
c,

CompilationUnitTree
root)

Prints a message of the specified kind at the location of the
tree within the provided compilation unit

**Parameters:**
- kind

- the kind of message
- msg

- the message, or an empty string if none
- t

- the tree to use as a position hint
- c

- the doc comment tree to use as a position hint
- root

- the compilation unit that contains tree

---

#### public abstract void setBreakIterator​(
BreakIterator
breakiterator)

Sets the break iterator to compute the first sentence of
documentation comments.

**Parameters:**
- breakiterator

- a break iterator or

null

to specify the default
sentence breaker

**Since:**
- 9

---

#### public abstract
DocTreeFactory
getDocTreeFactory()

Returns a utility object for creating

DocTree

objects.

**Returns:**
- a utility object for creating

DocTree

objects

**Since:**
- 9

---

### Additional Sections

#### Class DocTrees

java.lang.Object

- com.sun.source.util.Trees
- - com.sun.source.util.DocTrees

com.sun.source.util.Trees

- com.sun.source.util.DocTrees

com.sun.source.util.DocTrees

```java
public abstract class
DocTrees

extends
Trees
```

Provides access to syntax trees for doc comments.

**Since:** 1.8

public abstract class

DocTrees

extends

Trees

Provides access to syntax trees for doc comments.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DocTrees

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

BreakIterator

getBreakIterator

()

Returns the break iterator used to compute the first sentence of
documentation comments.

abstract

DocCommentTree

getDocCommentTree

​(

TreePath

path)

Returns the doc comment tree, if any, for the Tree node identified by a given TreePath.

abstract

DocCommentTree

getDocCommentTree

​(

Element

e)

Returns the doc comment tree of the given element.

abstract

DocCommentTree

getDocCommentTree

​(

Element

e,

String

relativePath)

Returns the doc comment tree of the given file whose path is
specified relative to the given element.

abstract

DocCommentTree

getDocCommentTree

​(

FileObject

fileObject)

Returns the doc comment tree of the given file.

abstract

DocTreeFactory

getDocTreeFactory

()

Returns a utility object for creating

DocTree

objects.

abstract

DocTreePath

getDocTreePath

​(

FileObject

fileObject,

PackageElement

packageElement)

Returns a doc tree path containing the doc comment tree of the given file.

abstract

Element

getElement

​(

DocTreePath

path)

Returns the language model element referred to by the leaf node of the given

DocTreePath

, or

null

if unknown.

abstract

List

<

DocTree

>

getFirstSentence

​(

List

<? extends

DocTree

> list)

Returns the list of

DocTree

representing the first sentence of
a comment.

abstract

DocSourcePositions

getSourcePositions

()

Returns a utility object for accessing the source positions
of documentation tree nodes.

static

DocTrees

instance

​(

ProcessingEnvironment

env)

Returns a DocTrees object for a given ProcessingEnvironment.

static

DocTrees

instance

​(

JavaCompiler.CompilationTask

task)

Returns a DocTrees object for a given CompilationTask.

abstract void

printMessage

​(

Diagnostic.Kind

kind,

CharSequence

msg,

DocTree

t,

DocCommentTree

c,

CompilationUnitTree

root)

Prints a message of the specified kind at the location of the
tree within the provided compilation unit

abstract void

setBreakIterator

​(

BreakIterator

breakiterator)

Sets the break iterator to compute the first sentence of
documentation comments.

- Methods declared in class com.sun.source.util.

Trees

getDocComment

,

getElement

,

getLub

,

getOriginalType

,

getPath

,

getPath

,

getPath

,

getPath

,

getScope

,

getTree

,

getTree

,

getTree

,

getTree

,

getTree

,

getTypeMirror

,

isAccessible

,

isAccessible

,

printMessage

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

DocTrees

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

BreakIterator

getBreakIterator

()

Returns the break iterator used to compute the first sentence of
documentation comments.

abstract

DocCommentTree

getDocCommentTree

​(

TreePath

path)

Returns the doc comment tree, if any, for the Tree node identified by a given TreePath.

abstract

DocCommentTree

getDocCommentTree

​(

Element

e)

Returns the doc comment tree of the given element.

abstract

DocCommentTree

getDocCommentTree

​(

Element

e,

String

relativePath)

Returns the doc comment tree of the given file whose path is
specified relative to the given element.

abstract

DocCommentTree

getDocCommentTree

​(

FileObject

fileObject)

Returns the doc comment tree of the given file.

abstract

DocTreeFactory

getDocTreeFactory

()

Returns a utility object for creating

DocTree

objects.

abstract

DocTreePath

getDocTreePath

​(

FileObject

fileObject,

PackageElement

packageElement)

Returns a doc tree path containing the doc comment tree of the given file.

abstract

Element

getElement

​(

DocTreePath

path)

Returns the language model element referred to by the leaf node of the given

DocTreePath

, or

null

if unknown.

abstract

List

<

DocTree

>

getFirstSentence

​(

List

<? extends

DocTree

> list)

Returns the list of

DocTree

representing the first sentence of
a comment.

abstract

DocSourcePositions

getSourcePositions

()

Returns a utility object for accessing the source positions
of documentation tree nodes.

static

DocTrees

instance

​(

ProcessingEnvironment

env)

Returns a DocTrees object for a given ProcessingEnvironment.

static

DocTrees

instance

​(

JavaCompiler.CompilationTask

task)

Returns a DocTrees object for a given CompilationTask.

abstract void

printMessage

​(

Diagnostic.Kind

kind,

CharSequence

msg,

DocTree

t,

DocCommentTree

c,

CompilationUnitTree

root)

Prints a message of the specified kind at the location of the
tree within the provided compilation unit

abstract void

setBreakIterator

​(

BreakIterator

breakiterator)

Sets the break iterator to compute the first sentence of
documentation comments.

- Methods declared in class com.sun.source.util.

Trees

getDocComment

,

getElement

,

getLub

,

getOriginalType

,

getPath

,

getPath

,

getPath

,

getPath

,

getScope

,

getTree

,

getTree

,

getTree

,

getTree

,

getTree

,

getTypeMirror

,

isAccessible

,

isAccessible

,

printMessage

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the break iterator used to compute the first sentence of
documentation comments.

Returns the doc comment tree, if any, for the Tree node identified by a given TreePath.

Returns the doc comment tree of the given element.

Returns the doc comment tree of the given file whose path is
specified relative to the given element.

Returns the doc comment tree of the given file.

Returns a utility object for creating

DocTree

objects.

Returns a doc tree path containing the doc comment tree of the given file.

Returns the language model element referred to by the leaf node of the given

DocTreePath

, or

null

if unknown.

Returns the list of

DocTree

representing the first sentence of
a comment.

Returns a utility object for accessing the source positions
of documentation tree nodes.

Returns a DocTrees object for a given ProcessingEnvironment.

Returns a DocTrees object for a given CompilationTask.

Prints a message of the specified kind at the location of the
tree within the provided compilation unit

Sets the break iterator to compute the first sentence of
documentation comments.

Methods declared in class com.sun.source.util.

Trees

getDocComment

,

getElement

,

getLub

,

getOriginalType

,

getPath

,

getPath

,

getPath

,

getPath

,

getScope

,

getTree

,

getTree

,

getTree

,

getTree

,

getTree

,

getTypeMirror

,

isAccessible

,

isAccessible

,

printMessage

---

#### Methods declared in class com.sun.source.util. Trees

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DocTrees

```java
public DocTrees()
```

============ METHOD DETAIL ==========

- Method Detail

- instance

```java
public static
DocTrees
instance​(
JavaCompiler.CompilationTask
task)
```

Returns a DocTrees object for a given CompilationTask.

**Parameters:** task

- the compilation task for which to get the Trees object
**Returns:** the DocTrees object
**Throws:** IllegalArgumentException

- if the task does not support the Trees API.

- instance

```java
public static
DocTrees
instance​(
ProcessingEnvironment
env)
```

Returns a DocTrees object for a given ProcessingEnvironment.

**Parameters:** env

- the processing environment for which to get the Trees object
**Returns:** the DocTrees object
**Throws:** IllegalArgumentException

- if the env does not support the Trees API.

- getBreakIterator

```java
public abstract
BreakIterator
getBreakIterator()
```

Returns the break iterator used to compute the first sentence of
documentation comments.
Returns

null

if none has been specified.

**Returns:** the break iterator
**Since:** 9

- getDocCommentTree

```java
public abstract
DocCommentTree
getDocCommentTree​(
TreePath
path)
```

Returns the doc comment tree, if any, for the Tree node identified by a given TreePath.
Returns

null

if no doc comment was found.

**Parameters:** path

- the path for the tree node
**Returns:** the doc comment tree

- getDocCommentTree

```java
public abstract
DocCommentTree
getDocCommentTree​(
Element
e)
```

Returns the doc comment tree of the given element.
Returns

null

if no doc comment was found.

**Parameters:** e

- an element whose documentation is required
**Returns:** the doc comment tree
**Since:** 9

- getDocCommentTree

```java
public abstract
DocCommentTree
getDocCommentTree​(
FileObject
fileObject)
```

Returns the doc comment tree of the given file. The file must be
an HTML file, in which case the doc comment tree represents the
entire contents of the file.
Returns

null

if no doc comment was found.
Future releases may support additional file types.

**Parameters:** fileObject

- the content container
**Returns:** the doc comment tree
**Since:** 9

- getDocCommentTree

```java
public abstract
DocCommentTree
getDocCommentTree​(
Element
e,

String
relativePath)
throws
IOException
```

Returns the doc comment tree of the given file whose path is
specified relative to the given element. The file must be an HTML
file, in which case the doc comment tree represents the contents
of the <body> tag, and any enclosing tags are ignored.
Returns

null

if no doc comment was found.
Future releases may support additional file types.

**Parameters:** e

- an element whose path is used as a reference
**Parameters:** relativePath

- the relative path from the Element
**Returns:** the doc comment tree
**Throws:** IOException

- if an exception occurs
**Since:** 9

- getDocTreePath

```java
public abstract
DocTreePath
getDocTreePath​(
FileObject
fileObject,

PackageElement
packageElement)
```

Returns a doc tree path containing the doc comment tree of the given file.
The file must be an HTML file, in which case the doc comment tree represents
the contents of the

<body>

tag, and any enclosing tags are ignored.
Any references to source code elements contained in

@see

and

{@link}

tags in the doc comment tree will be evaluated in the
context of the given package element.
Returns

null

if no doc comment was found.

**Parameters:** fileObject

- a file object encapsulating the HTML content
**Parameters:** packageElement

- a package element to associate with the given file object
representing a legacy package.html, null otherwise
**Returns:** a doc tree path containing the doc comment parsed from the given file
**Throws:** IllegalArgumentException

- if the fileObject is not an HTML file
**Since:** 9

- getElement

```java
public abstract
Element
getElement​(
DocTreePath
path)
```

Returns the language model element referred to by the leaf node of the given

DocTreePath

, or

null

if unknown.

**Parameters:** path

- the path for the tree node
**Returns:** the element

- getFirstSentence

```java
public abstract
List
<
DocTree
> getFirstSentence​(
List
<? extends
DocTree
> list)
```

Returns the list of

DocTree

representing the first sentence of
a comment.

**Parameters:** list

- the DocTree list to interrogate
**Returns:** the first sentence
**Since:** 9

- getSourcePositions

```java
public abstract
DocSourcePositions
getSourcePositions()
```

Returns a utility object for accessing the source positions
of documentation tree nodes.

**Specified by:** getSourcePositions

in class

Trees
**Returns:** the utility object

- printMessage

```java
public abstract void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

DocTree
t,

DocCommentTree
c,

CompilationUnitTree
root)
```

Prints a message of the specified kind at the location of the
tree within the provided compilation unit

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none
**Parameters:** t

- the tree to use as a position hint
**Parameters:** c

- the doc comment tree to use as a position hint
**Parameters:** root

- the compilation unit that contains tree

- setBreakIterator

```java
public abstract void setBreakIterator​(
BreakIterator
breakiterator)
```

Sets the break iterator to compute the first sentence of
documentation comments.

**Parameters:** breakiterator

- a break iterator or

null

to specify the default
sentence breaker
**Since:** 9

- getDocTreeFactory

```java
public abstract
DocTreeFactory
getDocTreeFactory()
```

Returns a utility object for creating

DocTree

objects.

**Returns:** a utility object for creating

DocTree

objects
**Since:** 9

Constructor Detail

- DocTrees

```java
public DocTrees()
```

---

#### Constructor Detail

DocTrees

```java
public DocTrees()
```

---

#### DocTrees

public DocTrees()

Method Detail

- instance

```java
public static
DocTrees
instance​(
JavaCompiler.CompilationTask
task)
```

Returns a DocTrees object for a given CompilationTask.

**Parameters:** task

- the compilation task for which to get the Trees object
**Returns:** the DocTrees object
**Throws:** IllegalArgumentException

- if the task does not support the Trees API.

- instance

```java
public static
DocTrees
instance​(
ProcessingEnvironment
env)
```

Returns a DocTrees object for a given ProcessingEnvironment.

**Parameters:** env

- the processing environment for which to get the Trees object
**Returns:** the DocTrees object
**Throws:** IllegalArgumentException

- if the env does not support the Trees API.

- getBreakIterator

```java
public abstract
BreakIterator
getBreakIterator()
```

Returns the break iterator used to compute the first sentence of
documentation comments.
Returns

null

if none has been specified.

**Returns:** the break iterator
**Since:** 9

- getDocCommentTree

```java
public abstract
DocCommentTree
getDocCommentTree​(
TreePath
path)
```

Returns the doc comment tree, if any, for the Tree node identified by a given TreePath.
Returns

null

if no doc comment was found.

**Parameters:** path

- the path for the tree node
**Returns:** the doc comment tree

- getDocCommentTree

```java
public abstract
DocCommentTree
getDocCommentTree​(
Element
e)
```

Returns the doc comment tree of the given element.
Returns

null

if no doc comment was found.

**Parameters:** e

- an element whose documentation is required
**Returns:** the doc comment tree
**Since:** 9

- getDocCommentTree

```java
public abstract
DocCommentTree
getDocCommentTree​(
FileObject
fileObject)
```

Returns the doc comment tree of the given file. The file must be
an HTML file, in which case the doc comment tree represents the
entire contents of the file.
Returns

null

if no doc comment was found.
Future releases may support additional file types.

**Parameters:** fileObject

- the content container
**Returns:** the doc comment tree
**Since:** 9

- getDocCommentTree

```java
public abstract
DocCommentTree
getDocCommentTree​(
Element
e,

String
relativePath)
throws
IOException
```

Returns the doc comment tree of the given file whose path is
specified relative to the given element. The file must be an HTML
file, in which case the doc comment tree represents the contents
of the <body> tag, and any enclosing tags are ignored.
Returns

null

if no doc comment was found.
Future releases may support additional file types.

**Parameters:** e

- an element whose path is used as a reference
**Parameters:** relativePath

- the relative path from the Element
**Returns:** the doc comment tree
**Throws:** IOException

- if an exception occurs
**Since:** 9

- getDocTreePath

```java
public abstract
DocTreePath
getDocTreePath​(
FileObject
fileObject,

PackageElement
packageElement)
```

Returns a doc tree path containing the doc comment tree of the given file.
The file must be an HTML file, in which case the doc comment tree represents
the contents of the

<body>

tag, and any enclosing tags are ignored.
Any references to source code elements contained in

@see

and

{@link}

tags in the doc comment tree will be evaluated in the
context of the given package element.
Returns

null

if no doc comment was found.

**Parameters:** fileObject

- a file object encapsulating the HTML content
**Parameters:** packageElement

- a package element to associate with the given file object
representing a legacy package.html, null otherwise
**Returns:** a doc tree path containing the doc comment parsed from the given file
**Throws:** IllegalArgumentException

- if the fileObject is not an HTML file
**Since:** 9

- getElement

```java
public abstract
Element
getElement​(
DocTreePath
path)
```

Returns the language model element referred to by the leaf node of the given

DocTreePath

, or

null

if unknown.

**Parameters:** path

- the path for the tree node
**Returns:** the element

- getFirstSentence

```java
public abstract
List
<
DocTree
> getFirstSentence​(
List
<? extends
DocTree
> list)
```

Returns the list of

DocTree

representing the first sentence of
a comment.

**Parameters:** list

- the DocTree list to interrogate
**Returns:** the first sentence
**Since:** 9

- getSourcePositions

```java
public abstract
DocSourcePositions
getSourcePositions()
```

Returns a utility object for accessing the source positions
of documentation tree nodes.

**Specified by:** getSourcePositions

in class

Trees
**Returns:** the utility object

- printMessage

```java
public abstract void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

DocTree
t,

DocCommentTree
c,

CompilationUnitTree
root)
```

Prints a message of the specified kind at the location of the
tree within the provided compilation unit

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none
**Parameters:** t

- the tree to use as a position hint
**Parameters:** c

- the doc comment tree to use as a position hint
**Parameters:** root

- the compilation unit that contains tree

- setBreakIterator

```java
public abstract void setBreakIterator​(
BreakIterator
breakiterator)
```

Sets the break iterator to compute the first sentence of
documentation comments.

**Parameters:** breakiterator

- a break iterator or

null

to specify the default
sentence breaker
**Since:** 9

- getDocTreeFactory

```java
public abstract
DocTreeFactory
getDocTreeFactory()
```

Returns a utility object for creating

DocTree

objects.

**Returns:** a utility object for creating

DocTree

objects
**Since:** 9

---

#### Method Detail

instance

```java
public static
DocTrees
instance​(
JavaCompiler.CompilationTask
task)
```

Returns a DocTrees object for a given CompilationTask.

**Parameters:** task

- the compilation task for which to get the Trees object
**Returns:** the DocTrees object
**Throws:** IllegalArgumentException

- if the task does not support the Trees API.

---

#### instance

public static

DocTrees

instance​(

JavaCompiler.CompilationTask

task)

Returns a DocTrees object for a given CompilationTask.

instance

```java
public static
DocTrees
instance​(
ProcessingEnvironment
env)
```

Returns a DocTrees object for a given ProcessingEnvironment.

**Parameters:** env

- the processing environment for which to get the Trees object
**Returns:** the DocTrees object
**Throws:** IllegalArgumentException

- if the env does not support the Trees API.

---

#### instance

public static

DocTrees

instance​(

ProcessingEnvironment

env)

Returns a DocTrees object for a given ProcessingEnvironment.

getBreakIterator

```java
public abstract
BreakIterator
getBreakIterator()
```

Returns the break iterator used to compute the first sentence of
documentation comments.
Returns

null

if none has been specified.

**Returns:** the break iterator
**Since:** 9

---

#### getBreakIterator

public abstract

BreakIterator

getBreakIterator()

Returns the break iterator used to compute the first sentence of
documentation comments.
Returns

null

if none has been specified.

getDocCommentTree

```java
public abstract
DocCommentTree
getDocCommentTree​(
TreePath
path)
```

Returns the doc comment tree, if any, for the Tree node identified by a given TreePath.
Returns

null

if no doc comment was found.

**Parameters:** path

- the path for the tree node
**Returns:** the doc comment tree

---

#### getDocCommentTree

public abstract

DocCommentTree

getDocCommentTree​(

TreePath

path)

Returns the doc comment tree, if any, for the Tree node identified by a given TreePath.
Returns

null

if no doc comment was found.

getDocCommentTree

```java
public abstract
DocCommentTree
getDocCommentTree​(
Element
e)
```

Returns the doc comment tree of the given element.
Returns

null

if no doc comment was found.

**Parameters:** e

- an element whose documentation is required
**Returns:** the doc comment tree
**Since:** 9

---

#### getDocCommentTree

public abstract

DocCommentTree

getDocCommentTree​(

Element

e)

Returns the doc comment tree of the given element.
Returns

null

if no doc comment was found.

getDocCommentTree

```java
public abstract
DocCommentTree
getDocCommentTree​(
FileObject
fileObject)
```

Returns the doc comment tree of the given file. The file must be
an HTML file, in which case the doc comment tree represents the
entire contents of the file.
Returns

null

if no doc comment was found.
Future releases may support additional file types.

**Parameters:** fileObject

- the content container
**Returns:** the doc comment tree
**Since:** 9

---

#### getDocCommentTree

public abstract

DocCommentTree

getDocCommentTree​(

FileObject

fileObject)

Returns the doc comment tree of the given file. The file must be
an HTML file, in which case the doc comment tree represents the
entire contents of the file.
Returns

null

if no doc comment was found.
Future releases may support additional file types.

getDocCommentTree

```java
public abstract
DocCommentTree
getDocCommentTree​(
Element
e,

String
relativePath)
throws
IOException
```

Returns the doc comment tree of the given file whose path is
specified relative to the given element. The file must be an HTML
file, in which case the doc comment tree represents the contents
of the <body> tag, and any enclosing tags are ignored.
Returns

null

if no doc comment was found.
Future releases may support additional file types.

**Parameters:** e

- an element whose path is used as a reference
**Parameters:** relativePath

- the relative path from the Element
**Returns:** the doc comment tree
**Throws:** IOException

- if an exception occurs
**Since:** 9

---

#### getDocCommentTree

public abstract

DocCommentTree

getDocCommentTree​(

Element

e,

String

relativePath)
throws

IOException

Returns the doc comment tree of the given file whose path is
specified relative to the given element. The file must be an HTML
file, in which case the doc comment tree represents the contents
of the <body> tag, and any enclosing tags are ignored.
Returns

null

if no doc comment was found.
Future releases may support additional file types.

getDocTreePath

```java
public abstract
DocTreePath
getDocTreePath​(
FileObject
fileObject,

PackageElement
packageElement)
```

Returns a doc tree path containing the doc comment tree of the given file.
The file must be an HTML file, in which case the doc comment tree represents
the contents of the

<body>

tag, and any enclosing tags are ignored.
Any references to source code elements contained in

@see

and

{@link}

tags in the doc comment tree will be evaluated in the
context of the given package element.
Returns

null

if no doc comment was found.

**Parameters:** fileObject

- a file object encapsulating the HTML content
**Parameters:** packageElement

- a package element to associate with the given file object
representing a legacy package.html, null otherwise
**Returns:** a doc tree path containing the doc comment parsed from the given file
**Throws:** IllegalArgumentException

- if the fileObject is not an HTML file
**Since:** 9

---

#### getDocTreePath

public abstract

DocTreePath

getDocTreePath​(

FileObject

fileObject,

PackageElement

packageElement)

Returns a doc tree path containing the doc comment tree of the given file.
The file must be an HTML file, in which case the doc comment tree represents
the contents of the

<body>

tag, and any enclosing tags are ignored.
Any references to source code elements contained in

@see

and

{@link}

tags in the doc comment tree will be evaluated in the
context of the given package element.
Returns

null

if no doc comment was found.

getElement

```java
public abstract
Element
getElement​(
DocTreePath
path)
```

Returns the language model element referred to by the leaf node of the given

DocTreePath

, or

null

if unknown.

**Parameters:** path

- the path for the tree node
**Returns:** the element

---

#### getElement

public abstract

Element

getElement​(

DocTreePath

path)

Returns the language model element referred to by the leaf node of the given

DocTreePath

, or

null

if unknown.

getFirstSentence

```java
public abstract
List
<
DocTree
> getFirstSentence​(
List
<? extends
DocTree
> list)
```

Returns the list of

DocTree

representing the first sentence of
a comment.

**Parameters:** list

- the DocTree list to interrogate
**Returns:** the first sentence
**Since:** 9

---

#### getFirstSentence

public abstract

List

<

DocTree

> getFirstSentence​(

List

<? extends

DocTree

> list)

Returns the list of

DocTree

representing the first sentence of
a comment.

getSourcePositions

```java
public abstract
DocSourcePositions
getSourcePositions()
```

Returns a utility object for accessing the source positions
of documentation tree nodes.

**Specified by:** getSourcePositions

in class

Trees
**Returns:** the utility object

---

#### getSourcePositions

public abstract

DocSourcePositions

getSourcePositions()

Returns a utility object for accessing the source positions
of documentation tree nodes.

printMessage

```java
public abstract void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

DocTree
t,

DocCommentTree
c,

CompilationUnitTree
root)
```

Prints a message of the specified kind at the location of the
tree within the provided compilation unit

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none
**Parameters:** t

- the tree to use as a position hint
**Parameters:** c

- the doc comment tree to use as a position hint
**Parameters:** root

- the compilation unit that contains tree

---

#### printMessage

public abstract void printMessage​(

Diagnostic.Kind

kind,

CharSequence

msg,

DocTree

t,

DocCommentTree

c,

CompilationUnitTree

root)

Prints a message of the specified kind at the location of the
tree within the provided compilation unit

setBreakIterator

```java
public abstract void setBreakIterator​(
BreakIterator
breakiterator)
```

Sets the break iterator to compute the first sentence of
documentation comments.

**Parameters:** breakiterator

- a break iterator or

null

to specify the default
sentence breaker
**Since:** 9

---

#### setBreakIterator

public abstract void setBreakIterator​(

BreakIterator

breakiterator)

Sets the break iterator to compute the first sentence of
documentation comments.

getDocTreeFactory

```java
public abstract
DocTreeFactory
getDocTreeFactory()
```

Returns a utility object for creating

DocTree

objects.

**Returns:** a utility object for creating

DocTree

objects
**Since:** 9

---

#### getDocTreeFactory

public abstract

DocTreeFactory

getDocTreeFactory()

Returns a utility object for creating

DocTree

objects.

---

