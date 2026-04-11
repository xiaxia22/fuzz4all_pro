# Class DefaultInternalObjectFilter

**Source:** `jdk.dynalink\jdk\dynalink\linker\support\DefaultInternalObjectFilter.html`

### Class Description

```java
public class
DefaultInternalObjectFilter

extends
Object

implements
MethodHandleTransformer
```

Default implementation for a

DynamicLinkerFactory.setInternalObjectsFilter(MethodHandleTransformer)

that delegates to a pair of filtering method handles. It takes a method
handle of

Object(Object)

type for filtering parameter values and
another one of the same type for filtering return values. It applies them as
parameter and return value filters on method handles passed to its

MethodHandleTransformer.transform(MethodHandle)

method, on those parameters and return values
that are declared to have type

Object

. Also handles

method handles that support variable
arity calls

with a last

Object[]

parameter. You can broadly think of
the parameter filter as being a wrapping method for exposing internal runtime
objects wrapped into an adapter with some public interface, and the return
value filter as being its inverse unwrapping method.

**All Implemented Interfaces:** MethodHandleTransformer

---

### Field Details

*No entries found.*

### Constructor Details

#### public DefaultInternalObjectFilter​(
MethodHandle
parameterFilter,

MethodHandle
returnFilter)

Creates a new filter.

**Parameters:**
- parameterFilter

- the filter for method parameters. Must be of type

Object(Object)

, or

null

.
- returnFilter

- the filter for return values. Must be of type

Object(Object)

, or

null

.

**Throws:**
- IllegalArgumentException

- if one or both filters are not of the
expected type.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class DefaultInternalObjectFilter

java.lang.Object

- jdk.dynalink.linker.support.DefaultInternalObjectFilter

jdk.dynalink.linker.support.DefaultInternalObjectFilter

**All Implemented Interfaces:** MethodHandleTransformer

```java
public class
DefaultInternalObjectFilter

extends
Object

implements
MethodHandleTransformer
```

Default implementation for a

DynamicLinkerFactory.setInternalObjectsFilter(MethodHandleTransformer)

that delegates to a pair of filtering method handles. It takes a method
handle of

Object(Object)

type for filtering parameter values and
another one of the same type for filtering return values. It applies them as
parameter and return value filters on method handles passed to its

MethodHandleTransformer.transform(MethodHandle)

method, on those parameters and return values
that are declared to have type

Object

. Also handles

method handles that support variable
arity calls

with a last

Object[]

parameter. You can broadly think of
the parameter filter as being a wrapping method for exposing internal runtime
objects wrapped into an adapter with some public interface, and the return
value filter as being its inverse unwrapping method.

public class

DefaultInternalObjectFilter

extends

Object

implements

MethodHandleTransformer

Default implementation for a

DynamicLinkerFactory.setInternalObjectsFilter(MethodHandleTransformer)

that delegates to a pair of filtering method handles. It takes a method
handle of

Object(Object)

type for filtering parameter values and
another one of the same type for filtering return values. It applies them as
parameter and return value filters on method handles passed to its

MethodHandleTransformer.transform(MethodHandle)

method, on those parameters and return values
that are declared to have type

Object

. Also handles

method handles that support variable
arity calls

with a last

Object[]

parameter. You can broadly think of
the parameter filter as being a wrapping method for exposing internal runtime
objects wrapped into an adapter with some public interface, and the return
value filter as being its inverse unwrapping method.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultInternalObjectFilter

​(

MethodHandle

parameterFilter,

MethodHandle

returnFilter)

Creates a new filter.

========== METHOD SUMMARY ===========

- Method Summary

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

- Methods declared in interface jdk.dynalink.linker.

MethodHandleTransformer

transform

Constructor Summary

Constructors

Constructor

Description

DefaultInternalObjectFilter

​(

MethodHandle

parameterFilter,

MethodHandle

returnFilter)

Creates a new filter.

---

#### Constructor Summary

Creates a new filter.

Method Summary

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

- Methods declared in interface jdk.dynalink.linker.

MethodHandleTransformer

transform

---

#### Method Summary

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

Methods declared in interface jdk.dynalink.linker.

MethodHandleTransformer

transform

---

#### Methods declared in interface jdk.dynalink.linker. MethodHandleTransformer

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultInternalObjectFilter

```java
public DefaultInternalObjectFilter​(
MethodHandle
parameterFilter,

MethodHandle
returnFilter)
```

Creates a new filter.

**Parameters:** parameterFilter

- the filter for method parameters. Must be of type

Object(Object)

, or

null

.
**Parameters:** returnFilter

- the filter for return values. Must be of type

Object(Object)

, or

null

.
**Throws:** IllegalArgumentException

- if one or both filters are not of the
expected type.

Constructor Detail

- DefaultInternalObjectFilter

```java
public DefaultInternalObjectFilter​(
MethodHandle
parameterFilter,

MethodHandle
returnFilter)
```

Creates a new filter.

**Parameters:** parameterFilter

- the filter for method parameters. Must be of type

Object(Object)

, or

null

.
**Parameters:** returnFilter

- the filter for return values. Must be of type

Object(Object)

, or

null

.
**Throws:** IllegalArgumentException

- if one or both filters are not of the
expected type.

---

#### Constructor Detail

DefaultInternalObjectFilter

```java
public DefaultInternalObjectFilter​(
MethodHandle
parameterFilter,

MethodHandle
returnFilter)
```

Creates a new filter.

**Parameters:** parameterFilter

- the filter for method parameters. Must be of type

Object(Object)

, or

null

.
**Parameters:** returnFilter

- the filter for return values. Must be of type

Object(Object)

, or

null

.
**Throws:** IllegalArgumentException

- if one or both filters are not of the
expected type.

---

#### DefaultInternalObjectFilter

public DefaultInternalObjectFilter​(

MethodHandle

parameterFilter,

MethodHandle

returnFilter)

Creates a new filter.

---

