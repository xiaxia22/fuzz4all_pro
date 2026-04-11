# Class SimpleTreeVisitorES6<R,​P>

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\SimpleTreeVisitorES6.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public class
SimpleTreeVisitorES6<R,​P>

extends
SimpleTreeVisitorES5_1
<R,​P>
```

A simple implementation of the TreeVisitor for ECMAScript edition 6.

The visit methods corresponding to ES 6 language constructs walk the
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

#### public SimpleTreeVisitorES6()

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

Visit Module tree.

**Specified by:**
- visitModule

in interface

TreeVisitor

<

R

,​

P

>

**Overrides:**
- visitModule

in class

SimpleTreeVisitorES5_1

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
- value from the visitor

---

#### public
R
visitExportEntry​(
ExportEntryTree
node,

P
p)

Visit Module ExportEntry tree.

**Specified by:**
- visitExportEntry

in interface

TreeVisitor

<

R

,​

P

>

**Overrides:**
- visitExportEntry

in class

SimpleTreeVisitorES5_1

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
- value from the visitor

---

#### public
R
visitImportEntry​(
ImportEntryTree
node,

P
p)

Visit Module ImportEntry tree.

**Specified by:**
- visitImportEntry

in interface

TreeVisitor

<

R

,​

P

>

**Overrides:**
- visitImportEntry

in class

SimpleTreeVisitorES5_1

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
- value from the visitor

---

#### public
R
visitClassDeclaration​(
ClassDeclarationTree
node,

P
p)

Visit class statement tree.

**Specified by:**
- visitClassDeclaration

in interface

TreeVisitor

<

R

,​

P

>

**Overrides:**
- visitClassDeclaration

in class

SimpleTreeVisitorES5_1

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
- value from the visitor

---

#### public
R
visitClassExpression​(
ClassExpressionTree
node,

P
p)

Visit class expression tree.

**Specified by:**
- visitClassExpression

in interface

TreeVisitor

<

R

,​

P

>

**Overrides:**
- visitClassExpression

in class

SimpleTreeVisitorES5_1

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
- value from the visitor

---

#### public
R
visitForOfLoop​(
ForOfLoopTree
node,

P
p)

Visit for..of statement tree.

**Specified by:**
- visitForOfLoop

in interface

TreeVisitor

<

R

,​

P

>

**Overrides:**
- visitForOfLoop

in class

SimpleTreeVisitorES5_1

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
- value from the visitor

---

#### public
R
visitYield​(
YieldTree
node,

P
p)

Visit 'yield' expression tree.

**Specified by:**
- visitYield

in interface

TreeVisitor

<

R

,​

P

>

**Overrides:**
- visitYield

in class

SimpleTreeVisitorES5_1

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
- value from the visitor

---

#### public
R
visitSpread​(
SpreadTree
node,

P
p)

Visit 'spread' expression tree.

**Specified by:**
- visitSpread

in interface

TreeVisitor

<

R

,​

P

>

**Overrides:**
- visitSpread

in class

SimpleTreeVisitorES5_1

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
- value from the visitor

---

#### public
R
visitTemplateLiteral​(
TemplateLiteralTree
node,

P
p)

Visit template literal tree.

**Specified by:**
- visitTemplateLiteral

in interface

TreeVisitor

<

R

,​

P

>

**Overrides:**
- visitTemplateLiteral

in class

SimpleTreeVisitorES5_1

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
- value from the visitor

---

### Additional Sections

#### Class SimpleTreeVisitorES6<R,​P>

java.lang.Object

- jdk.nashorn.api.tree.SimpleTreeVisitorES5_1

<R,​P>
- - jdk.nashorn.api.tree.SimpleTreeVisitorES6<R,​P>

jdk.nashorn.api.tree.SimpleTreeVisitorES5_1

<R,​P>

- jdk.nashorn.api.tree.SimpleTreeVisitorES6<R,​P>

jdk.nashorn.api.tree.SimpleTreeVisitorES6<R,​P>

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

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public class
SimpleTreeVisitorES6<R,​P>

extends
SimpleTreeVisitorES5_1
<R,​P>
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A simple implementation of the TreeVisitor for ECMAScript edition 6.

The visit methods corresponding to ES 6 language constructs walk the
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

SimpleTreeVisitorES6<R,​P>

extends

SimpleTreeVisitorES5_1

<R,​P>

A simple implementation of the TreeVisitor for ECMAScript edition 6.

The visit methods corresponding to ES 6 language constructs walk the
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

The visit methods corresponding to ES 6 language constructs walk the
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

SimpleTreeVisitorES6

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

Visit class statement tree.

R

visitClassExpression

​(

ClassExpressionTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit class expression tree.

R

visitExportEntry

​(

ExportEntryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module ExportEntry tree.

R

visitForOfLoop

​(

ForOfLoopTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit for..of statement tree.

R

visitImportEntry

​(

ImportEntryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module ImportEntry tree.

R

visitModule

​(

ModuleTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module tree.

R

visitSpread

​(

SpreadTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'spread' expression tree.

R

visitTemplateLiteral

​(

TemplateLiteralTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit template literal tree.

R

visitYield

​(

YieldTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'yield' expression tree.

- Methods declared in class jdk.nashorn.api.tree.

SimpleTreeVisitorES5_1

visitUnknown

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

SimpleTreeVisitorES6

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

Visit class statement tree.

R

visitClassExpression

​(

ClassExpressionTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit class expression tree.

R

visitExportEntry

​(

ExportEntryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module ExportEntry tree.

R

visitForOfLoop

​(

ForOfLoopTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit for..of statement tree.

R

visitImportEntry

​(

ImportEntryTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module ImportEntry tree.

R

visitModule

​(

ModuleTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit Module tree.

R

visitSpread

​(

SpreadTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'spread' expression tree.

R

visitTemplateLiteral

​(

TemplateLiteralTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit template literal tree.

R

visitYield

​(

YieldTree

node,

P

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Visit 'yield' expression tree.

- Methods declared in class jdk.nashorn.api.tree.

SimpleTreeVisitorES5_1

visitUnknown

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

Visit class statement tree.

Visit class expression tree.

Visit Module ExportEntry tree.

Visit for..of statement tree.

Visit Module ImportEntry tree.

Visit Module tree.

Visit 'spread' expression tree.

Visit template literal tree.

Visit 'yield' expression tree.

Methods declared in class jdk.nashorn.api.tree.

SimpleTreeVisitorES5_1

visitUnknown

---

#### Methods declared in class jdk.nashorn.api.tree. SimpleTreeVisitorES5_1

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

- SimpleTreeVisitorES6

```java
public SimpleTreeVisitorES6()
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

