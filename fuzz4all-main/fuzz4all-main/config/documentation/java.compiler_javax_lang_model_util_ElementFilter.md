# Class ElementFilter

**Source:** `java.compiler\javax\lang\model\util\ElementFilter.html`

### Class Description

```java
public class
ElementFilter

extends
Object
```

Filters for selecting just the elements of interest from a
collection of elements. The returned sets and lists are new
collections and do use the argument as a backing store. The
methods in this class do not make any attempts to guard against
concurrent modifications of the arguments. The returned sets and
lists are mutable but unsafe for concurrent access. A returned set
has the same iteration order as the argument set to a method.

If iterables and sets containing

null

are passed as
arguments to methods in this class, a

NullPointerException

will be thrown.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
List
<
VariableElement
> fieldsIn​(
Iterable
<? extends
Element
> elements)

Returns a list of fields in

elements

.

**Parameters:**
- elements

- the elements to filter

**Returns:**
- a list of fields in

elements

---

#### public static
Set
<
VariableElement
> fieldsIn​(
Set
<? extends
Element
> elements)

Returns a set of fields in

elements

.

**Parameters:**
- elements

- the elements to filter

**Returns:**
- a set of fields in

elements

---

#### public static
List
<
ExecutableElement
> constructorsIn​(
Iterable
<? extends
Element
> elements)

Returns a list of constructors in

elements

.

**Parameters:**
- elements

- the elements to filter

**Returns:**
- a list of constructors in

elements

---

#### public static
Set
<
ExecutableElement
> constructorsIn​(
Set
<? extends
Element
> elements)

Returns a set of constructors in

elements

.

**Parameters:**
- elements

- the elements to filter

**Returns:**
- a set of constructors in

elements

---

#### public static
List
<
ExecutableElement
> methodsIn​(
Iterable
<? extends
Element
> elements)

Returns a list of methods in

elements

.

**Parameters:**
- elements

- the elements to filter

**Returns:**
- a list of methods in

elements

---

#### public static
Set
<
ExecutableElement
> methodsIn​(
Set
<? extends
Element
> elements)

Returns a set of methods in

elements

.

**Parameters:**
- elements

- the elements to filter

**Returns:**
- a set of methods in

elements

---

#### public static
List
<
TypeElement
> typesIn​(
Iterable
<? extends
Element
> elements)

Returns a list of types in

elements

.

**Parameters:**
- elements

- the elements to filter

**Returns:**
- a list of types in

elements

---

#### public static
Set
<
TypeElement
> typesIn​(
Set
<? extends
Element
> elements)

Returns a set of types in

elements

.

**Parameters:**
- elements

- the elements to filter

**Returns:**
- a set of types in

elements

---

#### public static
List
<
PackageElement
> packagesIn​(
Iterable
<? extends
Element
> elements)

Returns a list of packages in

elements

.

**Parameters:**
- elements

- the elements to filter

**Returns:**
- a list of packages in

elements

---

#### public static
Set
<
PackageElement
> packagesIn​(
Set
<? extends
Element
> elements)

Returns a set of packages in

elements

.

**Parameters:**
- elements

- the elements to filter

**Returns:**
- a set of packages in

elements

---

#### public static
List
<
ModuleElement
> modulesIn​(
Iterable
<? extends
Element
> elements)

Returns a list of modules in

elements

.

**Parameters:**
- elements

- the elements to filter

**Returns:**
- a list of modules in

elements

**Since:**
- 9

---

#### public static
Set
<
ModuleElement
> modulesIn​(
Set
<? extends
Element
> elements)

Returns a set of modules in

elements

.

**Parameters:**
- elements

- the elements to filter

**Returns:**
- a set of modules in

elements

**Since:**
- 9

---

#### public static
List
<
ModuleElement.ExportsDirective
> exportsIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)

Returns a list of

exports

directives in

directives

.

**Parameters:**
- directives

- the directives to filter

**Returns:**
- a list of

exports

directives in

directives

**Since:**
- 9

---

#### public static
List
<
ModuleElement.OpensDirective
> opensIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)

Returns a list of

opens

directives in

directives

.

**Parameters:**
- directives

- the directives to filter

