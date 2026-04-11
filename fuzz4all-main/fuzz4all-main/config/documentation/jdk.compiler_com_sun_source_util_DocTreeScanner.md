# Class DocTreeScanner<R,​P>

**Source:** `jdk.compiler\com\sun\source\util\DocTreeScanner.html`

### Class Description

```java
public class
DocTreeScanner<R,​P>

extends
Object

implements
DocTreeVisitor
<R,​P>
```

A TreeVisitor that visits all the child tree nodes.
To visit nodes of a particular type, just override the
corresponding visitXYZ method.
Inside your method, call super.visitXYZ to visit descendant
nodes.

The default implementation of the visitXYZ methods will determine
a result as follows:

- If the node being visited has no children, the result will be

null

.

If the node being visited has one child, the result will be the
result of calling

scan

on that child. The child may be a simple node
or itself a list of nodes.

If the node being visited has more than one child, the result will
be determined by calling

scan

each child in turn, and then combining the
result of each scan after the first with the cumulative result
so far, as determined by the

reduce(R, R)

method. Each child may be either
a simple node of a list of nodes. The default behavior of the

reduce

method is such that the result of the visitXYZ method will be the result of
the last child scanned.

Here is an example to count the number of erroneous nodes in a tree:

```java
class CountErrors extends DocTreeScanner<Integer,Void> {
@Override
public Integer visitErroneous(ErroneousTree node, Void p) {
return 1;
}
@Override
public Integer reduce(Integer r1, Integer r2) {
return (r1 == null ? 0 : r1) + (r2 == null ? 0 : r2);
}
}
```

**All Implemented Interfaces:** DocTreeVisitor

<R,​P>

---

### Field Details

*No entries found.*

### Constructor Details

#### public DocTreeScanner()

*No description found.*

---

### Method Details

#### public
R
scan​(
DocTree
node,

P
p)

Scans a single node.

**Parameters:**
- node

- the node to be scanned
- p

- a parameter value passed to the visit method

**Returns:**
- the result value from the visit method

---

#### public
R
scan​(
Iterable
<? extends
DocTree
> nodes,

P
p)

Scans a sequence of nodes.

**Parameters:**
- nodes

- the nodes to be scanned
- p

- a parameter value to be passed to the visit method for each node

**Returns:**
- the combined return value from the visit methods.
The values are combined using the

reduce

method.

---

#### public
R
reduce​(
R
r1,

R
r2)

Reduces two results into a combined result.
The default implementation is to return the first parameter.
The general contract of the method is that it may take any action whatsoever.

**Parameters:**
- r1

- the first of the values to be combined
- r2

- the second of the values to be combined

**Returns:**
- the result of combining the two parameters

---

#### public
R
visitAttribute​(
AttributeTree
node,

P
p)

Visits an AttributeTree node. This implementation returns

null

.

**Specified by:**
- visitAttribute

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitAuthor​(
AuthorTree
node,

P
p)

Visits an AuthorTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitAuthor

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitComment​(
CommentTree
node,

P
p)

Visits a CommentTree node. This implementation returns

null

.

**Specified by:**
- visitComment

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitDeprecated​(
DeprecatedTree
node,

P
p)

Visits a DeprecatedTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitDeprecated

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitDocComment​(
DocCommentTree
node,

P
p)

Visits a DocCommentTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitDocComment

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitDocRoot​(
DocRootTree
node,

P
p)

Visits a DocRootTree node. This implementation returns

null

.

**Specified by:**
- visitDocRoot

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitDocType​(
DocTypeTree
node,

P
p)

Visits a DocTypeTree node. This implementation returns

null

.

**Specified by:**
- visitDocType

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitEndElement​(
EndElementTree
node,

P
p)

Visits an EndElementTree node. This implementation returns

null

.

**Specified by:**
- visitEndElement

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitEntity​(
EntityTree
node,

P
p)

Visits an EntityTree node. This implementation returns

null

.

**Specified by:**
- visitEntity

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitErroneous​(
ErroneousTree
node,

P
p)

Visits an ErroneousTree node. This implementation returns

null

.

**Specified by:**
- visitErroneous

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitHidden​(
HiddenTree
node,

P
p)

Visits a HiddenTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitHidden

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitIdentifier​(
IdentifierTree
node,

P
p)

Visits an IdentifierTree node. This implementation returns

null

.

**Specified by:**
- visitIdentifier

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitIndex​(
IndexTree
node,

P
p)

Visits an IndexTree node. This implementation returns

null

.

**Specified by:**
- visitIndex

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitInheritDoc​(
InheritDocTree
node,

P
p)

Visits an InheritDocTree node. This implementation returns

null

.

**Specified by:**
- visitInheritDoc

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitLink​(
LinkTree
node,

P
p)

Visits a LinkTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitLink

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitLiteral​(
LiteralTree
node,

P
p)

Visits an LiteralTree node. This implementation returns

null

.

**Specified by:**
- visitLiteral

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitParam​(
ParamTree
node,

P
p)

Visits a ParamTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitParam

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitProvides​(
ProvidesTree
node,

P
p)

Visits a ProvidesTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitProvides

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitReference​(
ReferenceTree
node,

P
p)

Visits a ReferenceTree node. This implementation returns

null

.

**Specified by:**
- visitReference

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitReturn​(
ReturnTree
node,

P
p)

Visits a ReturnTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitReturn

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitSee​(
SeeTree
node,

P
p)

Visits a SeeTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitSee

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitSerial​(
SerialTree
node,

P
p)

Visits a SerialTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitSerial

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitSerialData​(
SerialDataTree
node,

P
p)

Visits a SerialDataTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitSerialData

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitSerialField​(
SerialFieldTree
node,

P
p)

Visits a SerialFieldTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitSerialField

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitSince​(
SinceTree
node,

P
p)

Visits a SinceTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitSince

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitStartElement​(
StartElementTree
node,

P
p)

Visits a StartElementTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitStartElement

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitSummary​(
SummaryTree
node,

P
p)

Visits a SummaryTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitSummary

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

**Since:**
- 10

---

#### public
R
visitText​(
TextTree
node,

P
p)

Visits a TextTree node. This implementation returns

null

.

**Specified by:**
- visitText

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitThrows​(
ThrowsTree
node,

P
p)

Visits a ThrowsTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitThrows

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitUnknownBlockTag​(
UnknownBlockTagTree
node,

P
p)

