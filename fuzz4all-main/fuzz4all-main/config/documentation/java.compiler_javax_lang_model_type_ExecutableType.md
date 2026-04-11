# Interface ExecutableType

**Source:** `java.compiler\javax\lang\model\type\ExecutableType.html`

### Class Description

```java
public interface
ExecutableType

extends
TypeMirror
```

Represents the type of an executable. An

executable

is a method, constructor, or initializer.

The executable is
represented as when viewed as a method (or constructor or
initializer) of some reference type.
If that reference type is parameterized, then its actual
type arguments are substituted into any types returned by the methods of
this interface.

**All Superinterfaces:** AnnotatedConstruct

,

TypeMirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<? extends
TypeVariable
> getTypeVariables()

Returns the type variables declared by the formal type parameters
of this executable.

**Returns:**
- the type variables declared by the formal type parameters,
or an empty list if there are none

---

#### TypeMirror
getReturnType()

Returns the return type of this executable.
Returns a

NoType

with kind

VOID

if this executable is not a method, or is a method that does not
return a value.

**Returns:**
- the return type of this executable

---

#### List
<? extends
TypeMirror
> getParameterTypes()

Returns the types of this executable's formal parameters.

**Returns:**
- the types of this executable's formal parameters,
or an empty list if there are none

---

#### TypeMirror
getReceiverType()

Returns the receiver type of this executable,
or

NoType

with
kind

NONE

if the executable has no receiver type.

An executable which is an instance method, or a constructor of an
inner class, has a receiver type derived from the

declaring type

.

An executable which is a static method, or a constructor of a
non-inner class, or an initializer (static or instance), has no
receiver type.

**Returns:**
- the receiver type of this executable

**Since:**
- 1.8

---

#### List
<? extends
TypeMirror
> getThrownTypes()

Returns the exceptions and other throwables listed in this
executable's

throws

clause.

**Returns:**
- the exceptions and other throwables listed in this
executable's

throws

clause,
or an empty list if there are none.

---

### Additional Sections

#### Interface ExecutableType

**All Superinterfaces:** AnnotatedConstruct

,

TypeMirror

```java
public interface
ExecutableType

extends
TypeMirror
```

Represents the type of an executable. An

executable

is a method, constructor, or initializer.

The executable is
represented as when viewed as a method (or constructor or
initializer) of some reference type.
If that reference type is parameterized, then its actual
type arguments are substituted into any types returned by the methods of
this interface.

**Since:** 1.6
**See Also:** ExecutableElement

public interface

ExecutableType

extends

TypeMirror

Represents the type of an executable. An

executable

is a method, constructor, or initializer.

The executable is
represented as when viewed as a method (or constructor or
initializer) of some reference type.
If that reference type is parameterized, then its actual
type arguments are substituted into any types returned by the methods of
this interface.

The executable is
represented as when viewed as a method (or constructor or
initializer) of some reference type.
If that reference type is parameterized, then its actual
type arguments are substituted into any types returned by the methods of
this interface.

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

TypeMirror

>

getParameterTypes

()

Returns the types of this executable's formal parameters.

TypeMirror

getReceiverType

()

Returns the receiver type of this executable,
or

NoType

with
kind

NONE

if the executable has no receiver type.

TypeMirror

getReturnType

()

Returns the return type of this executable.

List

<? extends

TypeMirror

>

getThrownTypes

()

Returns the exceptions and other throwables listed in this
executable's

throws

clause.

List

<? extends

TypeVariable

>

getTypeVariables

()

Returns the type variables declared by the formal type parameters
of this executable.

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotation

,

getAnnotationMirrors

,

getAnnotationsByType

- Methods declared in interface javax.lang.model.type.

TypeMirror

accept

,

equals

,

getKind

,

hashCode

,

toString

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<? extends

TypeMirror

>

getParameterTypes

()

Returns the types of this executable's formal parameters.

TypeMirror

getReceiverType

()

Returns the receiver type of this executable,
or

NoType

with
kind

NONE

if the executable has no receiver type.

TypeMirror

getReturnType

()

Returns the return type of this executable.

List

<? extends

TypeMirror

>

getThrownTypes

()

Returns the exceptions and other throwables listed in this
executable's

throws

clause.

List

<? extends

TypeVariable

>

getTypeVariables

()

Returns the type variables declared by the formal type parameters
of this executable.

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotation

,

getAnnotationMirrors

,

getAnnotationsByType

- Methods declared in interface javax.lang.model.type.

TypeMirror

accept

,

equals

,

getKind

,

hashCode

,

toString

---

#### Method Summary

Returns the types of this executable's formal parameters.

Returns the receiver type of this executable,
or

NoType

with
kind

NONE

if the executable has no receiver type.

Returns the return type of this executable.

Returns the exceptions and other throwables listed in this
executable's

throws

clause.

Returns the type variables declared by the formal type parameters
of this executable.

Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotation

,

getAnnotationMirrors

,

getAnnotationsByType

---

#### Methods declared in interface javax.lang.model. AnnotatedConstruct

Methods declared in interface javax.lang.model.type.

TypeMirror

accept

,

equals

,

getKind

,

hashCode

,

toString

---

#### Methods declared in interface javax.lang.model.type. TypeMirror

============ METHOD DETAIL ==========

