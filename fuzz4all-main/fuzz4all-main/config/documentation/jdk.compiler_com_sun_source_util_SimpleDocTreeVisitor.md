# Class SimpleDocTreeVisitor<R,​P>

**Source:** `jdk.compiler\com\sun\source\util\SimpleDocTreeVisitor.html`

### Class Description

```java
public class
SimpleDocTreeVisitor<R,​P>

extends
Object

implements
DocTreeVisitor
<R,​P>
```

A simple visitor for tree nodes.

**Type Parameters:** R

- the return type of this visitor's methods. Use

Void

for visitors that do not need to return results.
**Type Parameters:** P

- the type of the additional parameter to this visitor's
methods. Use

Void

for visitors that do not need an
additional parameter.

---

### Field Details

#### protected final
R
DEFAULT_VALUE

The default value, returned by the

default action

.

---

### Constructor Details

#### protected SimpleDocTreeVisitor()

Creates a visitor, with a DEFAULT_VALUE of

null

.

---

#### protected SimpleDocTreeVisitor​(
R
defaultValue)

Creates a visitor, with a specified DEFAULT_VALUE.

**Parameters:**
- defaultValue

- the default value to be returned by the default action.

---

### Method Details

#### protected
R
defaultAction​(
DocTree
node,

P
p)

The default action, used by all visit methods that are not overridden.

**Parameters:**
- node

- the node being visited
- p

- the parameter value passed to the visit method

**Returns:**
- the result value to be returned from the visit method

---

#### public final
R
visit​(
DocTree
node,

P
p)

Invokes the appropriate visit method specific to the type of the node.

**Parameters:**
- node

- the node on which to dispatch
- p

- a parameter to be passed to the appropriate visit method

**Returns:**
- the value returns from the appropriate visit method

---

#### public final
R
visit​(
Iterable
<? extends
DocTree
> nodes,

P
p)

Invokes the appropriate visit method on each of a sequence of nodes.

**Parameters:**
- nodes

- the nodes on which to dispatch
- p

- a parameter value to be passed to each appropriate visit method

**Returns:**
- the value return from the last of the visit methods, or null
if none were called.

---

#### public
R
visitAttribute​(
AttributeTree
node,

P
p)

Visits an AttributeTree node. This implementation calls

defaultAction

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
- the result of

defaultAction

---

#### public
R
visitAuthor​(
AuthorTree
node,

P
p)

Visits an AuthorTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

---

#### public
R
visitComment​(
CommentTree
node,

P
p)

Visits a CommentTree node. This implementation calls

defaultAction

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
- the result of

defaultAction

---

#### public
R
visitDeprecated​(
DeprecatedTree
node,

P
p)

Visits a DeprecatedTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

---

#### public
R
visitDocComment​(
DocCommentTree
node,

P
p)

Visits a DocCommentTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

---

#### public
R
visitDocRoot​(
DocRootTree
node,

P
p)

Visits a DocRootTree node. This implementation calls

defaultAction

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
- the result of

defaultAction

---

#### public
R
visitDocType​(
DocTypeTree
node,

P
p)

Visits a DocTypeTree node.

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
- the result of

defaultAction

**Since:**
- 10

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

#### public
R
visitEndElement​(
EndElementTree
node,

P
p)

Visits an EndElementTree node. This implementation calls

defaultAction

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
- the result of

defaultAction

---

#### public
R
visitEntity​(
EntityTree
node,

P
p)

Visits an EntityTree node. This implementation calls

defaultAction

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
- the result of

defaultAction

---

#### public
R
visitErroneous​(
ErroneousTree
node,

P
p)

Visits an ErroneousTree node. This implementation calls

defaultAction

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
- the result of

defaultAction

---

#### public
R
visitHidden​(
HiddenTree
node,

P
p)

Visits a HiddenTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

**Since:**
- 9

---

#### public
R
visitIdentifier​(
IdentifierTree
node,

P
p)

Visits an IdentifierTree node. This implementation calls

defaultAction

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
- the result of

defaultAction

---

