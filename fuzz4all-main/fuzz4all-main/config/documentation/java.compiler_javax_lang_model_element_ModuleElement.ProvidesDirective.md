# Interface ModuleElement.ProvidesDirective

**Source:** `java.compiler\javax\lang\model\element\ModuleElement.ProvidesDirective.html`

### Class Description

```java
public static interface
ModuleElement.ProvidesDirective

extends
ModuleElement.Directive
```

An implementation of a service provided by a module.

**All Superinterfaces:** ModuleElement.Directive

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### TypeElement
getService()

Returns the service being provided.

**Returns:**
- the service being provided

---

#### List
<? extends
TypeElement
> getImplementations()

Returns the implementations of the service being provided.

**Returns:**
- the implementations of the service being provided

---

### Additional Sections

#### Interface ModuleElement.ProvidesDirective

**All Superinterfaces:** ModuleElement.Directive

**Enclosing interface:** ModuleElement

```java
public static interface
ModuleElement.ProvidesDirective

extends
ModuleElement.Directive
```

An implementation of a service provided by a module.

**Since:** 9

public static interface

ModuleElement.ProvidesDirective

extends

ModuleElement.Directive

An implementation of a service provided by a module.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<? extends

TypeElement

>

getImplementations

()

Returns the implementations of the service being provided.

TypeElement

getService

()

Returns the service being provided.

- Methods declared in interface javax.lang.model.element.

ModuleElement.Directive

accept

,

getKind

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<? extends

TypeElement

>

getImplementations

()

Returns the implementations of the service being provided.

TypeElement

getService

()

Returns the service being provided.

- Methods declared in interface javax.lang.model.element.

ModuleElement.Directive

accept

,

getKind

---

#### Method Summary

Returns the implementations of the service being provided.

Returns the service being provided.

Methods declared in interface javax.lang.model.element.

ModuleElement.Directive

accept

,

getKind

---

#### Methods declared in interface javax.lang.model.element. ModuleElement.Directive

============ METHOD DETAIL ==========

- Method Detail

- getService

```java
TypeElement
getService()
```

Returns the service being provided.

**Returns:** the service being provided

- getImplementations

```java
List
<? extends
TypeElement
> getImplementations()
```

Returns the implementations of the service being provided.

**Returns:** the implementations of the service being provided

Method Detail

- getService

```java
TypeElement
getService()
```

Returns the service being provided.

**Returns:** the service being provided

- getImplementations

```java
List
<? extends
TypeElement
> getImplementations()
```

Returns the implementations of the service being provided.

**Returns:** the implementations of the service being provided

---

#### Method Detail

getService

```java
TypeElement
getService()
```

Returns the service being provided.

**Returns:** the service being provided

---

#### getService

TypeElement

getService()

Returns the service being provided.

getImplementations

```java
List
<? extends
TypeElement
> getImplementations()
```

Returns the implementations of the service being provided.

**Returns:** the implementations of the service being provided

---

#### getImplementations

List

<? extends

TypeElement

> getImplementations()

Returns the implementations of the service being provided.

---