**Returns:**
- a list of

opens

directives in

directives

**Since:**
- 9

---

#### public static
List
<
ModuleElement.ProvidesDirective
> providesIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)

Returns a list of

provides

directives in

directives

.

**Parameters:**
- directives

- the directives to filter

**Returns:**
- a list of

provides

directives in

directives

**Since:**
- 9

---

#### public static
List
<
ModuleElement.RequiresDirective
> requiresIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)

Returns a list of

requires

directives in

directives

.

**Parameters:**
- directives

- the directives to filter

**Returns:**
- a list of

requires

directives in

directives

**Since:**
- 9

---

#### public static
List
<
ModuleElement.UsesDirective
> usesIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)

Returns a list of

uses

directives in

directives

.

**Parameters:**
- directives

- the directives to filter

**Returns:**
- a list of

uses

directives in

directives

**Since:**
- 9

---

### Additional Sections

#### Class ElementFilter

java.lang.Object

- javax.lang.model.util.ElementFilter

javax.lang.model.util.ElementFilter

```java
public class
ElementFilter

extends
Object
```

Filters for selecting just the elements of interest from a
collection of elements. The returned sets and lists are new
collections and do use the argument as a backing store. The
methods in this class do not make any attempts to guard against
concurrent modifications of the arguments. The returned sets and
lists are mutable but unsafe for concurrent access. A returned set
has the same iteration order as the argument set to a method.

If iterables and sets containing

null

are passed as
arguments to methods in this class, a

NullPointerException

will be thrown.

**Since:** 1.6

public class

ElementFilter

extends

Object

Filters for selecting just the elements of interest from a
collection of elements. The returned sets and lists are new
collections and do use the argument as a backing store. The
methods in this class do not make any attempts to guard against
concurrent modifications of the arguments. The returned sets and
lists are mutable but unsafe for concurrent access. A returned set
has the same iteration order as the argument set to a method.

If iterables and sets containing

null

are passed as
arguments to methods in this class, a

NullPointerException

will be thrown.

If iterables and sets containing

null

are passed as
arguments to methods in this class, a

NullPointerException

will be thrown.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

List

<

ExecutableElement

>

constructorsIn

​(

Iterable

<? extends

Element

> elements)

Returns a list of constructors in

elements

.

static

Set

<

ExecutableElement

>

constructorsIn

​(

Set

<? extends

Element

> elements)

Returns a set of constructors in

elements

.

static

List

<

ModuleElement.ExportsDirective

>

exportsIn

​(

Iterable

<? extends

ModuleElement.Directive

> directives)

Returns a list of

exports

directives in

directives

.

static

List

<

VariableElement

>

fieldsIn

​(

Iterable

<? extends

Element

> elements)

Returns a list of fields in

elements

.

static

Set

<

VariableElement

>

fieldsIn

​(

Set

<? extends

Element

> elements)

Returns a set of fields in

elements

.

static

List

<

ExecutableElement

>

methodsIn

​(

Iterable

<? extends

Element

> elements)

Returns a list of methods in

elements

.

static

Set

<

ExecutableElement

>

methodsIn

​(

Set

<? extends

Element

> elements)

Returns a set of methods in

elements

.

static

List

<

ModuleElement

>

modulesIn

​(

Iterable

<? extends

Element

> elements)

Returns a list of modules in

elements

.

static

Set

<

ModuleElement

>

modulesIn

​(

Set

<? extends

Element

> elements)

Returns a set of modules in

elements

.

static

List

<

ModuleElement.OpensDirective

>

opensIn

​(

Iterable

<? extends

ModuleElement.Directive

> directives)

Returns a list of

opens

directives in

directives

.

static

List

<

PackageElement

>

packagesIn

​(

Iterable

<? extends

Element

> elements)

Returns a list of packages in

elements

.

static

Set

<

PackageElement

>

packagesIn

​(

Set

<? extends

Element

> elements)

Returns a set of packages in

elements

.

static

List

<

ModuleElement.ProvidesDirective

>

providesIn

​(

Iterable

<? extends

ModuleElement.Directive

> directives)

Returns a list of

provides

directives in

directives

.

static

List

<

