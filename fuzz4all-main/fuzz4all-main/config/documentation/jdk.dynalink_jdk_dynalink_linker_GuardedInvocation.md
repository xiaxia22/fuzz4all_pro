# Class GuardedInvocation

**Source:** `jdk.dynalink\jdk\dynalink\linker\GuardedInvocation.html`

### Class Description

```java
public class
GuardedInvocation

extends
Object
```

Represents a conditionally valid method handle. Usually produced as a return
value of

GuardingDynamicLinker.getGuardedInvocation(LinkRequest, LinkerServices)

and

GuardingTypeConverterFactory.convertToType(Class, Class, Supplier)

.
It is an immutable tuple of an invocation method handle, a guard method
handle that defines the applicability of the invocation handle, zero or more
switch points that can be used for external invalidation of the invocation
handle, and an exception type that if thrown during an invocation of the
method handle also invalidates it. The invocation handle is suitable for
invocation if the guard handle returns true for its arguments, and as long
as any of the switch points are not invalidated, and as long as it does not
throw an exception of the designated type. The guard, the switch points, and
the exception type are all optional (a guarded invocation having none of them
is unconditionally valid).

---

### Field Details

*No entries found.*

### Constructor Details

#### public GuardedInvocation​(
MethodHandle
invocation)

Creates a new unconditional guarded invocation. It is unconditional as it
has no invalidations.

**Parameters:**
- invocation

- the method handle representing the invocation. Must not
be null.

**Throws:**
- NullPointerException

- if invocation is null.

---

#### public GuardedInvocation​(
MethodHandle
invocation,

MethodHandle
guard)

Creates a new guarded invocation, with a guard method handle.

**Parameters:**
- invocation

- the method handle representing the invocation. Must not
be null.
- guard

- the method handle representing the guard. Must have be
compatible with the

invocation

handle as per

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

.
For some useful guards, check out the

Guards

class. It can be
null to represent an unconditional invocation.

**Throws:**
- NullPointerException

- if invocation is null.

---

#### public GuardedInvocation​(
MethodHandle
invocation,

SwitchPoint
switchPoint)

Creates a new guarded invocation that can be invalidated by a switch
point.

**Parameters:**
- invocation

- the method handle representing the invocation. Must
not be null.
- switchPoint

- the optional switch point that can be used to
invalidate this linkage. It can be null. If it is null, this represents
an unconditional invocation.

**Throws:**
- NullPointerException

- if invocation is null.

---

#### public GuardedInvocation​(
MethodHandle
invocation,

MethodHandle
guard,

SwitchPoint
switchPoint)

Creates a new guarded invocation, with both a guard method handle and a
switch point that can be used to invalidate it.

**Parameters:**
- invocation

- the method handle representing the invocation. Must
not be null.
- guard

- the method handle representing the guard. Must have be
compatible with the

invocation

handle as per

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

.
For some useful guards, check out the

Guards

class. It can be
null. If both it and the switch point are null, this represents an
unconditional invocation.
- switchPoint

- the optional switch point that can be used to
invalidate this linkage.

**Throws:**
- NullPointerException

- if invocation is null.

---

#### public GuardedInvocation​(
MethodHandle
invocation,

MethodHandle
guard,

SwitchPoint
switchPoint,

Class
<? extends
Throwable
> exception)

Creates a new guarded invocation, with a guard method handle, a
switch point that can be used to invalidate it, and an exception that if
thrown when invoked also invalidates it.

**Parameters:**
- invocation

- the method handle representing the invocation. Must not
be null.
- guard

- the method handle representing the guard. Must have be
compatible with the

invocation

handle as per

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

.
For some useful guards, check out the

Guards

class. It can be
null. If it and the switch point and the exception are all null, this
represents an unconditional invocation.
- switchPoint

- the optional switch point that can be used to
invalidate this linkage.
- exception

- the optional exception type that is when thrown by the
invocation also invalidates it.

**Throws:**
- NullPointerException

- if invocation is null.

---

#### public GuardedInvocation​(
MethodHandle
invocation,

MethodHandle
guard,

SwitchPoint
[] switchPoints,

Class
<? extends
Throwable
> exception)

Creates a new guarded invocation, with a guard method handle, any number
of switch points that can be used to invalidate it, and an exception that
if thrown when invoked also invalidates it.

**Parameters:**
- invocation

- the method handle representing the invocation. Must not
be null.
- guard

- the method handle representing the guard. Must have be
compatible with the

invocation

handle as per

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

.
For some useful guards, check out the

Guards

class. It can be
null. If it and the exception are both null, and no switch points were
specified, this represents an unconditional invocation.
- switchPoints

- optional switch points that can be used to
invalidate this linkage.
- exception

- the optional exception type that is when thrown by the
invocation also invalidates it.

**Throws:**
- NullPointerException

- if invocation is null.

---

### Method Details

#### public
MethodHandle
getInvocation()

Returns the invocation method handle.

**Returns:**
- the invocation method handle. It will never be null.

---

#### public
MethodHandle
getGuard()

Returns the guard method handle.

**Returns:**
- the guard method handle. Can be null.

---

#### public
SwitchPoint
[] getSwitchPoints()

Returns the switch points that can be used to invalidate the linkage of
this invocation handle.

**Returns:**
- the switch points that can be used to invalidate the linkage of
this invocation handle. Can be null.

---

#### public
Class
<? extends
Throwable
> getException()

Returns the exception type that if thrown by the invocation should
invalidate the linkage of this guarded invocation.

**Returns:**
- the exception type that if thrown should be used to invalidate
the linkage. Can be null.

---

#### public boolean hasBeenInvalidated()

Returns true if and only if this guarded invocation has at least one
invalidated switch point.

**Returns:**
- true if and only if this guarded invocation has at least one
invalidated switch point.

---

#### public
GuardedInvocation
replaceMethods​(
MethodHandle
newInvocation,

MethodHandle
newGuard)

Creates a new guarded invocation with different methods, preserving the switch point.

**Parameters:**
- newInvocation

- the new invocation
- newGuard

- the new guard

**Returns:**
- a new guarded invocation with the replaced methods and the same switch point as this invocation.

---

#### public
GuardedInvocation
addSwitchPoint​(
SwitchPoint
newSwitchPoint)

Create a new guarded invocation with an added switch point.

**Parameters:**
- newSwitchPoint

- new switch point. Can be null in which case this
method return the current guarded invocation with no changes.

**Returns:**
- a guarded invocation with the added switch point.

---

#### public
GuardedInvocation
asType​(
MethodType
newType)

Changes the type of the invocation, as if

MethodHandle.asType(MethodType)

was applied to its invocation
and its guard, if it has one (with return type changed to boolean, and
parameter count potentially truncated for the guard). If the invocation
already is of the required type, returns this object.

**Parameters:**
- newType

- the new type of the invocation.

**Returns:**
- a guarded invocation with the new type applied to it.

---

#### public
GuardedInvocation
asType​(
LinkerServices
linkerServices,

MethodType
newType)

Changes the type of the invocation, as if

LinkerServices.asType(MethodHandle, MethodType)

was applied to
its invocation and its guard, if it has one (with return type changed to
boolean, and parameter count potentially truncated for the guard). If the
invocation already is of the required type, returns this object.

**Parameters:**
- linkerServices

- the linker services to use for the conversion
- newType