Visit Module tree.

**Specified by:** visitModule

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitModule

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit Module ExportEntry tree.

**Specified by:** visitExportEntry

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitExportEntry

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit Module ImportEntry tree.

**Specified by:** visitImportEntry

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitImportEntry

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit class statement tree.

**Specified by:** visitClassDeclaration

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitClassDeclaration

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit class expression tree.

**Specified by:** visitClassExpression

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitClassExpression

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit for..of statement tree.

**Specified by:** visitForOfLoop

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitForOfLoop

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit 'yield' expression tree.

**Specified by:** visitYield

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitYield

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit 'spread' expression tree.

**Specified by:** visitSpread

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitSpread

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit template literal tree.

**Specified by:** visitTemplateLiteral

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitTemplateLiteral

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

Constructor Detail

- SimpleTreeVisitorES6

```java
public SimpleTreeVisitorES6()
```

Deprecated, for removal: This API element is subject to removal in a future version.

---

#### Constructor Detail

SimpleTreeVisitorES6

```java
public SimpleTreeVisitorES6()
```

Deprecated, for removal: This API element is subject to removal in a future version.

---

#### SimpleTreeVisitorES6

public SimpleTreeVisitorES6()

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

Visit Module tree.

**Specified by:** visitModule

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitModule

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit Module ExportEntry tree.

**Specified by:** visitExportEntry

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitExportEntry

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit Module ImportEntry tree.

**Specified by:** visitImportEntry

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitImportEntry

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit class statement tree.

**Specified by:** visitClassDeclaration

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitClassDeclaration

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit class expression tree.

**Specified by:** visitClassExpression

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitClassExpression

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit for..of statement tree.

**Specified by:** visitForOfLoop

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitForOfLoop

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit 'yield' expression tree.

**Specified by:** visitYield

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitYield

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit 'spread' expression tree.

**Specified by:** visitSpread

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitSpread

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit template literal tree.

**Specified by:** visitTemplateLiteral

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitTemplateLiteral

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

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

Visit Module tree.

**Specified by:** visitModule

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitModule

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitModule

public

R

visitModule​(

ModuleTree

node,

P

p)

Visit Module tree.

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

Visit Module ExportEntry tree.

**Specified by:** visitExportEntry

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitExportEntry

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitExportEntry

public

R

visitExportEntry​(

ExportEntryTree

node,

P

p)

Visit Module ExportEntry tree.

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

Visit Module ImportEntry tree.

**Specified by:** visitImportEntry

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitImportEntry

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitImportEntry

public

R

visitImportEntry​(

ImportEntryTree

node,

P

p)

Visit Module ImportEntry tree.

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

Visit class statement tree.

**Specified by:** visitClassDeclaration

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitClassDeclaration

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitClassDeclaration

public

R

visitClassDeclaration​(

ClassDeclarationTree

node,

P

p)

Visit class statement tree.

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

Visit class expression tree.

**Specified by:** visitClassExpression

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitClassExpression

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitClassExpression

public

R

visitClassExpression​(

ClassExpressionTree

node,

P

p)

Visit class expression tree.

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

Visit for..of statement tree.

**Specified by:** visitForOfLoop

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitForOfLoop

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitForOfLoop

public

R

visitForOfLoop​(

ForOfLoopTree

node,

P

p)

Visit for..of statement tree.

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

Visit 'yield' expression tree.

**Specified by:** visitYield

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitYield

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitYield

public

R

visitYield​(

YieldTree

node,

P

p)

Visit 'yield' expression tree.

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

Visit 'spread' expression tree.

**Specified by:** visitSpread

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitSpread

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitSpread

public

R

visitSpread​(

SpreadTree

node,

P

p)

Visit 'spread' expression tree.

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

Visit template literal tree.

**Specified by:** visitTemplateLiteral

in interface

TreeVisitor

<

R

,​

P

>
**Overrides:** visitTemplateLiteral

in class

SimpleTreeVisitorES5_1

<

R

,​

P

>
**Parameters:** node

- node being visited
**Parameters:** p

- extra parameter passed to the visitor
**Returns:** value from the visitor

---

#### visitTemplateLiteral

public

R

visitTemplateLiteral​(

TemplateLiteralTree

node,

P

p)

Visit template literal tree.

---

