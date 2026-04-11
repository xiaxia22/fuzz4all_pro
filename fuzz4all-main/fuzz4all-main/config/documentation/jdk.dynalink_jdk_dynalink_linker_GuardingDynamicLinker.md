# Interface GuardingDynamicLinker

**Source:** `jdk.dynalink\jdk\dynalink\linker\GuardingDynamicLinker.html`

### Class Description

```java
public interface
GuardingDynamicLinker
```

The base interface for language-specific dynamic linkers. Such linkers
always have to produce method handles with guards, as the validity of the
method handle for calls at a call site inevitably depends on some condition
(at the very least, it depends on the receiver belonging to the language
runtime of the linker). Language runtime implementors will normally implement
the linking logic for their own language as one or more

GuardingDynamicLinker

classes. They will typically set them as

prioritized linkers

in the

DynamicLinkerFactory

they configure for themselves, and maybe also
set some as

fallback
linkers

to handle language-specific "property not found" etc. conditions.

Consider implementing

TypeBasedGuardingDynamicLinker

interface
instead of this interface for those linkers that are based on the Java class
of the objects. If you need to implement language-specific type conversions,
have your

GuardingDynamicLinker

also implement the

GuardingTypeConverterFactory

interface.

Languages can export linkers to other language runtimes for

automatic discovery

using a

GuardingDynamicLinkerExporter

.

**All Known Subinterfaces:** TypeBasedGuardingDynamicLinker

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### GuardedInvocation
getGuardedInvocation​(
LinkRequest
linkRequest,

LinkerServices
linkerServices)
throws
Exception

Creates a guarded invocation appropriate for a particular invocation with
the specified arguments at a call site.

**Parameters:**
- linkRequest

- the object describing the request for linking a
particular invocation
- linkerServices

- linker services

**Returns:**
- a guarded invocation with a method handle suitable for the
arguments, as well as a guard condition that if fails should trigger
relinking. Must return null if it can't resolve the invocation. If the
returned invocation is unconditional (which is actually quite rare), the
guard in the return value can be null. The invocation can also have any
number of switch points for asynchronous invalidation of the linkage, as
well as a

Throwable

subclass that describes an expected exception
condition that also triggers relinking (often it is faster to rely on an
infrequent but expected

ClassCastException

than on an always
evaluated

instanceof

guard). While the linker must produce an
invocation with parameter types matching those in the call site
descriptor of the link request, it should not try to match the return
type expected at the call site except when it can do it with only the
conversions that lose neither precision nor magnitude, see

LinkerServices.asTypeLosslessReturn(MethodHandle, MethodType)

for
further explanation.

**Throws:**
- Exception

- if the operation fails for whatever reason

---

### Additional Sections

#### Interface GuardingDynamicLinker

**All Known Subinterfaces:** TypeBasedGuardingDynamicLinker

**All Known Implementing Classes:** BeansLinker

,

CompositeGuardingDynamicLinker

,

CompositeTypeBasedGuardingDynamicLinker

```java
public interface
GuardingDynamicLinker
```

The base interface for language-specific dynamic linkers. Such linkers
always have to produce method handles with guards, as the validity of the
method handle for calls at a call site inevitably depends on some condition
(at the very least, it depends on the receiver belonging to the language
runtime of the linker). Language runtime implementors will normally implement
the linking logic for their own language as one or more

GuardingDynamicLinker

classes. They will typically set them as

prioritized linkers

in the

DynamicLinkerFactory

they configure for themselves, and maybe also
set some as

fallback
linkers

to handle language-specific "property not found" etc. conditions.

Consider implementing

TypeBasedGuardingDynamicLinker

interface
instead of this interface for those linkers that are based on the Java class
of the objects. If you need to implement language-specific type conversions,
have your

GuardingDynamicLinker

also implement the

GuardingTypeConverterFactory

interface.

Languages can export linkers to other language runtimes for

automatic discovery

using a

GuardingDynamicLinkerExporter

.

public interface

GuardingDynamicLinker

The base interface for language-specific dynamic linkers. Such linkers
always have to produce method handles with guards, as the validity of the
method handle for calls at a call site inevitably depends on some condition
(at the very least, it depends on the receiver belonging to the language
runtime of the linker). Language runtime implementors will normally implement
the linking logic for their own language as one or more

GuardingDynamicLinker

classes. They will typically set them as

prioritized linkers

in the

DynamicLinkerFactory

they configure for themselves, and maybe also
set some as

fallback
linkers

to handle language-specific "property not found" etc. conditions.

Consider implementing

TypeBasedGuardingDynamicLinker

interface
instead of this interface for those linkers that are based on the Java class
of the objects. If you need to implement language-specific type conversions,
have your

GuardingDynamicLinker

also implement the

GuardingTypeConverterFactory

interface.

Languages can export linkers to other language runtimes for

automatic discovery

using a

GuardingDynamicLinkerExporter

.

Consider implementing

TypeBasedGuardingDynamicLinker

interface
instead of this interface for those linkers that are based on the Java class
of the objects. If you need to implement language-specific type conversions,
have your