- the new type of the invocation.

**Returns:**
- a guarded invocation with the new type applied to it.

---

#### public
GuardedInvocation
asTypeSafeReturn​(
LinkerServices
linkerServices,

MethodType
newType)

Changes the type of the invocation, as if

LinkerServices.asTypeLosslessReturn(MethodHandle, MethodType)

was
applied to its invocation and

LinkerServices.asType(MethodHandle, MethodType)

applied to its
guard, if it has one (with return type changed to boolean, and parameter
count potentially truncated for the guard). If the invocation doesn't
change its type, returns this object.

**Parameters:**
- linkerServices

- the linker services to use for the conversion
- newType

- the new type of the invocation.

**Returns:**
- a guarded invocation with the new type applied to it.

---

#### public
GuardedInvocation
asType​(
CallSiteDescriptor
desc)

Changes the type of the invocation, as if

MethodHandle.asType(MethodType)

was applied to its invocation
and its guard, if it has one (with return type changed to boolean for
guard). If the invocation already is of the required type, returns this
object.

**Parameters:**
- desc

- a call descriptor whose method type is adapted.

**Returns:**
- a guarded invocation with the new type applied to it.

---

#### public
GuardedInvocation
filterArguments​(int pos,

MethodHandle
... filters)

Applies argument filters to both the invocation and the guard
(if it exists and has at least

pos + 1

parameters) with

MethodHandles.filterArguments(MethodHandle, int, MethodHandle...)

.

**Parameters:**
- pos

- the position of the first argument being filtered
- filters

- the argument filters

**Returns:**
- a filtered invocation

---

#### public
GuardedInvocation
dropArguments​(int pos,

List
<
Class
<?>> valueTypes)

Makes an invocation that drops arguments in both the invocation and the
guard (if it exists and has at least

pos

parameters) with

MethodHandles.dropArguments(MethodHandle, int, List)

.

**Parameters:**
- pos

- the position of the first argument being dropped
- valueTypes

- the types of the values being dropped

**Returns:**
- an invocation that drops arguments

---

#### public
GuardedInvocation
dropArguments​(int pos,

Class
<?>... valueTypes)

Makes an invocation that drops arguments in both the invocation and the
guard (if it exists and has at least

pos

parameters) with

MethodHandles.dropArguments(MethodHandle, int, Class...)

.

**Parameters:**
- pos

- the position of the first argument being dropped
- valueTypes

- the types of the values being dropped

**Returns:**
- an invocation that drops arguments

---

#### public
MethodHandle
compose​(
MethodHandle
fallback)

Composes the invocation, guard, switch points, and the exception into a
composite method handle that knows how to fall back when the guard fails
or the invocation is invalidated.

**Parameters:**
- fallback

- the fallback method handle for when a switch point is
invalidated, a guard returns false, or invalidating exception is thrown.

**Returns:**
- a composite method handle.

---

#### public
MethodHandle
compose​(
MethodHandle
guardFallback,

MethodHandle
switchpointFallback,

MethodHandle
catchFallback)

Composes the invocation, guard, switch points, and the exception into a
composite method handle that knows how to fall back when the guard fails
or the invocation is invalidated.

**Parameters:**
- switchpointFallback

- the fallback method handle in case a switch
point is invalidated.
- guardFallback

- the fallback method handle in case guard returns
false.
- catchFallback

- the fallback method in case the exception handler
triggers.

**Returns:**
- a composite method handle.

---

### Additional Sections

#### Class GuardedInvocation

java.lang.Object

- jdk.dynalink.linker.GuardedInvocation

jdk.dynalink.linker.GuardedInvocation

```java
public class
GuardedInvocation

extends
Object
```

Represents a conditionally valid method handle. Usually produced as a return
value of

GuardingDynamicLinker.getGuardedInvocation(LinkRequest, LinkerServices)

and

GuardingTypeConverterFactory.convertToType(Class, Class, Supplier)

.
It is an immutable tuple of an invocation method handle, a guard method
handle that defines the applicability of the invocation handle, zero or more
switch points that can be used for external invalidation of the invocation
handle, and an exception type that if thrown during an invocation of the
method handle also invalidates it. The invocation handle is suitable for
invocation if the guard handle returns true for its arguments, and as long
as any of the switch points are not invalidated, and as long as it does not
throw an exception of the designated type. The guard, the switch points, and
the exception type are all optional (a guarded invocation having none of them
is unconditionally valid).

public class

GuardedInvocation

extends

Object

Represents a conditionally valid method handle. Usually produced as a return
value of

GuardingDynamicLinker.getGuardedInvocation(LinkRequest, LinkerServices)

and

GuardingTypeConverterFactory.convertToType(Class, Class, Supplier)

.
It is an immutable tuple of an invocation method handle, a guard method
handle that defines the applicability of the invocation handle, zero or more
switch points that can be used for external invalidation of the invocation
handle, and an exception type that if thrown during an invocation of the
method handle also invalidates it. The invocation handle is suitable for
invocation if the guard handle returns true for its arguments, and as long
as any of the switch points are not invalidated, and as long as it does not
throw an exception of the designated type. The guard, the switch points, and
the exception type are all optional (a guarded invocation having none of them
is unconditionally valid).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GuardedInvocation

​(

MethodHandle

invocation)

Creates a new unconditional guarded invocation.

GuardedInvocation

​(

MethodHandle

invocation,

MethodHandle

guard)

Creates a new guarded invocation, with a guard method handle.

GuardedInvocation

​(

MethodHandle

invocation,

MethodHandle

guard,

SwitchPoint

switchPoint)

Creates a new guarded invocation, with both a guard method handle and a
switch point that can be used to invalidate it.

GuardedInvocation

​(

MethodHandle

invocation,

MethodHandle

guard,

SwitchPoint

[] switchPoints,

Class

<? extends

Throwable

> exception)

Creates a new guarded invocation, with a guard method handle, any number
of switch points that can be used to invalidate it, and an exception that
if thrown when invoked also invalidates it.

GuardedInvocation

​(

MethodHandle

invocation,

MethodHandle

guard,

SwitchPoint

switchPoint,

Class

<? extends

Throwable

> exception)

Creates a new guarded invocation, with a guard method handle, a
switch point that can be used to invalidate it, and an exception that if
thrown when invoked also invalidates it.

GuardedInvocation

​(

MethodHandle

invocation,

SwitchPoint

switchPoint)

Creates a new guarded invocation that can be invalidated by a switch
point.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

GuardedInvocation

addSwitchPoint

​(

SwitchPoint

newSwitchPoint)

Create a new guarded invocation with an added switch point.

GuardedInvocation

asType

​(

MethodType

newType)

Changes the type of the invocation, as if

MethodHandle.asType(MethodType)

was applied to its invocation
and its guard, if it has one (with return type changed to boolean, and
parameter count potentially truncated for the guard).

GuardedInvocation

asType

​(

CallSiteDescriptor

desc)

Changes the type of the invocation, as if

MethodHandle.asType(MethodType)

was applied to its invocation
and its guard, if it has one (with return type changed to boolean for
guard).

GuardedInvocation

asType

​(

LinkerServices

linkerServices,

MethodType

newType)

Changes the type of the invocation, as if

LinkerServices.asType(MethodHandle, MethodType)

was applied to
its invocation and its guard, if it has one (with return type changed to
boolean, and parameter count potentially truncated for the guard).

