# Class ConstantCallSite

**Source:** `java.base\java\lang\invoke\ConstantCallSite.html`

### Class Description

```java
public class
ConstantCallSite

extends
CallSite
```

A

ConstantCallSite

is a

CallSite

whose target is permanent, and can never be changed.
An

invokedynamic

instruction linked to a

ConstantCallSite

is permanently
bound to the call site's target.

**Since:** 1.7

---

### Field Details

*No entries found.*

### Constructor Details

#### public ConstantCallSite​(
MethodHandle
target)

Creates a call site with a permanent target.

**Parameters:**
- target

- the target to be permanently associated with this call site

**Throws:**
- NullPointerException

- if the proposed target is null

---

#### protected ConstantCallSite​(
MethodType
targetType,

MethodHandle
createTargetHook)
throws
Throwable

Creates a call site with a permanent target, possibly bound to the call site itself.

During construction of the call site, the

createTargetHook

is invoked to
produce the actual target, as if by a call of the form

(MethodHandle) createTargetHook.invoke(this)

.

Note that user code cannot perform such an action directly in a subclass constructor,
since the target must be fixed before the

ConstantCallSite

constructor returns.

The hook is said to bind the call site to a target method handle,
and a typical action would be

someTarget.bindTo(this)

.
However, the hook is free to take any action whatever,
including ignoring the call site and returning a constant target.

The result returned by the hook must be a method handle of exactly
the same type as the call site.

While the hook is being called, the new

ConstantCallSite

object is in a partially constructed state.
In this state,
a call to

getTarget

, or any other attempt to use the target,
will result in an

IllegalStateException

.
It is legal at all times to obtain the call site's type using the

type

method.

**Parameters:**
- targetType

- the type of the method handle to be permanently associated with this call site
- createTargetHook

- a method handle to invoke (on the call site) to produce the call site's target

**Throws:**
- WrongMethodTypeException

- if the hook cannot be invoked on the required arguments,
or if the target returned by the hook is not of the given

targetType
- NullPointerException

- if the hook returns a null value
- ClassCastException

- if the hook returns something other than a

MethodHandle
- Throwable

- anything else thrown by the hook function

---

### Method Details

#### public final
MethodHandle
getTarget()

Returns the target method of the call site, which behaves
like a

final

field of the

ConstantCallSite

.
That is, the target is always the original value passed
to the constructor call which created this instance.

**Specified by:**
- getTarget

in class

CallSite

**Returns:**
- the immutable linkage state of this call site, a constant method handle

**Throws:**
- IllegalStateException

- if the

ConstantCallSite

constructor has not completed

**See Also:**
- ConstantCallSite

,

VolatileCallSite

,

CallSite.setTarget(java.lang.invoke.MethodHandle)

,

getTarget()

,

MutableCallSite.getTarget()

,

VolatileCallSite.getTarget()

---

#### public final void setTarget​(
MethodHandle
ignore)

Always throws an

UnsupportedOperationException

.
This kind of call site cannot change its target.

**Specified by:**
- setTarget

in class

CallSite

**Parameters:**
- ignore

- a new target proposed for the call site, which is ignored

**Throws:**
- UnsupportedOperationException

- because this kind of call site cannot change its target

**See Also:**
- CallSite.getTarget()

,

setTarget(java.lang.invoke.MethodHandle)

,

MutableCallSite.setTarget(java.lang.invoke.MethodHandle)

,

VolatileCallSite.setTarget(java.lang.invoke.MethodHandle)

---

#### public final
MethodHandle
dynamicInvoker()

Returns this call site's permanent target.
Since that target will never change, this is a correct implementation
of

CallSite.dynamicInvoker

.

**Specified by:**
- dynamicInvoker

in class

CallSite

**Returns:**
- the immutable linkage state of this call site, a constant method handle

**Throws:**
- IllegalStateException

- if the

ConstantCallSite

constructor has not completed

---

### Additional Sections

#### Class ConstantCallSite

java.lang.Object

- java.lang.invoke.CallSite
- - java.lang.invoke.ConstantCallSite

java.lang.invoke.CallSite

- java.lang.invoke.ConstantCallSite

java.lang.invoke.ConstantCallSite

```java
public class
ConstantCallSite

extends
CallSite
```

A

ConstantCallSite