Visits an UnknownBlockTagTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitUnknownBlockTag

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitUnknownInlineTag​(
UnknownInlineTagTree
node,

P
p)

Visits an UnknownInlineTagTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitUnknownInlineTag

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitUses​(
UsesTree
node,

P
p)

Visits a UsesTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitUses

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitValue​(
ValueTree
node,

P
p)

Visits a ValueTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitValue

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitVersion​(
VersionTree
node,

P
p)

Visits a VersionTreeTree node. This implementation scans the children in left to right order.

**Specified by:**
- visitVersion

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

#### public
R
visitOther​(
DocTree
node,

P
p)

Visits an unknown type of DocTree node.
This can occur if the set of tags evolves and new kinds
of nodes are added to the

DocTree

hierarchy. This implementation returns

null

.

**Specified by:**
- visitOther

in interface

DocTreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- the result of scanning

---

### Additional Sections

#### Class DocTreeScanner<R,​P>

java.lang.Object

- com.sun.source.util.DocTreeScanner<R,​P>

com.sun.source.util.DocTreeScanner<R,​P>

**All Implemented Interfaces:** DocTreeVisitor

<R,​P>

**Direct Known Subclasses:** DocTreePathScanner

```java
public class
DocTreeScanner<R,​P>

extends
Object

implements
DocTreeVisitor
<R,​P>
```

A TreeVisitor that visits all the child tree nodes.
To visit nodes of a particular type, just override the
corresponding visitXYZ method.
Inside your method, call super.visitXYZ to visit descendant
nodes.

The default implementation of the visitXYZ methods will determine
a result as follows:

- If the node being visited has no children, the result will be

null

.

If the node being visited has one child, the result will be the
result of calling

scan

on that child. The child may be a simple node
or itself a list of nodes.

If the node being visited has more than one child, the result will
be determined by calling

scan

each child in turn, and then combining the
result of each scan after the first with the cumulative result
so far, as determined by the

reduce(R, R)

method. Each child may be either
a simple node of a list of nodes. The default behavior of the

reduce

method is such that the result of the visitXYZ method will be the result of
the last child scanned.

Here is an example to count the number of erroneous nodes in a tree:

```java
class CountErrors extends DocTreeScanner<Integer,Void> {
@Override
public Integer visitErroneous(ErroneousTree node, Void p) {
return 1;
}
@Override
public Integer reduce(Integer r1, Integer r2) {
return (r1 == null ? 0 : r1) + (r2 == null ? 0 : r2);
}
}
```

**Since:** 1.8

public class

DocTreeScanner<R,​P>

extends

Object

implements

DocTreeVisitor

<R,​P>

A TreeVisitor that visits all the child tree nodes.
To visit nodes of a particular type, just override the
corresponding visitXYZ method.
Inside your method, call super.visitXYZ to visit descendant
nodes.

The default implementation of the visitXYZ methods will determine
a result as follows:

- If the node being visited has no children, the result will be

null

.

If the node being visited has one child, the result will be the
result of calling

scan

on that child. The child may be a simple node
or itself a list of nodes.

If the node being visited has more than one child, the result will
be determined by calling

scan

each child in turn, and then combining the
result of each scan after the first with the cumulative result
so far, as determined by the

reduce(R, R)

method. Each child may be either
a simple node of a list of nodes. The default behavior of the

reduce

method is such that the result of the visitXYZ method will be the result of
the last child scanned.

Here is an example to count the number of erroneous nodes in a tree:

```java
class CountErrors extends DocTreeScanner<Integer,Void> {
@Override
public Integer visitErroneous(ErroneousTree node, Void p) {
return 1;
}
@Override
public Integer reduce(Integer r1, Integer r2) {
return (r1 == null ? 0 : r1) + (r2 == null ? 0 : r2);
}
}
```

The default implementation of the visitXYZ methods will determine
a result as follows:

- If the node being visited has no children, the result will be

null

.

If the node being visited has one child, the result will be the
result of calling

scan

on that child. The child may be a simple node
or itself a list of nodes.

If the node being visited has more than one child, the result will
be determined by calling

scan

each child in turn, and then combining the
result of each scan after the first with the cumulative result
so far, as determined by the

reduce(R, R)

method. Each child may be either
a simple node of a list of nodes. The default behavior of the

reduce

method is such that the result of the visitXYZ method will be the result of
the last child scanned.

Here is an example to count the number of erroneous nodes in a tree:

```java
class CountErrors extends DocTreeScanner<Integer,Void> {
@Override
public Integer visitErroneous(ErroneousTree node, Void p) {
return 1;
}
@Override
public Integer reduce(Integer r1, Integer r2) {
return (r1 == null ? 0 : r1) + (r2 == null ? 0 : r2);
}
}
```

If the node being visited has no children, the result will be

null

.

If the node being visited has one child, the result will be the
result of calling

scan

on that child. The child may be a simple node
or itself a list of nodes.

If the node being visited has more than one child, the result will
be determined by calling

scan

each child in turn, and then combining the
result of each scan after the first with the cumulative result
so far, as determined by the

reduce(R, R)

method. Each child may be either
a simple node of a list of nodes. The default behavior of the

reduce

method is such that the result of the visitXYZ method will be the result of
the last child scanned.

Here is an example to count the number of erroneous nodes in a tree:

```java
class CountErrors extends DocTreeScanner<Integer,Void> {
@Override
public Integer visitErroneous(ErroneousTree node, Void p) {
return 1;
}
@Override
public Integer reduce(Integer r1, Integer r2) {
return (r1 == null ? 0 : r1) + (r2 == null ? 0 : r2);
}
}
```