#### public
R
visitIndex​(
IndexTree
node,

P
p)

Visits an IndexTree node. This implementation calls

defaultAction

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
- the result of

defaultAction

**Since:**
- 9

---

#### public
R
visitInheritDoc​(
InheritDocTree
node,

P
p)

Visits an InheritDocTree node. This implementation calls

defaultAction

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
- the result of

defaultAction

---

#### public
R
visitLink​(
LinkTree
node,

P
p)

Visits a LinkTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

---

#### public
R
visitLiteral​(
LiteralTree
node,

P
p)

Visits an LiteralTree node. This implementation calls

defaultAction

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
- the result of

defaultAction

---

#### public
R
visitParam​(
ParamTree
node,

P
p)

Visits a ParamTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

---

#### public
R
visitProvides​(
ProvidesTree
node,

P
p)

Visits a ProvidesTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

**Since:**
- 9

---

#### public
R
visitReference​(
ReferenceTree
node,

P
p)

Visits a ReferenceTree node. This implementation calls

defaultAction

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
- the result of

defaultAction

---

#### public
R
visitReturn​(
ReturnTree
node,

P
p)

Visits a ReturnTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

---

#### public
R
visitSee​(
SeeTree
node,

P
p)

Visits a SeeTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

---

#### public
R
visitSerial​(
SerialTree
node,

P
p)

Visits a SerialTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

---

#### public
R
visitSerialData​(
SerialDataTree
node,

P
p)

Visits a SerialDataTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

---

#### public
R
visitSerialField​(
SerialFieldTree
node,

P
p)

Visits a SerialFieldTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

---

#### public
R
visitSince​(
SinceTree
node,

P
p)

Visits a SinceTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

---

#### public
R
visitStartElement​(
StartElementTree
node,

P
p)

Visits a StartElementTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

---

#### public
R
visitSummary​(
SummaryTree
node,

P
p)

Visits a SummaryTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

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

Visits a TextTree node. This implementation calls

defaultAction

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
- the result of

defaultAction

---

#### public
R
visitThrows​(
ThrowsTree
node,

P
p)

Visits a ThrowsTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

---

#### public
R
visitUnknownBlockTag​(
UnknownBlockTagTree
node,

P
p)

Visits an UnknownBlockTagTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

---

#### public
R
visitUnknownInlineTag​(
UnknownInlineTagTree
node,

P
p)

Visits an UnknownInlineTagTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

---

#### public
R
visitUses​(
UsesTree
node,

P
p)

Visits a UsesTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

**Since:**
- 9

---

#### public
R
visitValue​(
ValueTree
node,

P
p)

Visits a ValueTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

---

#### public
R
visitVersion​(
VersionTree
node,

P
p)

Visits a VersionTreeTree node. This implementation calls

defaultAction

.

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
- the result of

defaultAction

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

hierarchy. This implementation calls

defaultAction

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
- the result of

defaultAction

---

### Additional Sections

#### Class SimpleDocTreeVisitor<R,​P>

java.lang.Object

- com.sun.source.util.SimpleDocTreeVisitor<R,​P>

com.sun.source.util.SimpleDocTreeVisitor<R,​P>

**Type Parameters:** R

- the return type of this visitor's methods. Use

Void

for visitors that do not need to return results.
**Type Parameters:** P

- the type of the additional parameter to this visitor's
methods. Use

Void

for visitors that do not need an
additional parameter.

**All Implemented Interfaces:** DocTreeVisitor

<R,​P>

```java
public class
SimpleDocTreeVisitor<R,​P>

extends
Object

implements
DocTreeVisitor
<R,​P>
```

A simple visitor for tree nodes.

**Since:** 1.8

public class

SimpleDocTreeVisitor<R,​P>

extends

Object

implements

DocTreeVisitor

<R,​P>

A simple visitor for tree nodes.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

R

DEFAULT_VALUE

The default value, returned by the

default action

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SimpleDocTreeVisitor

()

Creates a visitor, with a DEFAULT_VALUE of

null

.

protected

SimpleDocTreeVisitor

​(

R

defaultValue)