is a

CallSite

whose target is permanent, and can never be changed.
An

invokedynamic

instruction linked to a

ConstantCallSite

is permanently
bound to the call site's target.

**Since:** 1.7

public class

ConstantCallSite

extends

CallSite

A

ConstantCallSite

is a

CallSite

whose target is permanent, and can never be changed.
An

invokedynamic

instruction linked to a

ConstantCallSite

is permanently
bound to the call site's target.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

ConstantCallSite

​(

MethodHandle

target)

Creates a call site with a permanent target.

protected

ConstantCallSite

​(

MethodType

targetType,

MethodHandle

createTargetHook)

Creates a call site with a permanent target, possibly bound to the call site itself.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MethodHandle

dynamicInvoker

()

Returns this call site's permanent target.

MethodHandle

getTarget

()

Returns the target method of the call site, which behaves
like a

final

field of the

ConstantCallSite

.

void

setTarget

​(

MethodHandle

ignore)

Always throws an

UnsupportedOperationException

.

- Methods declared in class java.lang.invoke.

CallSite

type

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

Modifier

Constructor

Description

ConstantCallSite

​(

MethodHandle

target)

Creates a call site with a permanent target.

protected

ConstantCallSite

​(

MethodType

targetType,

MethodHandle

createTargetHook)

Creates a call site with a permanent target, possibly bound to the call site itself.

---

#### Constructor Summary

Creates a call site with a permanent target.

Creates a call site with a permanent target, possibly bound to the call site itself.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MethodHandle

dynamicInvoker

()

Returns this call site's permanent target.

MethodHandle

getTarget

()

Returns the target method of the call site, which behaves
like a

final

field of the

ConstantCallSite

.

void

setTarget

​(

MethodHandle

ignore)

Always throws an

UnsupportedOperationException

.

- Methods declared in class java.lang.invoke.

CallSite

type

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

Returns this call site's permanent target.

Returns the target method of the call site, which behaves
like a

final

field of the

ConstantCallSite

.

Always throws an

UnsupportedOperationException

.

Methods declared in class java.lang.invoke.

CallSite

type

---

#### Methods declared in class java.lang.invoke. CallSite

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

- ConstantCallSite

```java
public ConstantCallSite​(
MethodHandle
target)
```

Creates a call site with a permanent target.

**Parameters:** target

- the target to be permanently associated with this call site
**Throws:** NullPointerException

- if the proposed target is null

- ConstantCallSite

```java
protected ConstantCallSite​(
MethodType
targetType,

MethodHandle
createTargetHook)
throws
Throwable
```

Creates a call site with a permanent target, possibly bound to the call site itself.

During construction of the call site, the

createTargetHook

is invoked to
produce the actual target, as if by a call of the form

(MethodHandle) createTargetHook.invoke(this)

.

Note that user code cannot perform such an action directly in a subclass constructor,
since the target must be fixed before the

ConstantCallSite

constructor returns.

The hook is said to bind the call site to a target method handle,
and a typical action would be

someTarget.bindTo(this)

.
However, the hook is free to take any action whatever,
including ignoring the call site and returning a constant target.

The result returned by the hook must be a method handle of exactly
the same type as the call site.

While the hook is being called, the new

ConstantCallSite

object is in a partially constructed state.
In this state,
a call to

getTarget

, or any other attempt to use the target,
will result in an

IllegalStateException

.
It is legal at all times to obtain the call site's type using the

type

method.

**Parameters:** targetType

- the type of the method handle to be permanently associated with this call site
**Parameters:** createTargetHook

- a method handle to invoke (on the call site) to produce the call site's target
**Throws:** WrongMethodTypeException

- if the hook cannot be invoked on the required arguments,
or if the target returned by the hook is not of the given

targetType
**Throws:** NullPointerException

- if the hook returns a null value
**Throws:** ClassCastException

- if the hook returns something other than a

MethodHandle
**Throws:** Throwable

- anything else thrown by the hook function

============ METHOD DETAIL ==========

- Method Detail

- getTarget

```java
public final
MethodHandle
getTarget()
```

Returns the target method of the call site, which behaves
like a

final

field of the

ConstantCallSite

.
That is, the target is always the original value passed
to the constructor call which created this instance.

**Specified by:** getTarget

in class