- Method Detail

- getTypeVariables

```java
List
<? extends
TypeVariable
> getTypeVariables()
```

Returns the type variables declared by the formal type parameters
of this executable.

**Returns:** the type variables declared by the formal type parameters,
or an empty list if there are none

- getReturnType

```java
TypeMirror
getReturnType()
```

Returns the return type of this executable.
Returns a

NoType

with kind

VOID

if this executable is not a method, or is a method that does not
return a value.

**Returns:** the return type of this executable

- getParameterTypes

```java
List
<? extends
TypeMirror
> getParameterTypes()
```

Returns the types of this executable's formal parameters.

**Returns:** the types of this executable's formal parameters,
or an empty list if there are none

- getReceiverType

```java
TypeMirror
getReceiverType()
```

Returns the receiver type of this executable,
or

NoType

with
kind

NONE

if the executable has no receiver type.

An executable which is an instance method, or a constructor of an
inner class, has a receiver type derived from the

declaring type

.

An executable which is a static method, or a constructor of a
non-inner class, or an initializer (static or instance), has no
receiver type.

**Returns:** the receiver type of this executable
**Since:** 1.8

- getThrownTypes

```java
List
<? extends
TypeMirror
> getThrownTypes()
```

Returns the exceptions and other throwables listed in this
executable's

throws

clause.

**Returns:** the exceptions and other throwables listed in this
executable's

throws

clause,
or an empty list if there are none.

Method Detail

- getTypeVariables

```java
List
<? extends
TypeVariable
> getTypeVariables()
```

Returns the type variables declared by the formal type parameters
of this executable.

**Returns:** the type variables declared by the formal type parameters,
or an empty list if there are none

- getReturnType

```java
TypeMirror
getReturnType()
```

Returns the return type of this executable.
Returns a

NoType

with kind

VOID

if this executable is not a method, or is a method that does not
return a value.

**Returns:** the return type of this executable

- getParameterTypes

```java
List
<? extends
TypeMirror
> getParameterTypes()
```

Returns the types of this executable's formal parameters.

**Returns:** the types of this executable's formal parameters,
or an empty list if there are none

- getReceiverType

```java
TypeMirror
getReceiverType()
```

Returns the receiver type of this executable,
or

NoType

with
kind

NONE

if the executable has no receiver type.

An executable which is an instance method, or a constructor of an
inner class, has a receiver type derived from the

declaring type

.

An executable which is a static method, or a constructor of a
non-inner class, or an initializer (static or instance), has no
receiver type.

**Returns:** the receiver type of this executable
**Since:** 1.8

- getThrownTypes

```java
List
<? extends
TypeMirror
> getThrownTypes()
```

Returns the exceptions and other throwables listed in this
executable's

throws

clause.

**Returns:** the exceptions and other throwables listed in this
executable's

throws

clause,
or an empty list if there are none.

---

#### Method Detail

getTypeVariables

```java
List
<? extends
TypeVariable
> getTypeVariables()
```

Returns the type variables declared by the formal type parameters
of this executable.

**Returns:** the type variables declared by the formal type parameters,
or an empty list if there are none

---

#### getTypeVariables

List

<? extends

TypeVariable

> getTypeVariables()

Returns the type variables declared by the formal type parameters
of this executable.

getReturnType

```java
TypeMirror
getReturnType()
```

Returns the return type of this executable.
Returns a

NoType

with kind

VOID

if this executable is not a method, or is a method that does not
return a value.

**Returns:** the return type of this executable

---

#### getReturnType

TypeMirror

getReturnType()

Returns the return type of this executable.
Returns a

NoType

with kind

VOID

if this executable is not a method, or is a method that does not
return a value.

getParameterTypes

```java
List
<? extends
TypeMirror
> getParameterTypes()
```

Returns the types of this executable's formal parameters.

**Returns:** the types of this executable's formal parameters,
or an empty list if there are none

---

#### getParameterTypes

List

<? extends

TypeMirror

> getParameterTypes()

Returns the types of this executable's formal parameters.

getReceiverType

```java
TypeMirror
getReceiverType()
```

Returns the receiver type of this executable,
or

NoType

with
kind

NONE

if the executable has no receiver type.

An executable which is an instance method, or a constructor of an
inner class, has a receiver type derived from the

declaring type

.

An executable which is a static method, or a constructor of a
non-inner class, or an initializer (static or instance), has no
receiver type.

**Returns:** the receiver type of this executable
**Since:** 1.8

---

#### getReceiverType

TypeMirror

getReceiverType()

Returns the receiver type of this executable,
or

NoType

with
kind

NONE

if the executable has no receiver type.

An executable which is an instance method, or a constructor of an
inner class, has a receiver type derived from the

declaring type

.

An executable which is a static method, or a constructor of a
non-inner class, or an initializer (static or instance), has no
receiver type.

getThrownTypes

```java
List
<? extends
TypeMirror
> getThrownTypes()
```

Returns the exceptions and other throwables listed in this
executable's

throws

clause.

**Returns:** the exceptions and other throwables listed in this
executable's

throws

clause,
or an empty list if there are none.

---

#### getThrownTypes

List

<? extends

TypeMirror

> getThrownTypes()

Returns the exceptions and other throwables listed in this
executable's

throws

clause.

---

