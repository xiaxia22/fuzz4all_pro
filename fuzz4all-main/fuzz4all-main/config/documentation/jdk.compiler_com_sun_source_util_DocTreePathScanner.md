# Class DocTreePathScanner<R,​P>

**Source:** `jdk.compiler\com\sun\source\util\DocTreePathScanner.html`

### Class Description

```java
public class
DocTreePathScanner<R,​P>

extends
DocTreeScanner
<R,​P>
```

A DocTreeVisitor that visits all the child tree nodes, and provides
support for maintaining a path for the parent nodes.
To visit nodes of a particular type, just override the
corresponding visitorXYZ method.
Inside your method, call super.visitXYZ to visit descendant
nodes.

**All Implemented Interfaces:** DocTreeVisitor

<R,​P>

---

### Field Details

*No entries found.*

### Constructor Details

#### public DocTreePathScanner()

*No description found.*

---

### Method Details

#### public
R
scan​(
DocTreePath
path,

P
p)

Scans a tree from a position identified by a tree path.

**Parameters:**
- path

- the path
- p

- a value to be passed to visitor methods

**Returns:**
- the result returned from the main visitor method

---

#### public
R
scan​(
DocTree
tree,

P
p)

Scans a single node.
The current path is updated for the duration of the scan.

**Overrides:**
- scan

in class

DocTreeScanner

<

R

,​

P

>

**Parameters:**
- tree

- the tree to be scanned
- p

- a value to be passed to visitor methods

**Returns:**
- the result returned from the main visitor method

---

#### public
DocTreePath
getCurrentPath()

Returns the current path for the node, as built up by the currently
active set of scan calls.

**Returns:**
- the current path

---

### Additional Sections

#### Class DocTreePathScanner<R,​P>

java.lang.Object

- com.sun.source.util.DocTreeScanner

<R,​P>
- - com.sun.source.util.DocTreePathScanner<R,​P>

com.sun.source.util.DocTreeScanner

<R,​P>

- com.sun.source.util.DocTreePathScanner<R,​P>

com.sun.source.util.DocTreePathScanner<R,​P>

**All Implemented Interfaces:** DocTreeVisitor

<R,​P>

```java
public class
DocTreePathScanner<R,​P>

extends
DocTreeScanner
<R,​P>
```

A DocTreeVisitor that visits all the child tree nodes, and provides
support for maintaining a path for the parent nodes.
To visit nodes of a particular type, just override the
corresponding visitorXYZ method.
Inside your method, call super.visitXYZ to visit descendant
nodes.

**Since:** 1.8

public class

DocTreePathScanner<R,​P>

extends

DocTreeScanner

<R,​P>

A DocTreeVisitor that visits all the child tree nodes, and provides
support for maintaining a path for the parent nodes.
To visit nodes of a particular type, just override the
corresponding visitorXYZ method.
Inside your method, call super.visitXYZ to visit descendant
nodes.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DocTreePathScanner

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

DocTreePath

getCurrentPath

()

Returns the current path for the node, as built up by the currently
active set of scan calls.

R

scan

​(

DocTree

tree,

P

p)

Scans a single node.

R

scan

​(

DocTreePath

path,

P

p)

Scans a tree from a position identified by a tree path.

- Methods declared in class com.sun.source.util.

DocTreeScanner

reduce

,

scan

,

visitAttribute

,

visitAuthor

,

visitComment

,

visitDeprecated

,

visitDocComment

,

visitDocRoot

,

visitDocType

,

visitEndElement

,

visitEntity

,

visitErroneous

,

visitHidden

,

visitIdentifier

,

visitIndex

,

visitInheritDoc

,

visitLink

,

visitLiteral

,

visitOther

,

visitParam

,

visitProvides

,

visitReference

,

visitReturn

,

visitSee

,

visitSerial

,

visitSerialData

,

visitSerialField

,

visitSince

,

visitStartElement

,

visitSummary

,

visitText

,

visitThrows

,

visitUnknownBlockTag

,

visitUnknownInlineTag

,

visitUses

,

visitValue

,

visitVersion

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

DocTreePathScanner

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

DocTreePath

getCurrentPath

()

Returns the current path for the node, as built up by the currently
active set of scan calls.

R

scan

​(

DocTree

tree,

P

p)

Scans a single node.

R

scan

​(

DocTreePath

path,

P

p)

Scans a tree from a position identified by a tree path.

- Methods declared in class com.sun.source.util.

DocTreeScanner

reduce

,

scan

,

visitAttribute

,

visitAuthor

,

visitComment

,

visitDeprecated

,

visitDocComment

,

visitDocRoot

,

visitDocType

,

visitEndElement

,

visitEntity

,

visitErroneous

,

visitHidden

,

visitIdentifier

,

visitIndex

,