CallSite
**Returns:** the immutable linkage state of this call site, a constant method handle
**Throws:** IllegalStateException

- if the

ConstantCallSite

constructor has not completed
**See Also:** ConstantCallSite

,

VolatileCallSite

,

CallSite.setTarget(java.lang.invoke.MethodHandle)

,

getTarget()

,

MutableCallSite.getTarget()

,

VolatileCallSite.getTarget()

- setTarget

```java
public final void setTarget​(
MethodHandle
ignore)
```

Always throws an

UnsupportedOperationException

.
This kind of call site cannot change its target.

**Specified by:** setTarget

in class

CallSite
**Parameters:** ignore

- a new target proposed for the call site, which is ignored
**Throws:** UnsupportedOperationException

- because this kind of call site cannot change its target
**See Also:** CallSite.getTarget()

,

setTarget(java.lang.invoke.MethodHandle)

,

MutableCallSite.setTarget(java.lang.invoke.MethodHandle)

,

VolatileCallSite.setTarget(java.lang.invoke.MethodHandle)

- dynamicInvoker

```java
public final
MethodHandle
dynamicInvoker()
```

Returns this call site's permanent target.
Since that target will never change, this is a correct implementation
of

CallSite.dynamicInvoker

.

**Specified by:** dynamicInvoker

in class

CallSite
**Returns:** the immutable linkage state of this call site, a constant method handle
**Throws:** IllegalStateException

- if the

ConstantCallSite

constructor has not completed

Constructor Detail

- ConstantCallSite

```java
public ConstantCallSite​(
MethodHandle
target)
```

Creates a call site with a permanent target.

**Parameters:** target

- the target to be permanently associated with this call site
**Throws:** NullPointerException

- if the proposed target is null

- ConstantCallSite

```java
protected ConstantCallSite​(
MethodType
targetType,

MethodHandle
createTargetHook)
throws
Throwable
```

Creates a call site with a permanent target, possibly bound to the call site itself.

During construction of the call site, the

createTargetHook

is invoked to
produce the actual target, as if by a call of the form

(MethodHandle) createTargetHook.invoke(this)

.

Note that user code cannot perform such an action directly in a subclass constructor,
since the target must be fixed before the

ConstantCallSite

constructor returns.

The hook is said to bind the call site to a target method handle,
and a typical action would be

someTarget.bindTo(this)

.
However, the hook is free to take any action whatever,
including ignoring the call site and returning a constant target.

The result returned by the hook must be a method handle of exactly
the same type as the call site.

While the hook is being called, the new

ConstantCallSite

object is in a partially constructed state.
In this state,
a call to

getTarget

, or any other attempt to use the target,
will result in an

IllegalStateException

.
It is legal at all times to obtain the call site's type using the

type

method.

**Parameters:** targetType

- the type of the method handle to be permanently associated with this call site
**Parameters:** createTargetHook

- a method handle to invoke (on the call site) to produce the call site's target
**Throws:** WrongMethodTypeException

- if the hook cannot be invoked on the required arguments,
or if the target returned by the hook is not of the given

targetType
**Throws:** NullPointerException

- if the hook returns a null value
**Throws:** ClassCastException

- if the hook returns something other than a

MethodHandle
**Throws:** Throwable

- anything else thrown by the hook function

---

#### Constructor Detail

ConstantCallSite

```java
public ConstantCallSite​(
MethodHandle
target)
```

Creates a call site with a permanent target.

**Parameters:** target

- the target to be permanently associated with this call site
**Throws:** NullPointerException

- if the proposed target is null

---

#### ConstantCallSite

public ConstantCallSite​(

MethodHandle

target)

Creates a call site with a permanent target.

ConstantCallSite

```java
protected ConstantCallSite​(
MethodType
targetType,

MethodHandle
createTargetHook)
throws
Throwable
```

Creates a call site with a permanent target, possibly bound to the call site itself.

During construction of the call site, the

createTargetHook

is invoked to
produce the actual target, as if by a call of the form

(MethodHandle) createTargetHook.invoke(this)

.

Note that user code cannot perform such an action directly in a subclass constructor,
since the target must be fixed before the

ConstantCallSite

constructor returns.

The hook is said to bind the call site to a target method handle,
and a typical action would be

someTarget.bindTo(this)

