# Interface RelinkableCallSite

**Source:** `jdk.dynalink\jdk\dynalink\RelinkableCallSite.html`

### Class Description

```java
public interface
RelinkableCallSite
```

Interface for call sites managed by a

DynamicLinker

. Users of
Dynalink must use subclasses of

CallSite

that also implement this
interface as their call site implementations. There is a readily usable

SimpleRelinkableCallSite

subclass that implements monomorphic inline
caching strategy as well as

ChainedCallSite

that implements a
polymorphic inline caching strategy and retains a chain of previously linked
method handles. A relinkable call site will be managed by a

DynamicLinker

object after being associated with it using its

DynamicLinker.link(RelinkableCallSite)

method.

**All Known Implementing Classes:** AbstractRelinkableCallSite

,

ChainedCallSite

,

SimpleRelinkableCallSite

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void initialize​(
MethodHandle
relinkAndInvoke)

Invoked by dynamic linker to initialize the relinkable call site by
setting a relink-and-invoke method handle. The call site implementation
is supposed to set this method handle as its target using

CallSite.setTarget(MethodHandle)

. Relink-and-invoke is the
initial method handle set by

DynamicLinker.link(RelinkableCallSite)

that will cause the call
site to be relinked to an appropriate target on its first invocation
based on its arguments, and that linked target will then be invoked
(hence the name). This linking protocol effectively delays linking until
the call site is invoked with actual arguments and thus ensures that
linkers can make nuanced linking decisions based on those arguments and
not just on the static method type of the call site.

**Parameters:**
- relinkAndInvoke

- a relink-and-invoke method handle supplied by
Dynalink.

---

#### CallSiteDescriptor
getDescriptor()

Returns the descriptor for this call site.

**Returns:**
- the descriptor for this call site.

---

#### void relink​(
GuardedInvocation
guardedInvocation,

MethodHandle
relinkAndInvoke)

This method will be called by the dynamic linker every time the call site
is relinked (but see

resetAndRelink(GuardedInvocation, MethodHandle)

for an
exception). It will be passed a

GuardedInvocation

that the call
site should incorporate into its target method handle. When this method
is called, the call site is allowed to keep other non-invalidated
invocations around for implementation of polymorphic inline caches and
compose them with this invocation to form its final target.

**Parameters:**
- guardedInvocation

- the guarded invocation that the call site should
incorporate into its target method handle.
- relinkAndInvoke

- a relink-and-invoke method handle. This is a
method handle matching the method type of the call site that is supplied
by the

DynamicLinker

as a callback. It should be used by this
call site as the ultimate fallback when it can't invoke its target with
the passed arguments. The fallback method is such that when it's invoked,
it'll try to obtain an adequate target

GuardedInvocation

for the
invocation, and subsequently invoke

relink(GuardedInvocation, MethodHandle)

or

resetAndRelink(GuardedInvocation, MethodHandle)

, and finally
invoke the target.

---

#### void resetAndRelink​(
GuardedInvocation
guardedInvocation,

MethodHandle
relinkAndInvoke)

This method will be called by the dynamic linker every time the call site
is relinked

and

the linker wishes the call site to throw away any
prior linkage state (that is how it differs from

relink(GuardedInvocation, MethodHandle)

). It will be passed a

GuardedInvocation

that the call site should use to build its new
target method handle. When this method is called, the call site is
discouraged from keeping any previous state, and is supposed to only
link the current invocation.

**Parameters:**
- guardedInvocation

- the guarded invocation that the call site should
use to build its target method handle.
- relinkAndInvoke

- a relink-and-invoke method handle. This is a
method handle matching the method type of the call site that is supplied
by the

DynamicLinker

as a callback. It should be used by this
call site as the ultimate fallback when it can't invoke its target with
the passed arguments. The fallback method is such that when it's invoked,
it'll try to obtain an adequate target

GuardedInvocation