ModuleElement.RequiresDirective

>

requiresIn

​(

Iterable

<? extends

ModuleElement.Directive

> directives)

Returns a list of

requires

directives in

directives

.

static

List

<

TypeElement

>

typesIn

​(

Iterable

<? extends

Element

> elements)

Returns a list of types in

elements

.

static

Set

<

TypeElement

>

typesIn

​(

Set

<? extends

Element

> elements)

Returns a set of types in

elements

.

static

List

<

ModuleElement.UsesDirective

>

usesIn

​(

Iterable

<? extends

ModuleElement.Directive

> directives)

Returns a list of

uses

directives in

directives

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

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

List

<

ExecutableElement

>

constructorsIn

​(

Iterable

<? extends

Element

> elements)

Returns a list of constructors in

elements

.

static

Set

<

ExecutableElement

>

constructorsIn

​(

Set

<? extends

Element

> elements)

Returns a set of constructors in

elements

.

static

List

<

ModuleElement.ExportsDirective

>

exportsIn

​(

Iterable

<? extends

ModuleElement.Directive

> directives)

Returns a list of

exports

directives in

directives

.

static

List

<

VariableElement

>

fieldsIn

​(

Iterable

<? extends

Element

> elements)

Returns a list of fields in

elements

.

static

Set

<

VariableElement

>

fieldsIn

​(

Set

<? extends

Element

> elements)

Returns a set of fields in

elements

.

static

List

<

ExecutableElement

>

methodsIn

​(

Iterable

<? extends

Element

> elements)

Returns a list of methods in

elements

.

static

Set

<

ExecutableElement

>

methodsIn

​(

Set

<? extends

Element

> elements)

Returns a set of methods in

elements

.

static

List

<

ModuleElement

>

modulesIn

​(

Iterable

<? extends

Element

> elements)

Returns a list of modules in

elements

.

static

Set

<

ModuleElement

>

modulesIn

​(

Set

<? extends

Element

> elements)

Returns a set of modules in

elements

.

static

List

<

ModuleElement.OpensDirective

>

opensIn

​(

Iterable

<? extends

ModuleElement.Directive

> directives)

Returns a list of

opens

directives in

directives

.

static

List

<

PackageElement

>

packagesIn

​(

Iterable

<? extends

Element

> elements)

Returns a list of packages in

elements

.

static

Set

<

PackageElement

>

packagesIn

​(

Set

<? extends

Element

> elements)

Returns a set of packages in

elements

.

static

List

<

ModuleElement.ProvidesDirective

>

providesIn

​(

Iterable

<? extends

ModuleElement.Directive

> directives)

Returns a list of

provides

directives in

directives

.

static

List

<

ModuleElement.RequiresDirective

>

requiresIn

​(

Iterable

<? extends

ModuleElement.Directive

> directives)

Returns a list of

requires

directives in

directives

.

static

List

<

TypeElement

>

typesIn

​(

Iterable

<? extends

Element

> elements)

Returns a list of types in

elements

.

static

Set

<

TypeElement

>

typesIn

​(

Set

<? extends

Element

> elements)

Returns a set of types in

elements

.

static

List

<

ModuleElement.UsesDirective

>

usesIn

​(

Iterable

<? extends

ModuleElement.Directive

> directives)

Returns a list of

uses

directives in

directives

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

---

#### Method Summary

Returns a list of constructors in

elements

.

Returns a set of constructors in

elements

.

Returns a list of

exports

directives in

directives

.

Returns a list of fields in

elements

.

Returns a set of fields in

elements

.

Returns a list of methods in

elements

.

Returns a set of methods in

elements

.

Returns a list of modules in

elements

.

Returns a set of modules in

elements

.

Returns a list of

opens

directives in

directives

.

Returns a list of packages in

elements

.

Returns a set of packages in

elements

.

Returns a list of

provides

directives in

directives

.

Returns a list of

requires

directives in

directives

.

Returns a list of types in

elements

.

Returns a set of types in

elements

.

Returns a list of

uses

directives in

directives

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

============ METHOD DETAIL ==========

- Method Detail

- fieldsIn

