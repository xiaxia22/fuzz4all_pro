# Class DynamicLinker

**Source:** `jdk.dynalink\jdk\dynalink\DynamicLinker.html`

### Class Description

```java
public final class
DynamicLinker

extends
Object
```

The linker for

RelinkableCallSite

objects. A dynamic linker is a main
objects when using Dynalink, it coordinates linking of call sites with
linkers of available language runtimes that are represented by

GuardingDynamicLinker

objects (you only need to deal with these if
you are yourself implementing a language runtime with its own object model
and/or type conversions). To use Dynalink, you have to create one or more
dynamic linkers using a

DynamicLinkerFactory

. Subsequently, you need
to invoke its

link(RelinkableCallSite)

method from

invokedynamic

bootstrap methods to let it manage all the call sites
they create. Usual usage would be to create at least one class per language
runtime to contain one linker instance as:

```java
class MyLanguageRuntime {
private static final GuardingDynamicLinker myLanguageLinker = new MyLanguageLinker();
private static final DynamicLinker dynamicLinker = createDynamicLinker();

private static DynamicLinker createDynamicLinker() {
final DynamicLinkerFactory factory = new DynamicLinkerFactory();
factory.setPrioritizedLinker(myLanguageLinker);
return factory.createLinker();
}

public static CallSite bootstrap(MethodHandles.Lookup lookup, String name, MethodType type) {
return dynamicLinker.link(
new SimpleRelinkableCallSite(
new CallSiteDescriptor(lookup, parseOperation(name), type)));
}

private static Operation parseOperation(String name) {
...
}
}
```

The above setup of one static linker instance is often too simple. You will
often have your language runtime have a concept of some kind of
"context class loader" and you will want to create one dynamic linker per
such class loader, to ensure it incorporates linkers for all other language
runtimes visible to that class loader (see

DynamicLinkerFactory.setClassLoader(ClassLoader)

).

There are three components you need to provide in the above example:

- You are expected to provide a

GuardingDynamicLinker

for your own
language. If your runtime doesn't have its own object model or type
conversions, you don't need to implement a

GuardingDynamicLinker

; you
would simply not invoke the

setPrioritizedLinker

method on the factory.
- The performance of the programs can depend on your choice of the class to
represent call sites. The above example used

SimpleRelinkableCallSite

, but you might want to use

ChainedCallSite

instead. You'll need to experiment and decide what
fits your runtime the best. You can further subclass either of these or
implement your own.
- You also need to provide

CallSiteDescriptor

s to your call sites.
They are immutable objects that contain all the information about the call
site: the class performing the lookups, the operation being invoked, and the
method signature. You will have to supply your own scheme to encode and
decode operations in the call site name or static parameters, that is why
in the above example the

parseOperation

method is left unimplemented.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public <T extends
RelinkableCallSite
> T link​(T callSite)

Links an invokedynamic call site. It will install a method handle into
the call site that invokes the relinking mechanism of this linker. Next
time the call site is invoked, it will be linked for the actual arguments
it was invoked with.

**Parameters:**
- callSite

- the call site to link.

**Returns:**
- the callSite, for easy call chaining.

**Type Parameters:**
- T

- the particular subclass of

RelinkableCallSite

for
which to create a link.

---

#### public
LinkerServices
getLinkerServices()

Returns the object representing the linker services of this class that
are normally exposed to individual

language-specific linkers

. While as a user of this class you normally
only care about the

link(RelinkableCallSite)

method, in certain
circumstances you might want to use the lower level services directly;
either to lookup specific method handles, to access the type converters,
and so on.

**Returns:**
- the object representing the linker services of this class.

---

#### public static
StackTraceElement
getLinkedCallSiteLocation()

Returns a stack trace element describing the location of the

invokedynamic

call site currently being linked on the current
thread. The operation is potentially expensive as it needs to generate a
stack trace to inspect it and is intended for use in diagnostics code.
For "free-floating" call sites (not associated with an

invokedynamic

instruction), the result is not well-defined.

**Returns:**
- a stack trace element describing the location of the call site
currently being linked, or null if it is not invoked while a call
site is being linked.

---

### Additional Sections

#### Class DynamicLinker

java.lang.Object

- jdk.dynalink.DynamicLinker

jdk.dynalink.DynamicLinker

```java
public final class
DynamicLinker

extends
Object
```

The linker for

RelinkableCallSite

objects. A dynamic linker is a main
objects when using Dynalink, it coordinates linking of call sites with
linkers of available language runtimes that are represented by

GuardingDynamicLinker