visitInheritDoc

,

visitLink

,

visitLiteral

,

visitOther

,

visitParam

,

visitProvides

,

visitReference

,

visitReturn

,

visitSee

,

visitSerial

,

visitSerialData

,

visitSerialField

,

visitSince

,

visitStartElement

,

visitSummary

,

visitText

,

visitThrows

,

visitUnknownBlockTag

,

visitUnknownInlineTag

,

visitUses

,

visitValue

,

visitVersion

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

Returns the current path for the node, as built up by the currently
active set of scan calls.

Scans a single node.

Scans a tree from a position identified by a tree path.

Methods declared in class com.sun.source.util.

DocTreeScanner

reduce

,

scan

,

visitAttribute

,

visitAuthor

,

visitComment

,

visitDeprecated

,

visitDocComment

,

visitDocRoot

,

visitDocType

,

visitEndElement

,

visitEntity

,

visitErroneous

,

visitHidden

,

visitIdentifier

,

visitIndex

,

visitInheritDoc

,

visitLink

,

visitLiteral

,

visitOther

,

visitParam

,

visitProvides

,

visitReference

,

visitReturn

,

visitSee

,

visitSerial

,

visitSerialData

,

visitSerialField

,

visitSince

,

visitStartElement

,

visitSummary

,

visitText

,

visitThrows

,

visitUnknownBlockTag

,

visitUnknownInlineTag

,

visitUses

,

visitValue

,

visitVersion

---

#### Methods declared in class com.sun.source.util. DocTreeScanner

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

- DocTreePathScanner

```java
public DocTreePathScanner()
```

============ METHOD DETAIL ==========

- Method Detail

- scan

```java
public
R
scan​(
DocTreePath
path,

P
p)
```

Scans a tree from a position identified by a tree path.

**Parameters:** path

- the path
**Parameters:** p

- a value to be passed to visitor methods
**Returns:** the result returned from the main visitor method

- scan

```java
public
R
scan​(
DocTree
tree,

P
p)
```

Scans a single node.
The current path is updated for the duration of the scan.

**Overrides:** scan

in class

DocTreeScanner

<

R

,​

P

>
**Parameters:** tree

- the tree to be scanned
**Parameters:** p

- a value to be passed to visitor methods
**Returns:** the result returned from the main visitor method

- getCurrentPath

```java
public
DocTreePath
getCurrentPath()
```

Returns the current path for the node, as built up by the currently
active set of scan calls.

**Returns:** the current path

Constructor Detail

- DocTreePathScanner

```java
public DocTreePathScanner()
```

---

#### Constructor Detail

DocTreePathScanner

```java
public DocTreePathScanner()
```

---

#### DocTreePathScanner

public DocTreePathScanner()

Method Detail

- scan

```java
public
R
scan​(
DocTreePath
path,

P
p)
```

Scans a tree from a position identified by a tree path.

**Parameters:** path

- the path
**Parameters:** p

- a value to be passed to visitor methods
**Returns:** the result returned from the main visitor method

- scan

```java
public
R
scan​(
DocTree
tree,

P
p)
```

Scans a single node.
The current path is updated for the duration of the scan.

**Overrides:** scan

in class

DocTreeScanner

<

R

,​

P

>
**Parameters:** tree

- the tree to be scanned
**Parameters:** p

- a value to be passed to visitor methods
**Returns:** the result returned from the main visitor method

- getCurrentPath

```java
public
DocTreePath
getCurrentPath()
```

Returns the current path for the node, as built up by the currently
active set of scan calls.

**Returns:** the current path

---

#### Method Detail

scan

```java
public
R
scan​(
DocTreePath
path,

P
p)
```

Scans a tree from a position identified by a tree path.

**Parameters:** path

- the path
**Parameters:** p

- a value to be passed to visitor methods
**Returns:** the result returned from the main visitor method

---

#### scan

public

R

scan​(

DocTreePath

path,

P

p)

Scans a tree from a position identified by a tree path.

scan

```java
public
R
scan​(
DocTree
tree,

P
p)
```

Scans a single node.
The current path is updated for the duration of the scan.

**Overrides:** scan

in class

DocTreeScanner

<

R

,​

P

>
**Parameters:** tree

- the tree to be scanned
**Parameters:** p

- a value to be passed to visitor methods
**Returns:** the result returned from the main visitor method

---

#### scan

public

R

scan​(

DocTree

tree,

P

p)

Scans a single node.
The current path is updated for the duration of the scan.

getCurrentPath

```java
public
DocTreePath
getCurrentPath()
```

Returns the current path for the node, as built up by the currently
active set of scan calls.

**Returns:** the current path

---

#### getCurrentPath

public

DocTreePath

getCurrentPath()

Returns the current path for the node, as built up by the currently
active set of scan calls.

---