GuardedInvocation

asTypeSafeReturn

​(

LinkerServices

linkerServices,

MethodType

newType)

Changes the type of the invocation, as if

LinkerServices.asTypeLosslessReturn(MethodHandle, MethodType)

was
applied to its invocation and

LinkerServices.asType(MethodHandle, MethodType)

applied to its
guard, if it has one (with return type changed to boolean, and parameter
count potentially truncated for the guard).

MethodHandle

compose

​(

MethodHandle

fallback)

Composes the invocation, guard, switch points, and the exception into a
composite method handle that knows how to fall back when the guard fails
or the invocation is invalidated.

MethodHandle

compose

​(

MethodHandle

guardFallback,

MethodHandle

switchpointFallback,

MethodHandle

catchFallback)

Composes the invocation, guard, switch points, and the exception into a
composite method handle that knows how to fall back when the guard fails
or the invocation is invalidated.

GuardedInvocation

dropArguments

​(int pos,

Class

<?>... valueTypes)

Makes an invocation that drops arguments in both the invocation and the
guard (if it exists and has at least

pos

parameters) with

MethodHandles.dropArguments(MethodHandle, int, Class...)

.

GuardedInvocation

dropArguments

​(int pos,

List

<

Class

<?>> valueTypes)

Makes an invocation that drops arguments in both the invocation and the
guard (if it exists and has at least

pos

parameters) with

MethodHandles.dropArguments(MethodHandle, int, List)

.

GuardedInvocation

filterArguments

​(int pos,

MethodHandle

... filters)

Applies argument filters to both the invocation and the guard
(if it exists and has at least

pos + 1

parameters) with

MethodHandles.filterArguments(MethodHandle, int, MethodHandle...)

.

Class

<? extends

Throwable

>

getException

()

Returns the exception type that if thrown by the invocation should
invalidate the linkage of this guarded invocation.

MethodHandle

getGuard

()

Returns the guard method handle.

MethodHandle

getInvocation

()

Returns the invocation method handle.

SwitchPoint

[]

getSwitchPoints

()

Returns the switch points that can be used to invalidate the linkage of
this invocation handle.

boolean

hasBeenInvalidated

()

Returns true if and only if this guarded invocation has at least one
invalidated switch point.

GuardedInvocation

replaceMethods

​(

MethodHandle

newInvocation,

MethodHandle

newGuard)

Creates a new guarded invocation with different methods, preserving the switch point.

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

Constructor Summary

Constructors

Constructor

Description

GuardedInvocation

​(

MethodHandle

invocation)

Creates a new unconditional guarded invocation.

GuardedInvocation

​(

MethodHandle

invocation,

MethodHandle

guard)

Creates a new guarded invocation, with a guard method handle.

GuardedInvocation

​(

MethodHandle

invocation,

MethodHandle

guard,

SwitchPoint

switchPoint)

Creates a new guarded invocation, with both a guard method handle and a
switch point that can be used to invalidate it.

GuardedInvocation

​(

MethodHandle

invocation,

MethodHandle

guard,

SwitchPoint

[] switchPoints,

Class

<? extends

Throwable

> exception)

Creates a new guarded invocation, with a guard method handle, any number
of switch points that can be used to invalidate it, and an exception that
if thrown when invoked also invalidates it.

GuardedInvocation

​(

MethodHandle

invocation,

MethodHandle

guard,

SwitchPoint

switchPoint,

Class

<? extends

Throwable

> exception)

Creates a new guarded invocation, with a guard method handle, a
switch point that can be used to invalidate it, and an exception that if
thrown when invoked also invalidates it.

GuardedInvocation

​(

MethodHandle

invocation,

SwitchPoint

switchPoint)

Creates a new guarded invocation that can be invalidated by a switch
point.

---

#### Constructor Summary

Creates a new unconditional guarded invocation.

Creates a new guarded invocation, with a guard method handle.

Creates a new guarded invocation, with both a guard method handle and a
switch point that can be used to invalidate it.

Creates a new guarded invocation, with a guard method handle, any number
of switch points that can be used to invalidate it, and an exception that
if thrown when invoked also invalidates it.

Creates a new guarded invocation, with a guard method handle, a
switch point that can be used to invalidate it, and an exception that if
thrown when invoked also invalidates it.

Creates a new guarded invocation that can be invalidated by a switch
point.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

GuardedInvocation

addSwitchPoint

​(

SwitchPoint

newSwitchPoint)

Create a new guarded invocation with an added switch point.

GuardedInvocation

asType

​(

MethodType

newType)

Changes the type of the invocation, as if

MethodHandle.asType(MethodType)

was applied to its invocation
and its guard, if it has one (with return type changed to boolean, and
parameter count potentially truncated for the guard).

GuardedInvocation

asType

​(

CallSiteDescriptor

desc)

Changes the type of the invocation, as if

MethodHandle.asType(MethodType)

was applied to its invocation
and its guard, if it has one (with return type changed to boolean for
guard).

GuardedInvocation

asType

​(

LinkerServices

linkerServices,

MethodType

newType)

Changes the type of the invocation, as if

LinkerServices.asType(MethodHandle, MethodType)

was applied to
its invocation and its guard, if it has one (with return type changed to
boolean, and parameter count potentially truncated for the guard).

GuardedInvocation

asTypeSafeReturn

​(

LinkerServices

linkerServices,

MethodType

newType)

Changes the type of the invocation, as if

LinkerServices.asTypeLosslessReturn(MethodHandle, MethodType)

was
applied to its invocation and

LinkerServices.asType(MethodHandle, MethodType)

applied to its
guard, if it has one (with return type changed to boolean, and parameter
count potentially truncated for the guard).

MethodHandle

compose

​(

MethodHandle

fallback)

Composes the invocation, guard, switch points, and the exception into a
composite method handle that knows how to fall back when the guard fails
or the invocation is invalidated.

MethodHandle

compose

​(

MethodHandle

guardFallback,

MethodHandle

switchpointFallback,

MethodHandle

catchFallback)

Composes the invocation, guard, switch points, and the exception into a
composite method handle that knows how to fall back when the guard fails
or the invocation is invalidated.

GuardedInvocation

dropArguments

​(int pos,

Class

<?>... valueTypes)

Makes an invocation that drops arguments in both the invocation and the
guard (if it exists and has at least

pos

parameters) with

MethodHandles.dropArguments(MethodHandle, int, Class...)

.

GuardedInvocation

dropArguments

​(int pos,

List

<

Class

<?>> valueTypes)

Makes an invocation that drops arguments in both the invocation and the
guard (if it exists and has at least

pos

parameters) with

MethodHandles.dropArguments(MethodHandle, int, List)

.

GuardedInvocation

filterArguments

​(int pos,

MethodHandle

... filters)

Applies argument filters to both the invocation and the guard
(if it exists and has at least

pos + 1

parameters) with

MethodHandles.filterArguments(MethodHandle, int, MethodHandle...)

.

Class

<? extends

Throwable

>

getException

()

Returns the exception type that if thrown by the invocation should
invalidate the linkage of this guarded invocation.

MethodHandle

getGuard

()

Returns the guard method handle.

MethodHandle

getInvocation

()

Returns the invocation method handle.

SwitchPoint

[]

getSwitchPoints

()

Returns the switch points that can be used to invalidate the linkage of
this invocation handle.