objects (you only need to deal with these if
you are yourself implementing a language runtime with its own object model
and/or type conversions). To use Dynalink, you have to create one or more
dynamic linkers using a

DynamicLinkerFactory

. Subsequently, you need
to invoke its

link(RelinkableCallSite)

method from

invokedynamic

bootstrap methods to let it manage all the call sites
they create. Usual usage would be to create at least one class per language
runtime to contain one linker instance as:

```java
class MyLanguageRuntime {
private static final GuardingDynamicLinker myLanguageLinker = new MyLanguageLinker();
private static final DynamicLinker dynamicLinker = createDynamicLinker();

private static DynamicLinker createDynamicLinker() {
final DynamicLinkerFactory factory = new DynamicLinkerFactory();
factory.setPrioritizedLinker(myLanguageLinker);
return factory.createLinker();
}

public static CallSite bootstrap(MethodHandles.Lookup lookup, String name, MethodType type) {
return dynamicLinker.link(
new SimpleRelinkableCallSite(
new CallSiteDescriptor(lookup, parseOperation(name), type)));
}

private static Operation parseOperation(String name) {
...
}
}
```

The above setup of one static linker instance is often too simple. You will
often have your language runtime have a concept of some kind of
"context class loader" and you will want to create one dynamic linker per
such class loader, to ensure it incorporates linkers for all other language
runtimes visible to that class loader (see

DynamicLinkerFactory.setClassLoader(ClassLoader)

).

There are three components you need to provide in the above example:

- You are expected to provide a

GuardingDynamicLinker

for your own
language. If your runtime doesn't have its own object model or type
conversions, you don't need to implement a

GuardingDynamicLinker

; you
would simply not invoke the

setPrioritizedLinker

method on the factory.
- The performance of the programs can depend on your choice of the class to
represent call sites. The above example used

SimpleRelinkableCallSite

, but you might want to use

ChainedCallSite

instead. You'll need to experiment and decide what
fits your runtime the best. You can further subclass either of these or
implement your own.
- You also need to provide

CallSiteDescriptor

s to your call sites.
They are immutable objects that contain all the information about the call
site: the class performing the lookups, the operation being invoked, and the
method signature. You will have to supply your own scheme to encode and
decode operations in the call site name or static parameters, that is why
in the above example the

parseOperation

method is left unimplemented.

public final class

DynamicLinker

extends

Object

The linker for

RelinkableCallSite

objects. A dynamic linker is a main
objects when using Dynalink, it coordinates linking of call sites with
linkers of available language runtimes that are represented by

GuardingDynamicLinker

objects (you only need to deal with these if
you are yourself implementing a language runtime with its own object model
and/or type conversions). To use Dynalink, you have to create one or more
dynamic linkers using a

DynamicLinkerFactory

. Subsequently, you need
to invoke its

link(RelinkableCallSite)

method from

invokedynamic

bootstrap methods to let it manage all the call sites
they create. Usual usage would be to create at least one class per language
runtime to contain one linker instance as:

```java
class MyLanguageRuntime {
private static final GuardingDynamicLinker myLanguageLinker = new MyLanguageLinker();
private static final DynamicLinker dynamicLinker = createDynamicLinker();

private static DynamicLinker createDynamicLinker() {
final DynamicLinkerFactory factory = new DynamicLinkerFactory();
factory.setPrioritizedLinker(myLanguageLinker);
return factory.createLinker();
}

public static CallSite bootstrap(MethodHandles.Lookup lookup, String name, MethodType type) {
return dynamicLinker.link(
new SimpleRelinkableCallSite(
new CallSiteDescriptor(lookup, parseOperation(name), type)));
}

private static Operation parseOperation(String name) {
...
}
}
```

The above setup of one static linker instance is often too simple. You will
often have your language runtime have a concept of some kind of
"context class loader" and you will want to create one dynamic linker per
such class loader, to ensure it incorporates linkers for all other language
runtimes visible to that class loader (see

DynamicLinkerFactory.setClassLoader(ClassLoader)

).

There are three components you need to provide in the above example:

- You are expected to provide a

GuardingDynamicLinker

for your own
language. If your runtime doesn't have its own object model or type
conversions, you don't need to implement a

GuardingDynamicLinker

; you
would simply not invoke the

setPrioritizedLinker

method on the factory.
- The performance of the programs can depend on your choice of the class to
represent call sites. The above example used

SimpleRelinkableCallSite

, but you might want to use

ChainedCallSite

instead. You'll need to experiment and decide what
fits your runtime the best. You can further subclass either of these or
implement your own.
- You also need to provide