```java
public static
List
<
VariableElement
> fieldsIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of fields in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of fields in

elements

- fieldsIn

```java
public static
Set
<
VariableElement
> fieldsIn​(
Set
<? extends
Element
> elements)
```

Returns a set of fields in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of fields in

elements

- constructorsIn

```java
public static
List
<
ExecutableElement
> constructorsIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of constructors in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of constructors in

elements

- constructorsIn

```java
public static
Set
<
ExecutableElement
> constructorsIn​(
Set
<? extends
Element
> elements)
```

Returns a set of constructors in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of constructors in

elements

- methodsIn

```java
public static
List
<
ExecutableElement
> methodsIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of methods in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of methods in

elements

- methodsIn

```java
public static
Set
<
ExecutableElement
> methodsIn​(
Set
<? extends
Element
> elements)
```

Returns a set of methods in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of methods in

elements

- typesIn

```java
public static
List
<
TypeElement
> typesIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of types in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of types in

elements

- typesIn

```java
public static
Set
<
TypeElement
> typesIn​(
Set
<? extends
Element
> elements)
```

Returns a set of types in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of types in

elements

- packagesIn

```java
public static
List
<
PackageElement
> packagesIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of packages in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of packages in

elements

- packagesIn

```java
public static
Set
<
PackageElement
> packagesIn​(
Set
<? extends
Element
> elements)
```

Returns a set of packages in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of packages in

elements

- modulesIn

```java
public static
List
<
ModuleElement
> modulesIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of modules in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of modules in

elements
**Since:** 9

- modulesIn

```java
public static
Set
<
ModuleElement
> modulesIn​(
Set
<? extends
Element
> elements)
```

Returns a set of modules in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of modules in

elements
**Since:** 9

- exportsIn

```java
public static
List
<
ModuleElement.ExportsDirective
> exportsIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)
```

Returns a list of

exports

directives in

directives

.

**Parameters:** directives

- the directives to filter
**Returns:** a list of

exports

directives in

directives
**Since:** 9

- opensIn

```java
public static
List
<
ModuleElement.OpensDirective
> opensIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)
```

Returns a list of

opens

directives in

directives

.

**Parameters:** directives

- the directives to filter
**Returns:** a list of

opens

directives in

directives
**Since:** 9

- providesIn

```java
public static
List
<
ModuleElement.ProvidesDirective
> providesIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)
```

Returns a list of

provides

directives in

directives

.

**Parameters:** directives

- the directives to filter
**Returns:** a list of

provides

directives in

directives
**Since:** 9

- requiresIn

```java
public static
List
<
ModuleElement.RequiresDirective
> requiresIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)
```

Returns a list of

requires

directives in

directives

.

**Parameters:** directives

- the directives to filter
**Returns:** a list of

requires

directives in

directives
**Since:** 9

- usesIn

```java
public static
List
<
ModuleElement.UsesDirective
> usesIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)
```

Returns a list of

uses

directives in

directives

.

**Parameters:** directives

- the directives to filter
**Returns:** a list of

uses

directives in

directives
**Since:** 9

Method Detail

- fieldsIn

```java
public static
List
<
VariableElement
> fieldsIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of fields in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of fields in

elements

- fieldsIn

```java
public static
Set
<
VariableElement
> fieldsIn​(
Set
<? extends
Element
> elements)
```

Returns a set of fields in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of fields in

elements

- constructorsIn

```java
public static
List
<
ExecutableElement
> constructorsIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of constructors in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of constructors in

elements

- constructorsIn

```java
public static
Set
<
ExecutableElement
> constructorsIn​(
Set
<? extends
Element
> elements)
```

Returns a set of constructors in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of constructors in

elements

- methodsIn

```java
public static
List
<
ExecutableElement
> methodsIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of methods in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of methods in

elements

- methodsIn

```java
public static
Set
<
ExecutableElement
> methodsIn​(
Set
<? extends
Element
> elements)
```

Returns a set of methods in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of methods in

elements

- typesIn

```java
public static
List
<
TypeElement
> typesIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of types in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of types in

elements

- typesIn

```java
public static
Set
<
TypeElement
> typesIn​(
Set
<? extends
Element
> elements)
```

Returns a set of types in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of types in

