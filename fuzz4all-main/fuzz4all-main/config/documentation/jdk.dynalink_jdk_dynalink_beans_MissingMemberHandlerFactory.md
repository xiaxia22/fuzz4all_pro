# Interface MissingMemberHandlerFactory

**Source:** `jdk.dynalink\jdk\dynalink\beans\MissingMemberHandlerFactory.html`

### Class Description

```java
@FunctionalInterface

public interface
MissingMemberHandlerFactory
```

A factory for creating method handles for linking missing member behavior
in

BeansLinker

. BeansLinker links these method handles into guarded
invocations for link requests specifying

GET_*

and

SET_*

StandardOperation

s when it is either certain or possible that the
requested member (property, method, or element) is missing. They will be
linked both for

named

and unnamed operations. The
implementer must ensure that the parameter types of the returned method
handle match the parameter types of the call site described in the link
request. The return types can differ, though, to allow

DynamicLinkerFactory.setPrelinkTransformer(jdk.dynalink.linker.GuardedInvocationTransformer)

late return type transformations}. It is allowed to return

null

for a
method handle if the default behavior is sufficient.

Default missing member behavior

When a

BeansLinker

is configured without a missing member handler
factory, or the factory returns

null

for a particular handler
creation invocation, the default behavior is used. The default behavior is to
return

null

from

GuardingDynamicLinker.getGuardedInvocation(LinkRequest, LinkerServices)

when it
can be determined at link time that the linked operation will never address
an existing member. This lets the

DynamicLinker

attempt the next
linker if there is one, or ultimately fail the link request with

NoSuchDynamicMethodException

. For other cases (typically all unnamed
member operations as well as most named operations on collection elements)

BeansLinker

will produce a conditional linkage that will return

null

when invoked at runtime with a name that does not match any
member for getters and silently ignore the passed values for setters.

Implementing exception-throwing behavior

Note that if the language-specific behavior for an operation on a missing
member is to throw an exception then the factory should produce a method
handle that throws the exception when invoked, and must not throw an
exception itself, as the linkage for the missing member is often conditional.

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### MethodHandle
createMissingMemberHandler​(
LinkRequest
linkRequest,

LinkerServices
linkerServices)
throws
Exception

Returns a method handle suitable for implementing missing member behavior
for a particular link request. See the class description for details.

**Parameters:**
- linkRequest

- the current link request
- linkerServices

- the current link services

**Returns:**
- a method handle that can be invoked if the property, element, or
method being addressed by an operation is missing. The return value can
be null.

**Throws:**
- Exception

- if the operation fails for any reason. Please observe
the class documentation notes for implementing exception-throwing
missing member behavior.

---

### Additional Sections

