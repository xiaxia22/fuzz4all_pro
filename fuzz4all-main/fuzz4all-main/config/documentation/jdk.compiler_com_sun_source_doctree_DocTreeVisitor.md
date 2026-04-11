# Interface DocTreeVisitor<R,​P>

**Source:** `jdk.compiler\com\sun\source\doctree\DocTreeVisitor.html`

### Class Description

```java
public interface
DocTreeVisitor<R,​P>
```

A visitor of trees, in the style of the visitor design pattern.
Classes implementing this interface are used to operate
on a tree when the kind of tree is unknown at compile time.
When a visitor is passed to an tree's

accept

method, the

visit

Xyz

method most applicable
to that tree is invoked.

Classes implementing this interface may or may not throw a

NullPointerException

if the additional parameter

p

is

null

; see documentation of the implementing class for
details.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, doc comment
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform.

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

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### R
visitAttribute​(
AttributeTree
node,

P
p)

Visits an AttributeTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitAuthor​(
AuthorTree
node,

P
p)

Visits an AuthorTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitComment​(
CommentTree
node,

P
p)

Visits a CommentTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitDeprecated​(
DeprecatedTree
node,

P
p)

Visits a DeprecatedTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitDocComment​(
DocCommentTree
node,

P
p)

Visits a DocCommentTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitDocRoot​(
DocRootTree
node,

P
p)

Visits a DocRootTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### default
R
visitDocType​(
DocTypeTree
node,

P
p)

Visits a DocTypeTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

**Since:**
- 10

**Implementation Requirements:**
- Visits a

DocTypeTree

node
by calling

visitOther(node, p)

.

---

#### R
visitEndElement​(
EndElementTree
node,

P
p)

Visits an EndElementTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitEntity​(
EntityTree
node,

P
p)

Visits an EntityTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitErroneous​(
ErroneousTree
node,

P
p)

Visits an ErroneousTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### default
R
visitHidden​(
HiddenTree
node,

P
p)

Visits a HiddenTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

**Since:**
- 9

**Implementation Requirements:**
- Visits a

HiddenTree

node
by calling

visitOther(node, p)

.

---

#### R
visitIdentifier​(
IdentifierTree
node,

P
p)

Visits an IdentifierTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### default
R
visitIndex​(
IndexTree
node,

P
p)

Visits an IndexTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

**Since:**
- 9

**Implementation Requirements:**
- Visits an

IndexTree

node
by calling

visitOther(node, p)

.

---

#### R
visitInheritDoc​(
InheritDocTree
node,

P
p)

Visits an InheritDocTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitLink​(
LinkTree
node,

P
p)

Visits a LinkTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitLiteral​(
LiteralTree
node,

P
p)

Visits an LiteralTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitParam​(
ParamTree
node,

P
p)

Visits a ParamTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### default
R
visitProvides​(
ProvidesTree
node,

P
p)

Visits a ProvidesTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

**Since:**
- 9

**Implementation Requirements:**
- Visits a

ProvidesTree

node
by calling

visitOther(node, p)

.

---

#### R
visitReference​(
ReferenceTree
node,

P
p)

Visits a ReferenceTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitReturn​(
ReturnTree
node,

P
p)

Visits a ReturnTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitSee​(
SeeTree
node,

P
p)

Visits a SeeTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitSerial​(
SerialTree
node,

P
p)

Visits a SerialTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitSerialData​(
SerialDataTree
node,

P
p)

Visits a SerialDataTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitSerialField​(
SerialFieldTree
node,

P
p)

Visits a SerialFieldTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitSince​(
SinceTree
node,

P
p)

Visits a SinceTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitStartElement​(
StartElementTree
node,

P
p)

Visits a StartElementTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### default
R
visitSummary​(
SummaryTree
node,

P
p)

Visits a SummaryTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

**Since:**
- 10

**Implementation Requirements:**
- Visits a

SummaryTree

node
by calling

visitOther(node, p)

.

---

#### R
visitText​(
TextTree
node,

P
p)

Visits a TextTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitThrows​(
ThrowsTree
node,

P
p)