Creates a visitor, with a specified DEFAULT_VALUE.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

R

defaultAction

​(

DocTree

node,

P

p)

The default action, used by all visit methods that are not overridden.

R

visit

​(

DocTree

node,

P

p)

Invokes the appropriate visit method specific to the type of the node.

R

visit

​(

Iterable

<? extends

DocTree

> nodes,

P

p)

Invokes the appropriate visit method on each of a sequence of nodes.

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

Field Summary

Fields

Modifier and Type

Field

Description

protected

R

DEFAULT_VALUE

The default value, returned by the

default action

.

---

#### Field Summary

The default value, returned by the

default action

.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SimpleDocTreeVisitor

()

Creates a visitor, with a DEFAULT_VALUE of

null

.

protected

SimpleDocTreeVisitor

​(

R

defaultValue)

Creates a visitor, with a specified DEFAULT_VALUE.

---

#### Constructor Summary

Creates a visitor, with a DEFAULT_VALUE of

null

.

Creates a visitor, with a specified DEFAULT_VALUE.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

R

defaultAction

​(

DocTree

node,

P

p)

The default action, used by all visit methods that are not overridden.

R

visit

​(

DocTree

node,

P

p)

Invokes the appropriate visit method specific to the type of the node.

R

visit

​(

Iterable

<? extends

DocTree

> nodes,

P

p)

Invokes the appropriate visit method on each of a sequence of nodes.

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

The default action, used by all visit methods that are not overridden.

Invokes the appropriate visit method specific to the type of the node.

Invokes the appropriate visit method on each of a sequence of nodes.

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

============ FIELD DETAIL ===========

- Field Detail

- DEFAULT_VALUE

```java
protected final
R
DEFAULT_VALUE
```

The default value, returned by the

default action

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SimpleDocTreeVisitor

```java
protected SimpleDocTreeVisitor()
```

Creates a visitor, with a DEFAULT_VALUE of

null

.

- SimpleDocTreeVisitor

```java
protected SimpleDocTreeVisitor​(
R
defaultValue)
```

Creates a visitor, with a specified DEFAULT_VALUE.

**Parameters:** defaultValue

- the default value to be returned by the default action.

============ METHOD DETAIL ==========

- Method Detail

- defaultAction

```java
protected
R
defaultAction​(
DocTree
node,

P
p)
```

The default action, used by all visit methods that are not overridden.

**Parameters:** node

- the node being visited
**Parameters:** p

- the parameter value passed to the visit method
**Returns:** the result value to be returned from the visit method

- visit

```java
public final
R
visit​(
DocTree
node,

P
p)
```

Invokes the appropriate visit method specific to the type of the node.

**Parameters:** node

- the node on which to dispatch
**Parameters:** p

- a parameter to be passed to the appropriate visit method
**Returns:** the value returns from the appropriate visit method

- visit

```java
public final
R
visit​(
Iterable
<? extends
DocTree
> nodes,

P
p)
```

Invokes the appropriate visit method on each of a sequence of nodes.

**Parameters:** nodes

- the nodes on which to dispatch
**Parameters:** p

- a parameter value to be passed to each appropriate visit method
**Returns:** the value return from the last of the visit methods, or null
if none were called.

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

Visits an AttributeTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits an AuthorTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a CommentTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits a DeprecatedTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a DocCommentTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a DocRootTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits a DocTypeTree node.

**Specified by:** visitDocType

in interface

DocTreeVisitor

<

R

,​

P

>
**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction
**Since:** 10

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

Visits an EndElementTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits an EntityTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits an ErroneousTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits a HiddenTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction
**Since:** 9

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

Visits an IdentifierTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits an IndexTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction
**Since:** 9

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

Visits an InheritDocTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits a LinkTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits an LiteralTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits a ParamTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a ProvidesTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction
**Since:** 9

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

Visits a ReferenceTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits a ReturnTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a SeeTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a SerialTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a SerialDataTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a SerialFieldTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a SinceTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a StartElementTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a SummaryTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction
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