#### Interface MissingMemberHandlerFactory

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
MissingMemberHandlerFactory
```

A factory for creating method handles for linking missing member behavior
in

BeansLinker

. BeansLinker links these method handles into guarded
invocations for link requests specifying

GET_*

and

SET_*

StandardOperation

s when it is either certain or possible that the
requested member (property, method, or element) is missing. They will be
linked both for

named

and unnamed operations. The
implementer must ensure that the parameter types of the returned method
handle match the parameter types of the call site described in the link
request. The return types can differ, though, to allow

DynamicLinkerFactory.setPrelinkTransformer(jdk.dynalink.linker.GuardedInvocationTransformer)

late return type transformations}. It is allowed to return

null

for a
method handle if the default behavior is sufficient.

Default missing member behavior

When a

BeansLinker

is configured without a missing member handler
factory, or the factory returns

null

for a particular handler
creation invocation, the default behavior is used. The default behavior is to
return

null

from

GuardingDynamicLinker.getGuardedInvocation(LinkRequest, LinkerServices)

when it
can be determined at link time that the linked operation will never address
an existing member. This lets the

DynamicLinker

attempt the next
linker if there is one, or ultimately fail the link request with

NoSuchDynamicMethodException

. For other cases (typically all unnamed
member operations as well as most named operations on collection elements)

BeansLinker

will produce a conditional linkage that will return

null

when invoked at runtime with a name that does not match any
member for getters and silently ignore the passed values for setters.

Implementing exception-throwing behavior

Note that if the language-specific behavior for an operation on a missing
member is to throw an exception then the factory should produce a method
handle that throws the exception when invoked, and must not throw an
exception itself, as the linkage for the missing member is often conditional.

**See Also:** BeansLinker(MissingMemberHandlerFactory)

@FunctionalInterface

public interface

MissingMemberHandlerFactory

A factory for creating method handles for linking missing member behavior
in

BeansLinker

. BeansLinker links these method handles into guarded
invocations for link requests specifying

GET_*

and

SET_*

StandardOperation

s when it is either certain or possible that the
requested member (property, method, or element) is missing. They will be
linked both for

named

and unnamed operations. The
implementer must ensure that the parameter types of the returned method
handle match the parameter types of the call site described in the link
request. The return types can differ, though, to allow

DynamicLinkerFactory.setPrelinkTransformer(jdk.dynalink.linker.GuardedInvocationTransformer)

late return type transformations}. It is allowed to return

null

for a
method handle if the default behavior is sufficient.

Default missing member behavior

When a

BeansLinker

is configured without a missing member handler
factory, or the factory returns

null

for a particular handler
creation invocation, the default behavior is used. The default behavior is to
return

null

from

GuardingDynamicLinker.getGuardedInvocation(LinkRequest, LinkerServices)

when it
can be determined at link time that the linked operation will never address
an existing member. This lets the

DynamicLinker

attempt the next
linker if there is one, or ultimately fail the link request with

NoSuchDynamicMethodException

. For other cases (typically all unnamed
member operations as well as most named operations on collection elements)

BeansLinker

will produce a conditional linkage that will return

null

when invoked at runtime with a name that does not match any
member for getters and silently ignore the passed values for setters.

Implementing exception-throwing behavior

Note that if the language-specific behavior for an operation on a missing
member is to throw an exception then the factory should produce a method
handle that throws the exception when invoked, and must not throw an
exception itself, as the linkage for the missing member is often conditional.

---

#### Implementing exception-throwing behavior

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

MethodHandle

createMissingMemberHandler

​(

LinkRequest

linkRequest,

LinkerServices

linkerServices)

Returns a method handle suitable for implementing missing member behavior
for a particular link request.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

MethodHandle

createMissingMemberHandler

​(

LinkRequest

linkRequest,

LinkerServices

linkerServices)

Returns a method handle suitable for implementing missing member behavior
for a particular link request.

---

#### Method Summary

Returns a method handle suitable for implementing missing member behavior
for a particular link request.

============ METHOD DETAIL ==========

- Method Detail

- createMissingMemberHandler

```java
MethodHandle
createMissingMemberHandler​(
LinkRequest
linkRequest,

LinkerServices
linkerServices)
throws
Exception
```

Returns a method handle suitable for implementing missing member behavior
for a particular link request. See the class description for details.

**Parameters:** linkRequest

- the current link request
**Parameters:** linkerServices

- the current link services
**Returns:** a method handle that can be invoked if the property, element, or
method being addressed by an operation is missing. The return value can
be null.
**Throws:** Exception

- if the operation fails for any reason. Please observe
the class documentation notes for implementing exception-throwing
missing member behavior.

Method Detail

- createMissingMemberHandler

```java
MethodHandle
createMissingMemberHandler​(
LinkRequest
linkRequest,

LinkerServices
linkerServices)
throws
Exception
```

Returns a method handle suitable for implementing missing member behavior
for a particular link request. See the class description for details.

**Parameters:** linkRequest

- the current link request
**Parameters:** linkerServices

- the current link services
**Returns:** a method handle that can be invoked if the property, element, or
method being addressed by an operation is missing. The return value can
be null.
**Throws:** Exception

- if the operation fails for any reason. Please observe
the class documentation notes for implementing exception-throwing
missing member behavior.

---

#### Method Detail

createMissingMemberHandler

```java
MethodHandle
createMissingMemberHandler​(
LinkRequest
linkRequest,

LinkerServices
linkerServices)
throws
Exception
```

Returns a method handle suitable for implementing missing member behavior
for a particular link request. See the class description for details.

**Parameters:** linkRequest

- the current link request
**Parameters:** linkerServices

- the current link services
**Returns:** a method handle that can be invoked if the property, element, or
method being addressed by an operation is missing. The return value can
be null.
**Throws:** Exception

- if the operation fails for any reason. Please observe
the class documentation notes for implementing exception-throwing
missing member behavior.

---

#### createMissingMemberHandler

MethodHandle

createMissingMemberHandler​(

LinkRequest

linkRequest,

LinkerServices

linkerServices)
throws

Exception

Returns a method handle suitable for implementing missing member behavior
for a particular link request. See the class description for details.

---

