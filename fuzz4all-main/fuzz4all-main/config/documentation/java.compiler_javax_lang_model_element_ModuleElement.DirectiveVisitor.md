# Interface ModuleElement.DirectiveVisitor<R,​P>

**Source:** `java.compiler\javax\lang\model\element\ModuleElement.DirectiveVisitor.html`

### Class Description

```java
public static interface
ModuleElement.DirectiveVisitor<R,​P>
```

A visitor of module directives, in the style of the visitor design
pattern. Classes implementing this interface are used to operate
on a directive when the kind of directive is unknown at compile time.
When a visitor is passed to a directive's

accept

method, the

visit

Xyz

method applicable
to that directive is invoked.

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
this interface to accommodate new, currently unknown, language
structures added to future versions of the Java™ programming
language. Methods to accommodate new language constructs will
be added in a source

compatible

way using

default methods

.

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

#### default
R
visit​(
ModuleElement.Directive
d)

Visits any directive as if by passing itself to that
directive's

accept

method and passing

null

for the additional parameter.

**Parameters:**
- d

- the directive to visit

**Returns:**
- a visitor-specified result

**Implementation Requirements:**
- The default implementation is

d.accept(v, null)

.

---

#### default
R
visit​(
ModuleElement.Directive
d,

P
p)

Visits any directive as if by passing itself to that
directive's

accept

method.

**Parameters:**
- d

- the directive to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

**Implementation Requirements:**
- The default implementation is

d.accept(v, p)

.

---

#### R
visitRequires​(
ModuleElement.RequiresDirective
d,

P
p)

Visits a

requires

directive.

**Parameters:**
- d

- the directive to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

---

#### R
visitExports​(
ModuleElement.ExportsDirective
d,

P
p)

Visits an

exports

directive.

**Parameters:**
- d

- the directive to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

---

#### R
visitOpens​(
ModuleElement.OpensDirective
d,

P
p)

Visits an

opens

directive.

**Parameters:**
- d

- the directive to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

---

#### R
visitUses​(
ModuleElement.UsesDirective
d,

P
p)

Visits a

uses

directive.

**Parameters:**
- d

- the directive to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

---

#### R
visitProvides​(
ModuleElement.ProvidesDirective
d,

P
p)

Visits a

provides

directive.

**Parameters:**
- d

- the directive to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

---

#### default
R
visitUnknown​(
ModuleElement.Directive
d,

P
p)

Visits an unknown directive.
This can occur if the language evolves and new kinds of directive are added.

**Parameters:**
- d

- the directive to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

**Throws:**
- UnknownDirectiveException

- a visitor implementation may optionally throw this exception

**Implementation Requirements:**
- The default implementation throws

new UnknownDirectiveException(d, p)

.

---

### Additional Sections

#### Interface ModuleElement.DirectiveVisitor<R,​P>

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

**Enclosing interface:** ModuleElement

```java
public static interface
ModuleElement.DirectiveVisitor<R,​P>
```

A visitor of module directives, in the style of the visitor design
pattern. Classes implementing this interface are used to operate
on a directive when the kind of directive is unknown at compile time.
When a visitor is passed to a directive's

accept

method, the

visit

Xyz

method applicable
to that directive is invoked.

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
this interface to accommodate new, currently unknown, language
structures added to future versions of the Java™ programming
language. Methods to accommodate new language constructs will
be added in a source

compatible

way using

default methods

.

**Since:** 9

public static interface

ModuleElement.DirectiveVisitor<R,​P>

A visitor of module directives, in the style of the visitor design
pattern. Classes implementing this interface are used to operate
on a directive when the kind of directive is unknown at compile time.
When a visitor is passed to a directive's

accept

method, the

visit

Xyz

method applicable
to that directive is invoked.

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
this interface to accommodate new, currently unknown, language
structures added to future versions of the Java™ programming
language. Methods to accommodate new language constructs will
be added in a source

compatible

way using

default methods

.

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
this interface to accommodate new, currently unknown, language
structures added to future versions of the Java™ programming
language. Methods to accommodate new language constructs will
be added in a source

compatible

way using

default methods

.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the Java™ programming
language. Methods to accommodate new language constructs will
be added in a source

compatible

way using

default methods

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

R

visit

​(

ModuleElement.Directive

d)