Visits a TextTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits a ThrowsTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits an UnknownBlockTagTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits an UnknownInlineTagTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a UsesTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction
**Since:** 9

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

Visits a ValueTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a VersionTreeTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

hierarchy. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

Field Detail

- DEFAULT_VALUE

```java
protected final
R
DEFAULT_VALUE
```

The default value, returned by the

default action

.

---

#### Field Detail

DEFAULT_VALUE

```java
protected final
R
DEFAULT_VALUE
```

The default value, returned by the

default action

.

---

#### DEFAULT_VALUE

protected final

R

DEFAULT_VALUE

The default value, returned by the

default action

.

Constructor Detail

- SimpleDocTreeVisitor

```java
protected SimpleDocTreeVisitor()
```

Creates a visitor, with a DEFAULT_VALUE of

null

.

- SimpleDocTreeVisitor

```java
protected SimpleDocTreeVisitor​(
R
defaultValue)
```

Creates a visitor, with a specified DEFAULT_VALUE.

**Parameters:** defaultValue

- the default value to be returned by the default action.

---

#### Constructor Detail

SimpleDocTreeVisitor

```java
protected SimpleDocTreeVisitor()
```

Creates a visitor, with a DEFAULT_VALUE of

null

.

---

#### SimpleDocTreeVisitor

protected SimpleDocTreeVisitor()

Creates a visitor, with a DEFAULT_VALUE of

null

.

SimpleDocTreeVisitor

```java
protected SimpleDocTreeVisitor​(
R
defaultValue)
```

Creates a visitor, with a specified DEFAULT_VALUE.

**Parameters:** defaultValue

- the default value to be returned by the default action.

---

#### SimpleDocTreeVisitor

protected SimpleDocTreeVisitor​(

R

defaultValue)

Creates a visitor, with a specified DEFAULT_VALUE.

Method Detail

- defaultAction

```java
protected
R
defaultAction​(
DocTree
node,

P
p)
```

The default action, used by all visit methods that are not overridden.

**Parameters:** node

- the node being visited
**Parameters:** p

- the parameter value passed to the visit method
**Returns:** the result value to be returned from the visit method

- visit

```java
public final
R
visit​(
DocTree
node,

P
p)
```

Invokes the appropriate visit method specific to the type of the node.

**Parameters:** node

- the node on which to dispatch
**Parameters:** p

- a parameter to be passed to the appropriate visit method
**Returns:** the value returns from the appropriate visit method

- visit

```java
public final
R
visit​(
Iterable
<? extends
DocTree
> nodes,

P
p)
```

Invokes the appropriate visit method on each of a sequence of nodes.

**Parameters:** nodes

- the nodes on which to dispatch
**Parameters:** p

- a parameter value to be passed to each appropriate visit method
**Returns:** the value return from the last of the visit methods, or null
if none were called.

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

Visits an AttributeTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits an AuthorTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a CommentTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits a DeprecatedTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a DocCommentTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a DocRootTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits a DocTypeTree node.

**Specified by:** visitDocType

in interface

DocTreeVisitor

<

R

,​

P

>
**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction
**Since:** 10

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

Visits an EndElementTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits an EntityTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits an ErroneousTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits a HiddenTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction
**Since:** 9

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

Visits an IdentifierTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits an IndexTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction
**Since:** 9

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

Visits an InheritDocTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits a LinkTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits an LiteralTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits a ParamTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a ProvidesTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction
**Since:** 9

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

Visits a ReferenceTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits a ReturnTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a SeeTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a SerialTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a SerialDataTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a SerialFieldTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a SinceTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a StartElementTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a SummaryTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction
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

Visits a TextTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

Visits a ThrowsTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits an UnknownBlockTagTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits an UnknownInlineTagTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a UsesTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction
**Since:** 9

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

Visits a ValueTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

Visits a VersionTreeTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

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

hierarchy. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

---

#### Method Detail

defaultAction

```java
protected
R
defaultAction​(
DocTree
node,

P
p)
```

The default action, used by all visit methods that are not overridden.

**Parameters:** node

- the node being visited
**Parameters:** p

