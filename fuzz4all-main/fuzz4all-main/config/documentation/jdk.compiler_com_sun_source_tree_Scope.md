# Interface Scope

**Source:** `jdk.compiler\com\sun\source\tree\Scope.html`

### Class Description

```java
public interface
Scope
```

Interface for determining locally available program elements, such as
local variables and imports.
Upon creation, a Scope is associated with a given program position;
for example, a

tree node

. This position may be used to
infer an enclosing method and/or class.

A Scope does not itself contain the details of the elements corresponding
to the parameters, methods and fields of the methods and classes containing
its position. However, these elements can be determined from the enclosing
elements.

Scopes may be contained in an enclosing scope. The outermost scope contains
those elements available via "star import" declarations; the scope within that
contains the top level elements of the compilation unit, including any named
imports.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Scope
getEnclosingScope()

Returns the enclosing scope.

**Returns:**
- the enclosing scope

---

#### TypeElement
getEnclosingClass()

Returns the innermost type element containing the position of this scope.

**Returns:**
- the innermost enclosing type element

---

#### ExecutableElement
getEnclosingMethod()

Returns the innermost executable element containing the position of this scope.

**Returns:**
- the innermost enclosing method declaration

---

#### Iterable
<? extends
Element
> getLocalElements()

Returns the elements directly contained in this scope.

**Returns:**
- the elements contained in this scope

---

### Additional Sections

#### Interface Scope

```java
public interface
Scope
```

Interface for determining locally available program elements, such as
local variables and imports.
Upon creation, a Scope is associated with a given program position;
for example, a

tree node

. This position may be used to
infer an enclosing method and/or class.

A Scope does not itself contain the details of the elements corresponding
to the parameters, methods and fields of the methods and classes containing
its position. However, these elements can be determined from the enclosing
elements.

Scopes may be contained in an enclosing scope. The outermost scope contains
those elements available via "star import" declarations; the scope within that
contains the top level elements of the compilation unit, including any named
imports.

**Since:** 1.6

public interface

Scope

Interface for determining locally available program elements, such as
local variables and imports.
Upon creation, a Scope is associated with a given program position;
for example, a

tree node

. This position may be used to
infer an enclosing method and/or class.

A Scope does not itself contain the details of the elements corresponding
to the parameters, methods and fields of the methods and classes containing
its position. However, these elements can be determined from the enclosing
elements.

Scopes may be contained in an enclosing scope. The outermost scope contains
those elements available via "star import" declarations; the scope within that
contains the top level elements of the compilation unit, including any named
imports.

A Scope does not itself contain the details of the elements corresponding
to the parameters, methods and fields of the methods and classes containing
its position. However, these elements can be determined from the enclosing
elements.

Scopes may be contained in an enclosing scope. The outermost scope contains
those elements available via "star import" declarations; the scope within that
contains the top level elements of the compilation unit, including any named
imports.

Scopes may be contained in an enclosing scope. The outermost scope contains
those elements available via "star import" declarations; the scope within that
contains the top level elements of the compilation unit, including any named
imports.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

TypeElement

getEnclosingClass

()

Returns the innermost type element containing the position of this scope.

ExecutableElement

getEnclosingMethod

()

Returns the innermost executable element containing the position of this scope.

Scope

getEnclosingScope

()

Returns the enclosing scope.

Iterable

<? extends

Element

>

getLocalElements

()

Returns the elements directly contained in this scope.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

TypeElement

getEnclosingClass

()

Returns the innermost type element containing the position of this scope.

ExecutableElement

getEnclosingMethod

()

Returns the innermost executable element containing the position of this scope.

Scope

getEnclosingScope

()

Returns the enclosing scope.

Iterable

<? extends

Element

>

getLocalElements

()

Returns the elements directly contained in this scope.

---

#### Method Summary

Returns the innermost type element containing the position of this scope.

Returns the innermost executable element containing the position of this scope.

Returns the enclosing scope.

Returns the elements directly contained in this scope.

============ METHOD DETAIL ==========

- Method Detail

- getEnclosingScope

```java
Scope
getEnclosingScope()
```

Returns the enclosing scope.

**Returns:** the enclosing scope

- getEnclosingClass

```java
TypeElement
getEnclosingClass()
```

Returns the innermost type element containing the position of this scope.

**Returns:** the innermost enclosing type element

- getEnclosingMethod

```java
ExecutableElement
getEnclosingMethod()
```

Returns the innermost executable element containing the position of this scope.

**Returns:** the innermost enclosing method declaration

- getLocalElements

```java
Iterable
<? extends
Element
> getLocalElements()
```

Returns the elements directly contained in this scope.

**Returns:** the elements contained in this scope

Method Detail

- getEnclosingScope

```java
Scope
getEnclosingScope()
```

Returns the enclosing scope.

**Returns:** the enclosing scope

- getEnclosingClass

```java
TypeElement
getEnclosingClass()
```

Returns the innermost type element containing the position of this scope.

**Returns:** the innermost enclosing type element

- getEnclosingMethod

```java
ExecutableElement
getEnclosingMethod()
```

Returns the innermost executable element containing the position of this scope.

**Returns:** the innermost enclosing method declaration

- getLocalElements

```java
Iterable
<? extends
Element
> getLocalElements()
```

Returns the elements directly contained in this scope.

**Returns:** the elements contained in this scope

---

#### Method Detail

getEnclosingScope

```java
Scope
getEnclosingScope()
```

Returns the enclosing scope.

**Returns:** the enclosing scope

---

#### getEnclosingScope

Scope

getEnclosingScope()

Returns the enclosing scope.

getEnclosingClass

```java
TypeElement
getEnclosingClass()
```

Returns the innermost type element containing the position of this scope.

**Returns:** the innermost enclosing type element

---

#### getEnclosingClass

TypeElement

getEnclosingClass()

Returns the innermost type element containing the position of this scope.

getEnclosingMethod

```java
ExecutableElement
getEnclosingMethod()
```

Returns the innermost executable element containing the position of this scope.

**Returns:** the innermost enclosing method declaration

---

#### getEnclosingMethod

ExecutableElement

getEnclosingMethod()

Returns the innermost executable element containing the position of this scope.

getLocalElements

```java
Iterable
<? extends
Element
> getLocalElements()
```

Returns the elements directly contained in this scope.

**Returns:** the elements contained in this scope

---

#### getLocalElements

Iterable

<? extends

Element

> getLocalElements()

Returns the elements directly contained in this scope.

---