boolean

hasBeenInvalidated

()

Returns true if and only if this guarded invocation has at least one
invalidated switch point.

GuardedInvocation

replaceMethods

​(

MethodHandle

newInvocation,

MethodHandle

newGuard)

Creates a new guarded invocation with different methods, preserving the switch point.

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

Create a new guarded invocation with an added switch point.

Changes the type of the invocation, as if

MethodHandle.asType(MethodType)

was applied to its invocation
and its guard, if it has one (with return type changed to boolean, and
parameter count potentially truncated for the guard).

Changes the type of the invocation, as if

MethodHandle.asType(MethodType)

was applied to its invocation
and its guard, if it has one (with return type changed to boolean for
guard).

Changes the type of the invocation, as if

LinkerServices.asType(MethodHandle, MethodType)

was applied to
its invocation and its guard, if it has one (with return type changed to
boolean, and parameter count potentially truncated for the guard).

Changes the type of the invocation, as if

LinkerServices.asTypeLosslessReturn(MethodHandle, MethodType)

was
applied to its invocation and

LinkerServices.asType(MethodHandle, MethodType)

applied to its
guard, if it has one (with return type changed to boolean, and parameter
count potentially truncated for the guard).

Composes the invocation, guard, switch points, and the exception into a
composite method handle that knows how to fall back when the guard fails
or the invocation is invalidated.

Makes an invocation that drops arguments in both the invocation and the
guard (if it exists and has at least

pos

parameters) with

MethodHandles.dropArguments(MethodHandle, int, Class...)

.

Makes an invocation that drops arguments in both the invocation and the
guard (if it exists and has at least

pos

parameters) with

MethodHandles.dropArguments(MethodHandle, int, List)

.

Applies argument filters to both the invocation and the guard
(if it exists and has at least

pos + 1

parameters) with

MethodHandles.filterArguments(MethodHandle, int, MethodHandle...)

.

Returns the exception type that if thrown by the invocation should
invalidate the linkage of this guarded invocation.

Returns the guard method handle.

Returns the invocation method handle.

Returns the switch points that can be used to invalidate the linkage of
this invocation handle.

Returns true if and only if this guarded invocation has at least one
invalidated switch point.

Creates a new guarded invocation with different methods, preserving the switch point.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation)
```

Creates a new unconditional guarded invocation. It is unconditional as it
has no invalidations.

**Parameters:** invocation

- the method handle representing the invocation. Must not
be null.
**Throws:** NullPointerException

- if invocation is null.

- GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation,

MethodHandle
guard)
```

Creates a new guarded invocation, with a guard method handle.

**Parameters:** invocation

- the method handle representing the invocation. Must not
be null.
**Parameters:** guard

- the method handle representing the guard. Must have be
compatible with the

invocation

handle as per

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

.
For some useful guards, check out the

Guards

class. It can be
null to represent an unconditional invocation.
**Throws:** NullPointerException

- if invocation is null.

- GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation,

SwitchPoint
switchPoint)
```

Creates a new guarded invocation that can be invalidated by a switch
point.

**Parameters:** invocation

- the method handle representing the invocation. Must
not be null.
**Parameters:** switchPoint

- the optional switch point that can be used to
invalidate this linkage. It can be null. If it is null, this represents
an unconditional invocation.
**Throws:** NullPointerException

- if invocation is null.

- GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation,

MethodHandle
guard,

SwitchPoint
switchPoint)
```

Creates a new guarded invocation, with both a guard method handle and a
switch point that can be used to invalidate it.

**Parameters:** invocation

- the method handle representing the invocation. Must
not be null.
**Parameters:** guard

- the method handle representing the guard. Must have be
compatible with the

invocation

handle as per

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

.
For some useful guards, check out the

Guards

class. It can be
null. If both it and the switch point are null, this represents an
unconditional invocation.
**Parameters:** switchPoint

- the optional switch point that can be used to
invalidate this linkage.
**Throws:** NullPointerException

- if invocation is null.

- GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation,

MethodHandle
guard,

SwitchPoint
switchPoint,

Class
<? extends
Throwable
> exception)
```

Creates a new guarded invocation, with a guard method handle, a
switch point that can be used to invalidate it, and an exception that if
thrown when invoked also invalidates it.

**Parameters:** invocation

- the method handle representing the invocation. Must not
be null.
**Parameters:** guard

- the method handle representing the guard. Must have be
compatible with the

invocation

handle as per

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

.
For some useful guards, check out the

Guards

class. It can be
null. If it and the switch point and the exception are all null, this
represents an unconditional invocation.
**Parameters:** switchPoint

- the optional switch point that can be used to
invalidate this linkage.
**Parameters:** exception

- the optional exception type that is when thrown by the
invocation also invalidates it.
**Throws:** NullPointerException

- if invocation is null.

- GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation,

MethodHandle
guard,

SwitchPoint
[] switchPoints,

Class
<? extends
Throwable
> exception)
```

Creates a new guarded invocation, with a guard method handle, any number
of switch points that can be used to invalidate it, and an exception that
if thrown when invoked also invalidates it.

**Parameters:** invocation

- the method handle representing the invocation. Must not
be null.
**Parameters:** guard

- the method handle representing the guard. Must have be
compatible with the

invocation

handle as per

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

.
For some useful guards, check out the

Guards

class. It can be
null. If it and the exception are both null, and no switch points were
specified, this represents an unconditional invocation.
**Parameters:** switchPoints

- optional switch points that can be used to
invalidate this linkage.
**Parameters:** exception

- the optional exception type that is when thrown by the
invocation also invalidates it.
**Throws:** NullPointerException

- if invocation is null.

============ METHOD DETAIL ==========

- Method Detail

- getInvocation

```java
public
MethodHandle
getInvocation()
```

Returns the invocation method handle.

**Returns:** the invocation method handle. It will never be null.

- getGuard

```java
public
MethodHandle
getGuard()
```

Returns the guard method handle.

**Returns:** the guard method handle. Can be null.

- getSwitchPoints

```java
public
SwitchPoint
[] getSwitchPoints()
```

Returns the switch points that can be used to invalidate the linkage of
this invocation handle.

**Returns:** the switch points that can be used to invalidate the linkage of
this invocation handle. Can be null.

- getException

```java
public
Class
<? extends
Throwable
> getException()
```

Returns the exception type that if thrown by the invocation should
invalidate the linkage of this guarded invocation.

**Returns:** the exception type that if thrown should be used to invalidate
the linkage. Can be null.

- hasBeenInvalidated

```java
public boolean hasBeenInvalidated()
```

Returns true if and only if this guarded invocation has at least one
invalidated switch point.

**Returns:** true if and only if this guarded invocation has at least one
invalidated switch point.

- replaceMethods

```java
public
GuardedInvocation
replaceMethods​(
MethodHandle
newInvocation,

MethodHandle
newGuard)
```

Creates a new guarded invocation with different methods, preserving the switch point.

**Parameters:** newInvocation

- the new invocation
**Parameters:** newGuard

- the new guard
**Returns:** a new guarded invocation with the replaced methods and the same switch point as this invocation.

- addSwitchPoint

```java
public
GuardedInvocation
addSwitchPoint​(
SwitchPoint
newSwitchPoint)
```

Create a new guarded invocation with an added switch point.