.
However, the hook is free to take any action whatever,
including ignoring the call site and returning a constant target.

The result returned by the hook must be a method handle of exactly
the same type as the call site.

While the hook is being called, the new

ConstantCallSite

object is in a partially constructed state.
In this state,
a call to

getTarget

, or any other attempt to use the target,
will result in an

IllegalStateException

.
It is legal at all times to obtain the call site's type using the

type

method.

**Parameters:** targetType

- the type of the method handle to be permanently associated with this call site
**Parameters:** createTargetHook

- a method handle to invoke (on the call site) to produce the call site's target
**Throws:** WrongMethodTypeException

- if the hook cannot be invoked on the required arguments,
or if the target returned by the hook is not of the given

targetType
**Throws:** NullPointerException

- if the hook returns a null value
**Throws:** ClassCastException

- if the hook returns something other than a

MethodHandle
**Throws:** Throwable

- anything else thrown by the hook function

---

#### ConstantCallSite

protected ConstantCallSite​(

MethodType

targetType,

MethodHandle

createTargetHook)
throws

Throwable

Creates a call site with a permanent target, possibly bound to the call site itself.

During construction of the call site, the

createTargetHook

is invoked to
produce the actual target, as if by a call of the form

(MethodHandle) createTargetHook.invoke(this)

.

Note that user code cannot perform such an action directly in a subclass constructor,
since the target must be fixed before the

ConstantCallSite

constructor returns.

The hook is said to bind the call site to a target method handle,
and a typical action would be

someTarget.bindTo(this)

.
However, the hook is free to take any action whatever,
including ignoring the call site and returning a constant target.

The result returned by the hook must be a method handle of exactly
the same type as the call site.

While the hook is being called, the new

ConstantCallSite

object is in a partially constructed state.
In this state,
a call to

getTarget

, or any other attempt to use the target,
will result in an

IllegalStateException

.
It is legal at all times to obtain the call site's type using the

type

method.

During construction of the call site, the

createTargetHook

is invoked to
produce the actual target, as if by a call of the form

(MethodHandle) createTargetHook.invoke(this)

.

Note that user code cannot perform such an action directly in a subclass constructor,
since the target must be fixed before the

ConstantCallSite

constructor returns.

The hook is said to bind the call site to a target method handle,
and a typical action would be

someTarget.bindTo(this)

.
However, the hook is free to take any action whatever,
including ignoring the call site and returning a constant target.

The result returned by the hook must be a method handle of exactly
the same type as the call site.

While the hook is being called, the new

ConstantCallSite

object is in a partially constructed state.
In this state,
a call to

getTarget

, or any other attempt to use the target,
will result in an

IllegalStateException

.
It is legal at all times to obtain the call site's type using the

type

method.

Note that user code cannot perform such an action directly in a subclass constructor,
since the target must be fixed before the

ConstantCallSite

constructor returns.

The hook is said to bind the call site to a target method handle,
and a typical action would be

someTarget.bindTo(this)

.
However, the hook is free to take any action whatever,
including ignoring the call site and returning a constant target.

The result returned by the hook must be a method handle of exactly
the same type as the call site.

While the hook is being called, the new

ConstantCallSite

object is in a partially constructed state.
In this state,
a call to

getTarget

, or any other attempt to use the target,
will result in an

IllegalStateException

.
It is legal at all times to obtain the call site's type using the

type

method.

The hook is said to bind the call site to a target method handle,
and a typical action would be

someTarget.bindTo(this)

.
However, the hook is free to take any action whatever,
including ignoring the call site and returning a constant target.

The result returned by the hook must be a method handle of exactly
the same type as the call site.

While the hook is being called, the new

ConstantCallSite

object is in a partially constructed state.
In this state,
a call to

getTarget

, or any other attempt to use the target,
will result in an

IllegalStateException

.
It is legal at all times to obtain the call site's type using the

type

method.

The result returned by the hook must be a method handle of exactly
the same type as the call site.

While the hook is being called, the new

ConstantCallSite

object is in a partially constructed state.
In this state,
a call to

getTarget

, or any other attempt to use the target,
will result in an

IllegalStateException

.
It is legal at all times to obtain the call site's type using the

type

method.

While the hook is being called, the new

ConstantCallSite