for the
invocation, and subsequently invoke

relink(GuardedInvocation, MethodHandle)

or

resetAndRelink(GuardedInvocation, MethodHandle)

, and finally
invoke the target.

---

### Additional Sections

#### Interface RelinkableCallSite

**All Known Implementing Classes:** AbstractRelinkableCallSite

,

ChainedCallSite

,

SimpleRelinkableCallSite

```java
public interface
RelinkableCallSite
```

Interface for call sites managed by a

DynamicLinker

. Users of
Dynalink must use subclasses of

CallSite

that also implement this
interface as their call site implementations. There is a readily usable

SimpleRelinkableCallSite

subclass that implements monomorphic inline
caching strategy as well as

ChainedCallSite

that implements a
polymorphic inline caching strategy and retains a chain of previously linked
method handles. A relinkable call site will be managed by a

DynamicLinker

object after being associated with it using its

DynamicLinker.link(RelinkableCallSite)

method.

public interface

RelinkableCallSite

Interface for call sites managed by a

DynamicLinker

. Users of
Dynalink must use subclasses of

CallSite

that also implement this
interface as their call site implementations. There is a readily usable

SimpleRelinkableCallSite

subclass that implements monomorphic inline
caching strategy as well as

ChainedCallSite

that implements a
polymorphic inline caching strategy and retains a chain of previously linked
method handles. A relinkable call site will be managed by a

DynamicLinker

object after being associated with it using its

DynamicLinker.link(RelinkableCallSite)

method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

CallSiteDescriptor

getDescriptor

()

Returns the descriptor for this call site.

void

initialize

​(

MethodHandle

relinkAndInvoke)

Invoked by dynamic linker to initialize the relinkable call site by
setting a relink-and-invoke method handle.

void

relink

​(

GuardedInvocation

guardedInvocation,

MethodHandle

relinkAndInvoke)

This method will be called by the dynamic linker every time the call site
is relinked (but see

resetAndRelink(GuardedInvocation, MethodHandle)

for an
exception).

void

resetAndRelink

​(

GuardedInvocation

guardedInvocation,

MethodHandle

relinkAndInvoke)

This method will be called by the dynamic linker every time the call site
is relinked

and

the linker wishes the call site to throw away any
prior linkage state (that is how it differs from

relink(GuardedInvocation, MethodHandle)

).

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

CallSiteDescriptor

getDescriptor

()

Returns the descriptor for this call site.

void

initialize

​(

MethodHandle

relinkAndInvoke)

Invoked by dynamic linker to initialize the relinkable call site by
setting a relink-and-invoke method handle.

void

relink

​(

GuardedInvocation

guardedInvocation,

MethodHandle

relinkAndInvoke)

This method will be called by the dynamic linker every time the call site
is relinked (but see

resetAndRelink(GuardedInvocation, MethodHandle)

for an
exception).

void

resetAndRelink

​(

GuardedInvocation

guardedInvocation,

MethodHandle

relinkAndInvoke)

This method will be called by the dynamic linker every time the call site
is relinked

and

the linker wishes the call site to throw away any
prior linkage state (that is how it differs from

relink(GuardedInvocation, MethodHandle)

).

---

#### Method Summary

Returns the descriptor for this call site.

Invoked by dynamic linker to initialize the relinkable call site by
setting a relink-and-invoke method handle.

This method will be called by the dynamic linker every time the call site
is relinked (but see

resetAndRelink(GuardedInvocation, MethodHandle)

for an
exception).

This method will be called by the dynamic linker every time the call site
is relinked

and

the linker wishes the call site to throw away any
prior linkage state (that is how it differs from

relink(GuardedInvocation, MethodHandle)

).

============ METHOD DETAIL ==========

- Method Detail

- initialize

```java
void initialize​(
MethodHandle
relinkAndInvoke)
```

Invoked by dynamic linker to initialize the relinkable call site by
setting a relink-and-invoke method handle. The call site implementation
is supposed to set this method handle as its target using

