# Interface GuardedInvocationTransformer

**Source:** `jdk.dynalink\jdk\dynalink\linker\GuardedInvocationTransformer.html`

### Class Description

```java
@FunctionalInterface

public interface
GuardedInvocationTransformer
```

Interface for objects that are used to transform one guarded invocation into
another one. Typical usage is for implementing

pre-link transformers

.

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### GuardedInvocation
filter​(
GuardedInvocation
inv,

LinkRequest
linkRequest,

LinkerServices
linkerServices)

Given a guarded invocation, return either the same or potentially
different guarded invocation.

**Parameters:**
- inv

- the original guarded invocation.
- linkRequest

- the link request for which the invocation was
generated (usually by some linker).
- linkerServices

- the linker services that can be used during
creation of a new invocation.

**Returns:**
- either the passed guarded invocation or a different one, with
the difference usually determined based on information in the link
request and the differing invocation created with the assistance of the
linker services. Whether or not

null

is an accepted return value
is dependent on the user of the filter.

**Throws:**
- NullPointerException

- is allowed to be thrown by implementations
if any of the passed arguments is null.

---

### Additional Sections

#### Interface GuardedInvocationTransformer

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
GuardedInvocationTransformer
```

Interface for objects that are used to transform one guarded invocation into
another one. Typical usage is for implementing

pre-link transformers

.

@FunctionalInterface

public interface

GuardedInvocationTransformer

Interface for objects that are used to transform one guarded invocation into
another one. Typical usage is for implementing

pre-link transformers

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

GuardedInvocation

filter

​(

GuardedInvocation

inv,

LinkRequest

linkRequest,

LinkerServices

linkerServices)

Given a guarded invocation, return either the same or potentially
different guarded invocation.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

GuardedInvocation

filter

​(

GuardedInvocation

inv,

LinkRequest

linkRequest,

LinkerServices

linkerServices)

Given a guarded invocation, return either the same or potentially
different guarded invocation.

---

#### Method Summary

Given a guarded invocation, return either the same or potentially
different guarded invocation.

============ METHOD DETAIL ==========

- Method Detail

- filter

```java
GuardedInvocation
filter​(
GuardedInvocation
inv,

LinkRequest
linkRequest,

LinkerServices
linkerServices)
```

Given a guarded invocation, return either the same or potentially
different guarded invocation.

**Parameters:** inv

- the original guarded invocation.
**Parameters:** linkRequest

- the link request for which the invocation was
generated (usually by some linker).
**Parameters:** linkerServices

- the linker services that can be used during
creation of a new invocation.
**Returns:** either the passed guarded invocation or a different one, with
the difference usually determined based on information in the link
request and the differing invocation created with the assistance of the
linker services. Whether or not

null

is an accepted return value
is dependent on the user of the filter.
**Throws:** NullPointerException

- is allowed to be thrown by implementations
if any of the passed arguments is null.

Method Detail

- filter

```java
GuardedInvocation
filter​(
GuardedInvocation
inv,

LinkRequest
linkRequest,

LinkerServices
linkerServices)
```

Given a guarded invocation, return either the same or potentially
different guarded invocation.

**Parameters:** inv

- the original guarded invocation.
**Parameters:** linkRequest

- the link request for which the invocation was
generated (usually by some linker).
**Parameters:** linkerServices

- the linker services that can be used during
creation of a new invocation.
**Returns:** either the passed guarded invocation or a different one, with
the difference usually determined based on information in the link
request and the differing invocation created with the assistance of the
linker services. Whether or not

null

is an accepted return value
is dependent on the user of the filter.
**Throws:** NullPointerException

- is allowed to be thrown by implementations
if any of the passed arguments is null.

---

#### Method Detail

filter

```java
GuardedInvocation
filter​(
GuardedInvocation
inv,

LinkRequest
linkRequest,

LinkerServices
linkerServices)
```

Given a guarded invocation, return either the same or potentially
different guarded invocation.

**Parameters:** inv

- the original guarded invocation.
**Parameters:** linkRequest

- the link request for which the invocation was
generated (usually by some linker).
**Parameters:** linkerServices

- the linker services that can be used during
creation of a new invocation.
**Returns:** either the passed guarded invocation or a different one, with
the difference usually determined based on information in the link
request and the differing invocation created with the assistance of the
linker services. Whether or not

null

is an accepted return value
is dependent on the user of the filter.
**Throws:** NullPointerException

- is allowed to be thrown by implementations
if any of the passed arguments is null.

---

#### filter

GuardedInvocation

filter​(

GuardedInvocation

inv,

LinkRequest

linkRequest,

LinkerServices

linkerServices)

Given a guarded invocation, return either the same or potentially
different guarded invocation.

---