**Parameters:** newSwitchPoint

- new switch point. Can be null in which case this
method return the current guarded invocation with no changes.
**Returns:** a guarded invocation with the added switch point.

- asType

```java
public
GuardedInvocation
asType​(
MethodType
newType)
```

Changes the type of the invocation, as if

MethodHandle.asType(MethodType)

was applied to its invocation
and its guard, if it has one (with return type changed to boolean, and
parameter count potentially truncated for the guard). If the invocation
already is of the required type, returns this object.

**Parameters:** newType

- the new type of the invocation.
**Returns:** a guarded invocation with the new type applied to it.

- asType

```java
public
GuardedInvocation
asType​(
LinkerServices
linkerServices,

MethodType
newType)
```

Changes the type of the invocation, as if

LinkerServices.asType(MethodHandle, MethodType)

was applied to
its invocation and its guard, if it has one (with return type changed to
boolean, and parameter count potentially truncated for the guard). If the
invocation already is of the required type, returns this object.

**Parameters:** linkerServices

- the linker services to use for the conversion
**Parameters:** newType

- the new type of the invocation.
**Returns:** a guarded invocation with the new type applied to it.

- asTypeSafeReturn

```java
public
GuardedInvocation
asTypeSafeReturn​(
LinkerServices
linkerServices,

MethodType
newType)
```

Changes the type of the invocation, as if

LinkerServices.asTypeLosslessReturn(MethodHandle, MethodType)

was
applied to its invocation and

LinkerServices.asType(MethodHandle, MethodType)

applied to its
guard, if it has one (with return type changed to boolean, and parameter
count potentially truncated for the guard). If the invocation doesn't
change its type, returns this object.

**Parameters:** linkerServices

- the linker services to use for the conversion
**Parameters:** newType

- the new type of the invocation.
**Returns:** a guarded invocation with the new type applied to it.

- asType

```java
public
GuardedInvocation
asType​(
CallSiteDescriptor
desc)
```

Changes the type of the invocation, as if

MethodHandle.asType(MethodType)

was applied to its invocation
and its guard, if it has one (with return type changed to boolean for
guard). If the invocation already is of the required type, returns this
object.

**Parameters:** desc

- a call descriptor whose method type is adapted.
**Returns:** a guarded invocation with the new type applied to it.

- filterArguments

```java
public
GuardedInvocation
filterArguments​(int pos,

MethodHandle
... filters)
```

Applies argument filters to both the invocation and the guard
(if it exists and has at least

pos + 1

parameters) with

MethodHandles.filterArguments(MethodHandle, int, MethodHandle...)

.

**Parameters:** pos

- the position of the first argument being filtered
**Parameters:** filters

- the argument filters
**Returns:** a filtered invocation

- dropArguments

```java
public
GuardedInvocation
dropArguments​(int pos,

List
<
Class
<?>> valueTypes)
```

Makes an invocation that drops arguments in both the invocation and the
guard (if it exists and has at least

pos

parameters) with

MethodHandles.dropArguments(MethodHandle, int, List)

.

**Parameters:** pos

- the position of the first argument being dropped
**Parameters:** valueTypes

- the types of the values being dropped
**Returns:** an invocation that drops arguments

- dropArguments

```java
public
GuardedInvocation
dropArguments​(int pos,

Class
<?>... valueTypes)
```

Makes an invocation that drops arguments in both the invocation and the
guard (if it exists and has at least

pos

parameters) with

MethodHandles.dropArguments(MethodHandle, int, Class...)

.

**Parameters:** pos

- the position of the first argument being dropped
**Parameters:** valueTypes

- the types of the values being dropped
**Returns:** an invocation that drops arguments

- compose

```java
public
MethodHandle
compose​(
MethodHandle
fallback)
```

Composes the invocation, guard, switch points, and the exception into a
composite method handle that knows how to fall back when the guard fails
or the invocation is invalidated.

**Parameters:** fallback

- the fallback method handle for when a switch point is
invalidated, a guard returns false, or invalidating exception is thrown.
**Returns:** a composite method handle.

- compose

```java
public
MethodHandle
compose​(
MethodHandle
guardFallback,

MethodHandle
switchpointFallback,

MethodHandle
catchFallback)
```

Composes the invocation, guard, switch points, and the exception into a
composite method handle that knows how to fall back when the guard fails
or the invocation is invalidated.

**Parameters:** switchpointFallback

- the fallback method handle in case a switch
point is invalidated.
**Parameters:** guardFallback

- the fallback method handle in case guard returns
false.
**Parameters:** catchFallback

- the fallback method in case the exception handler
triggers.
**Returns:** a composite method handle.

Constructor Detail

- GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation)
```

Creates a new unconditional guarded invocation. It is unconditional as it
has no invalidations.

**Parameters:** invocation

- the method handle representing the invocation. Must not
be null.
**Throws:** NullPointerException

- if invocation is null.

- GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation,

MethodHandle
guard)
```

Creates a new guarded invocation, with a guard method handle.

**Parameters:** invocation

- the method handle representing the invocation. Must not
be null.
**Parameters:** guard

- the method handle representing the guard. Must have be
compatible with the

invocation

handle as per

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

.
For some useful guards, check out the

Guards

class. It can be
null to represent an unconditional invocation.
**Throws:** NullPointerException

- if invocation is null.

- GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation,

SwitchPoint
switchPoint)
```

Creates a new guarded invocation that can be invalidated by a switch
point.

**Parameters:** invocation

- the method handle representing the invocation. Must
not be null.
**Parameters:** switchPoint

- the optional switch point that can be used to
invalidate this linkage. It can be null. If it is null, this represents
an unconditional invocation.
**Throws:** NullPointerException

- if invocation is null.

- GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation,

MethodHandle
guard,

SwitchPoint
switchPoint)
```

Creates a new guarded invocation, with both a guard method handle and a
switch point that can be used to invalidate it.

**Parameters:** invocation

- the method handle representing the invocation. Must
not be null.
**Parameters:** guard

- the method handle representing the guard. Must have be
compatible with the

invocation

handle as per

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

.
For some useful guards, check out the

Guards

class. It can be
null. If both it and the switch point are null, this represents an
unconditional invocation.
**Parameters:** switchPoint

- the optional switch point that can be used to
invalidate this linkage.
**Throws:** NullPointerException

- if invocation is null.

- GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation,

MethodHandle
guard,

SwitchPoint
switchPoint,

Class
<? extends
Throwable
> exception)
```

Creates a new guarded invocation, with a guard method handle, a
switch point that can be used to invalidate it, and an exception that if
thrown when invoked also invalidates it.

**Parameters:** invocation

- the method handle representing the invocation. Must not
be null.
**Parameters:** guard

- the method handle representing the guard. Must have be
compatible with the

invocation

handle as per

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

.
For some useful guards, check out the

Guards

class. It can be
null. If it and the switch point and the exception are all null, this
represents an unconditional invocation.
**Parameters:** switchPoint

- the optional switch point that can be used to
invalidate this linkage.
**Parameters:** exception

- the optional exception type that is when thrown by the
invocation also invalidates it.
**Throws:** NullPointerException

- if invocation is null.

- GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation,

MethodHandle
guard,

SwitchPoint
[] switchPoints,

Class
<? extends
Throwable
> exception)
```