CallSite.setTarget(MethodHandle)

. Relink-and-invoke is the
initial method handle set by

DynamicLinker.link(RelinkableCallSite)

that will cause the call
site to be relinked to an appropriate target on its first invocation
based on its arguments, and that linked target will then be invoked
(hence the name). This linking protocol effectively delays linking until
the call site is invoked with actual arguments and thus ensures that
linkers can make nuanced linking decisions based on those arguments and
not just on the static method type of the call site.

**Parameters:** relinkAndInvoke

- a relink-and-invoke method handle supplied by
Dynalink.

- getDescriptor

```java
CallSiteDescriptor
getDescriptor()
```

Returns the descriptor for this call site.

**Returns:** the descriptor for this call site.

- relink

```java
void relink​(
GuardedInvocation
guardedInvocation,

MethodHandle
relinkAndInvoke)
```

This method will be called by the dynamic linker every time the call site
is relinked (but see

resetAndRelink(GuardedInvocation, MethodHandle)

for an
exception). It will be passed a

GuardedInvocation

that the call
site should incorporate into its target method handle. When this method
is called, the call site is allowed to keep other non-invalidated
invocations around for implementation of polymorphic inline caches and
compose them with this invocation to form its final target.

**Parameters:** guardedInvocation

- the guarded invocation that the call site should
incorporate into its target method handle.
**Parameters:** relinkAndInvoke

- a relink-and-invoke method handle. This is a
method handle matching the method type of the call site that is supplied
by the

DynamicLinker

as a callback. It should be used by this
call site as the ultimate fallback when it can't invoke its target with
the passed arguments. The fallback method is such that when it's invoked,
it'll try to obtain an adequate target

GuardedInvocation

for the
invocation, and subsequently invoke

relink(GuardedInvocation, MethodHandle)

or

resetAndRelink(GuardedInvocation, MethodHandle)

, and finally
invoke the target.

- resetAndRelink

```java
void resetAndRelink​(
GuardedInvocation
guardedInvocation,

MethodHandle
relinkAndInvoke)
```

This method will be called by the dynamic linker every time the call site
is relinked

and

the linker wishes the call site to throw away any
prior linkage state (that is how it differs from

relink(GuardedInvocation, MethodHandle)

). It will be passed a

GuardedInvocation

that the call site should use to build its new
target method handle. When this method is called, the call site is
discouraged from keeping any previous state, and is supposed to only
link the current invocation.

**Parameters:** guardedInvocation

- the guarded invocation that the call site should
use to build its target method handle.
**Parameters:** relinkAndInvoke

- a relink-and-invoke method handle. This is a
method handle matching the method type of the call site that is supplied
by the

DynamicLinker

as a callback. It should be used by this
call site as the ultimate fallback when it can't invoke its target with
the passed arguments. The fallback method is such that when it's invoked,
it'll try to obtain an adequate target

GuardedInvocation

for the
invocation, and subsequently invoke

relink(GuardedInvocation, MethodHandle)

or

resetAndRelink(GuardedInvocation, MethodHandle)

, and finally
invoke the target.

Method Detail

- initialize

```java
void initialize​(
MethodHandle
relinkAndInvoke)
```

Invoked by dynamic linker to initialize the relinkable call site by
setting a relink-and-invoke method handle. The call site implementation
is supposed to set this method handle as its target using

CallSite.setTarget(MethodHandle)

. Relink-and-invoke is the
initial method handle set by

DynamicLinker.link(RelinkableCallSite)

that will cause the call
site to be relinked to an appropriate target on its first invocation
based on its arguments, and that linked target will then be invoked
(hence the name). This linking protocol effectively delays linking until
the call site is invoked with actual arguments and thus ensures that
linkers can make nuanced linking decisions based on those arguments and
not just on the static method type of the call site.