GuardingDynamicLinker

also implement the

GuardingTypeConverterFactory

interface.

Languages can export linkers to other language runtimes for

automatic discovery

using a

GuardingDynamicLinkerExporter

.

Languages can export linkers to other language runtimes for

automatic discovery

using a

GuardingDynamicLinkerExporter

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

getGuardedInvocation

​(

LinkRequest

linkRequest,

LinkerServices

linkerServices)

Creates a guarded invocation appropriate for a particular invocation with
the specified arguments at a call site.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

GuardedInvocation

getGuardedInvocation

​(

LinkRequest

linkRequest,

LinkerServices

linkerServices)

Creates a guarded invocation appropriate for a particular invocation with
the specified arguments at a call site.

---

#### Method Summary

Creates a guarded invocation appropriate for a particular invocation with
the specified arguments at a call site.

============ METHOD DETAIL ==========

- Method Detail

- getGuardedInvocation

```java
GuardedInvocation
getGuardedInvocation​(
LinkRequest
linkRequest,

LinkerServices
linkerServices)
throws
Exception
```

Creates a guarded invocation appropriate for a particular invocation with
the specified arguments at a call site.

**Parameters:** linkRequest

- the object describing the request for linking a
particular invocation
**Parameters:** linkerServices

- linker services
**Returns:** a guarded invocation with a method handle suitable for the
arguments, as well as a guard condition that if fails should trigger
relinking. Must return null if it can't resolve the invocation. If the
returned invocation is unconditional (which is actually quite rare), the
guard in the return value can be null. The invocation can also have any
number of switch points for asynchronous invalidation of the linkage, as
well as a

Throwable

subclass that describes an expected exception
condition that also triggers relinking (often it is faster to rely on an
infrequent but expected

ClassCastException

than on an always
evaluated

instanceof

guard). While the linker must produce an
invocation with parameter types matching those in the call site
descriptor of the link request, it should not try to match the return
type expected at the call site except when it can do it with only the
conversions that lose neither precision nor magnitude, see

LinkerServices.asTypeLosslessReturn(MethodHandle, MethodType)

for
further explanation.
**Throws:** Exception

- if the operation fails for whatever reason

Method Detail

- getGuardedInvocation

```java
GuardedInvocation
getGuardedInvocation​(
LinkRequest
linkRequest,

LinkerServices
linkerServices)
throws
Exception
```

Creates a guarded invocation appropriate for a particular invocation with
the specified arguments at a call site.

**Parameters:** linkRequest

- the object describing the request for linking a
particular invocation
**Parameters:** linkerServices

- linker services
**Returns:** a guarded invocation with a method handle suitable for the
arguments, as well as a guard condition that if fails should trigger
relinking. Must return null if it can't resolve the invocation. If the
returned invocation is unconditional (which is actually quite rare), the
guard in the return value can be null. The invocation can also have any
number of switch points for asynchronous invalidation of the linkage, as
well as a

Throwable

subclass that describes an expected exception
condition that also triggers relinking (often it is faster to rely on an
infrequent but expected

ClassCastException

than on an always
evaluated

instanceof

guard). While the linker must produce an
invocation with parameter types matching those in the call site
descriptor of the link request, it should not try to match the return
type expected at the call site except when it can do it with only the
conversions that lose neither precision nor magnitude, see

LinkerServices.asTypeLosslessReturn(MethodHandle, MethodType)

for
further explanation.
**Throws:** Exception

- if the operation fails for whatever reason

---

#### Method Detail

getGuardedInvocation

```java
GuardedInvocation
getGuardedInvocation​(
LinkRequest
linkRequest,

LinkerServices
linkerServices)
throws
Exception
```

Creates a guarded invocation appropriate for a particular invocation with
the specified arguments at a call site.

**Parameters:** linkRequest

- the object describing the request for linking a
particular invocation
**Parameters:** linkerServices

- linker services
**Returns:** a guarded invocation with a method handle suitable for the
arguments, as well as a guard condition that if fails should trigger
relinking. Must return null if it can't resolve the invocation. If the
returned invocation is unconditional (which is actually quite rare), the
guard in the return value can be null. The invocation can also have any
number of switch points for asynchronous invalidation of the linkage, as
well as a

Throwable

subclass that describes an expected exception
condition that also triggers relinking (often it is faster to rely on an
infrequent but expected

ClassCastException

than on an always
evaluated

instanceof

guard). While the linker must produce an
invocation with parameter types matching those in the call site
descriptor of the link request, it should not try to match the return
type expected at the call site except when it can do it with only the
conversions that lose neither precision nor magnitude, see

LinkerServices.asTypeLosslessReturn(MethodHandle, MethodType)

for
further explanation.
**Throws:** Exception

- if the operation fails for whatever reason

---

#### getGuardedInvocation

GuardedInvocation

getGuardedInvocation​(

LinkRequest

linkRequest,

LinkerServices

linkerServices)
throws

Exception

Creates a guarded invocation appropriate for a particular invocation with
the specified arguments at a call site.

---