Visits any directive as if by passing itself to that
directive's

accept

method and passing

null

for the additional parameter.

default

R

visit

​(

ModuleElement.Directive

d,

P

p)

Visits any directive as if by passing itself to that
directive's

accept

method.

R

visitExports

​(

ModuleElement.ExportsDirective

d,

P

p)

Visits an

exports

directive.

R

visitOpens

​(

ModuleElement.OpensDirective

d,

P

p)

Visits an

opens

directive.

R

visitProvides

​(

ModuleElement.ProvidesDirective

d,

P

p)

Visits a

provides

directive.

R

visitRequires

​(

ModuleElement.RequiresDirective

d,

P

p)

Visits a

requires

directive.

default

R

visitUnknown

​(

ModuleElement.Directive

d,

P

p)

Visits an unknown directive.

R

visitUses

​(

ModuleElement.UsesDirective

d,

P

p)

Visits a

uses

directive.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

R

visit

​(

ModuleElement.Directive

d)

Visits any directive as if by passing itself to that
directive's

accept

method and passing

null

for the additional parameter.

default

R

visit

​(

ModuleElement.Directive

d,

P

p)

Visits any directive as if by passing itself to that
directive's

accept

method.

R

visitExports

​(

ModuleElement.ExportsDirective

d,

P

p)

Visits an

exports

directive.

R

visitOpens

​(

ModuleElement.OpensDirective

d,

P

p)

Visits an

opens

directive.

R

visitProvides

​(

ModuleElement.ProvidesDirective

d,

P

p)

Visits a

provides

directive.

R

visitRequires

​(

ModuleElement.RequiresDirective

d,

P

p)

Visits a

requires

directive.

default

R

visitUnknown

​(

ModuleElement.Directive

d,

P

p)

Visits an unknown directive.

R

visitUses

​(

ModuleElement.UsesDirective

d,

P

p)

Visits a

uses

directive.

---

#### Method Summary

Visits any directive as if by passing itself to that
directive's

accept

method and passing

null

for the additional parameter.

Visits any directive as if by passing itself to that
directive's

accept

method.

Visits an

exports

directive.

Visits an

opens

directive.

Visits a

provides

directive.

Visits a

requires

directive.

Visits an unknown directive.

Visits a

uses

directive.

============ METHOD DETAIL ==========

- Method Detail

- visit

```java
default
R
visit​(
ModuleElement.Directive
d)
```

Visits any directive as if by passing itself to that
directive's

accept

method and passing

null

for the additional parameter.

**Implementation Requirements:** The default implementation is

d.accept(v, null)

.
**Parameters:** d

- the directive to visit
**Returns:** a visitor-specified result

- visit

```java
default
R
visit​(
ModuleElement.Directive
d,

P
p)
```

Visits any directive as if by passing itself to that
directive's

accept

method.

**Implementation Requirements:** The default implementation is

d.accept(v, p)

.
**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitRequires

```java
R
visitRequires​(
ModuleElement.RequiresDirective
d,

P
p)
```

Visits a

requires

directive.

**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitExports

```java
R
visitExports​(
ModuleElement.ExportsDirective
d,

P
p)
```

Visits an

exports

directive.

**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitOpens

```java
R
visitOpens​(
ModuleElement.OpensDirective
d,

P
p)
```

Visits an

opens

directive.

**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitUses

```java
R
visitUses​(
ModuleElement.UsesDirective
d,

P
p)
```

Visits a

uses

directive.

**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitProvides

```java
R
visitProvides​(
ModuleElement.ProvidesDirective
d,

P
p)
```

Visits a

provides

directive.

**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitUnknown

```java
default
R
visitUnknown​(
ModuleElement.Directive
d,

P
p)
```

Visits an unknown directive.
This can occur if the language evolves and new kinds of directive are added.

**Implementation Requirements:** The default implementation throws

new UnknownDirectiveException(d, p)

.
**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Throws:** UnknownDirectiveException

- a visitor implementation may optionally throw this exception

Method Detail

- visit

```java
default
R
visit​(
ModuleElement.Directive
d)
```

Visits any directive as if by passing itself to that
directive's

accept

method and passing

null

for the additional parameter.

**Implementation Requirements:** The default implementation is

d.accept(v, null)