**Parameters:** relinkAndInvoke

- a relink-and-invoke method handle supplied by
Dynalink.

- getDescriptor

```java
CallSiteDescriptor
getDescriptor()
```

Returns the descriptor for this call site.

**Returns:** the descriptor for this call site.

- relink

```java
void relink​(
GuardedInvocation
guardedInvocation,

MethodHandle
relinkAndInvoke)
```

This method will be called by the dynamic linker every time the call site
is relinked (but see

resetAndRelink(GuardedInvocation, MethodHandle)

for an
exception). It will be passed a

GuardedInvocation

that the call
site should incorporate into its target method handle. When this method
is called, the call site is allowed to keep other non-invalidated
invocations around for implementation of polymorphic inline caches and
compose them with this invocation to form its final target.

**Parameters:** guardedInvocation

- the guarded invocation that the call site should
incorporate into its target method handle.
**Parameters:** relinkAndInvoke

- a relink-and-invoke method handle. This is a
method handle matching the method type of the call site that is supplied
by the

DynamicLinker

as a callback. It should be used by this
call site as the ultimate fallback when it can't invoke its target with
the passed arguments. The fallback method is such that when it's invoked,
it'll try to obtain an adequate target

GuardedInvocation

for the
invocation, and subsequently invoke

relink(GuardedInvocation, MethodHandle)

or

resetAndRelink(GuardedInvocation, MethodHandle)

, and finally
invoke the target.

- resetAndRelink

```java
void resetAndRelink​(
GuardedInvocation
guardedInvocation,

MethodHandle
relinkAndInvoke)
```

This method will be called by the dynamic linker every time the call site
is relinked

and

the linker wishes the call site to throw away any
prior linkage state (that is how it differs from

relink(GuardedInvocation, MethodHandle)

). It will be passed a

GuardedInvocation

that the call site should use to build its new
target method handle. When this method is called, the call site is
discouraged from keeping any previous state, and is supposed to only
link the current invocation.

**Parameters:** guardedInvocation

- the guarded invocation that the call site should
use to build its target method handle.
**Parameters:** relinkAndInvoke

- a relink-and-invoke method handle. This is a
method handle matching the method type of the call site that is supplied
by the

DynamicLinker

as a callback. It should be used by this
call site as the ultimate fallback when it can't invoke its target with
the passed arguments. The fallback method is such that when it's invoked,
it'll try to obtain an adequate target

GuardedInvocation

for the
invocation, and subsequently invoke

relink(GuardedInvocation, MethodHandle)

or

resetAndRelink(GuardedInvocation, MethodHandle)

, and finally
invoke the target.

---

#### Method Detail

initialize

```java
void initialize​(
MethodHandle
relinkAndInvoke)
```

Invoked by dynamic linker to initialize the relinkable call site by
setting a relink-and-invoke method handle. The call site implementation
is supposed to set this method handle as its target using

CallSite.setTarget(MethodHandle)

. Relink-and-invoke is the
initial method handle set by

DynamicLinker.link(RelinkableCallSite)

that will cause the call
site to be relinked to an appropriate target on its first invocation
based on its arguments, and that linked target will then be invoked
(hence the name). This linking protocol effectively delays linking until
the call site is invoked with actual arguments and thus ensures that
linkers can make nuanced linking decisions based on those arguments and
not just on the static method type of the call site.

**Parameters:** relinkAndInvoke

- a relink-and-invoke method handle supplied by
Dynalink.

---

#### initialize

void initialize​(

MethodHandle

relinkAndInvoke)

Invoked by dynamic linker to initialize the relinkable call site by
setting a relink-and-invoke method handle. The call site implementation
is supposed to set this method handle as its target using

CallSite.setTarget(MethodHandle)

. Relink-and-invoke is the
initial method handle set by

DynamicLinker.link(RelinkableCallSite)