Creates a new guarded invocation, with a guard method handle, any number
of switch points that can be used to invalidate it, and an exception that
if thrown when invoked also invalidates it.

**Parameters:** invocation

- the method handle representing the invocation. Must not
be null.
**Parameters:** guard

- the method handle representing the guard. Must have be
compatible with the

invocation

handle as per

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

.
For some useful guards, check out the

Guards

class. It can be
null. If it and the exception are both null, and no switch points were
specified, this represents an unconditional invocation.
**Parameters:** switchPoints

- optional switch points that can be used to
invalidate this linkage.
**Parameters:** exception

- the optional exception type that is when thrown by the
invocation also invalidates it.
**Throws:** NullPointerException

- if invocation is null.

---

#### Constructor Detail

GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation)
```

Creates a new unconditional guarded invocation. It is unconditional as it
has no invalidations.

**Parameters:** invocation

- the method handle representing the invocation. Must not
be null.
**Throws:** NullPointerException

- if invocation is null.

---

#### GuardedInvocation

public GuardedInvocation​(

MethodHandle

invocation)

Creates a new unconditional guarded invocation. It is unconditional as it
has no invalidations.

GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation,

MethodHandle
guard)
```

Creates a new guarded invocation, with a guard method handle.

**Parameters:** invocation

- the method handle representing the invocation. Must not
be null.
**Parameters:** guard

- the method handle representing the guard. Must have be
compatible with the

invocation

handle as per

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

.
For some useful guards, check out the

Guards

class. It can be
null to represent an unconditional invocation.
**Throws:** NullPointerException

- if invocation is null.

---

#### GuardedInvocation

public GuardedInvocation​(

MethodHandle

invocation,

MethodHandle

guard)

Creates a new guarded invocation, with a guard method handle.

GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation,

SwitchPoint
switchPoint)
```

Creates a new guarded invocation that can be invalidated by a switch
point.

**Parameters:** invocation

- the method handle representing the invocation. Must
not be null.
**Parameters:** switchPoint

- the optional switch point that can be used to
invalidate this linkage. It can be null. If it is null, this represents
an unconditional invocation.
**Throws:** NullPointerException

- if invocation is null.

---

#### GuardedInvocation

public GuardedInvocation​(

MethodHandle

invocation,

SwitchPoint

switchPoint)

Creates a new guarded invocation that can be invalidated by a switch
point.

GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation,

MethodHandle
guard,

SwitchPoint
switchPoint)
```

Creates a new guarded invocation, with both a guard method handle and a
switch point that can be used to invalidate it.

**Parameters:** invocation

- the method handle representing the invocation. Must
not be null.
**Parameters:** guard

- the method handle representing the guard. Must have be
compatible with the

invocation

handle as per

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

.
For some useful guards, check out the

Guards

class. It can be
null. If both it and the switch point are null, this represents an
unconditional invocation.
**Parameters:** switchPoint

- the optional switch point that can be used to
invalidate this linkage.
**Throws:** NullPointerException

- if invocation is null.

---

#### GuardedInvocation

public GuardedInvocation​(

MethodHandle

invocation,

MethodHandle

guard,

SwitchPoint

switchPoint)

Creates a new guarded invocation, with both a guard method handle and a
switch point that can be used to invalidate it.

GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation,

MethodHandle
guard,

SwitchPoint
switchPoint,