object is in a partially constructed state.
In this state,
a call to

getTarget

, or any other attempt to use the target,
will result in an

IllegalStateException

.
It is legal at all times to obtain the call site's type using the

type

method.

Method Detail

- getTarget

```java
public final
MethodHandle
getTarget()
```

Returns the target method of the call site, which behaves
like a

final

field of the

ConstantCallSite

.
That is, the target is always the original value passed
to the constructor call which created this instance.

**Specified by:** getTarget

in class

CallSite
**Returns:** the immutable linkage state of this call site, a constant method handle
**Throws:** IllegalStateException

- if the

ConstantCallSite

constructor has not completed
**See Also:** ConstantCallSite

,

VolatileCallSite

,

CallSite.setTarget(java.lang.invoke.MethodHandle)

,

getTarget()

,

MutableCallSite.getTarget()

,

VolatileCallSite.getTarget()

- setTarget

```java
public final void setTarget​(
MethodHandle
ignore)
```

Always throws an

UnsupportedOperationException

.
This kind of call site cannot change its target.

**Specified by:** setTarget

in class

CallSite
**Parameters:** ignore

- a new target proposed for the call site, which is ignored
**Throws:** UnsupportedOperationException

- because this kind of call site cannot change its target
**See Also:** CallSite.getTarget()

,

setTarget(java.lang.invoke.MethodHandle)

,

MutableCallSite.setTarget(java.lang.invoke.MethodHandle)

,

VolatileCallSite.setTarget(java.lang.invoke.MethodHandle)

- dynamicInvoker

```java
public final
MethodHandle
dynamicInvoker()
```

Returns this call site's permanent target.
Since that target will never change, this is a correct implementation
of

CallSite.dynamicInvoker

.

**Specified by:** dynamicInvoker

in class

CallSite
**Returns:** the immutable linkage state of this call site, a constant method handle
**Throws:** IllegalStateException

- if the

ConstantCallSite

constructor has not completed

---

#### Method Detail

getTarget

```java
public final
MethodHandle
getTarget()
```

Returns the target method of the call site, which behaves
like a

final

field of the

ConstantCallSite

.
That is, the target is always the original value passed
to the constructor call which created this instance.

**Specified by:** getTarget

in class

CallSite
**Returns:** the immutable linkage state of this call site, a constant method handle
**Throws:** IllegalStateException

- if the

ConstantCallSite

constructor has not completed
**See Also:** ConstantCallSite

,

VolatileCallSite

,

CallSite.setTarget(java.lang.invoke.MethodHandle)

,

getTarget()

,

MutableCallSite.getTarget()

,

VolatileCallSite.getTarget()

---

#### getTarget

public final

MethodHandle

getTarget()

Returns the target method of the call site, which behaves
like a

final

field of the

ConstantCallSite

.
That is, the target is always the original value passed
to the constructor call which created this instance.

setTarget

```java
public final void setTarget​(
MethodHandle
ignore)
```

Always throws an

UnsupportedOperationException

.
This kind of call site cannot change its target.

**Specified by:** setTarget

in class

CallSite
**Parameters:** ignore

- a new target proposed for the call site, which is ignored
**Throws:** UnsupportedOperationException

- because this kind of call site cannot change its target
**See Also:** CallSite.getTarget()

,

setTarget(java.lang.invoke.MethodHandle)

,

MutableCallSite.setTarget(java.lang.invoke.MethodHandle)

,

VolatileCallSite.setTarget(java.lang.invoke.MethodHandle)

---

#### setTarget

public final void setTarget​(

MethodHandle

ignore)

Always throws an

UnsupportedOperationException

.
This kind of call site cannot change its target.

dynamicInvoker

```java
public final
MethodHandle
dynamicInvoker()
```

Returns this call site's permanent target.
Since that target will never change, this is a correct implementation
of

CallSite.dynamicInvoker

.

**Specified by:** dynamicInvoker

in class

CallSite
**Returns:** the immutable linkage state of this call site, a constant method handle
**Throws:** IllegalStateException

- if the

ConstantCallSite

constructor has not completed

---

#### dynamicInvoker

public final

MethodHandle

dynamicInvoker()

Returns this call site's permanent target.
Since that target will never change, this is a correct implementation
of

CallSite.dynamicInvoker

.

---