that will cause the call
site to be relinked to an appropriate target on its first invocation
based on its arguments, and that linked target will then be invoked
(hence the name). This linking protocol effectively delays linking until
the call site is invoked with actual arguments and thus ensures that
linkers can make nuanced linking decisions based on those arguments and
not just on the static method type of the call site.

getDescriptor

```java
CallSiteDescriptor
getDescriptor()
```

Returns the descriptor for this call site.

**Returns:** the descriptor for this call site.

---

#### getDescriptor

CallSiteDescriptor

getDescriptor()

Returns the descriptor for this call site.

relink

```java
void relink​(
GuardedInvocation
guardedInvocation,

MethodHandle
relinkAndInvoke)
```

This method will be called by the dynamic linker every time the call site
is relinked (but see

resetAndRelink(GuardedInvocation, MethodHandle)

for an
exception). It will be passed a

GuardedInvocation

that the call
site should incorporate into its target method handle. When this method
is called, the call site is allowed to keep other non-invalidated
invocations around for implementation of polymorphic inline caches and
compose them with this invocation to form its final target.

**Parameters:** guardedInvocation

- the guarded invocation that the call site should
incorporate into its target method handle.
**Parameters:** relinkAndInvoke

- a relink-and-invoke method handle. This is a
method handle matching the method type of the call site that is supplied
by the

DynamicLinker

as a callback. It should be used by this
call site as the ultimate fallback when it can't invoke its target with
the passed arguments. The fallback method is such that when it's invoked,
it'll try to obtain an adequate target

GuardedInvocation

for the
invocation, and subsequently invoke

relink(GuardedInvocation, MethodHandle)

or

resetAndRelink(GuardedInvocation, MethodHandle)

, and finally
invoke the target.

---

#### relink

void relink​(

GuardedInvocation

guardedInvocation,

MethodHandle

relinkAndInvoke)

This method will be called by the dynamic linker every time the call site
is relinked (but see

resetAndRelink(GuardedInvocation, MethodHandle)

for an
exception). It will be passed a

GuardedInvocation

that the call
site should incorporate into its target method handle. When this method
is called, the call site is allowed to keep other non-invalidated
invocations around for implementation of polymorphic inline caches and
compose them with this invocation to form its final target.

resetAndRelink

```java
void resetAndRelink​(
GuardedInvocation
guardedInvocation,

MethodHandle
relinkAndInvoke)
```

This method will be called by the dynamic linker every time the call site
is relinked

and

the linker wishes the call site to throw away any
prior linkage state (that is how it differs from

relink(GuardedInvocation, MethodHandle)

). It will be passed a

GuardedInvocation

that the call site should use to build its new
target method handle. When this method is called, the call site is
discouraged from keeping any previous state, and is supposed to only
link the current invocation.

**Parameters:** guardedInvocation

- the guarded invocation that the call site should
use to build its target method handle.
**Parameters:** relinkAndInvoke

- a relink-and-invoke method handle. This is a
method handle matching the method type of the call site that is supplied
by the

DynamicLinker

as a callback. It should be used by this
call site as the ultimate fallback when it can't invoke its target with
the passed arguments. The fallback method is such that when it's invoked,
it'll try to obtain an adequate target

GuardedInvocation

for the
invocation, and subsequently invoke

relink(GuardedInvocation, MethodHandle)

or

resetAndRelink(GuardedInvocation, MethodHandle)

, and finally
invoke the target.

---

#### resetAndRelink

void resetAndRelink​(

GuardedInvocation

guardedInvocation,

MethodHandle

relinkAndInvoke)

This method will be called by the dynamic linker every time the call site
is relinked

and

the linker wishes the call site to throw away any
prior linkage state (that is how it differs from

relink(GuardedInvocation, MethodHandle)

). It will be passed a

GuardedInvocation

that the call site should use to build its new
target method handle. When this method is called, the call site is
discouraged from keeping any previous state, and is supposed to only
link the current invocation.

---