- the parameter value passed to the visit method
**Returns:** the result value to be returned from the visit method

---

#### defaultAction

protected

R

defaultAction​(

DocTree

node,

P

p)

The default action, used by all visit methods that are not overridden.

visit

```java
public final
R
visit​(
DocTree
node,

P
p)
```

Invokes the appropriate visit method specific to the type of the node.

**Parameters:** node

- the node on which to dispatch
**Parameters:** p

- a parameter to be passed to the appropriate visit method
**Returns:** the value returns from the appropriate visit method

---

#### visit

public final

R

visit​(

DocTree

node,

P

p)

Invokes the appropriate visit method specific to the type of the node.

visit

```java
public final
R
visit​(
Iterable
<? extends
DocTree
> nodes,

P
p)
```

Invokes the appropriate visit method on each of a sequence of nodes.

**Parameters:** nodes

- the nodes on which to dispatch
**Parameters:** p

- a parameter value to be passed to each appropriate visit method
**Returns:** the value return from the last of the visit methods, or null
if none were called.

---

#### visit

public final

R

visit​(

Iterable

<? extends

DocTree

> nodes,

P

p)

Invokes the appropriate visit method on each of a sequence of nodes.

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

Visits an AttributeTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

---

#### visitAttribute

public

R

visitAttribute​(

AttributeTree

node,

P

p)

Visits an AttributeTree node. This implementation calls

defaultAction

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

Visits an AuthorTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitAuthor

public

R

visitAuthor​(

AuthorTree

node,

P

p)

Visits an AuthorTree node. This implementation calls

defaultAction

.

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

Visits a CommentTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

---

#### visitComment

public

R

visitComment​(

CommentTree

node,

P

p)

Visits a CommentTree node. This implementation calls

defaultAction

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

Visits a DeprecatedTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitDeprecated

public

R

visitDeprecated​(

DeprecatedTree

node,

P

p)

Visits a DeprecatedTree node. This implementation calls

defaultAction

.

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

Visits a DocCommentTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitDocComment

public

R

visitDocComment​(

DocCommentTree

node,

P

p)

Visits a DocCommentTree node. This implementation calls

defaultAction

.

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

Visits a DocRootTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

---

#### visitDocRoot

public

R

visitDocRoot​(

DocRootTree

node,

P

p)

Visits a DocRootTree node. This implementation calls

defaultAction

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

Visits a DocTypeTree node.

**Specified by:** visitDocType

in interface

DocTreeVisitor

<

R

,​

P

>
**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** the result of

defaultAction
**Since:** 10

---

#### visitDocType

public

R

visitDocType​(

DocTypeTree

node,

P

p)

Visits a DocTypeTree node.

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

Visits an EndElementTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

---

#### visitEndElement

public

R

visitEndElement​(

EndElementTree

node,

P

p)

Visits an EndElementTree node. This implementation calls

defaultAction

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

Visits an EntityTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

---

#### visitEntity

public

R

visitEntity​(

EntityTree

node,

P

p)

Visits an EntityTree node. This implementation calls

defaultAction

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

Visits an ErroneousTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

---

#### visitErroneous

public

R

visitErroneous​(

ErroneousTree

node,

P

p)

Visits an ErroneousTree node. This implementation calls

defaultAction

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

Visits a HiddenTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction
**Since:** 9

---

#### visitHidden

public

R

visitHidden​(

HiddenTree

node,

P

p)

Visits a HiddenTree node. This implementation calls

defaultAction

.

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

Visits an IdentifierTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

---

#### visitIdentifier

public

R

visitIdentifier​(

IdentifierTree

node,

P

p)

Visits an IdentifierTree node. This implementation calls

defaultAction

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

Visits an IndexTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction
**Since:** 9

---

#### visitIndex

public

R

visitIndex​(

IndexTree

node,

P

p)

Visits an IndexTree node. This implementation calls

defaultAction

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

Visits an InheritDocTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

---

#### visitInheritDoc

public

R

visitInheritDoc​(

InheritDocTree

node,

P

p)

