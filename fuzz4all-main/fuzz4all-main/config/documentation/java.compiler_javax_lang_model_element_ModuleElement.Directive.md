# Interface ModuleElement.Directive

**Source:** `java.compiler\javax\lang\model\element\ModuleElement.Directive.html`

### Class Description

```java
public static interface
ModuleElement.Directive
```

Represents a directive within the declaration of this
module. The directives of a module declaration configure the
module in the Java Platform Module System.

**All Known Subinterfaces:** ModuleElement.ExportsDirective

,

ModuleElement.OpensDirective

,

ModuleElement.ProvidesDirective

,

ModuleElement.RequiresDirective

,

ModuleElement.UsesDirective

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ModuleElement.DirectiveKind
getKind()

Returns the

kind

of this directive.

**Returns:**
- the kind of this directive

---

#### <R,​P> R accept​(
ModuleElement.DirectiveVisitor
<R,​P> v,
P p)

Applies a visitor to this directive.

**Parameters:**
- v

- the visitor operating on this directive
- p

- additional parameter to the visitor

**Returns:**
- a visitor-specified result

**Type Parameters:**
- R

- the return type of the visitor's methods
- P

- the type of the additional parameter to the visitor's methods

---

### Additional Sections

#### Interface ModuleElement.Directive

**All Known Subinterfaces:** ModuleElement.ExportsDirective

,

ModuleElement.OpensDirective

,

ModuleElement.ProvidesDirective

,

ModuleElement.RequiresDirective

,

ModuleElement.UsesDirective

**Enclosing interface:** ModuleElement

```java
public static interface
ModuleElement.Directive
```

Represents a directive within the declaration of this
module. The directives of a module declaration configure the
module in the Java Platform Module System.

**Since:** 9

public static interface

ModuleElement.Directive

Represents a directive within the declaration of this
module. The directives of a module declaration configure the
module in the Java Platform Module System.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

<R,​P>

R

accept

​(

ModuleElement.DirectiveVisitor

<R,​P> v,
P p)

Applies a visitor to this directive.

ModuleElement.DirectiveKind

getKind

()

Returns the

kind

of this directive.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

<R,​P>

R

accept

​(

ModuleElement.DirectiveVisitor

<R,​P> v,
P p)

Applies a visitor to this directive.

ModuleElement.DirectiveKind

getKind

()

Returns the

kind

of this directive.

---

#### Method Summary

Applies a visitor to this directive.

Returns the

kind

of this directive.

============ METHOD DETAIL ==========

- Method Detail

- getKind

```java
ModuleElement.DirectiveKind
getKind()
```

Returns the

kind

of this directive.

**Returns:** the kind of this directive

- accept

```java
<R,​P> R accept​(
ModuleElement.DirectiveVisitor
<R,​P> v,
P p)
```

Applies a visitor to this directive.

**Type Parameters:** R

- the return type of the visitor's methods
**Type Parameters:** P

- the type of the additional parameter to the visitor's methods
**Parameters:** v

- the visitor operating on this directive
**Parameters:** p

- additional parameter to the visitor
**Returns:** a visitor-specified result

Method Detail

- getKind

```java
ModuleElement.DirectiveKind
getKind()
```

Returns the

kind

of this directive.

**Returns:** the kind of this directive

- accept

```java
<R,​P> R accept​(
ModuleElement.DirectiveVisitor
<R,​P> v,
P p)
```

Applies a visitor to this directive.

**Type Parameters:** R

- the return type of the visitor's methods
**Type Parameters:** P

- the type of the additional parameter to the visitor's methods
**Parameters:** v

- the visitor operating on this directive
**Parameters:** p

- additional parameter to the visitor
**Returns:** a visitor-specified result

---

#### Method Detail

getKind

```java
ModuleElement.DirectiveKind
getKind()
```

Returns the

kind

of this directive.

**Returns:** the kind of this directive

---

#### getKind

ModuleElement.DirectiveKind

getKind()

Returns the

kind

of this directive.

accept

```java
<R,​P> R accept​(
ModuleElement.DirectiveVisitor
<R,​P> v,
P p)
```

Applies a visitor to this directive.

**Type Parameters:** R

- the return type of the visitor's methods
**Type Parameters:** P

- the type of the additional parameter to the visitor's methods
**Parameters:** v

- the visitor operating on this directive
**Parameters:** p

- additional parameter to the visitor
**Returns:** a visitor-specified result

---

#### accept

<R,​P> R accept​(

ModuleElement.DirectiveVisitor

<R,​P> v,
P p)

Applies a visitor to this directive.

---