class CountErrors extends DocTreeScanner<Integer,Void> {
@Override
public Integer visitErroneous(ErroneousTree node, Void p) {
return 1;
}
@Override
public Integer reduce(Integer r1, Integer r2) {
return (r1 == null ? 0 : r1) + (r2 == null ? 0 : r2);
}
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DocTreeScanner

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

R

reduce

​(

R

r1,

R

r2)

Reduces two results into a combined result.

R

scan

​(

DocTree

node,

P

p)

Scans a single node.

R

scan

​(

Iterable

<? extends

DocTree

> nodes,

P

p)

Scans a sequence of nodes.

R

visitAttribute

​(

AttributeTree

node,

P

p)

Visits an AttributeTree node.

R

visitAuthor

​(

AuthorTree

node,

P

p)

Visits an AuthorTree node.

R

visitComment

​(

CommentTree

node,

P

p)

Visits a CommentTree node.

R

visitDeprecated

​(

DeprecatedTree

node,

P

p)

Visits a DeprecatedTree node.

R

visitDocComment

​(

DocCommentTree

node,

P

p)

Visits a DocCommentTree node.

R

visitDocRoot

​(

DocRootTree

node,

P

p)

Visits a DocRootTree node.

R

visitDocType

​(

DocTypeTree

node,

P

p)

Visits a DocTypeTree node.

R

visitEndElement

​(

EndElementTree

node,

P

p)

Visits an EndElementTree node.

R

visitEntity

​(

EntityTree

node,

P

p)

Visits an EntityTree node.

R

visitErroneous

​(

ErroneousTree

node,

P

p)

Visits an ErroneousTree node.

R

visitHidden

​(

HiddenTree

node,

P

p)

Visits a HiddenTree node.

R

visitIdentifier

​(

IdentifierTree

node,

P

p)

Visits an IdentifierTree node.

R

visitIndex

​(

IndexTree

node,

P

p)

Visits an IndexTree node.

R

visitInheritDoc

​(

InheritDocTree

node,

P

p)

Visits an InheritDocTree node.

R

visitLink

​(

LinkTree

node,

P

p)

Visits a LinkTree node.

R

visitLiteral

​(

LiteralTree

node,

P

p)

Visits an LiteralTree node.

R

visitOther

​(

DocTree

node,

P

p)

Visits an unknown type of DocTree node.

R

visitParam

​(

ParamTree

node,

P

p)

Visits a ParamTree node.

R

visitProvides

​(

ProvidesTree

node,

P

p)

Visits a ProvidesTree node.

R

visitReference

​(

ReferenceTree

node,

P

p)

Visits a ReferenceTree node.

R

visitReturn

​(

ReturnTree

node,

P

p)

Visits a ReturnTree node.

R

visitSee

​(

SeeTree

node,

P

p)

Visits a SeeTree node.

R

visitSerial

​(

SerialTree

node,

P

p)

Visits a SerialTree node.

R

visitSerialData

​(

SerialDataTree

node,

P

p)

Visits a SerialDataTree node.

R

visitSerialField

​(

SerialFieldTree

node,

P

p)

Visits a SerialFieldTree node.

R

visitSince

​(

SinceTree

node,

P

p)

Visits a SinceTree node.

R

visitStartElement

​(

StartElementTree

node,

P

p)

Visits a StartElementTree node.

R

visitSummary

​(

SummaryTree

node,

P

p)

Visits a SummaryTree node.

R

visitText

​(

TextTree

node,

P

p)

Visits a TextTree node.

R

visitThrows

​(

ThrowsTree

node,

P

p)

Visits a ThrowsTree node.

R

visitUnknownBlockTag

​(

UnknownBlockTagTree

node,

P

p)

Visits an UnknownBlockTagTree node.

R

visitUnknownInlineTag

​(

UnknownInlineTagTree

node,

P

p)

Visits an UnknownInlineTagTree node.

R

visitUses

​(

UsesTree

node,

P

p)

Visits a UsesTree node.

R

visitValue

​(

ValueTree

node,

P

p)

Visits a ValueTree node.

R

visitVersion

​(

VersionTree

node,

P

p)

Visits a VersionTreeTree node.

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

DocTreeScanner

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

R

reduce

​(

R

r1,

R

r2)

Reduces two results into a combined result.

R

scan

​(

DocTree

node,

P

p)

Scans a single node.

R

scan

​(

Iterable

<? extends

DocTree

> nodes,

P

p)

Scans a sequence of nodes.

R

visitAttribute

​(

AttributeTree

node,

P

p)

Visits an AttributeTree node.

R

visitAuthor

​(

AuthorTree

node,

P

p)

Visits an AuthorTree node.

R

visitComment

​(

CommentTree

node,

P

p)

Visits a CommentTree node.

R

visitDeprecated

​(

DeprecatedTree

node,

P

p)

Visits a DeprecatedTree node.

R

visitDocComment

​(

DocCommentTree

node,

P

p)

Visits a DocCommentTree node.

R

visitDocRoot

​(

DocRootTree

node,

P

p)

Visits a DocRootTree node.

R

visitDocType

​(

DocTypeTree

node,

P

p)

Visits a DocTypeTree node.

R

visitEndElement

​(

EndElementTree

node,

P

p)

Visits an EndElementTree node.

R

visitEntity

​(

EntityTree

node,

P

p)

Visits an EntityTree node.

R

visitErroneous

​(

ErroneousTree

node,

P

p)

Visits an ErroneousTree node.

R

visitHidden

​(

HiddenTree

node,

P

p)

Visits a HiddenTree node.

R

visitIdentifier

​(

IdentifierTree

node,

P

p)

Visits an IdentifierTree node.

R

visitIndex

​(

IndexTree

node,

P

p)

Visits an IndexTree node.

R

visitInheritDoc

​(

InheritDocTree

node,

P

p)

Visits an InheritDocTree node.

R

visitLink

​(

LinkTree

node,

P

p)

Visits a LinkTree node.

R

visitLiteral

​(

LiteralTree

node,

P

p)

Visits an LiteralTree node.

R

visitOther

​(

DocTree

node,

P

p)

Visits an unknown type of DocTree node.

R

visitParam

​(

ParamTree

node,

P

p)

Visits a ParamTree node.

R

visitProvides

​(

ProvidesTree

node,

P

p)

Visits a ProvidesTree node.

R

visitReference

​(

ReferenceTree

node,

P

p)

Visits a ReferenceTree node.

R

visitReturn

​(

ReturnTree

node,

P

p)

Visits a ReturnTree node.

R

visitSee

​(

SeeTree

node,

P

p)

Visits a SeeTree node.

R

visitSerial

​(

SerialTree

node,

P

p)

Visits a SerialTree node.

R

visitSerialData

​(

SerialDataTree

node,

P

p)

Visits a SerialDataTree node.

R

visitSerialField

​(

SerialFieldTree

node,

P

p)

Visits a SerialFieldTree node.

R

visitSince

​(

SinceTree

node,

P

p)

Visits a SinceTree node.

R

visitStartElement

​(

StartElementTree

node,

P

p)

Visits a StartElementTree node.

R

visitSummary

​(

SummaryTree

node,

P

p)

Visits a SummaryTree node.

R

visitText

​(

TextTree

node,

P

p)

Visits a TextTree node.

R

visitThrows

​(

ThrowsTree

node,

P

p)

Visits a ThrowsTree node.

R

visitUnknownBlockTag

​(

UnknownBlockTagTree

node,

P

p)

Visits an UnknownBlockTagTree node.

R

visitUnknownInlineTag

​(

UnknownInlineTagTree

node,

P

p)

Visits an UnknownInlineTagTree node.

R

visitUses

​(

UsesTree

node,

P

p)

Visits a UsesTree node.

R

visitValue

​(

ValueTree

node,

P

p)

Visits a ValueTree node.

R

visitVersion

​(

VersionTree

node,

P

p)

Visits a VersionTreeTree node.

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

Reduces two results into a combined result.

Scans a single node.

Scans a sequence of nodes.

Visits an AttributeTree node.

Visits an AuthorTree node.

Visits a CommentTree node.

Visits a DeprecatedTree node.

Visits a DocCommentTree node.

Visits a DocRootTree node.

Visits a DocTypeTree node.

Visits an EndElementTree node.

Visits an EntityTree node.

Visits an ErroneousTree node.

Visits a HiddenTree node.

Visits an IdentifierTree node.

Visits an IndexTree node.

Visits an InheritDocTree node.

Visits a LinkTree node.

Visits an LiteralTree node.

Visits an unknown type of DocTree node.

Visits a ParamTree node.

Visits a ProvidesTree node.

Visits a ReferenceTree node.

Visits a ReturnTree node.

Visits a SeeTree node.

Visits a SerialTree node.

Visits a SerialDataTree node.

Visits a SerialFieldTree node.

Visits a SinceTree node.

Visits a StartElementTree node.

Visits a SummaryTree node.

Visits a TextTree node.

Visits a ThrowsTree node.

Visits an UnknownBlockTagTree node.

Visits an UnknownInlineTagTree node.

Visits a UsesTree node.

Visits a ValueTree node.

Visits a VersionTreeTree node.

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

- DocTreeScanner

```java
public DocTreeScanner()
```

============ METHOD DETAIL ==========

- Method Detail

- scan

```java
public
R
scan​(
DocTree
node,

P
p)
```

Scans a single node.

**Parameters:** node

- the node to be scanned
**Parameters:** p

- a parameter value passed to the visit method
**Returns:** the result value from the visit method

- scan

```java
public
R
scan​(
Iterable
<? extends
DocTree
> nodes,

P
p)
```

Scans a sequence of nodes.

**Parameters:** nodes

- the nodes to be scanned
**Parameters:** p

- a parameter value to be passed to the visit method for each node
**Returns:** the combined return value from the visit methods.
The values are combined using the

reduce

method.

- reduce

```java
public
R
reduce​(
R
r1,

R
r2)
```

Reduces two results into a combined result.
The default implementation is to return the first parameter.
The general contract of the method is that it may take any action whatsoever.

**Parameters:** r1

- the first of the values to be combined
**Parameters:** r2

- the second of the values to be combined
**Returns:** the result of combining the two parameters

- visitAttribute

```java
public
R
visitAttribute​(
AttributeTree
node,

P
p)
```

Visits an AttributeTree node. This implementation returns

null

.

**Specified by:** visitAttribute

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitAuthor

```java
public
R
visitAuthor​(
AuthorTree
node,

P
p)
```

Visits an AuthorTree node. This implementation scans the children in left to right order.

**Specified by:** visitAuthor

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitComment

```java
public
R
visitComment​(
CommentTree
node,

P
p)
```

Visits a CommentTree node. This implementation returns

null

.

**Specified by:** visitComment

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitDeprecated

```java
public
R
visitDeprecated​(
DeprecatedTree
node,

P
p)
```

Visits a DeprecatedTree node. This implementation scans the children in left to right order.

**Specified by:** visitDeprecated

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitDocComment

```java
public
R
visitDocComment​(
DocCommentTree
node,

P
p)
```

Visits a DocCommentTree node. This implementation scans the children in left to right order.

**Specified by:** visitDocComment

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitDocRoot

```java
public
R
visitDocRoot​(
DocRootTree
node,

P
p)
```

Visits a DocRootTree node. This implementation returns

null

.

**Specified by:** visitDocRoot

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitDocType

```java
public
R
visitDocType​(
DocTypeTree
node,

P
p)
```

Visits a DocTypeTree node. This implementation returns

null

.

**Specified by:** visitDocType

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitEndElement

```java
public
R
visitEndElement​(
EndElementTree
node,

P
p)
```

Visits an EndElementTree node. This implementation returns

null

.

**Specified by:** visitEndElement

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitEntity

```java
public
R
visitEntity​(
EntityTree
node,

P
p)
```

Visits an EntityTree node. This implementation returns

null

.

**Specified by:** visitEntity

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitErroneous

```java
public
R
visitErroneous​(
ErroneousTree
node,

P
p)
```

Visits an ErroneousTree node. This implementation returns

null

.

**Specified by:** visitErroneous

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitHidden

```java
public
R
visitHidden​(
HiddenTree
node,

P
p)
```

Visits a HiddenTree node. This implementation scans the children in left to right order.

**Specified by:** visitHidden

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitIdentifier

```java
public
R
visitIdentifier​(
IdentifierTree
node,

P
p)
```

Visits an IdentifierTree node. This implementation returns

null

.

**Specified by:** visitIdentifier

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitIndex

```java
public
R
visitIndex​(
IndexTree
node,

P
p)
```

Visits an IndexTree node. This implementation returns

null

.

**Specified by:** visitIndex

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitInheritDoc

```java
public
R
visitInheritDoc​(
InheritDocTree
node,

P
p)
```

Visits an InheritDocTree node. This implementation returns

null

.

**Specified by:** visitInheritDoc

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitLink

```java
public
R
visitLink​(
LinkTree
node,

P
p)
```

Visits a LinkTree node. This implementation scans the children in left to right order.

**Specified by:** visitLink

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitLiteral

```java
public
R
visitLiteral​(
LiteralTree
node,

P
p)
```

Visits an LiteralTree node. This implementation returns

null

.

**Specified by:** visitLiteral

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitParam

```java
public
R
visitParam​(
ParamTree
node,

P
p)
```

Visits a ParamTree node. This implementation scans the children in left to right order.

**Specified by:** visitParam

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitProvides

```java
public
R
visitProvides​(
ProvidesTree
node,

P
p)
```

Visits a ProvidesTree node. This implementation scans the children in left to right order.

**Specified by:** visitProvides

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitReference

```java
public
R
visitReference​(
ReferenceTree
node,

P
p)
```

Visits a ReferenceTree node. This implementation returns

null

.

**Specified by:** visitReference

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitReturn

```java
public
R
visitReturn​(
ReturnTree
node,

P
p)
```

Visits a ReturnTree node. This implementation scans the children in left to right order.

**Specified by:** visitReturn

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitSee

```java
public
R
visitSee​(
SeeTree
node,

P
p)
```

Visits a SeeTree node. This implementation scans the children in left to right order.

**Specified by:** visitSee

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitSerial

```java
public
R
visitSerial​(
SerialTree
node,

P
p)
```

Visits a SerialTree node. This implementation scans the children in left to right order.

**Specified by:** visitSerial

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitSerialData

```java
public
R
visitSerialData​(
SerialDataTree
node,

P
p)
```

Visits a SerialDataTree node. This implementation scans the children in left to right order.

**Specified by:** visitSerialData

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitSerialField

```java
public
R
visitSerialField​(
SerialFieldTree
node,

P
p)
```

Visits a SerialFieldTree node. This implementation scans the children in left to right order.

**Specified by:** visitSerialField

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitSince

```java
public
R
visitSince​(
SinceTree
node,

P
p)
```

Visits a SinceTree node. This implementation scans the children in left to right order.

**Specified by:** visitSince

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitStartElement

```java
public
R
visitStartElement​(
StartElementTree
node,

P
p)
```

Visits a StartElementTree node. This implementation scans the children in left to right order.

**Specified by:** visitStartElement

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitSummary

```java
public
R
visitSummary​(
SummaryTree
node,

P
p)
```

Visits a SummaryTree node. This implementation scans the children in left to right order.

**Specified by:** visitSummary

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning
**Since:** 10

- visitText

```java
public
R
visitText​(
TextTree
node,

P
p)
```

Visits a TextTree node. This implementation returns

null

.

**Specified by:** visitText

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitThrows

```java
public
R
visitThrows​(
ThrowsTree
node,

P
p)
```

Visits a ThrowsTree node. This implementation scans the children in left to right order.

**Specified by:** visitThrows

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitUnknownBlockTag

```java
public
R
visitUnknownBlockTag​(
UnknownBlockTagTree
node,

P
p)
```

Visits an UnknownBlockTagTree node. This implementation scans the children in left to right order.

**Specified by:** visitUnknownBlockTag

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitUnknownInlineTag

```java
public
R
visitUnknownInlineTag​(
UnknownInlineTagTree
node,

P
p)
```

Visits an UnknownInlineTagTree node. This implementation scans the children in left to right order.

**Specified by:** visitUnknownInlineTag

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitUses

```java
public
R
visitUses​(
UsesTree
node,

P
p)
```

Visits a UsesTree node. This implementation scans the children in left to right order.

**Specified by:** visitUses

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitValue

```java
public
R
visitValue​(
ValueTree
node,

P
p)
```

Visits a ValueTree node. This implementation scans the children in left to right order.

**Specified by:** visitValue

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitVersion

```java
public
R
visitVersion​(
VersionTree
node,

P
p)
```

Visits a VersionTreeTree node. This implementation scans the children in left to right order.

**Specified by:** visitVersion

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitOther

```java
public
R
visitOther​(
DocTree
node,

P
p)
```

Visits an unknown type of DocTree node.
This can occur if the set of tags evolves and new kinds
of nodes are added to the

DocTree

hierarchy. This implementation returns

null

.

**Specified by:** visitOther

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

Constructor Detail

- DocTreeScanner

```java
public DocTreeScanner()
```

---

#### Constructor Detail

DocTreeScanner

```java
public DocTreeScanner()
```

---

#### DocTreeScanner

public DocTreeScanner()

Method Detail

- scan

```java
public
R
scan​(
DocTree
node,

P
p)
```

Scans a single node.

**Parameters:** node

- the node to be scanned
**Parameters:** p

- a parameter value passed to the visit method
**Returns:** the result value from the visit method

- scan

```java
public
R
scan​(
Iterable
<? extends
DocTree
> nodes,

P
p)
```

Scans a sequence of nodes.

**Parameters:** nodes

- the nodes to be scanned
**Parameters:** p

- a parameter value to be passed to the visit method for each node
**Returns:** the combined return value from the visit methods.
The values are combined using the

reduce

method.

- reduce

```java
public
R
reduce​(
R
r1,

R
r2)
```

Reduces two results into a combined result.
The default implementation is to return the first parameter.
The general contract of the method is that it may take any action whatsoever.

**Parameters:** r1

- the first of the values to be combined
**Parameters:** r2

- the second of the values to be combined
**Returns:** the result of combining the two parameters

- visitAttribute

```java
public
R
visitAttribute​(
AttributeTree
node,

P
p)
```

Visits an AttributeTree node. This implementation returns

null

.

**Specified by:** visitAttribute

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitAuthor

```java
public
R
visitAuthor​(
AuthorTree
node,

P
p)
```

Visits an AuthorTree node. This implementation scans the children in left to right order.

**Specified by:** visitAuthor

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitComment

```java
public
R
visitComment​(
CommentTree
node,

P
p)
```

Visits a CommentTree node. This implementation returns

null

.

**Specified by:** visitComment

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitDeprecated

```java
public
R
visitDeprecated​(
DeprecatedTree
node,

P
p)
```

Visits a DeprecatedTree node. This implementation scans the children in left to right order.

**Specified by:** visitDeprecated

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitDocComment

```java
public
R
visitDocComment​(
DocCommentTree
node,

P
p)
```

Visits a DocCommentTree node. This implementation scans the children in left to right order.

**Specified by:** visitDocComment

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitDocRoot

```java
public
R
visitDocRoot​(
DocRootTree
node,

P
p)
```

Visits a DocRootTree node. This implementation returns

null

.

**Specified by:** visitDocRoot

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitDocType

```java
public
R
visitDocType​(
DocTypeTree
node,

P
p)
```

Visits a DocTypeTree node. This implementation returns

null

.

**Specified by:** visitDocType

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitEndElement

```java
public
R
visitEndElement​(
EndElementTree
node,

P
p)
```

Visits an EndElementTree node. This implementation returns

null

.

**Specified by:** visitEndElement

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitEntity

```java
public
R
visitEntity​(
EntityTree
node,

P
p)
```

Visits an EntityTree node. This implementation returns

null

.

**Specified by:** visitEntity

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitErroneous

```java
public
R
visitErroneous​(
ErroneousTree
node,

P
p)
```

Visits an ErroneousTree node. This implementation returns

null

.

**Specified by:** visitErroneous

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitHidden

```java
public
R
visitHidden​(
HiddenTree
node,

P
p)
```

Visits a HiddenTree node. This implementation scans the children in left to right order.

**Specified by:** visitHidden

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitIdentifier

```java
public
R
visitIdentifier​(
IdentifierTree
node,

P
p)
```

Visits an IdentifierTree node. This implementation returns

null

.

**Specified by:** visitIdentifier

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitIndex

```java
public
R
visitIndex​(
IndexTree
node,

P
p)
```

Visits an IndexTree node. This implementation returns

null

.

**Specified by:** visitIndex

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitInheritDoc

```java
public
R
visitInheritDoc​(
InheritDocTree
node,

P
p)
```

Visits an InheritDocTree node. This implementation returns

null

.

**Specified by:** visitInheritDoc

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitLink

```java
public
R
visitLink​(
LinkTree
node,

P
p)
```

Visits a LinkTree node. This implementation scans the children in left to right order.

**Specified by:** visitLink

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitLiteral

```java
public
R
visitLiteral​(
LiteralTree
node,

P
p)
```

Visits an LiteralTree node. This implementation returns

null

.

**Specified by:** visitLiteral

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitParam

```java
public
R
visitParam​(
ParamTree
node,

P
p)
```

Visits a ParamTree node. This implementation scans the children in left to right order.

**Specified by:** visitParam

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitProvides

```java
public
R
visitProvides​(
ProvidesTree
node,

P
p)
```

Visits a ProvidesTree node. This implementation scans the children in left to right order.

**Specified by:** visitProvides

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitReference

```java
public
R
visitReference​(
ReferenceTree
node,

P
p)
```

Visits a ReferenceTree node. This implementation returns

null

.

**Specified by:** visitReference

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitReturn

```java
public
R
visitReturn​(
ReturnTree
node,

P
p)
```

Visits a ReturnTree node. This implementation scans the children in left to right order.

**Specified by:** visitReturn

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitSee

```java
public
R
visitSee​(
SeeTree
node,

P
p)
```

Visits a SeeTree node. This implementation scans the children in left to right order.

**Specified by:** visitSee

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitSerial

```java
public
R
visitSerial​(
SerialTree
node,

P
p)
```

Visits a SerialTree node. This implementation scans the children in left to right order.

**Specified by:** visitSerial

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitSerialData

```java
public
R
visitSerialData​(
SerialDataTree
node,

P
p)
```

Visits a SerialDataTree node. This implementation scans the children in left to right order.

**Specified by:** visitSerialData

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitSerialField

```java
public
R
visitSerialField​(
SerialFieldTree
node,

P
p)
```

Visits a SerialFieldTree node. This implementation scans the children in left to right order.

**Specified by:** visitSerialField

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitSince

```java
public
R
visitSince​(
SinceTree
node,

P
p)
```

Visits a SinceTree node. This implementation scans the children in left to right order.

**Specified by:** visitSince

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitStartElement

```java
public
R
visitStartElement​(
StartElementTree
node,

P
p)
```

Visits a StartElementTree node. This implementation scans the children in left to right order.

**Specified by:** visitStartElement

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitSummary

```java
public
R
visitSummary​(
SummaryTree
node,

P
p)
```

Visits a SummaryTree node. This implementation scans the children in left to right order.

**Specified by:** visitSummary

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning
**Since:** 10

- visitText

```java
public
R
visitText​(
TextTree
node,

P
p)
```

Visits a TextTree node. This implementation returns

null

.

**Specified by:** visitText

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitThrows

```java
public
R
visitThrows​(
ThrowsTree
node,

P
p)
```

Visits a ThrowsTree node. This implementation scans the children in left to right order.

**Specified by:** visitThrows

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitUnknownBlockTag

```java
public
R
visitUnknownBlockTag​(
UnknownBlockTagTree
node,

P
p)
```

Visits an UnknownBlockTagTree node. This implementation scans the children in left to right order.

**Specified by:** visitUnknownBlockTag

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitUnknownInlineTag

```java
public
R
visitUnknownInlineTag​(
UnknownInlineTagTree
node,

P
p)
```

Visits an UnknownInlineTagTree node. This implementation scans the children in left to right order.

**Specified by:** visitUnknownInlineTag

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitUses

```java
public
R
visitUses​(
UsesTree
node,

P
p)
```

Visits a UsesTree node. This implementation scans the children in left to right order.

**Specified by:** visitUses

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitValue

```java
public
R
visitValue​(
ValueTree
node,

P
p)
```

Visits a ValueTree node. This implementation scans the children in left to right order.

**Specified by:** visitValue

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitVersion

```java
public
R
visitVersion​(
VersionTree
node,

P
p)
```

Visits a VersionTreeTree node. This implementation scans the children in left to right order.

**Specified by:** visitVersion

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

- visitOther

```java
public
R
visitOther​(
DocTree
node,

P
p)
```

Visits an unknown type of DocTree node.
This can occur if the set of tags evolves and new kinds
of nodes are added to the

DocTree

hierarchy. This implementation returns

null

.

**Specified by:** visitOther

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### Method Detail

scan

```java
public
R
scan​(
DocTree
node,

P
p)
```

Scans a single node.

**Parameters:** node

- the node to be scanned
**Parameters:** p

- a parameter value passed to the visit method
**Returns:** the result value from the visit method

---

#### scan

public

R

scan​(

DocTree

node,

P

p)

Scans a single node.

scan

```java
public
R
scan​(
Iterable
<? extends
DocTree
> nodes,

P
p)
```

Scans a sequence of nodes.

**Parameters:** nodes

- the nodes to be scanned
**Parameters:** p

- a parameter value to be passed to the visit method for each node
**Returns:** the combined return value from the visit methods.
The values are combined using the

reduce

method.

---

#### scan

public

R

scan​(

Iterable

<? extends

DocTree

> nodes,

P

p)

Scans a sequence of nodes.

reduce

```java
public
R
reduce​(
R
r1,

R
r2)
```

Reduces two results into a combined result.
The default implementation is to return the first parameter.
The general contract of the method is that it may take any action whatsoever.

**Parameters:** r1

- the first of the values to be combined
**Parameters:** r2

- the second of the values to be combined
**Returns:** the result of combining the two parameters

---

#### reduce

public

R

reduce​(

R

r1,

R

r2)

Reduces two results into a combined result.
The default implementation is to return the first parameter.
The general contract of the method is that it may take any action whatsoever.

visitAttribute

```java
public
R
visitAttribute​(
AttributeTree
node,

P
p)
```

Visits an AttributeTree node. This implementation returns

null

.

**Specified by:** visitAttribute

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitAttribute

public

R

visitAttribute​(

AttributeTree

node,

P

p)

Visits an AttributeTree node. This implementation returns

null

.

visitAuthor

```java
public
R
visitAuthor​(
AuthorTree
node,

P
p)
```

Visits an AuthorTree node. This implementation scans the children in left to right order.

**Specified by:** visitAuthor

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitAuthor

public

R

visitAuthor​(

AuthorTree

node,

P

p)

Visits an AuthorTree node. This implementation scans the children in left to right order.

visitComment

```java
public
R
visitComment​(
CommentTree
node,

P
p)
```

Visits a CommentTree node. This implementation returns

null

.

**Specified by:** visitComment

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitComment

public

R

visitComment​(

CommentTree

node,

P

p)

Visits a CommentTree node. This implementation returns

null

.

visitDeprecated

```java
public
R
visitDeprecated​(
DeprecatedTree
node,

P
p)
```

Visits a DeprecatedTree node. This implementation scans the children in left to right order.

**Specified by:** visitDeprecated

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitDeprecated

public

R

visitDeprecated​(

DeprecatedTree

node,

P

p)

Visits a DeprecatedTree node. This implementation scans the children in left to right order.

visitDocComment

```java
public
R
visitDocComment​(
DocCommentTree
node,

P
p)
```

Visits a DocCommentTree node. This implementation scans the children in left to right order.

**Specified by:** visitDocComment

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitDocComment

public

R

visitDocComment​(

DocCommentTree

node,

P

p)

Visits a DocCommentTree node. This implementation scans the children in left to right order.

visitDocRoot

```java
public
R
visitDocRoot​(
DocRootTree
node,

P
p)
```

Visits a DocRootTree node. This implementation returns

null

.

**Specified by:** visitDocRoot

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitDocRoot

public

R

visitDocRoot​(

DocRootTree

node,

P

p)

Visits a DocRootTree node. This implementation returns

null

.

visitDocType

```java
public
R
visitDocType​(
DocTypeTree
node,

P
p)
```

Visits a DocTypeTree node. This implementation returns

null

.

**Specified by:** visitDocType

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitDocType

public

R

visitDocType​(

DocTypeTree

node,

P

p)

Visits a DocTypeTree node. This implementation returns

null

.

visitEndElement

```java
public
R
visitEndElement​(
EndElementTree
node,

P
p)
```

Visits an EndElementTree node. This implementation returns

null

.

**Specified by:** visitEndElement

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitEndElement

public

R

visitEndElement​(

EndElementTree

node,

P

p)

Visits an EndElementTree node. This implementation returns

null

.

visitEntity

```java
public
R
visitEntity​(
EntityTree
node,

P
p)
```

Visits an EntityTree node. This implementation returns

null

.

**Specified by:** visitEntity

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitEntity

public

R

visitEntity​(

EntityTree

node,

P

p)

Visits an EntityTree node. This implementation returns

null

.

visitErroneous

```java
public
R
visitErroneous​(
ErroneousTree
node,

P
p)
```

Visits an ErroneousTree node. This implementation returns

null

.

**Specified by:** visitErroneous

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitErroneous

public

R

visitErroneous​(

ErroneousTree

node,

P

p)

Visits an ErroneousTree node. This implementation returns

null

.

visitHidden

```java
public
R
visitHidden​(
HiddenTree
node,

P
p)
```

Visits a HiddenTree node. This implementation scans the children in left to right order.

**Specified by:** visitHidden

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitHidden

public

R

visitHidden​(

HiddenTree

node,

P

p)

Visits a HiddenTree node. This implementation scans the children in left to right order.

visitIdentifier

```java
public
R
visitIdentifier​(
IdentifierTree
node,

P
p)
```

Visits an IdentifierTree node. This implementation returns

null

.

**Specified by:** visitIdentifier

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitIdentifier

public

R

visitIdentifier​(

IdentifierTree

node,

P

p)

Visits an IdentifierTree node. This implementation returns

null

.

visitIndex

```java
public
R
visitIndex​(
IndexTree
node,

P
p)
```

Visits an IndexTree node. This implementation returns

null

.

**Specified by:** visitIndex

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitIndex

public

R

visitIndex​(

IndexTree

node,

P

p)

Visits an IndexTree node. This implementation returns

null

.

visitInheritDoc

```java
public
R
visitInheritDoc​(
InheritDocTree
node,

P
p)
```

Visits an InheritDocTree node. This implementation returns

null

.

**Specified by:** visitInheritDoc

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitInheritDoc

public

R

visitInheritDoc​(

InheritDocTree

node,

P

p)

Visits an InheritDocTree node. This implementation returns

null

.

visitLink

```java
public
R
visitLink​(
LinkTree
node,

P
p)
```

Visits a LinkTree node. This implementation scans the children in left to right order.

**Specified by:** visitLink

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitLink

public

R

visitLink​(

LinkTree

node,

P

p)

Visits a LinkTree node. This implementation scans the children in left to right order.

visitLiteral

```java
public
R
visitLiteral​(
LiteralTree
node,

P
p)
```

Visits an LiteralTree node. This implementation returns

null

.

**Specified by:** visitLiteral

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitLiteral

public

R

visitLiteral​(

LiteralTree

node,

P

p)

Visits an LiteralTree node. This implementation returns

null

.

visitParam

```java
public
R
visitParam​(
ParamTree
node,

P
p)
```

Visits a ParamTree node. This implementation scans the children in left to right order.

**Specified by:** visitParam

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitParam

public

R

visitParam​(

ParamTree

node,

P

p)

Visits a ParamTree node. This implementation scans the children in left to right order.

visitProvides

```java
public
R
visitProvides​(
ProvidesTree
node,

P
p)
```

Visits a ProvidesTree node. This implementation scans the children in left to right order.

**Specified by:** visitProvides

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitProvides

public

R

visitProvides​(

ProvidesTree

node,

P

p)

Visits a ProvidesTree node. This implementation scans the children in left to right order.

visitReference

```java
public
R
visitReference​(
ReferenceTree
node,

P
p)
```

Visits a ReferenceTree node. This implementation returns

null

.

**Specified by:** visitReference

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitReference

public

R

visitReference​(

ReferenceTree

node,

P

p)

Visits a ReferenceTree node. This implementation returns

null

.

visitReturn

```java
public
R
visitReturn​(
ReturnTree
node,

P
p)
```

Visits a ReturnTree node. This implementation scans the children in left to right order.

**Specified by:** visitReturn

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitReturn

public

R

visitReturn​(

ReturnTree

node,

P

p)

Visits a ReturnTree node. This implementation scans the children in left to right order.

visitSee

```java
public
R
visitSee​(
SeeTree
node,

P
p)
```

Visits a SeeTree node. This implementation scans the children in left to right order.

**Specified by:** visitSee

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitSee

public

R

visitSee​(

SeeTree

node,

P

p)

Visits a SeeTree node. This implementation scans the children in left to right order.

visitSerial

```java
public
R
visitSerial​(
SerialTree
node,

P
p)
```

Visits a SerialTree node. This implementation scans the children in left to right order.

**Specified by:** visitSerial

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitSerial

public

R

visitSerial​(

SerialTree

node,

P

p)

Visits a SerialTree node. This implementation scans the children in left to right order.

visitSerialData

```java
public
R
visitSerialData​(
SerialDataTree
node,

P
p)
```

Visits a SerialDataTree node. This implementation scans the children in left to right order.

**Specified by:** visitSerialData

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitSerialData

public

R

visitSerialData​(

SerialDataTree

node,

P

p)

Visits a SerialDataTree node. This implementation scans the children in left to right order.

visitSerialField

```java
public
R
visitSerialField​(
SerialFieldTree
node,

P
p)
```

Visits a SerialFieldTree node. This implementation scans the children in left to right order.

**Specified by:** visitSerialField

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitSerialField

public

R

visitSerialField​(

SerialFieldTree

node,

P

p)

Visits a SerialFieldTree node. This implementation scans the children in left to right order.

visitSince

```java
public
R
visitSince​(
SinceTree
node,

P
p)
```

Visits a SinceTree node. This implementation scans the children in left to right order.

**Specified by:** visitSince

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitSince

public

R

visitSince​(

SinceTree

node,

P

p)

Visits a SinceTree node. This implementation scans the children in left to right order.

visitStartElement

```java
public
R
visitStartElement​(
StartElementTree
node,

P
p)
```

Visits a StartElementTree node. This implementation scans the children in left to right order.

**Specified by:** visitStartElement

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitStartElement

public

R

visitStartElement​(

StartElementTree

node,

P

p)

Visits a StartElementTree node. This implementation scans the children in left to right order.

visitSummary

```java
public
R
visitSummary​(
SummaryTree
node,

P
p)
```

Visits a SummaryTree node. This implementation scans the children in left to right order.

**Specified by:** visitSummary

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning
**Since:** 10

---

#### visitSummary

public

R

visitSummary​(

SummaryTree

node,

P

p)

Visits a SummaryTree node. This implementation scans the children in left to right order.

visitText

```java
public
R
visitText​(
TextTree
node,

P
p)
```

Visits a TextTree node. This implementation returns

null

.

**Specified by:** visitText

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitText

public

R

visitText​(

TextTree

node,

P

p)

Visits a TextTree node. This implementation returns

null

.

visitThrows

```java
public
R
visitThrows​(
ThrowsTree
node,

P
p)
```

Visits a ThrowsTree node. This implementation scans the children in left to right order.

**Specified by:** visitThrows

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitThrows

public

R

visitThrows​(

ThrowsTree

node,

P

p)

Visits a ThrowsTree node. This implementation scans the children in left to right order.

visitUnknownBlockTag

```java
public
R
visitUnknownBlockTag​(
UnknownBlockTagTree
node,

P
p)
```

Visits an UnknownBlockTagTree node. This implementation scans the children in left to right order.

**Specified by:** visitUnknownBlockTag

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitUnknownBlockTag

public

R

visitUnknownBlockTag​(

UnknownBlockTagTree

node,

P

p)

Visits an UnknownBlockTagTree node. This implementation scans the children in left to right order.

visitUnknownInlineTag

```java
public
R
visitUnknownInlineTag​(
UnknownInlineTagTree
node,

P
p)
```

Visits an UnknownInlineTagTree node. This implementation scans the children in left to right order.

**Specified by:** visitUnknownInlineTag

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitUnknownInlineTag

public

R

visitUnknownInlineTag​(

UnknownInlineTagTree

node,

P

p)

Visits an UnknownInlineTagTree node. This implementation scans the children in left to right order.

visitUses

```java
public
R
visitUses​(
UsesTree
node,

P
p)
```

Visits a UsesTree node. This implementation scans the children in left to right order.

**Specified by:** visitUses

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitUses

public

R

visitUses​(

UsesTree

node,

P

p)

Visits a UsesTree node. This implementation scans the children in left to right order.

visitValue

```java
public
R
visitValue​(
ValueTree
node,

P
p)
```

Visits a ValueTree node. This implementation scans the children in left to right order.

**Specified by:** visitValue

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitValue

public

R

visitValue​(

ValueTree

node,

P

p)

Visits a ValueTree node. This implementation scans the children in left to right order.

visitVersion

```java
public
R
visitVersion​(
VersionTree
node,

P
p)
```

Visits a VersionTreeTree node. This implementation scans the children in left to right order.

**Specified by:** visitVersion

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitVersion

public

R

visitVersion​(

VersionTree

node,

P

p)

Visits a VersionTreeTree node. This implementation scans the children in left to right order.

visitOther

```java
public
R
visitOther​(
DocTree
node,

P
p)
```

Visits an unknown type of DocTree node.
This can occur if the set of tags evolves and new kinds
of nodes are added to the

DocTree

hierarchy. This implementation returns

null

.

**Specified by:** visitOther

in interface

DocTreeVisitor

<

R

,​

P

>
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of scanning

---

#### visitOther

public

R

visitOther​(

DocTree

node,

P

p)

Visits an unknown type of DocTree node.
This can occur if the set of tags evolves and new kinds
of nodes are added to the

DocTree

hierarchy. This implementation returns

null

.

---