Visits an InheritDocTree node. This implementation calls

defaultAction

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

Visits a LinkTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitLink

public

R

visitLink​(

LinkTree

node,

P

p)

Visits a LinkTree node. This implementation calls

defaultAction

.

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

Visits an LiteralTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

---

#### visitLiteral

public

R

visitLiteral​(

LiteralTree

node,

P

p)

Visits an LiteralTree node. This implementation calls

defaultAction

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

Visits a ParamTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitParam

public

R

visitParam​(

ParamTree

node,

P

p)

Visits a ParamTree node. This implementation calls

defaultAction

.

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

Visits a ProvidesTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction
**Since:** 9

---

#### visitProvides

public

R

visitProvides​(

ProvidesTree

node,

P

p)

Visits a ProvidesTree node. This implementation calls

defaultAction

.

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

Visits a ReferenceTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

---

#### visitReference

public

R

visitReference​(

ReferenceTree

node,

P

p)

Visits a ReferenceTree node. This implementation calls

defaultAction

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

Visits a ReturnTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitReturn

public

R

visitReturn​(

ReturnTree

node,

P

p)

Visits a ReturnTree node. This implementation calls

defaultAction

.

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

Visits a SeeTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitSee

public

R

visitSee​(

SeeTree

node,

P

p)

Visits a SeeTree node. This implementation calls

defaultAction

.

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

Visits a SerialTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitSerial

public

R

visitSerial​(

SerialTree

node,

P

p)

Visits a SerialTree node. This implementation calls

defaultAction

.

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

Visits a SerialDataTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitSerialData

public

R

visitSerialData​(

SerialDataTree

node,

P

p)

Visits a SerialDataTree node. This implementation calls

defaultAction

.

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

Visits a SerialFieldTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitSerialField

public

R

visitSerialField​(

SerialFieldTree

node,

P

p)

Visits a SerialFieldTree node. This implementation calls

defaultAction

.

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

Visits a SinceTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitSince

public

R

visitSince​(

SinceTree

node,

P

p)

Visits a SinceTree node. This implementation calls

defaultAction

.

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

Visits a StartElementTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitStartElement

public

R

visitStartElement​(

StartElementTree

node,

P

p)

Visits a StartElementTree node. This implementation calls

defaultAction

.

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

Visits a SummaryTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction
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

Visits a SummaryTree node. This implementation calls

defaultAction

.

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

Visits a TextTree node. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

---

#### visitText

public

R

visitText​(

TextTree

node,

P

p)

Visits a TextTree node. This implementation calls

defaultAction

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

Visits a ThrowsTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitThrows

public

R

visitThrows​(

ThrowsTree

node,

P

p)

Visits a ThrowsTree node. This implementation calls

defaultAction

.

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

Visits an UnknownBlockTagTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitUnknownBlockTag

public

R

visitUnknownBlockTag​(

UnknownBlockTagTree

node,

P

p)

Visits an UnknownBlockTagTree node. This implementation calls

defaultAction

.

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

Visits an UnknownInlineTagTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitUnknownInlineTag

public

R

visitUnknownInlineTag​(

UnknownInlineTagTree

node,

P

p)

Visits an UnknownInlineTagTree node. This implementation calls

defaultAction

.

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

Visits a UsesTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction
**Since:** 9

---

#### visitUses

public

R

visitUses​(

UsesTree

node,

P

p)

Visits a UsesTree node. This implementation calls

defaultAction

.

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

Visits a ValueTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitValue

public

R

visitValue​(

ValueTree

node,

P

p)

Visits a ValueTree node. This implementation calls

defaultAction

.

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

Visits a VersionTreeTree node. This implementation calls

defaultAction

.

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
**Returns:** the result of

defaultAction

---

#### visitVersion

public

R

visitVersion​(

VersionTree

node,

P

p)

Visits a VersionTreeTree node. This implementation calls

defaultAction

.

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

hierarchy. This implementation calls

defaultAction

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
**Returns:** the result of

defaultAction

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

hierarchy. This implementation calls

defaultAction

.

---