CallSiteDescriptor

s to your call sites.
They are immutable objects that contain all the information about the call
site: the class performing the lookups, the operation being invoked, and the
method signature. You will have to supply your own scheme to encode and
decode operations in the call site name or static parameters, that is why
in the above example the

parseOperation

method is left unimplemented.

class MyLanguageRuntime {
private static final GuardingDynamicLinker myLanguageLinker = new MyLanguageLinker();
private static final DynamicLinker dynamicLinker = createDynamicLinker();

private static DynamicLinker createDynamicLinker() {
final DynamicLinkerFactory factory = new DynamicLinkerFactory();
factory.setPrioritizedLinker(myLanguageLinker);
return factory.createLinker();
}

public static CallSite bootstrap(MethodHandles.Lookup lookup, String name, MethodType type) {
return dynamicLinker.link(
new SimpleRelinkableCallSite(
new CallSiteDescriptor(lookup, parseOperation(name), type)));
}

private static Operation parseOperation(String name) {
...
}
}

There are three components you need to provide in the above example:

- You are expected to provide a

GuardingDynamicLinker

for your own
language. If your runtime doesn't have its own object model or type
conversions, you don't need to implement a

GuardingDynamicLinker

; you
would simply not invoke the

setPrioritizedLinker

method on the factory.
- The performance of the programs can depend on your choice of the class to
represent call sites. The above example used

SimpleRelinkableCallSite

, but you might want to use

ChainedCallSite

instead. You'll need to experiment and decide what
fits your runtime the best. You can further subclass either of these or
implement your own.
- You also need to provide

CallSiteDescriptor

s to your call sites.
They are immutable objects that contain all the information about the call
site: the class performing the lookups, the operation being invoked, and the
method signature. You will have to supply your own scheme to encode and
decode operations in the call site name or static parameters, that is why
in the above example the

parseOperation

method is left unimplemented.

You are expected to provide a

GuardingDynamicLinker

for your own
language. If your runtime doesn't have its own object model or type
conversions, you don't need to implement a

GuardingDynamicLinker

; you
would simply not invoke the

setPrioritizedLinker

method on the factory.

The performance of the programs can depend on your choice of the class to
represent call sites. The above example used

SimpleRelinkableCallSite

, but you might want to use

ChainedCallSite

instead. You'll need to experiment and decide what
fits your runtime the best. You can further subclass either of these or
implement your own.

You also need to provide

CallSiteDescriptor

s to your call sites.
They are immutable objects that contain all the information about the call
site: the class performing the lookups, the operation being invoked, and the
method signature. You will have to supply your own scheme to encode and
decode operations in the call site name or static parameters, that is why
in the above example the

parseOperation

method is left unimplemented.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

StackTraceElement

getLinkedCallSiteLocation

()

Returns a stack trace element describing the location of the

invokedynamic

call site currently being linked on the current
thread.

LinkerServices

getLinkerServices

()

Returns the object representing the linker services of this class that
are normally exposed to individual

language-specific linkers

.

<T extends

RelinkableCallSite

>

T

link

​(T callSite)

Links an invokedynamic call site.

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

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

StackTraceElement

getLinkedCallSiteLocation

()

Returns a stack trace element describing the location of the

invokedynamic

call site currently being linked on the current
thread.

LinkerServices

getLinkerServices

()

Returns the object representing the linker services of this class that
are normally exposed to individual

language-specific linkers

.

<T extends

RelinkableCallSite

>

T

link

​(T callSite)

Links an invokedynamic call site.

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

Returns a stack trace element describing the location of the

invokedynamic

call site currently being linked on the current
thread.

Returns the object representing the linker services of this class that
are normally exposed to individual

language-specific linkers

.

Links an invokedynamic call site.

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

============ METHOD DETAIL ==========

- Method Detail

- link

```java
public <T extends
RelinkableCallSite
> T link​(T callSite)
```

Links an invokedynamic call site. It will install a method handle into
the call site that invokes the relinking mechanism of this linker. Next
time the call site is invoked, it will be linked for the actual arguments
it was invoked with.

**Type Parameters:** T

- the particular subclass of

RelinkableCallSite

for
which to create a link.
**Parameters:** callSite

- the call site to link.
**Returns:** the callSite, for easy call chaining.

- getLinkerServices

```java
public
LinkerServices
getLinkerServices()
```

Returns the object representing the linker services of this class that
are normally exposed to individual

language-specific linkers

. While as a user of this class you normally
only care about the

link(RelinkableCallSite)