Class
<? extends
Throwable
> exception)
```

Creates a new guarded invocation, with a guard method handle, a
switch point that can be used to invalidate it, and an exception that if
thrown when invoked also invalidates it.

**Parameters:** invocation

- the method handle representing the invocation. Must not
be null.
**Parameters:** guard

- the method handle representing the guard. Must have be
compatible with the

invocation

handle as per

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

.
For some useful guards, check out the

Guards

class. It can be
null. If it and the switch point and the exception are all null, this
represents an unconditional invocation.
**Parameters:** switchPoint

- the optional switch point that can be used to
invalidate this linkage.
**Parameters:** exception

- the optional exception type that is when thrown by the
invocation also invalidates it.
**Throws:** NullPointerException

- if invocation is null.

---

#### GuardedInvocation

public GuardedInvocation​(

MethodHandle

invocation,

MethodHandle

guard,

SwitchPoint

switchPoint,

Class

<? extends

Throwable

> exception)

Creates a new guarded invocation, with a guard method handle, a
switch point that can be used to invalidate it, and an exception that if
thrown when invoked also invalidates it.

GuardedInvocation

```java
public GuardedInvocation​(
MethodHandle
invocation,

MethodHandle
guard,

SwitchPoint
[] switchPoints,

Class
<? extends
Throwable
> exception)
```

Creates a new guarded invocation, with a guard method handle, any number
of switch points that can be used to invalidate it, and an exception that
if thrown when invoked also invalidates it.

**Parameters:** invocation

- the method handle representing the invocation. Must not
be null.
**Parameters:** guard

- the method handle representing the guard. Must have be
compatible with the

invocation

handle as per

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

.
For some useful guards, check out the

Guards

class. It can be
null. If it and the exception are both null, and no switch points were
specified, this represents an unconditional invocation.
**Parameters:** switchPoints

- optional switch points that can be used to
invalidate this linkage.
**Parameters:** exception

- the optional exception type that is when thrown by the
invocation also invalidates it.
**Throws:** NullPointerException

- if invocation is null.

---

#### GuardedInvocation

public GuardedInvocation​(

MethodHandle

invocation,

MethodHandle

guard,

SwitchPoint

[] switchPoints,

Class

<? extends

Throwable

> exception)

Creates a new guarded invocation, with a guard method handle, any number
of switch points that can be used to invalidate it, and an exception that
if thrown when invoked also invalidates it.

Method Detail

- getInvocation

```java
public
MethodHandle
getInvocation()
```

Returns the invocation method handle.

**Returns:** the invocation method handle. It will never be null.

- getGuard

```java
public
MethodHandle
getGuard()
```

Returns the guard method handle.

**Returns:** the guard method handle. Can be null.

- getSwitchPoints

```java
public
SwitchPoint
[] getSwitchPoints()
```

Returns the switch points that can be used to invalidate the linkage of
this invocation handle.

**Returns:** the switch points that can be used to invalidate the linkage of
this invocation handle. Can be null.

- getException

```java
public
Class
<? extends
Throwable
> getException()
```

Returns the exception type that if thrown by the invocation should
invalidate the linkage of this guarded invocation.

**Returns:** the exception type that if thrown should be used to invalidate
the linkage. Can be null.

- hasBeenInvalidated

```java
public boolean hasBeenInvalidated()
```

Returns true if and only if this guarded invocation has at least one
invalidated switch point.

**Returns:** true if and only if this guarded invocation has at least one
invalidated switch point.

- replaceMethods

```java
public
GuardedInvocation
replaceMethods​(
MethodHandle
newInvocation,

MethodHandle
newGuard)
```

Creates a new guarded invocation with different methods, preserving the switch point.

**Parameters:** newInvocation

- the new invocation
**Parameters:** newGuard

- the new guard
**Returns:** a new guarded invocation with the replaced methods and the same switch point as this invocation.

- addSwitchPoint

```java
public
GuardedInvocation
addSwitchPoint​(
SwitchPoint
newSwitchPoint)
```

Create a new guarded invocation with an added switch point.

**Parameters:** newSwitchPoint

- new switch point. Can be null in which case this
method return the current guarded invocation with no changes.
**Returns:** a guarded invocation with the added switch point.

- asType

```java
public
GuardedInvocation
asType​(
MethodType
newType)
```

Changes the type of the invocation, as if

MethodHandle.asType(MethodType)

was applied to its invocation
and its guard, if it has one (with return type changed to boolean, and
parameter count potentially truncated for the guard). If the invocation
already is of the required type, returns this object.

**Parameters:** newType

- the new type of the invocation.
**Returns:** a guarded invocation with the new type applied to it.

- asType

```java
public
GuardedInvocation
asType​(
LinkerServices
linkerServices,

MethodType
newType)
```

Changes the type of the invocation, as if

LinkerServices.asType(MethodHandle, MethodType)

was applied to
its invocation and its guard, if it has one (with return type changed to
boolean, and parameter count potentially truncated for the guard). If the
invocation already is of the required type, returns this object.

**Parameters:** linkerServices

- the linker services to use for the conversion
**Parameters:** newType

- the new type of the invocation.
**Returns:** a guarded invocation with the new type applied to it.

- asTypeSafeReturn

```java
public
GuardedInvocation
asTypeSafeReturn​(
LinkerServices
linkerServices,

MethodType
newType)
```

Changes the type of the invocation, as if

LinkerServices.asTypeLosslessReturn(MethodHandle, MethodType)

was
applied to its invocation and

LinkerServices.asType(MethodHandle, MethodType)

applied to its
guard, if it has one (with return type changed to boolean, and parameter
count potentially truncated for the guard). If the invocation doesn't
change its type, returns this object.

**Parameters:** linkerServices

- the linker services to use for the conversion
**Parameters:** newType

- the new type of the invocation.
**Returns:** a guarded invocation with the new type applied to it.

- asType

```java
public
GuardedInvocation
asType​(
CallSiteDescriptor
desc)
```

Changes the type of the invocation, as if

MethodHandle.asType(MethodType)

was applied to its invocation
and its guard, if it has one (with return type changed to boolean for
guard). If the invocation already is of the required type, returns this
object.

**Parameters:** desc

- a call descriptor whose method type is adapted.
**Returns:** a guarded invocation with the new type applied to it.

- filterArguments

```java
public
GuardedInvocation
filterArguments​(int pos,

MethodHandle
... filters)
```

Applies argument filters to both the invocation and the guard
(if it exists and has at least

pos + 1

parameters) with

MethodHandles.filterArguments(MethodHandle, int, MethodHandle...)

.

**Parameters:** pos

- the position of the first argument being filtered
**Parameters:** filters

- the argument filters
**Returns:** a filtered invocation

- dropArguments

```java
public
GuardedInvocation
dropArguments​(int pos,

List
<
Class
<?>> valueTypes)
```

Makes an invocation that drops arguments in both the invocation and the
guard (if it exists and has at least

pos

parameters) with

MethodHandles.dropArguments(MethodHandle, int, List)

.

**Parameters:** pos

- the position of the first argument being dropped
**Parameters:** valueTypes

- the types of the values being dropped
**Returns:** an invocation that drops arguments

- dropArguments

```java
public
GuardedInvocation
dropArguments​(int pos,

Class
<?>... valueTypes)
```

Makes an invocation that drops arguments in both the invocation and the
guard (if it exists and has at least

pos

parameters) with

MethodHandles.dropArguments(MethodHandle, int, Class...)

.

**Parameters:** pos

- the position of the first argument being dropped
**Parameters:** valueTypes

- the types of the values being dropped
**Returns:** an invocation that drops arguments

- compose

```java
public
MethodHandle
compose​(
MethodHandle
fallback)
```

Composes the invocation, guard, switch points, and the exception into a
composite method handle that knows how to fall back when the guard fails
or the invocation is invalidated.

**Parameters:** fallback

- the fallback method handle for when a switch point is
invalidated, a guard returns false, or invalidating exception is thrown.
**Returns:** a composite method handle.

- compose

```java
public
MethodHandle
compose​(
MethodHandle
guardFallback,

MethodHandle
switchpointFallback,

MethodHandle
catchFallback)
```

Composes the invocation, guard, switch points, and the exception into a
composite method handle that knows how to fall back when the guard fails
or the invocation is invalidated.

**Parameters:** switchpointFallback

- the fallback method handle in case a switch
point is invalidated.
**Parameters:** guardFallback

- the fallback method handle in case guard returns
false.
**Parameters:** catchFallback

- the fallback method in case the exception handler
triggers.
**Returns:** a composite method handle.

---

#### Method Detail

getInvocation

```java
public
MethodHandle
getInvocation()
```

Returns the invocation method handle.

**Returns:** the invocation method handle. It will never be null.

---

#### getInvocation

public

MethodHandle

getInvocation()

Returns the invocation method handle.

getGuard

```java
public
MethodHandle
getGuard()
```

Returns the guard method handle.

**Returns:** the guard method handle. Can be null.

---

#### getGuard

public

MethodHandle

getGuard()

Returns the guard method handle.

getSwitchPoints

```java
public
SwitchPoint
[] getSwitchPoints()
```

Returns the switch points that can be used to invalidate the linkage of
this invocation handle.

**Returns:** the switch points that can be used to invalidate the linkage of
this invocation handle. Can be null.

---

#### getSwitchPoints

public

SwitchPoint

[] getSwitchPoints()

Returns the switch points that can be used to invalidate the linkage of
this invocation handle.

getException

```java
public
Class
<? extends
Throwable
> getException()
```

Returns the exception type that if thrown by the invocation should
invalidate the linkage of this guarded invocation.

**Returns:** the exception type that if thrown should be used to invalidate
the linkage. Can be null.

---

#### getException

public

Class

<? extends

Throwable

> getException()

Returns the exception type that if thrown by the invocation should
invalidate the linkage of this guarded invocation.

hasBeenInvalidated

```java
public boolean hasBeenInvalidated()
```

Returns true if and only if this guarded invocation has at least one
invalidated switch point.

**Returns:** true if and only if this guarded invocation has at least one
invalidated switch point.

---

#### hasBeenInvalidated

public boolean hasBeenInvalidated()

Returns true if and only if this guarded invocation has at least one
invalidated switch point.

replaceMethods

```java
public
GuardedInvocation
replaceMethods​(
MethodHandle
newInvocation,

MethodHandle
newGuard)
```

Creates a new guarded invocation with different methods, preserving the switch point.

**Parameters:** newInvocation

- the new invocation
**Parameters:** newGuard

- the new guard
**Returns:** a new guarded invocation with the replaced methods and the same switch point as this invocation.

---

#### replaceMethods

public

GuardedInvocation

replaceMethods​(

MethodHandle

newInvocation,

MethodHandle

newGuard)

Creates a new guarded invocation with different methods, preserving the switch point.

addSwitchPoint

```java
public
GuardedInvocation
addSwitchPoint​(
SwitchPoint
newSwitchPoint)
```

Create a new guarded invocation with an added switch point.

**Parameters:** newSwitchPoint

- new switch point. Can be null in which case this
method return the current guarded invocation with no changes.
**Returns:** a guarded invocation with the added switch point.

---

#### addSwitchPoint

public

GuardedInvocation

addSwitchPoint​(

SwitchPoint

newSwitchPoint)

Create a new guarded invocation with an added switch point.

asType

```java
public
GuardedInvocation
asType​(
MethodType
newType)
```

Changes the type of the invocation, as if

MethodHandle.asType(MethodType)

was applied to its invocation
and its guard, if it has one (with return type changed to boolean, and
parameter count potentially truncated for the guard). If the invocation
already is of the required type, returns this object.

**Parameters:** newType

- the new type of the invocation.
**Returns:** a guarded invocation with the new type applied to it.

---

#### asType

public

GuardedInvocation

asType​(

MethodType

newType)

Changes the type of the invocation, as if

MethodHandle.asType(MethodType)

was applied to its invocation
and its guard, if it has one (with return type changed to boolean, and
parameter count potentially truncated for the guard). If the invocation
already is of the required type, returns this object.

asType

```java
public
GuardedInvocation
asType​(
LinkerServices
linkerServices,

MethodType
newType)
```

Changes the type of the invocation, as if

LinkerServices.asType(MethodHandle, MethodType)

was applied to
its invocation and its guard, if it has one (with return type changed to
boolean, and parameter count potentially truncated for the guard). If the
invocation already is of the required type, returns this object.

**Parameters:** linkerServices

- the linker services to use for the conversion
**Parameters:** newType

- the new type of the invocation.
**Returns:** a guarded invocation with the new type applied to it.

---

#### asType

public

GuardedInvocation

asType​(

LinkerServices

linkerServices,

MethodType

newType)

Changes the type of the invocation, as if

LinkerServices.asType(MethodHandle, MethodType)

was applied to
its invocation and its guard, if it has one (with return type changed to
boolean, and parameter count potentially truncated for the guard). If the
invocation already is of the required type, returns this object.

asTypeSafeReturn

```java
public
GuardedInvocation
asTypeSafeReturn​(
LinkerServices
linkerServices,

MethodType
newType)
```

Changes the type of the invocation, as if

LinkerServices.asTypeLosslessReturn(MethodHandle, MethodType)

was
applied to its invocation and

LinkerServices.asType(MethodHandle, MethodType)

applied to its
guard, if it has one (with return type changed to boolean, and parameter
count potentially truncated for the guard). If the invocation doesn't
change its type, returns this object.

**Parameters:** linkerServices

- the linker services to use for the conversion
**Parameters:** newType

- the new type of the invocation.
**Returns:** a guarded invocation with the new type applied to it.

---

#### asTypeSafeReturn

public

GuardedInvocation

asTypeSafeReturn​(

LinkerServices

linkerServices,

MethodType

newType)

Changes the type of the invocation, as if

LinkerServices.asTypeLosslessReturn(MethodHandle, MethodType)

was
applied to its invocation and

LinkerServices.asType(MethodHandle, MethodType)

applied to its
guard, if it has one (with return type changed to boolean, and parameter
count potentially truncated for the guard). If the invocation doesn't
change its type, returns this object.

asType

```java
public
GuardedInvocation
asType​(
CallSiteDescriptor
desc)
```

Changes the type of the invocation, as if

MethodHandle.asType(MethodType)

was applied to its invocation
and its guard, if it has one (with return type changed to boolean for
guard). If the invocation already is of the required type, returns this
object.

**Parameters:** desc

- a call descriptor whose method type is adapted.
**Returns:** a guarded invocation with the new type applied to it.

---

#### asType

public

GuardedInvocation

asType​(

CallSiteDescriptor

desc)

Changes the type of the invocation, as if

MethodHandle.asType(MethodType)

was applied to its invocation
and its guard, if it has one (with return type changed to boolean for
guard). If the invocation already is of the required type, returns this
object.

filterArguments

```java
public
GuardedInvocation
filterArguments​(int pos,

MethodHandle
... filters)
```

Applies argument filters to both the invocation and the guard
(if it exists and has at least

pos + 1

parameters) with

MethodHandles.filterArguments(MethodHandle, int, MethodHandle...)

.

**Parameters:** pos

- the position of the first argument being filtered
**Parameters:** filters

- the argument filters
**Returns:** a filtered invocation

---

#### filterArguments

public

GuardedInvocation

filterArguments​(int pos,

MethodHandle

... filters)

Applies argument filters to both the invocation and the guard
(if it exists and has at least

pos + 1

parameters) with

MethodHandles.filterArguments(MethodHandle, int, MethodHandle...)

.

dropArguments

```java
public
GuardedInvocation
dropArguments​(int pos,

List
<
Class
<?>> valueTypes)
```

Makes an invocation that drops arguments in both the invocation and the
guard (if it exists and has at least

pos

parameters) with

MethodHandles.dropArguments(MethodHandle, int, List)

.

**Parameters:** pos

- the position of the first argument being dropped
**Parameters:** valueTypes

- the types of the values being dropped
**Returns:** an invocation that drops arguments

---

#### dropArguments

public

GuardedInvocation

dropArguments​(int pos,

List

<

Class

<?>> valueTypes)

Makes an invocation that drops arguments in both the invocation and the
guard (if it exists and has at least

pos

parameters) with

MethodHandles.dropArguments(MethodHandle, int, List)

.

dropArguments

```java
public
GuardedInvocation
dropArguments​(int pos,

Class
<?>... valueTypes)
```

Makes an invocation that drops arguments in both the invocation and the
guard (if it exists and has at least

pos

parameters) with

MethodHandles.dropArguments(MethodHandle, int, Class...)

.

**Parameters:** pos

- the position of the first argument being dropped
**Parameters:** valueTypes

- the types of the values being dropped
**Returns:** an invocation that drops arguments

---

#### dropArguments

public

GuardedInvocation

dropArguments​(int pos,

Class

<?>... valueTypes)

Makes an invocation that drops arguments in both the invocation and the
guard (if it exists and has at least

pos

parameters) with

MethodHandles.dropArguments(MethodHandle, int, Class...)

.

compose

```java
public
MethodHandle
compose​(
MethodHandle
fallback)
```

Composes the invocation, guard, switch points, and the exception into a
composite method handle that knows how to fall back when the guard fails
or the invocation is invalidated.

**Parameters:** fallback

- the fallback method handle for when a switch point is
invalidated, a guard returns false, or invalidating exception is thrown.
**Returns:** a composite method handle.

---

#### compose

public

MethodHandle

compose​(

MethodHandle

fallback)

Composes the invocation, guard, switch points, and the exception into a
composite method handle that knows how to fall back when the guard fails
or the invocation is invalidated.

compose

```java
public
MethodHandle
compose​(
MethodHandle
guardFallback,

MethodHandle
switchpointFallback,

MethodHandle
catchFallback)
```

Composes the invocation, guard, switch points, and the exception into a
composite method handle that knows how to fall back when the guard fails
or the invocation is invalidated.

**Parameters:** switchpointFallback

- the fallback method handle in case a switch
point is invalidated.
**Parameters:** guardFallback

- the fallback method handle in case guard returns
false.
**Parameters:** catchFallback

- the fallback method in case the exception handler
triggers.
**Returns:** a composite method handle.

---

#### compose

public

MethodHandle

compose​(

MethodHandle

guardFallback,

MethodHandle

switchpointFallback,

MethodHandle

catchFallback)

Composes the invocation, guard, switch points, and the exception into a
composite method handle that knows how to fall back when the guard fails
or the invocation is invalidated.

---