Visits a ThrowsTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitUnknownBlockTag​(
UnknownBlockTagTree
node,

P
p)

Visits an UnknownBlockTagTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitUnknownInlineTag​(
UnknownInlineTagTree
node,

P
p)

Visits an UnknownInlineTagTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### default
R
visitUses​(
UsesTree
node,

P
p)

Visits a UsesTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

**Since:**
- 9

**Implementation Requirements:**
- Visits a

UsesTree

node
by calling

visitOther(node, p)

.

---

#### R
visitValue​(
ValueTree
node,

P
p)

Visits a ValueTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitVersion​(
VersionTree
node,

P
p)

Visits a VersionTreeTree node.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

#### R
visitOther​(
DocTree
node,

P
p)

Visits an unknown type of DocTree node.
This can occur if the set of tags evolves and new kinds
of nodes are added to the

DocTree

hierarchy.

**Parameters:**
- node

- the node being visited
- p

- a parameter value

**Returns:**
- a result value

---

### Additional Sections

#### Interface DocTreeVisitor<R,​P>

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

**All Known Implementing Classes:** DocTreePathScanner

,

DocTreeScanner

,

SimpleDocTreeVisitor

```java
public interface
DocTreeVisitor<R,​P>
```

A visitor of trees, in the style of the visitor design pattern.
Classes implementing this interface are used to operate
on a tree when the kind of tree is unknown at compile time.
When a visitor is passed to an tree's

accept

method, the

visit

Xyz

method most applicable
to that tree is invoked.

Classes implementing this interface may or may not throw a

NullPointerException

if the additional parameter

p

is

null

; see documentation of the implementing class for
details.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, doc comment
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform.

**Since:** 1.8

public interface

DocTreeVisitor<R,​P>

A visitor of trees, in the style of the visitor design pattern.
Classes implementing this interface are used to operate
on a tree when the kind of tree is unknown at compile time.
When a visitor is passed to an tree's

accept

method, the

visit

Xyz

method most applicable
to that tree is invoked.

Classes implementing this interface may or may not throw a

NullPointerException

if the additional parameter

p

is

null

; see documentation of the implementing class for
details.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, doc comment
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform.

Classes implementing this interface may or may not throw a

NullPointerException

if the additional parameter

p

is

null

; see documentation of the implementing class for
details.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, doc comment
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, doc comment
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

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

default

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

default

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

default

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

default

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

default

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

default

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

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

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

default

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

default

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

default

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

default

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

default

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

default

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

---

#### Method Summary

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

============ METHOD DETAIL ==========

- Method Detail

- visitAttribute

```java
R
visitAttribute​(
AttributeTree
node,

P
p)
```

Visits an AttributeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitAuthor

```java
R
visitAuthor​(
AuthorTree
node,

P
p)
```

Visits an AuthorTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitComment

```java
R
visitComment​(
CommentTree
node,

P
p)
```

Visits a CommentTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitDeprecated

```java
R
visitDeprecated​(
DeprecatedTree
node,

P
p)
```

Visits a DeprecatedTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitDocComment

```java
R
visitDocComment​(
DocCommentTree
node,

P
p)
```

Visits a DocCommentTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitDocRoot

```java
R
visitDocRoot​(
DocRootTree
node,

P
p)
```

Visits a DocRootTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitDocType

```java
default
R
visitDocType​(
DocTypeTree
node,

P
p)
```

Visits a DocTypeTree node.

**Implementation Requirements:** Visits a

DocTypeTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 10

- visitEndElement

```java
R
visitEndElement​(
EndElementTree
node,

P
p)
```

Visits an EndElementTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitEntity

```java
R
visitEntity​(
EntityTree
node,

P
p)
```

Visits an EntityTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitErroneous

```java
R
visitErroneous​(
ErroneousTree
node,

P
p)
```

Visits an ErroneousTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitHidden

```java
default
R
visitHidden​(
HiddenTree
node,

P
p)
```

Visits a HiddenTree node.

**Implementation Requirements:** Visits a

HiddenTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 9

- visitIdentifier

```java
R
visitIdentifier​(
IdentifierTree
node,

P
p)
```