method, in certain
circumstances you might want to use the lower level services directly;
either to lookup specific method handles, to access the type converters,
and so on.

**Returns:** the object representing the linker services of this class.

- getLinkedCallSiteLocation

```java
public static
StackTraceElement
getLinkedCallSiteLocation()
```

Returns a stack trace element describing the location of the

invokedynamic

call site currently being linked on the current
thread. The operation is potentially expensive as it needs to generate a
stack trace to inspect it and is intended for use in diagnostics code.
For "free-floating" call sites (not associated with an

invokedynamic

instruction), the result is not well-defined.

**Returns:** a stack trace element describing the location of the call site
currently being linked, or null if it is not invoked while a call
site is being linked.

Method Detail

- link

```java
public <T extends
RelinkableCallSite
> T link​(T callSite)
```

Links an invokedynamic call site. It will install a method handle into
the call site that invokes the relinking mechanism of this linker. Next
time the call site is invoked, it will be linked for the actual arguments
it was invoked with.

**Type Parameters:** T

- the particular subclass of

RelinkableCallSite

for
which to create a link.
**Parameters:** callSite

- the call site to link.
**Returns:** the callSite, for easy call chaining.

- getLinkerServices

```java
public
LinkerServices
getLinkerServices()
```

Returns the object representing the linker services of this class that
are normally exposed to individual

language-specific linkers

. While as a user of this class you normally
only care about the

link(RelinkableCallSite)

method, in certain
circumstances you might want to use the lower level services directly;
either to lookup specific method handles, to access the type converters,
and so on.

**Returns:** the object representing the linker services of this class.

- getLinkedCallSiteLocation

```java
public static
StackTraceElement
getLinkedCallSiteLocation()
```

Returns a stack trace element describing the location of the

invokedynamic

call site currently being linked on the current
thread. The operation is potentially expensive as it needs to generate a
stack trace to inspect it and is intended for use in diagnostics code.
For "free-floating" call sites (not associated with an

invokedynamic

instruction), the result is not well-defined.

**Returns:** a stack trace element describing the location of the call site
currently being linked, or null if it is not invoked while a call
site is being linked.

---

#### Method Detail

link

```java
public <T extends
RelinkableCallSite
> T link​(T callSite)
```

Links an invokedynamic call site. It will install a method handle into
the call site that invokes the relinking mechanism of this linker. Next
time the call site is invoked, it will be linked for the actual arguments
it was invoked with.

**Type Parameters:** T

- the particular subclass of

RelinkableCallSite

for
which to create a link.
**Parameters:** callSite

- the call site to link.
**Returns:** the callSite, for easy call chaining.

---

#### link

public <T extends

RelinkableCallSite

> T link​(T callSite)

Links an invokedynamic call site. It will install a method handle into
the call site that invokes the relinking mechanism of this linker. Next
time the call site is invoked, it will be linked for the actual arguments
it was invoked with.

getLinkerServices

```java
public
LinkerServices
getLinkerServices()
```

Returns the object representing the linker services of this class that
are normally exposed to individual

language-specific linkers

. While as a user of this class you normally
only care about the

link(RelinkableCallSite)

method, in certain
circumstances you might want to use the lower level services directly;
either to lookup specific method handles, to access the type converters,
and so on.

**Returns:** the object representing the linker services of this class.

---

#### getLinkerServices

public

LinkerServices

getLinkerServices()

Returns the object representing the linker services of this class that
are normally exposed to individual

language-specific linkers

. While as a user of this class you normally
only care about the

link(RelinkableCallSite)

method, in certain
circumstances you might want to use the lower level services directly;
either to lookup specific method handles, to access the type converters,
and so on.

getLinkedCallSiteLocation

```java
public static
StackTraceElement
getLinkedCallSiteLocation()
```

Returns a stack trace element describing the location of the

invokedynamic

call site currently being linked on the current
thread. The operation is potentially expensive as it needs to generate a
stack trace to inspect it and is intended for use in diagnostics code.
For "free-floating" call sites (not associated with an

invokedynamic

instruction), the result is not well-defined.

**Returns:** a stack trace element describing the location of the call site
currently being linked, or null if it is not invoked while a call
site is being linked.

---

#### getLinkedCallSiteLocation

public static

StackTraceElement

getLinkedCallSiteLocation()

Returns a stack trace element describing the location of the

invokedynamic

call site currently being linked on the current
thread. The operation is potentially expensive as it needs to generate a
stack trace to inspect it and is intended for use in diagnostics code.
For "free-floating" call sites (not associated with an

invokedynamic

instruction), the result is not well-defined.

---

