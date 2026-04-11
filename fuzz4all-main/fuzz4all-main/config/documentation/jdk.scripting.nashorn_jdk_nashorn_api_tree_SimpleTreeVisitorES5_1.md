# Class SimpleTreeVisitorES5_1<R,​P>

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\SimpleTreeVisitorES5_1.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public class
SimpleTreeVisitorES5_1<R,​P>

extends
Object

implements
TreeVisitor
<R,​P>
```

A simple implementation of the TreeVisitor for ECMAScript edition 5.1.

The visit methods corresponding to ES 5.1 language constructs walk the
"components" of the given tree by calling accept method passing the
current visitor and the additional parameter.

For constructs introduced in later versions,

visitUnknown

is called instead which throws

UnknownTreeException

.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

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

#### public SimpleTreeVisitorES5_1()

*No description found.*

---

### Method Details

#### public
R
visitModule​(
ModuleTree
node,

P
p)

Visits a

ModuleTree

tree by calling

visitUnknown

.

**Specified by:**
- visitModule

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- the result of

visitUnknown

---

#### public
R
visitExportEntry​(
ExportEntryTree
node,

P
p)

Visits an

ExportEntryTree

tree by calling

visitUnknown

.

**Specified by:**
- visitExportEntry

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- the result of

visitUnknown

---

#### public
R
visitImportEntry​(
ImportEntryTree
node,

P
p)

Visits an

ImportEntryTree

tree by calling

visitUnknown

.

**Specified by:**
- visitImportEntry

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- the result of

visitUnknown

---

#### public
R
visitClassDeclaration​(
ClassDeclarationTree
node,

P
p)

Visits a

ClassDeclarationTree

tree by calling

visitUnknown

.

**Specified by:**
- visitClassDeclaration

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- the result of

visitUnknown

---

#### public
R
visitClassExpression​(
ClassExpressionTree
node,

P
p)

Visits a

ClassExpressionTree

tree by calling

visitUnknown

.

**Specified by:**
- visitClassExpression

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- the result of

visitUnknown

---

#### public
R
visitForOfLoop​(
ForOfLoopTree
node,

P
p)

Visits a

ForOfLoopTree

tree by calling

visitUnknown

.

**Specified by:**
- visitForOfLoop

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- the result of

visitUnknown

---

#### public
R
visitTemplateLiteral​(
TemplateLiteralTree
node,

P
p)

Visits a

TemplateLiteralTree

tree by calling

visitUnknown

.

**Specified by:**
- visitTemplateLiteral

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- the result of

visitUnknown

---

#### public
R
visitSpread​(
SpreadTree
node,

P
p)

Visits a

SpreadTree

tree by calling

visitUnknown

.

**Specified by:**
- visitSpread

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- the result of

visitUnknown

---

#### public
R
visitYield​(
YieldTree
node,

P
p)

Visits a

YieldTree

tree by calling

visitUnknown

.

**Specified by:**
- visitYield

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- the result of

visitUnknown

---

#### public
R
visitUnknown​(
Tree
node,

P
p)

Visit unknown expression/statement tree. This fallback will be
called if new Tree subtypes are introduced in future. A specific
implementation may throw {

unknown tree exception

if the visitor implementation was for an older language version.

**Specified by:**
- visitUnknown

in interface

TreeVisitor

<

R

,​

P

>

**Parameters:**
- node

- node being visited
- p

- extra parameter passed to the visitor

**Returns:**
- abnormal return by throwing exception always

**Throws:**
- UnknownTreeException

- a visitor implementation may optionally throw this exception

**Implementation Requirements:**
- The default implementation of this method in

SimpleTreeVisitorES5_1

will always throw

UnknownTypeException

. This behavior is not required of a
subclass.

---

### Additional Sections

#### Class SimpleTreeVisitorES5_1<R,​P>

java.lang.Object

- jdk.nashorn.api.tree.SimpleTreeVisitorES5_1<R,​P>

jdk.nashorn.api.tree.SimpleTreeVisitorES5_1<R,​P>

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

**All Implemented Interfaces:** TreeVisitor

<R,​P>

**Direct Known Subclasses:** SimpleTreeVisitorES6

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public class
SimpleTreeVisitorES5_1<R,​P>

extends
Object

implements
TreeVisitor
<R,​P>
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A simple implementation of the TreeVisitor for ECMAScript edition 5.1.

The visit methods corresponding to ES 5.1 language constructs walk the
"components" of the given tree by calling accept method passing the
current visitor and the additional parameter.

For constructs introduced in later versions,

visitUnknown

is called instead which throws

UnknownTreeException

.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

@Deprecated

(

since

="11",

forRemoval

=true)
public class

SimpleTreeVisitorES5_1<R,​P>

extends

Object

implements

TreeVisitor

<R,​P>

A simple implementation of the TreeVisitor for ECMAScript edition 5.1.

The visit methods corresponding to ES 5.1 language constructs walk the
"components" of the given tree by calling accept method passing the
current visitor and the additional parameter.

For constructs introduced in later versions,

visitUnknown

is called instead which throws

UnknownTreeException

.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

The visit methods corresponding to ES 5.1 language constructs walk the
"components" of the given tree by calling accept method passing the
current visitor and the additional parameter.

For constructs introduced in later versions,

visitUnknown

is called instead which throws

UnknownTreeException

.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

For constructs introduced in later versions,

visitUnknown

is called instead which throws

UnknownTreeException

.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SimpleTreeVisitorES5_1

()

Deprecated, for removal: This API element is subject to removal in a future version.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

R

visitClassDeclaration

​(

ClassDeclarationTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ClassDeclarationTree

tree by calling

visitUnknown

.

R

visitClassExpression

​(

ClassExpressionTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ClassExpressionTree

tree by calling

visitUnknown

.

R

visitExportEntry

​(

ExportEntryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits an

ExportEntryTree

tree by calling

visitUnknown

.

R

visitForOfLoop

​(

ForOfLoopTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ForOfLoopTree

tree by calling

visitUnknown

.

R

visitImportEntry

​(

ImportEntryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits an

ImportEntryTree

tree by calling

visitUnknown

.

R

visitModule

​(

ModuleTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ModuleTree

tree by calling

visitUnknown

.

R

visitSpread

​(

SpreadTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

SpreadTree

tree by calling

visitUnknown

.

R

visitTemplateLiteral

​(

TemplateLiteralTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

TemplateLiteralTree

tree by calling

visitUnknown

.

R

visitUnknown

​(

Tree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit unknown expression/statement tree.

R

visitYield

​(

YieldTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

YieldTree

tree by calling

visitUnknown

.

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

- Methods declared in interface jdk.nashorn.api.tree.

TreeVisitor

visitArrayAccess

,

visitArrayLiteral

,

visitAssignment

,

visitBinary

,

visitBlock

,

visitBreak

,

visitCase

,

visitCatch

,

visitCompilationUnit

,

visitCompoundAssignment

,

visitConditionalExpression

,

visitContinue

,

visitDebugger

,

visitDoWhileLoop

,

visitEmptyStatement

,

visitErroneous

,

visitExpressionStatement

,

visitForInLoop

,

visitForLoop

,

visitFunctionCall

,

visitFunctionDeclaration

,

visitFunctionExpression

,

visitIdentifier

,

visitIf

,

visitInstanceOf

,

visitLabeledStatement

,

visitLiteral

,

visitMemberSelect

,

visitNew

,

visitObjectLiteral

,

visitParenthesized

,

visitProperty

,

visitRegExpLiteral

,

visitReturn

,

visitSwitch

,

visitThrow

,

visitTry

,

visitUnary

,

visitVariable

,

visitWhileLoop

,

visitWith

Constructor Summary

Constructors

Constructor

Description

SimpleTreeVisitorES5_1

()

Deprecated, for removal: This API element is subject to removal in a future version.

---

#### Constructor Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

R

visitClassDeclaration

​(

ClassDeclarationTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ClassDeclarationTree

tree by calling

visitUnknown

.

R

visitClassExpression

​(

ClassExpressionTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ClassExpressionTree

tree by calling

visitUnknown

.

R

visitExportEntry

​(

ExportEntryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits an

ExportEntryTree

tree by calling

visitUnknown

.

R

visitForOfLoop

​(

ForOfLoopTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ForOfLoopTree

tree by calling

visitUnknown

.

R

visitImportEntry

​(

ImportEntryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits an

ImportEntryTree

tree by calling

visitUnknown

.

R

visitModule

​(

ModuleTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ModuleTree

tree by calling

visitUnknown

.

R

visitSpread

​(

SpreadTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

SpreadTree

tree by calling

visitUnknown

.

R

visitTemplateLiteral

​(

TemplateLiteralTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

TemplateLiteralTree

tree by calling

visitUnknown

.

R

visitUnknown

​(

Tree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit unknown expression/statement tree.

R

visitYield

​(

YieldTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

YieldTree

tree by calling

visitUnknown

.

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

- Methods declared in interface jdk.nashorn.api.tree.

TreeVisitor

visitArrayAccess

,

visitArrayLiteral

,

visitAssignment

,

visitBinary

,

visitBlock

,

visitBreak

,

visitCase

,

visitCatch

,

visitCompilationUnit

,

visitCompoundAssignment

,

visitConditionalExpression

,

visitContinue

,

visitDebugger

,

visitDoWhileLoop

,

visitEmptyStatement

,

visitErroneous

,

visitExpressionStatement

,

visitForInLoop

,

visitForLoop

,

visitFunctionCall

,

visitFunctionDeclaration

,

visitFunctionExpression

,

visitIdentifier

,

visitIf

,

visitInstanceOf

,

visitLabeledStatement

,

visitLiteral

,

visitMemberSelect

,

visitNew

,

visitObjectLiteral

,

visitParenthesized

,

visitProperty

,

visitRegExpLiteral

,

visitReturn

,

visitSwitch

,

visitThrow

,

visitTry

,

visitUnary

,

visitVariable

,

visitWhileLoop

,

visitWith

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ClassDeclarationTree

tree by calling

visitUnknown

.

Visits a

ClassExpressionTree

tree by calling

visitUnknown

.

Visits an

ExportEntryTree

tree by calling

visitUnknown

.

Visits a

ForOfLoopTree

tree by calling

visitUnknown

.

Visits an

ImportEntryTree

tree by calling

visitUnknown

.

Visits a

ModuleTree

tree by calling

visitUnknown

.

Visits a

SpreadTree

tree by calling

visitUnknown

.

Visits a

TemplateLiteralTree

tree by calling

visitUnknown

.

Visit unknown expression/statement tree.

Visits a

YieldTree

tree by calling

visitUnknown

.

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

Methods declared in interface jdk.nashorn.api.tree.

TreeVisitor

visitArrayAccess

,

visitArrayLiteral

,

visitAssignment

,

visitBinary

,

visitBlock

,

visitBreak

,

visitCase

,

visitCatch

,

visitCompilationUnit

,

visitCompoundAssignment

,

visitConditionalExpression

,

visitContinue

,

visitDebugger

,

visitDoWhileLoop

,

visitEmptyStatement

,

visitErroneous

,

visitExpressionStatement

,

visitForInLoop

,

visitForLoop

,

visitFunctionCall

,

visitFunctionDeclaration

,

visitFunctionExpression

,

visitIdentifier

,

visitIf

,

visitInstanceOf

,

visitLabeledStatement

,

visitLiteral

,

visitMemberSelect

,

visitNew

,

visitObjectLiteral

,

visitParenthesized

,

visitProperty

,

visitRegExpLiteral

,

visitReturn

,

visitSwitch

,

visitThrow

,

visitTry

,

visitUnary

,

visitVariable

,

visitWhileLoop

,

visitWith

---

#### Methods declared in interface jdk.nashorn.api.tree. TreeVisitor

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SimpleTreeVisitorES5_1

```java
public SimpleTreeVisitorES5_1()
```

Deprecated, for removal: This API element is subject to removal in a future version.

============ METHOD DETAIL ==========

- Method Detail

- visitModule

```java
public
R
visitModule​(
ModuleTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ModuleTree

tree by calling

visitUnknown

.

**Specified by:** visitModule

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitExportEntry

```java
public
R
visitExportEntry​(
ExportEntryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits an

ExportEntryTree

tree by calling

visitUnknown

.

**Specified by:** visitExportEntry

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitImportEntry

```java
public
R
visitImportEntry​(
ImportEntryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits an

ImportEntryTree

tree by calling

visitUnknown

.

**Specified by:** visitImportEntry

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitClassDeclaration

```java
public
R
visitClassDeclaration​(
ClassDeclarationTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ClassDeclarationTree

tree by calling

visitUnknown

.

**Specified by:** visitClassDeclaration

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitClassExpression

```java
public
R
visitClassExpression​(
ClassExpressionTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ClassExpressionTree

tree by calling

visitUnknown

.

**Specified by:** visitClassExpression

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitForOfLoop

```java
public
R
visitForOfLoop​(
ForOfLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ForOfLoopTree

tree by calling

visitUnknown

.

**Specified by:** visitForOfLoop

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitTemplateLiteral

```java
public
R
visitTemplateLiteral​(
TemplateLiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

TemplateLiteralTree

tree by calling

visitUnknown

.

**Specified by:** visitTemplateLiteral

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitSpread

```java
public
R
visitSpread​(
SpreadTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

SpreadTree

tree by calling

visitUnknown

.

**Specified by:** visitSpread

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitYield

```java
public
R
visitYield​(
YieldTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

YieldTree

tree by calling

visitUnknown

.

**Specified by:** visitYield

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitUnknown

```java
public
R
visitUnknown​(
Tree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit unknown expression/statement tree. This fallback will be
called if new Tree subtypes are introduced in future. A specific
implementation may throw {

unknown tree exception

if the visitor implementation was for an older language version.

**Specified by:** visitUnknown

in interface

TreeVisitor

<

R

,​

P

>
**Implementation Requirements:** The default implementation of this method in

SimpleTreeVisitorES5_1

will always throw

UnknownTypeException

. This behavior is not required of a
subclass.
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** abnormal return by throwing exception always
**Throws:** UnknownTreeException

- a visitor implementation may optionally throw this exception

Constructor Detail

- SimpleTreeVisitorES5_1

```java
public SimpleTreeVisitorES5_1()
```

Deprecated, for removal: This API element is subject to removal in a future version.

---

#### Constructor Detail

SimpleTreeVisitorES5_1

```java
public SimpleTreeVisitorES5_1()
```

Deprecated, for removal: This API element is subject to removal in a future version.

---

#### SimpleTreeVisitorES5_1

public SimpleTreeVisitorES5_1()

Method Detail

- visitModule

```java
public
R
visitModule​(
ModuleTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ModuleTree

tree by calling

visitUnknown

.

**Specified by:** visitModule

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitExportEntry

```java
public
R
visitExportEntry​(
ExportEntryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits an

ExportEntryTree

tree by calling

visitUnknown

.

**Specified by:** visitExportEntry

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitImportEntry

```java
public
R
visitImportEntry​(
ImportEntryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits an

ImportEntryTree

tree by calling

visitUnknown

.

**Specified by:** visitImportEntry

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitClassDeclaration

```java
public
R
visitClassDeclaration​(
ClassDeclarationTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ClassDeclarationTree

tree by calling

visitUnknown

.

**Specified by:** visitClassDeclaration

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitClassExpression

```java
public
R
visitClassExpression​(
ClassExpressionTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ClassExpressionTree

tree by calling

visitUnknown

.

**Specified by:** visitClassExpression

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitForOfLoop

```java
public
R
visitForOfLoop​(
ForOfLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ForOfLoopTree

tree by calling

visitUnknown

.

**Specified by:** visitForOfLoop

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitTemplateLiteral

```java
public
R
visitTemplateLiteral​(
TemplateLiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

TemplateLiteralTree

tree by calling

visitUnknown

.

**Specified by:** visitTemplateLiteral

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitSpread

```java
public
R
visitSpread​(
SpreadTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

SpreadTree

tree by calling

visitUnknown

.

**Specified by:** visitSpread

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitYield

```java
public
R
visitYield​(
YieldTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

YieldTree

tree by calling

visitUnknown

.

**Specified by:** visitYield

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

- visitUnknown

```java
public
R
visitUnknown​(
Tree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit unknown expression/statement tree. This fallback will be
called if new Tree subtypes are introduced in future. A specific
implementation may throw {

unknown tree exception

if the visitor implementation was for an older language version.

**Specified by:** visitUnknown

in interface

TreeVisitor

<

R

,​

P

>
**Implementation Requirements:** The default implementation of this method in

SimpleTreeVisitorES5_1

will always throw

UnknownTypeException

. This behavior is not required of a
subclass.
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** abnormal return by throwing exception always
**Throws:** UnknownTreeException

- a visitor implementation may optionally throw this exception

---

#### Method Detail

visitModule

```java
public
R
visitModule​(
ModuleTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ModuleTree

tree by calling

visitUnknown

.

**Specified by:** visitModule

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

---

#### visitModule

public

R

visitModule​(

ModuleTree

node,

P

p)

Visits a

ModuleTree

tree by calling

visitUnknown

.

visitExportEntry

```java
public
R
visitExportEntry​(
ExportEntryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits an

ExportEntryTree

tree by calling

visitUnknown

.

**Specified by:** visitExportEntry

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

---

#### visitExportEntry

public

R

visitExportEntry​(

ExportEntryTree

node,

P

p)

Visits an

ExportEntryTree

tree by calling

visitUnknown

.

visitImportEntry

```java
public
R
visitImportEntry​(
ImportEntryTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits an

ImportEntryTree

tree by calling

visitUnknown

.

**Specified by:** visitImportEntry

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

---

#### visitImportEntry

public

R

visitImportEntry​(

ImportEntryTree

node,

P

p)

Visits an

ImportEntryTree

tree by calling

visitUnknown

.

visitClassDeclaration

```java
public
R
visitClassDeclaration​(
ClassDeclarationTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ClassDeclarationTree

tree by calling

visitUnknown

.

**Specified by:** visitClassDeclaration

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

---

#### visitClassDeclaration

public

R

visitClassDeclaration​(

ClassDeclarationTree

node,

P

p)

Visits a

ClassDeclarationTree

tree by calling

visitUnknown

.

visitClassExpression

```java
public
R
visitClassExpression​(
ClassExpressionTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ClassExpressionTree

tree by calling

visitUnknown

.

**Specified by:** visitClassExpression

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

---

#### visitClassExpression

public

R

visitClassExpression​(

ClassExpressionTree

node,

P

p)

Visits a

ClassExpressionTree

tree by calling

visitUnknown

.

visitForOfLoop

```java
public
R
visitForOfLoop​(
ForOfLoopTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

ForOfLoopTree

tree by calling

visitUnknown

.

**Specified by:** visitForOfLoop

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

---

#### visitForOfLoop

public

R

visitForOfLoop​(

ForOfLoopTree

node,

P

p)

Visits a

ForOfLoopTree

tree by calling

visitUnknown

.

visitTemplateLiteral

```java
public
R
visitTemplateLiteral​(
TemplateLiteralTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

TemplateLiteralTree

tree by calling

visitUnknown

.

**Specified by:** visitTemplateLiteral

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

---

#### visitTemplateLiteral

public

R

visitTemplateLiteral​(

TemplateLiteralTree

node,

P

p)

Visits a

TemplateLiteralTree

tree by calling

visitUnknown

.

visitSpread

```java
public
R
visitSpread​(
SpreadTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

SpreadTree

tree by calling

visitUnknown

.

**Specified by:** visitSpread

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

---

#### visitSpread

public

R

visitSpread​(

SpreadTree

node,

P

p)

Visits a

SpreadTree

tree by calling

visitUnknown

.

visitYield

```java
public
R
visitYield​(
YieldTree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visits a

YieldTree

tree by calling

visitUnknown

.

**Specified by:** visitYield

in interface

TreeVisitor

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** the result of

visitUnknown

---

#### visitYield

public

R

visitYield​(

YieldTree

node,

P

p)

Visits a

YieldTree

tree by calling

visitUnknown

.

visitUnknown

```java
public
R
visitUnknown​(
Tree
node,

P
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Visit unknown expression/statement tree. This fallback will be
called if new Tree subtypes are introduced in future. A specific
implementation may throw {

unknown tree exception

if the visitor implementation was for an older language version.

**Specified by:** visitUnknown

in interface

TreeVisitor

<

R

,​

P

>
**Implementation Requirements:** The default implementation of this method in

SimpleTreeVisitorES5_1

will always throw

UnknownTypeException

. This behavior is not required of a
subclass.
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** abnormal return by throwing exception always
**Throws:** UnknownTreeException

- a visitor implementation may optionally throw this exception

---

#### visitUnknown

public

R

visitUnknown​(

Tree

node,

P

p)

Visit unknown expression/statement tree. This fallback will be
called if new Tree subtypes are introduced in future. A specific
implementation may throw {

unknown tree exception

if the visitor implementation was for an older language version.

---