Visits an IdentifierTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitIndex

```java
default
R
visitIndex​(
IndexTree
node,

P
p)
```

Visits an IndexTree node.

**Implementation Requirements:** Visits an

IndexTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 9

- visitInheritDoc

```java
R
visitInheritDoc​(
InheritDocTree
node,

P
p)
```

Visits an InheritDocTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitLink

```java
R
visitLink​(
LinkTree
node,

P
p)
```

Visits a LinkTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitLiteral

```java
R
visitLiteral​(
LiteralTree
node,

P
p)
```

Visits an LiteralTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitParam

```java
R
visitParam​(
ParamTree
node,

P
p)
```

Visits a ParamTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitProvides

```java
default
R
visitProvides​(
ProvidesTree
node,

P
p)
```

Visits a ProvidesTree node.

**Implementation Requirements:** Visits a

ProvidesTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 9

- visitReference

```java
R
visitReference​(
ReferenceTree
node,

P
p)
```

Visits a ReferenceTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitReturn

```java
R
visitReturn​(
ReturnTree
node,

P
p)
```

Visits a ReturnTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitSee

```java
R
visitSee​(
SeeTree
node,

P
p)
```

Visits a SeeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitSerial

```java
R
visitSerial​(
SerialTree
node,

P
p)
```

Visits a SerialTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitSerialData

```java
R
visitSerialData​(
SerialDataTree
node,

P
p)
```

Visits a SerialDataTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitSerialField

```java
R
visitSerialField​(
SerialFieldTree
node,

P
p)
```

Visits a SerialFieldTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitSince

```java
R
visitSince​(
SinceTree
node,

P
p)
```

Visits a SinceTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitStartElement

```java
R
visitStartElement​(
StartElementTree
node,

P
p)
```

Visits a StartElementTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitSummary

```java
default
R
visitSummary​(
SummaryTree
node,

P
p)
```

Visits a SummaryTree node.

**Implementation Requirements:** Visits a

SummaryTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 10

- visitText

```java
R
visitText​(
TextTree
node,

P
p)
```

Visits a TextTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitThrows

```java
R
visitThrows​(
ThrowsTree
node,

P
p)
```

Visits a ThrowsTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitUnknownBlockTag

```java
R
visitUnknownBlockTag​(
UnknownBlockTagTree
node,

P
p)
```

Visits an UnknownBlockTagTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitUnknownInlineTag

```java
R
visitUnknownInlineTag​(
UnknownInlineTagTree
node,

P
p)
```

Visits an UnknownInlineTagTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitUses

```java
default
R
visitUses​(
UsesTree
node,

P
p)
```

Visits a UsesTree node.

**Implementation Requirements:** Visits a

UsesTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 9

- visitValue

```java
R
visitValue​(
ValueTree
node,

P
p)
```

Visits a ValueTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitVersion

```java
R
visitVersion​(
VersionTree
node,

P
p)
```

Visits a VersionTreeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitOther

```java
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

hierarchy.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

Method Detail

- visitAttribute

```java
R
visitAttribute​(
AttributeTree
node,

P
p)
```

Visits an AttributeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitAuthor

```java
R
visitAuthor​(
AuthorTree
node,

P
p)
```

Visits an AuthorTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitComment

```java
R
visitComment​(
CommentTree
node,

P
p)
```

Visits a CommentTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitDeprecated

```java
R
visitDeprecated​(
DeprecatedTree
node,

P
p)
```

Visits a DeprecatedTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitDocComment

```java
R
visitDocComment​(
DocCommentTree
node,

P
p)
```

Visits a DocCommentTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitDocRoot

```java
R
visitDocRoot​(
DocRootTree
node,

P
p)
```

Visits a DocRootTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitDocType

```java
default
R
visitDocType​(
DocTypeTree
node,

P
p)
```

Visits a DocTypeTree node.

**Implementation Requirements:** Visits a

DocTypeTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 10

- visitEndElement

```java
R
visitEndElement​(
EndElementTree
node,

P
p)
```

Visits an EndElementTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitEntity

```java
R
visitEntity​(
EntityTree
node,

P
p)
```

Visits an EntityTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitErroneous

```java
R
visitErroneous​(
ErroneousTree
node,

P
p)
```

Visits an ErroneousTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitHidden

```java
default
R
visitHidden​(
HiddenTree
node,

P
p)
```

Visits a HiddenTree node.

**Implementation Requirements:** Visits a

HiddenTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 9

- visitIdentifier

```java
R
visitIdentifier​(
IdentifierTree
node,

P
p)
```

Visits an IdentifierTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitIndex

```java
default
R
visitIndex​(
IndexTree
node,

P
p)
```

Visits an IndexTree node.

**Implementation Requirements:** Visits an

IndexTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 9

- visitInheritDoc

```java
R
visitInheritDoc​(
InheritDocTree
node,

P
p)
```

Visits an InheritDocTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitLink

```java
R
visitLink​(
LinkTree
node,

P
p)
```

Visits a LinkTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitLiteral

```java
R
visitLiteral​(
LiteralTree
node,

P
p)
```

Visits an LiteralTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitParam

```java
R
visitParam​(
ParamTree
node,

P
p)
```

Visits a ParamTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitProvides

```java
default
R
visitProvides​(
ProvidesTree
node,

P
p)
```

Visits a ProvidesTree node.

**Implementation Requirements:** Visits a

ProvidesTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 9

- visitReference

```java
R
visitReference​(
ReferenceTree
node,

P
p)
```

Visits a ReferenceTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitReturn

```java
R
visitReturn​(
ReturnTree
node,

P
p)
```

Visits a ReturnTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitSee

```java
R
visitSee​(
SeeTree
node,

P
p)
```

Visits a SeeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitSerial

```java
R
visitSerial​(
SerialTree
node,

P
p)
```

Visits a SerialTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitSerialData

```java
R
visitSerialData​(
SerialDataTree
node,

P
p)
```

Visits a SerialDataTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitSerialField

```java
R
visitSerialField​(
SerialFieldTree
node,

P
p)
```

Visits a SerialFieldTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitSince

```java
R
visitSince​(
SinceTree
node,

P
p)
```

Visits a SinceTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitStartElement

```java
R
visitStartElement​(
StartElementTree
node,

P
p)
```

Visits a StartElementTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitSummary

```java
default
R
visitSummary​(
SummaryTree
node,

P
p)
```

Visits a SummaryTree node.

**Implementation Requirements:** Visits a

SummaryTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 10

- visitText

```java
R
visitText​(
TextTree
node,

P
p)
```

Visits a TextTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitThrows

```java
R
visitThrows​(
ThrowsTree
node,

P
p)
```

Visits a ThrowsTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitUnknownBlockTag

```java
R
visitUnknownBlockTag​(
UnknownBlockTagTree
node,

P
p)
```

Visits an UnknownBlockTagTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitUnknownInlineTag

```java
R
visitUnknownInlineTag​(
UnknownInlineTagTree
node,

P
p)
```

Visits an UnknownInlineTagTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitUses

```java
default
R
visitUses​(
UsesTree
node,

P
p)
```

Visits a UsesTree node.

**Implementation Requirements:** Visits a

UsesTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 9

- visitValue

```java
R
visitValue​(
ValueTree
node,

P
p)
```

Visits a ValueTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitVersion

```java
R
visitVersion​(
VersionTree
node,

P
p)
```

Visits a VersionTreeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

- visitOther

```java
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

hierarchy.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### Method Detail

visitAttribute

```java
R
visitAttribute​(
AttributeTree
node,

P
p)
```

Visits an AttributeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitAttribute

R

visitAttribute​(

AttributeTree

node,

P

p)

Visits an AttributeTree node.

visitAuthor

```java
R
visitAuthor​(
AuthorTree
node,

P
p)
```

Visits an AuthorTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitAuthor

R

visitAuthor​(

AuthorTree

node,

P

p)

Visits an AuthorTree node.

visitComment

```java
R
visitComment​(
CommentTree
node,

P
p)
```

Visits a CommentTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitComment

R