elements

- packagesIn

```java
public static
List
<
PackageElement
> packagesIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of packages in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of packages in

elements

- packagesIn

```java
public static
Set
<
PackageElement
> packagesIn​(
Set
<? extends
Element
> elements)
```

Returns a set of packages in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of packages in

elements

- modulesIn

```java
public static
List
<
ModuleElement
> modulesIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of modules in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of modules in

elements
**Since:** 9

- modulesIn

```java
public static
Set
<
ModuleElement
> modulesIn​(
Set
<? extends
Element
> elements)
```

Returns a set of modules in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of modules in

elements
**Since:** 9

- exportsIn

```java
public static
List
<
ModuleElement.ExportsDirective
> exportsIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)
```

Returns a list of

exports

directives in

directives

.

**Parameters:** directives

- the directives to filter
**Returns:** a list of

exports

directives in

directives
**Since:** 9

- opensIn

```java
public static
List
<
ModuleElement.OpensDirective
> opensIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)
```

Returns a list of

opens

directives in

directives

.

**Parameters:** directives

- the directives to filter
**Returns:** a list of

opens

directives in

directives
**Since:** 9

- providesIn

```java
public static
List
<
ModuleElement.ProvidesDirective
> providesIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)
```

Returns a list of

provides

directives in

directives

.

**Parameters:** directives

- the directives to filter
**Returns:** a list of

provides

directives in

directives
**Since:** 9

- requiresIn

```java
public static
List
<
ModuleElement.RequiresDirective
> requiresIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)
```

Returns a list of

requires

directives in

directives

.

**Parameters:** directives

- the directives to filter
**Returns:** a list of

requires

directives in

directives
**Since:** 9

- usesIn

```java
public static
List
<
ModuleElement.UsesDirective
> usesIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)
```

Returns a list of

uses

directives in

directives

.

**Parameters:** directives

- the directives to filter
**Returns:** a list of

uses

directives in

directives
**Since:** 9

---

#### Method Detail

fieldsIn

```java
public static
List
<
VariableElement
> fieldsIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of fields in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of fields in

elements

---

#### fieldsIn

public static

List

<

VariableElement

> fieldsIn​(

Iterable

<? extends

Element

> elements)

Returns a list of fields in

elements

.

fieldsIn

```java
public static
Set
<
VariableElement
> fieldsIn​(
Set
<? extends
Element
> elements)
```

Returns a set of fields in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of fields in

elements

---

#### fieldsIn

public static

Set

<

VariableElement

> fieldsIn​(

Set

<? extends

Element

> elements)

Returns a set of fields in

elements

.

constructorsIn

```java
public static
List
<
ExecutableElement
> constructorsIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of constructors in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of constructors in

elements

---

#### constructorsIn

public static

List

<

ExecutableElement

> constructorsIn​(

Iterable

<? extends

Element

> elements)

Returns a list of constructors in

elements

.

constructorsIn

```java
public static
Set
<
ExecutableElement
> constructorsIn​(
Set
<? extends
Element
> elements)
```

Returns a set of constructors in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of constructors in

elements

---

#### constructorsIn

public static

Set

<

ExecutableElement

> constructorsIn​(

Set

<? extends

Element

> elements)

Returns a set of constructors in

elements

.

methodsIn

```java
public static
List
<
ExecutableElement
> methodsIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of methods in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of methods in

elements

---

#### methodsIn

public static

List

<

ExecutableElement

> methodsIn​(

Iterable

<? extends

Element

> elements)

Returns a list of methods in

elements

.

methodsIn

```java
public static
Set
<
ExecutableElement
> methodsIn​(
Set
<? extends
Element
> elements)
```

Returns a set of methods in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of methods in

elements

---

#### methodsIn

public static

Set

<

ExecutableElement

> methodsIn​(

Set

<? extends

Element

> elements)

Returns a set of methods in

elements

.

typesIn

```java
public static
List
<
TypeElement
> typesIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of types in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of types in

elements

---

#### typesIn

public static

List

<

TypeElement

> typesIn​(

Iterable

<? extends

Element

> elements)

Returns a list of types in

elements

.

typesIn