.
**Parameters:** d

- the directive to visit
**Returns:** a visitor-specified result

- visit

```java
default
R
visit​(
ModuleElement.Directive
d,

P
p)
```

Visits any directive as if by passing itself to that
directive's

accept

method.

**Implementation Requirements:** The default implementation is

d.accept(v, p)

.
**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitRequires

```java
R
visitRequires​(
ModuleElement.RequiresDirective
d,

P
p)
```

Visits a

requires

directive.

**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitExports

```java
R
visitExports​(
ModuleElement.ExportsDirective
d,

P
p)
```

Visits an

exports

directive.

**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitOpens

```java
R
visitOpens​(
ModuleElement.OpensDirective
d,

P
p)
```

Visits an

opens

directive.

**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitUses

```java
R
visitUses​(
ModuleElement.UsesDirective
d,

P
p)
```

Visits a

uses

directive.

**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitProvides

```java
R
visitProvides​(
ModuleElement.ProvidesDirective
d,

P
p)
```

Visits a

provides

directive.

**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitUnknown

```java
default
R
visitUnknown​(
ModuleElement.Directive
d,

P
p)
```

Visits an unknown directive.
This can occur if the language evolves and new kinds of directive are added.

**Implementation Requirements:** The default implementation throws

new UnknownDirectiveException(d, p)

.
**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Throws:** UnknownDirectiveException

- a visitor implementation may optionally throw this exception

---

#### Method Detail

visit

```java
default
R
visit​(
ModuleElement.Directive
d)
```

Visits any directive as if by passing itself to that
directive's

accept

method and passing

null

for the additional parameter.

**Implementation Requirements:** The default implementation is

d.accept(v, null)

.
**Parameters:** d

- the directive to visit
**Returns:** a visitor-specified result

---

#### visit

default

R

visit​(

ModuleElement.Directive

d)

Visits any directive as if by passing itself to that
directive's

accept

method and passing

null

for the additional parameter.

visit

```java
default
R
visit​(
ModuleElement.Directive
d,

P
p)
```

Visits any directive as if by passing itself to that
directive's

accept

method.

**Implementation Requirements:** The default implementation is

d.accept(v, p)

.
**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visit

default

R

visit​(

ModuleElement.Directive

d,

P

p)

Visits any directive as if by passing itself to that
directive's

accept

method.

visitRequires

```java
R
visitRequires​(
ModuleElement.RequiresDirective
d,

P
p)
```

Visits a

requires

directive.

**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitRequires

R

visitRequires​(

ModuleElement.RequiresDirective

d,

P

p)

Visits a

requires

directive.

visitExports

```java
R
visitExports​(
ModuleElement.ExportsDirective
d,

P
p)
```

Visits an

exports

directive.

**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitExports

R

visitExports​(

ModuleElement.ExportsDirective

d,

P

p)

Visits an

exports

directive.

visitOpens

```java
R
visitOpens​(
ModuleElement.OpensDirective
d,

P
p)
```

Visits an

opens

directive.

**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitOpens

R

visitOpens​(

ModuleElement.OpensDirective

d,

P

p)

Visits an

opens

directive.

visitUses

```java
R
visitUses​(
ModuleElement.UsesDirective
d,

P
p)
```

Visits a

uses

directive.

**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitUses

R

visitUses​(

ModuleElement.UsesDirective

d,

P

p)

Visits a

uses

directive.

visitProvides

```java
R
visitProvides​(
ModuleElement.ProvidesDirective
d,

P
p)
```

Visits a

provides

directive.

**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitProvides

R

visitProvides​(

ModuleElement.ProvidesDirective

d,

P

p)

Visits a

provides

directive.

visitUnknown

```java
default
R
visitUnknown​(
ModuleElement.Directive
d,

P
p)
```

Visits an unknown directive.
This can occur if the language evolves and new kinds of directive are added.

**Implementation Requirements:** The default implementation throws

new UnknownDirectiveException(d, p)

.
**Parameters:** d

- the directive to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Throws:** UnknownDirectiveException

- a visitor implementation may optionally throw this exception

---

#### visitUnknown

default

R

visitUnknown​(

ModuleElement.Directive

d,

P

p)

Visits an unknown directive.
This can occur if the language evolves and new kinds of directive are added.

---