visitComment​(

CommentTree

node,

P

p)

Visits a CommentTree node.

visitDeprecated

```java
R
visitDeprecated​(
DeprecatedTree
node,

P
p)
```

Visits a DeprecatedTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitDeprecated

R

visitDeprecated​(

DeprecatedTree

node,

P

p)

Visits a DeprecatedTree node.

visitDocComment

```java
R
visitDocComment​(
DocCommentTree
node,

P
p)
```

Visits a DocCommentTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitDocComment

R

visitDocComment​(

DocCommentTree

node,

P

p)

Visits a DocCommentTree node.

visitDocRoot

```java
R
visitDocRoot​(
DocRootTree
node,

P
p)
```

Visits a DocRootTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitDocRoot

R

visitDocRoot​(

DocRootTree

node,

P

p)

Visits a DocRootTree node.

visitDocType

```java
default
R
visitDocType​(
DocTypeTree
node,

P
p)
```

Visits a DocTypeTree node.

**Implementation Requirements:** Visits a

DocTypeTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 10

---

#### visitDocType

default

R

visitDocType​(

DocTypeTree

node,

P

p)

Visits a DocTypeTree node.

visitEndElement

```java
R
visitEndElement​(
EndElementTree
node,

P
p)
```

Visits an EndElementTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitEndElement

R

visitEndElement​(

EndElementTree

node,

P

p)

Visits an EndElementTree node.

visitEntity

```java
R
visitEntity​(
EntityTree
node,

P
p)
```

Visits an EntityTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitEntity

R

visitEntity​(

EntityTree

node,

P

p)

Visits an EntityTree node.

visitErroneous

```java
R
visitErroneous​(
ErroneousTree
node,

P
p)
```

Visits an ErroneousTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitErroneous

R

visitErroneous​(

ErroneousTree

node,

P

p)

Visits an ErroneousTree node.

visitHidden

```java
default
R
visitHidden​(
HiddenTree
node,

P
p)
```

Visits a HiddenTree node.

**Implementation Requirements:** Visits a

HiddenTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 9

---

#### visitHidden

default

R

visitHidden​(

HiddenTree

node,

P

p)

Visits a HiddenTree node.

visitIdentifier

```java
R
visitIdentifier​(
IdentifierTree
node,

P
p)
```

Visits an IdentifierTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitIdentifier

R

visitIdentifier​(

IdentifierTree

node,

P

p)

Visits an IdentifierTree node.

visitIndex

```java
default
R
visitIndex​(
IndexTree
node,

P
p)
```

Visits an IndexTree node.

**Implementation Requirements:** Visits an

IndexTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 9

---

#### visitIndex

default

R

visitIndex​(

IndexTree

node,

P

p)

Visits an IndexTree node.

visitInheritDoc

```java
R
visitInheritDoc​(
InheritDocTree
node,

P
p)
```

Visits an InheritDocTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitInheritDoc

R

visitInheritDoc​(

InheritDocTree

node,

P

p)

Visits an InheritDocTree node.

visitLink

```java
R
visitLink​(
LinkTree
node,

P
p)
```

Visits a LinkTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitLink

R

visitLink​(

LinkTree

node,

P

p)

Visits a LinkTree node.

visitLiteral

```java
R
visitLiteral​(
LiteralTree
node,

P
p)
```

Visits an LiteralTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitLiteral

R

visitLiteral​(

LiteralTree

node,

P

p)

Visits an LiteralTree node.

visitParam

```java
R
visitParam​(
ParamTree
node,

P
p)
```

Visits a ParamTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitParam

R

visitParam​(

ParamTree

node,

P

p)

Visits a ParamTree node.

visitProvides

```java
default
R
visitProvides​(
ProvidesTree
node,

P
p)
```

Visits a ProvidesTree node.

**Implementation Requirements:** Visits a

ProvidesTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 9

---

#### visitProvides

default

R

visitProvides​(

ProvidesTree

node,

P

p)

Visits a ProvidesTree node.

visitReference

```java
R
visitReference​(
ReferenceTree
node,

P
p)
```

Visits a ReferenceTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitReference

R

visitReference​(

ReferenceTree

node,

P

p)

Visits a ReferenceTree node.

visitReturn

```java
R
visitReturn​(
ReturnTree
node,

P
p)
```

Visits a ReturnTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitReturn

R

visitReturn​(

ReturnTree

node,

P

p)

Visits a ReturnTree node.

visitSee

```java
R
visitSee​(
SeeTree
node,

P
p)
```

Visits a SeeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitSee

R

visitSee​(

SeeTree

node,

P

p)

Visits a SeeTree node.

visitSerial

```java
R
visitSerial​(
SerialTree
node,

P
p)
```

Visits a SerialTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitSerial

R

visitSerial​(

SerialTree

node,

P

p)

Visits a SerialTree node.

visitSerialData

```java
R
visitSerialData​(
SerialDataTree
node,

P
p)
```

Visits a SerialDataTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitSerialData

R

visitSerialData​(

SerialDataTree

node,

P

p)

Visits a SerialDataTree node.

visitSerialField

```java
R
visitSerialField​(
SerialFieldTree
node,

P
p)
```

Visits a SerialFieldTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitSerialField

R

visitSerialField​(

SerialFieldTree

node,

P

p)

Visits a SerialFieldTree node.

visitSince

```java
R
visitSince​(
SinceTree
node,

P
p)
```

Visits a SinceTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitSince

R

visitSince​(

SinceTree

node,

P

p)

Visits a SinceTree node.

visitStartElement

```java
R
visitStartElement​(
StartElementTree
node,

P
p)
```

Visits a StartElementTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitStartElement

R

visitStartElement​(

StartElementTree

node,

P

p)

Visits a StartElementTree node.

visitSummary

```java
default
R
visitSummary​(
SummaryTree
node,

P
p)
```

Visits a SummaryTree node.

**Implementation Requirements:** Visits a

SummaryTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 10

---

#### visitSummary

default

R

visitSummary​(

SummaryTree

node,

P

p)

Visits a SummaryTree node.

visitText

```java
R
visitText​(
TextTree
node,

P
p)
```

Visits a TextTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitText

R

visitText​(

TextTree

node,

P

p)

Visits a TextTree node.

visitThrows

```java
R
visitThrows​(
ThrowsTree
node,

P
p)
```

Visits a ThrowsTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitThrows

R

visitThrows​(

ThrowsTree

node,

P

p)

Visits a ThrowsTree node.

visitUnknownBlockTag

```java
R
visitUnknownBlockTag​(
UnknownBlockTagTree
node,

P
p)
```

Visits an UnknownBlockTagTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitUnknownBlockTag

R

visitUnknownBlockTag​(

UnknownBlockTagTree

node,

P

p)

Visits an UnknownBlockTagTree node.

visitUnknownInlineTag

```java
R
visitUnknownInlineTag​(
UnknownInlineTagTree
node,

P
p)
```

Visits an UnknownInlineTagTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitUnknownInlineTag

R

visitUnknownInlineTag​(

UnknownInlineTagTree

node,

P

p)

Visits an UnknownInlineTagTree node.

visitUses

```java
default
R
visitUses​(
UsesTree
node,

P
p)
```

Visits a UsesTree node.

**Implementation Requirements:** Visits a

UsesTree

node
by calling

visitOther(node, p)

.
**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value
**Since:** 9

---

#### visitUses

default

R

visitUses​(

UsesTree

node,

P

p)

Visits a UsesTree node.

visitValue

```java
R
visitValue​(
ValueTree
node,

P
p)
```

Visits a ValueTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitValue

R

visitValue​(

ValueTree

node,

P

p)

Visits a ValueTree node.

visitVersion

```java
R
visitVersion​(
VersionTree
node,

P
p)
```

Visits a VersionTreeTree node.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitVersion

R

visitVersion​(

VersionTree

node,

P

p)

Visits a VersionTreeTree node.

visitOther

```java
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

hierarchy.

**Parameters:** node

- the node being visited
**Parameters:** p

- a parameter value
**Returns:** a result value

---

#### visitOther

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

hierarchy.

---