```java
public static
Set
<
TypeElement
> typesIn​(
Set
<? extends
Element
> elements)
```

Returns a set of types in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of types in

elements

---

#### typesIn

public static

Set

<

TypeElement

> typesIn​(

Set

<? extends

Element

> elements)

Returns a set of types in

elements

.

packagesIn

```java
public static
List
<
PackageElement
> packagesIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of packages in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of packages in

elements

---

#### packagesIn

public static

List

<

PackageElement

> packagesIn​(

Iterable

<? extends

Element

> elements)

Returns a list of packages in

elements

.

packagesIn

```java
public static
Set
<
PackageElement
> packagesIn​(
Set
<? extends
Element
> elements)
```

Returns a set of packages in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of packages in

elements

---

#### packagesIn

public static

Set

<

PackageElement

> packagesIn​(

Set

<? extends

Element

> elements)

Returns a set of packages in

elements

.

modulesIn

```java
public static
List
<
ModuleElement
> modulesIn​(
Iterable
<? extends
Element
> elements)
```

Returns a list of modules in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a list of modules in

elements
**Since:** 9

---

#### modulesIn

public static

List

<

ModuleElement

> modulesIn​(

Iterable

<? extends

Element

> elements)

Returns a list of modules in

elements

.

modulesIn

```java
public static
Set
<
ModuleElement
> modulesIn​(
Set
<? extends
Element
> elements)
```

Returns a set of modules in

elements

.

**Parameters:** elements

- the elements to filter
**Returns:** a set of modules in

elements
**Since:** 9

---

#### modulesIn

public static

Set

<

ModuleElement

> modulesIn​(

Set

<? extends

Element

> elements)

Returns a set of modules in

elements

.

exportsIn

```java
public static
List
<
ModuleElement.ExportsDirective
> exportsIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)
```

Returns a list of

exports

directives in

directives

.

**Parameters:** directives

- the directives to filter
**Returns:** a list of

exports

directives in

directives
**Since:** 9

---

#### exportsIn

public static

List

<

ModuleElement.ExportsDirective

> exportsIn​(

Iterable

<? extends

ModuleElement.Directive

> directives)

Returns a list of

exports

directives in

directives

.

opensIn

```java
public static
List
<
ModuleElement.OpensDirective
> opensIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)
```

Returns a list of

opens

directives in

directives

.

**Parameters:** directives

- the directives to filter
**Returns:** a list of

opens

directives in

directives
**Since:** 9

---

#### opensIn

public static

List

<

ModuleElement.OpensDirective

> opensIn​(

Iterable

<? extends

ModuleElement.Directive

> directives)

Returns a list of

opens

directives in

directives

.

providesIn

```java
public static
List
<
ModuleElement.ProvidesDirective
> providesIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)
```

Returns a list of

provides

directives in

directives

.

**Parameters:** directives

- the directives to filter
**Returns:** a list of

provides

directives in

directives
**Since:** 9

---

#### providesIn

public static

List

<

ModuleElement.ProvidesDirective

> providesIn​(

Iterable

<? extends

ModuleElement.Directive

> directives)

Returns a list of

provides

directives in

directives

.

requiresIn

```java
public static
List
<
ModuleElement.RequiresDirective
> requiresIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)
```

Returns a list of

requires

directives in

directives

.

**Parameters:** directives

- the directives to filter
**Returns:** a list of

requires

directives in

directives
**Since:** 9

---

#### requiresIn

public static

List

<

ModuleElement.RequiresDirective

> requiresIn​(

Iterable

<? extends

ModuleElement.Directive

> directives)

Returns a list of

requires

directives in

directives

.

usesIn

```java
public static
List
<
ModuleElement.UsesDirective
> usesIn​(
Iterable
<? extends
ModuleElement.Directive
> directives)
```

Returns a list of

uses

directives in

directives

.

**Parameters:** directives

- the directives to filter
**Returns:** a list of

uses

directives in

directives
**Since:** 9

---

#### usesIn

public static

List

<

ModuleElement.UsesDirective

> usesIn​(

Iterable

<? extends

ModuleElement.Directive

> directives)

Returns a list of

uses

directives in

directives

.

---

