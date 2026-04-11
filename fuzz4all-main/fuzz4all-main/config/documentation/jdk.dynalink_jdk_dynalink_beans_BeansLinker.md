# Class BeansLinker

**Source:** `jdk.dynalink\jdk\dynalink\beans\BeansLinker.html`

### Class Description

```java
public class
BeansLinker

extends
Object

implements
GuardingDynamicLinker
```

A linker for ordinary Java objects. Normally used as the ultimate fallback
linker by the

DynamicLinkerFactory

so it is given the chance to link
calls to all objects that no other linker recognized. Specifically, this
linker will:

- expose all public methods of form

setXxx()

,

getXxx()

,
and

isXxx()

as property setters and getters for

StandardOperation.SET

and

StandardOperation.GET

operations in the

StandardNamespace.PROPERTY

namespace;
- expose all public methods for retrieval for

StandardOperation.GET

operation in the

StandardNamespace.METHOD

namespace;
the methods thus retrieved can then be invoked using

StandardOperation.CALL

.
- expose all public fields as properties, unless there are getters or
setters for the properties of the same name;
- expose elements of native Java arrays,

List

and

Map

objects as

StandardOperation.GET

and

StandardOperation.SET

operations in the

StandardNamespace.ELEMENT

namespace;
- expose removal of elements of

List

and

Map

objects as

StandardOperation.REMOVE

operation in the

StandardNamespace.ELEMENT

namespace;
- expose a virtual property named

length

on Java arrays,

Collection

and

Map

objects;
- expose

StandardOperation.NEW

on instances of

StaticClass

as calls to constructors, including those static class objects that represent
Java arrays (their constructors take a single

int

parameter
representing the length of the array to create);
- expose static methods, fields, and properties of classes in a similar
manner to how instance method, fields, and properties are exposed, on

StaticClass

objects.
- expose a virtual property named

static

on instances of

Class

to access their

StaticClass

.

Overloaded method resolution

is performed automatically
for property setters, methods, and constructors. Additionally, manual
overloaded method selection is supported by having a call site specify a name
for a method that contains an explicit signature, e.g.

StandardOperation.GET.withNamespace(METHOD).named("parseInt(String,int)")

You can use non-qualified class names in such signatures regardless of those
classes' packages, they will match any class with the same non-qualified name. You
only have to use a fully qualified class name in case non-qualified class
names would cause selection ambiguity (that is extremely rare). Overloaded
resolution for constructors is not automatic as there is no logical place to
attach that functionality to but if a language wishes to provide this
functionality, it can use

getConstructorMethod(Class, String)

as a
useful building block for it.

Variable argument invocation

is handled for both methods
and constructors.

Caller sensitive methods

can be linked as long as they
are otherwise public and link requests have call site descriptors carrying
full-strength

MethodHandles.Lookup

objects and not weakened lookups or the public
lookup.

The behavior for handling missing members

can be
customized by passing a

MissingMemberHandlerFactory

to the

constructor

.

The class also exposes various methods for discovery of available
property and method names on classes and class instances, as well as access
to per-class linkers using the

getLinkerForClass(Class)

method.

**All Implemented Interfaces:** GuardingDynamicLinker

---

### Field Details

*No entries found.*

### Constructor Details

#### public BeansLinker()

Creates a new beans linker. Equivalent to

BeansLinker(MissingMemberHandlerFactory)

with

null

passed as the missing member handler factory, resulting in
the default behavior for linking and evaluating missing members.

---

#### public BeansLinker​(
MissingMemberHandlerFactory
missingMemberHandlerFactory)

Creates a new beans linker with the specified factory for creating
missing member handlers. The passed factory can be null if the default
behavior is adequate. See

MissingMemberHandlerFactory

for details.

**Parameters:**
- missingMemberHandlerFactory

- a factory for creating handlers for
operations on missing members.

---

### Method Details

#### public
TypeBasedGuardingDynamicLinker
getLinkerForClass​(
Class
<?> clazz)

Returns a bean linker for a particular single class. Useful when you need
to override or extend the behavior of linking for some classes in your
language runtime's linker, but still want to delegate to the default
behavior in some cases.

**Parameters:**
- clazz

- the class

**Returns:**
- a bean linker for that class

---

#### public static boolean isDynamicMethod​(
Object
obj)

Returns true if the object is a Java dynamic method (e.g., one
obtained through a

GET:METHOD

operation on a Java object or

StaticClass

or through

getConstructorMethod(Class, String)

.

**Parameters:**
- obj

- the object we want to test for being a Java dynamic method.

**Returns:**
- true if it is a dynamic method, false otherwise.

---

#### public static boolean isDynamicConstructor​(
Object
obj)

Returns true if the object is a Java constructor (obtained through

getConstructorMethod(Class, String)

}.

**Parameters:**
- obj

- the object we want to test for being a Java constructor.

**Returns:**
- true if it is a constructor, false otherwise.

---

#### public static
Object
getConstructorMethod​(
Class
<?> clazz,

String
signature)

Return the dynamic method of constructor of the given class and the given
signature. This method is useful for exposing a functionality for
selecting an overloaded constructor based on an explicit signature, as
this functionality is not otherwise exposed by Dynalink as

StaticClass

objects act as overloaded constructors without
explicit signature selection. Example usage would be:

getConstructorMethod(java.awt.Color.class, "int, int, int")

.

**Parameters:**
- clazz

- the class
- signature

- full signature of the constructor. Note how you can use
names of primitive types, array names with normal Java notation (e.g.

"int[]"

), and normally you can even use unqualified class names
(e.g.

"String, List"

instead of

"java.lang.String, java.util.List"

as long as they don't cause
ambiguity in the specific parameter position.

**Returns:**
- dynamic method for the constructor or null if no constructor with
the specified signature exists.

---

#### public static
Set
<
String
> getReadableInstancePropertyNames​(
Class
<?> clazz)

Returns a set of names of all readable instance properties of a class.

**Parameters:**
- clazz

- the class

**Returns:**
- a set of names of all readable instance properties of a class.

---

#### public static
Set
<
String
> getWritableInstancePropertyNames​(
Class
<?> clazz)

Returns a set of names of all writable instance properties of a class.

**Parameters:**
- clazz

- the class

**Returns:**
- a set of names of all writable instance properties of a class.

---

#### public static
Set
<
String
> getInstanceMethodNames​(
Class
<?> clazz)

Returns a set of names of all instance methods of a class.

**Parameters:**
- clazz

- the class

**Returns:**
- a set of names of all instance methods of a class.

---

#### public static
Set
<
String
> getReadableStaticPropertyNames​(
Class
<?> clazz)

Returns a set of names of all readable static properties of a class.

**Parameters:**
- clazz

- the class

**Returns:**
- a set of names of all readable static properties of a class.

---

#### public static
Set
<
String
> getWritableStaticPropertyNames​(
Class
<?> clazz)

Returns a set of names of all writable static properties of a class.

**Parameters:**
- clazz

- the class

**Returns:**
- a set of names of all writable static properties of a class.

---

#### public static
Set
<
String
> getStaticMethodNames​(
Class
<?> clazz)

Returns a set of names of all static methods of a class.

**Parameters:**
- clazz

- the class

**Returns:**
- a set of names of all static methods of a class.

---

### Additional Sections

#### Class BeansLinker

java.lang.Object

- jdk.dynalink.beans.BeansLinker

jdk.dynalink.beans.BeansLinker

**All Implemented Interfaces:** GuardingDynamicLinker

```java
public class
BeansLinker

extends
Object

implements
GuardingDynamicLinker
```

A linker for ordinary Java objects. Normally used as the ultimate fallback
linker by the

DynamicLinkerFactory

so it is given the chance to link
calls to all objects that no other linker recognized. Specifically, this
linker will:

- expose all public methods of form

setXxx()

,

getXxx()

,
and

isXxx()

as property setters and getters for

StandardOperation.SET

and

StandardOperation.GET

operations in the

StandardNamespace.PROPERTY

namespace;
- expose all public methods for retrieval for

StandardOperation.GET

operation in the

StandardNamespace.METHOD

namespace;
the methods thus retrieved can then be invoked using

StandardOperation.CALL

.
- expose all public fields as properties, unless there are getters or
setters for the properties of the same name;
- expose elements of native Java arrays,

List

and

Map

objects as

StandardOperation.GET

and

StandardOperation.SET

operations in the

StandardNamespace.ELEMENT

namespace;
- expose removal of elements of

List

and

Map

objects as

StandardOperation.REMOVE

operation in the

StandardNamespace.ELEMENT

namespace;
- expose a virtual property named

length

on Java arrays,

Collection

and

Map

objects;
- expose

StandardOperation.NEW

on instances of

StaticClass

as calls to constructors, including those static class objects that represent
Java arrays (their constructors take a single

int

parameter
representing the length of the array to create);
- expose static methods, fields, and properties of classes in a similar
manner to how instance method, fields, and properties are exposed, on

StaticClass

objects.
- expose a virtual property named

static

on instances of

Class

to access their

StaticClass

.

Overloaded method resolution

is performed automatically
for property setters, methods, and constructors. Additionally, manual
overloaded method selection is supported by having a call site specify a name
for a method that contains an explicit signature, e.g.

StandardOperation.GET.withNamespace(METHOD).named("parseInt(String,int)")

You can use non-qualified class names in such signatures regardless of those
classes' packages, they will match any class with the same non-qualified name. You
only have to use a fully qualified class name in case non-qualified class
names would cause selection ambiguity (that is extremely rare). Overloaded
resolution for constructors is not automatic as there is no logical place to
attach that functionality to but if a language wishes to provide this
functionality, it can use

getConstructorMethod(Class, String)

as a
useful building block for it.

Variable argument invocation

is handled for both methods
and constructors.

Caller sensitive methods

can be linked as long as they
are otherwise public and link requests have call site descriptors carrying
full-strength

MethodHandles.Lookup

objects and not weakened lookups or the public
lookup.

The behavior for handling missing members

can be
customized by passing a

MissingMemberHandlerFactory

to the

constructor

.

The class also exposes various methods for discovery of available
property and method names on classes and class instances, as well as access
to per-class linkers using the

getLinkerForClass(Class)

method.

public class

BeansLinker

extends

Object

implements

GuardingDynamicLinker

A linker for ordinary Java objects. Normally used as the ultimate fallback
linker by the

DynamicLinkerFactory

so it is given the chance to link
calls to all objects that no other linker recognized. Specifically, this
linker will:

- expose all public methods of form

setXxx()

,

getXxx()

,
and

isXxx()

as property setters and getters for

StandardOperation.SET

and

StandardOperation.GET

operations in the

StandardNamespace.PROPERTY

namespace;
- expose all public methods for retrieval for

StandardOperation.GET

operation in the

StandardNamespace.METHOD

namespace;
the methods thus retrieved can then be invoked using

StandardOperation.CALL

.
- expose all public fields as properties, unless there are getters or
setters for the properties of the same name;
- expose elements of native Java arrays,

List

and

Map

objects as

StandardOperation.GET

and

StandardOperation.SET

operations in the

StandardNamespace.ELEMENT

namespace;
- expose removal of elements of

List

and

Map

objects as

StandardOperation.REMOVE

operation in the

StandardNamespace.ELEMENT

namespace;
- expose a virtual property named

length

on Java arrays,

Collection

and

Map

objects;
- expose

StandardOperation.NEW

on instances of

StaticClass

as calls to constructors, including those static class objects that represent
Java arrays (their constructors take a single

int

parameter
representing the length of the array to create);
- expose static methods, fields, and properties of classes in a similar
manner to how instance method, fields, and properties are exposed, on

StaticClass

objects.
- expose a virtual property named

static

on instances of

Class

to access their

StaticClass

.

Overloaded method resolution

is performed automatically
for property setters, methods, and constructors. Additionally, manual
overloaded method selection is supported by having a call site specify a name
for a method that contains an explicit signature, e.g.

StandardOperation.GET.withNamespace(METHOD).named("parseInt(String,int)")

You can use non-qualified class names in such signatures regardless of those
classes' packages, they will match any class with the same non-qualified name. You
only have to use a fully qualified class name in case non-qualified class
names would cause selection ambiguity (that is extremely rare). Overloaded
resolution for constructors is not automatic as there is no logical place to
attach that functionality to but if a language wishes to provide this
functionality, it can use

getConstructorMethod(Class, String)

as a
useful building block for it.

Variable argument invocation

is handled for both methods
and constructors.

Caller sensitive methods

can be linked as long as they
are otherwise public and link requests have call site descriptors carrying
full-strength

MethodHandles.Lookup

objects and not weakened lookups or the public
lookup.

The behavior for handling missing members

can be
customized by passing a

MissingMemberHandlerFactory

to the

constructor

.

The class also exposes various methods for discovery of available
property and method names on classes and class instances, as well as access
to per-class linkers using the

getLinkerForClass(Class)

method.

expose all public methods of form

setXxx()

,

getXxx()

,
and

isXxx()

as property setters and getters for

StandardOperation.SET

and

StandardOperation.GET

operations in the

StandardNamespace.PROPERTY

namespace;

expose all public methods for retrieval for

StandardOperation.GET

operation in the

StandardNamespace.METHOD

namespace;
the methods thus retrieved can then be invoked using

StandardOperation.CALL

.

expose all public fields as properties, unless there are getters or
setters for the properties of the same name;

expose elements of native Java arrays,

List

and

Map

objects as

StandardOperation.GET

and

StandardOperation.SET

operations in the

StandardNamespace.ELEMENT

namespace;

expose removal of elements of

List

and

Map

objects as

StandardOperation.REMOVE

operation in the

StandardNamespace.ELEMENT

namespace;

expose a virtual property named

length

on Java arrays,

Collection

and

Map

objects;

expose

StandardOperation.NEW

on instances of

StaticClass

as calls to constructors, including those static class objects that represent
Java arrays (their constructors take a single

int

parameter
representing the length of the array to create);

expose static methods, fields, and properties of classes in a similar
manner to how instance method, fields, and properties are exposed, on

StaticClass

objects.

expose a virtual property named

static

on instances of

Class

to access their

StaticClass

.

Overloaded method resolution

is performed automatically
for property setters, methods, and constructors. Additionally, manual
overloaded method selection is supported by having a call site specify a name
for a method that contains an explicit signature, e.g.

StandardOperation.GET.withNamespace(METHOD).named("parseInt(String,int)")

You can use non-qualified class names in such signatures regardless of those
classes' packages, they will match any class with the same non-qualified name. You
only have to use a fully qualified class name in case non-qualified class
names would cause selection ambiguity (that is extremely rare). Overloaded
resolution for constructors is not automatic as there is no logical place to
attach that functionality to but if a language wishes to provide this
functionality, it can use

getConstructorMethod(Class, String)

as a
useful building block for it.

Variable argument invocation

is handled for both methods
and constructors.

Caller sensitive methods

can be linked as long as they
are otherwise public and link requests have call site descriptors carrying
full-strength

MethodHandles.Lookup

objects and not weakened lookups or the public
lookup.

The behavior for handling missing members

can be
customized by passing a

MissingMemberHandlerFactory

to the

constructor

.

The class also exposes various methods for discovery of available
property and method names on classes and class instances, as well as access
to per-class linkers using the

getLinkerForClass(Class)

method.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BeansLinker

()

Creates a new beans linker.

BeansLinker

​(

MissingMemberHandlerFactory

missingMemberHandlerFactory)

Creates a new beans linker with the specified factory for creating
missing member handlers.

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

Object

getConstructorMethod

​(

Class

<?> clazz,

String

signature)

Return the dynamic method of constructor of the given class and the given
signature.

static

Set

<

String

>

getInstanceMethodNames

​(

Class

<?> clazz)

Returns a set of names of all instance methods of a class.

TypeBasedGuardingDynamicLinker

getLinkerForClass

​(

Class

<?> clazz)

Returns a bean linker for a particular single class.

static

Set

<

String

>

getReadableInstancePropertyNames

​(

Class

<?> clazz)

Returns a set of names of all readable instance properties of a class.

static

Set

<

String

>

getReadableStaticPropertyNames

​(

Class

<?> clazz)

Returns a set of names of all readable static properties of a class.

static

Set

<

String

>

getStaticMethodNames

​(

Class

<?> clazz)

Returns a set of names of all static methods of a class.

static

Set

<

String

>

getWritableInstancePropertyNames

​(

Class

<?> clazz)

Returns a set of names of all writable instance properties of a class.

static

Set

<

String

>

getWritableStaticPropertyNames

​(

Class

<?> clazz)

Returns a set of names of all writable static properties of a class.

static boolean

isDynamicConstructor

​(

Object

obj)

Returns true if the object is a Java constructor (obtained through

getConstructorMethod(Class, String)

}.

static boolean

isDynamicMethod

​(

Object

obj)

Returns true if the object is a Java dynamic method (e.g., one
obtained through a

GET:METHOD

operation on a Java object or

StaticClass

or through

getConstructorMethod(Class, String)

.

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

GuardingDynamicLinker

getGuardedInvocation

Constructor Summary

Constructors

Constructor

Description

BeansLinker

()

Creates a new beans linker.

BeansLinker

​(

MissingMemberHandlerFactory

missingMemberHandlerFactory)

Creates a new beans linker with the specified factory for creating
missing member handlers.

---

#### Constructor Summary

Creates a new beans linker.

Creates a new beans linker with the specified factory for creating
missing member handlers.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Object

getConstructorMethod

​(

Class

<?> clazz,

String

signature)

Return the dynamic method of constructor of the given class and the given
signature.

static

Set

<

String

>

getInstanceMethodNames

​(

Class

<?> clazz)

Returns a set of names of all instance methods of a class.

TypeBasedGuardingDynamicLinker

getLinkerForClass

​(

Class

<?> clazz)

Returns a bean linker for a particular single class.

static

Set

<

String

>

getReadableInstancePropertyNames

​(

Class

<?> clazz)

Returns a set of names of all readable instance properties of a class.

static

Set

<

String

>

getReadableStaticPropertyNames

​(

Class

<?> clazz)

Returns a set of names of all readable static properties of a class.

static

Set

<

String

>

getStaticMethodNames

​(

Class

<?> clazz)

Returns a set of names of all static methods of a class.

static

Set

<

String

>

getWritableInstancePropertyNames

​(

Class

<?> clazz)

Returns a set of names of all writable instance properties of a class.

static

Set

<

String

>

getWritableStaticPropertyNames

​(

Class

<?> clazz)

Returns a set of names of all writable static properties of a class.

static boolean

isDynamicConstructor

​(

Object

obj)

Returns true if the object is a Java constructor (obtained through

getConstructorMethod(Class, String)

}.

static boolean

isDynamicMethod

​(

Object

obj)

Returns true if the object is a Java dynamic method (e.g., one
obtained through a

GET:METHOD

operation on a Java object or

StaticClass

or through

getConstructorMethod(Class, String)

.

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

GuardingDynamicLinker

getGuardedInvocation

---

#### Method Summary

Return the dynamic method of constructor of the given class and the given
signature.

Returns a set of names of all instance methods of a class.

Returns a bean linker for a particular single class.

Returns a set of names of all readable instance properties of a class.

Returns a set of names of all readable static properties of a class.

Returns a set of names of all static methods of a class.

Returns a set of names of all writable instance properties of a class.

Returns a set of names of all writable static properties of a class.

Returns true if the object is a Java constructor (obtained through

getConstructorMethod(Class, String)

}.

Returns true if the object is a Java dynamic method (e.g., one
obtained through a

GET:METHOD

operation on a Java object or

StaticClass

or through

getConstructorMethod(Class, String)

.

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

GuardingDynamicLinker

getGuardedInvocation

---

#### Methods declared in interface jdk.dynalink.linker. GuardingDynamicLinker

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BeansLinker

```java
public BeansLinker()
```

Creates a new beans linker. Equivalent to

BeansLinker(MissingMemberHandlerFactory)

with

null

passed as the missing member handler factory, resulting in
the default behavior for linking and evaluating missing members.

- BeansLinker

```java
public BeansLinker​(
MissingMemberHandlerFactory
missingMemberHandlerFactory)
```

Creates a new beans linker with the specified factory for creating
missing member handlers. The passed factory can be null if the default
behavior is adequate. See

MissingMemberHandlerFactory

for details.

**Parameters:** missingMemberHandlerFactory

- a factory for creating handlers for
operations on missing members.

============ METHOD DETAIL ==========

- Method Detail

- getLinkerForClass

```java
public
TypeBasedGuardingDynamicLinker
getLinkerForClass​(
Class
<?> clazz)
```

Returns a bean linker for a particular single class. Useful when you need
to override or extend the behavior of linking for some classes in your
language runtime's linker, but still want to delegate to the default
behavior in some cases.

**Parameters:** clazz

- the class
**Returns:** a bean linker for that class

- isDynamicMethod

```java
public static boolean isDynamicMethod​(
Object
obj)
```

Returns true if the object is a Java dynamic method (e.g., one
obtained through a

GET:METHOD

operation on a Java object or

StaticClass

or through

getConstructorMethod(Class, String)

.

**Parameters:** obj

- the object we want to test for being a Java dynamic method.
**Returns:** true if it is a dynamic method, false otherwise.

- isDynamicConstructor

```java
public static boolean isDynamicConstructor​(
Object
obj)
```

Returns true if the object is a Java constructor (obtained through

getConstructorMethod(Class, String)

}.

**Parameters:** obj

- the object we want to test for being a Java constructor.
**Returns:** true if it is a constructor, false otherwise.

- getConstructorMethod

```java
public static
Object
getConstructorMethod​(
Class
<?> clazz,

String
signature)
```

Return the dynamic method of constructor of the given class and the given
signature. This method is useful for exposing a functionality for
selecting an overloaded constructor based on an explicit signature, as
this functionality is not otherwise exposed by Dynalink as

StaticClass

objects act as overloaded constructors without
explicit signature selection. Example usage would be:

getConstructorMethod(java.awt.Color.class, "int, int, int")

.

**Parameters:** clazz

- the class
**Parameters:** signature

- full signature of the constructor. Note how you can use
names of primitive types, array names with normal Java notation (e.g.

"int[]"

), and normally you can even use unqualified class names
(e.g.

"String, List"

instead of

"java.lang.String, java.util.List"

as long as they don't cause
ambiguity in the specific parameter position.
**Returns:** dynamic method for the constructor or null if no constructor with
the specified signature exists.

- getReadableInstancePropertyNames

```java
public static
Set
<
String
> getReadableInstancePropertyNames​(
Class
<?> clazz)
```

Returns a set of names of all readable instance properties of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all readable instance properties of a class.

- getWritableInstancePropertyNames

```java
public static
Set
<
String
> getWritableInstancePropertyNames​(
Class
<?> clazz)
```

Returns a set of names of all writable instance properties of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all writable instance properties of a class.

- getInstanceMethodNames

```java
public static
Set
<
String
> getInstanceMethodNames​(
Class
<?> clazz)
```

Returns a set of names of all instance methods of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all instance methods of a class.

- getReadableStaticPropertyNames

```java
public static
Set
<
String
> getReadableStaticPropertyNames​(
Class
<?> clazz)
```

Returns a set of names of all readable static properties of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all readable static properties of a class.

- getWritableStaticPropertyNames

```java
public static
Set
<
String
> getWritableStaticPropertyNames​(
Class
<?> clazz)
```

Returns a set of names of all writable static properties of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all writable static properties of a class.

- getStaticMethodNames

```java
public static
Set
<
String
> getStaticMethodNames​(
Class
<?> clazz)
```

Returns a set of names of all static methods of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all static methods of a class.

Constructor Detail

- BeansLinker

```java
public BeansLinker()
```

Creates a new beans linker. Equivalent to

BeansLinker(MissingMemberHandlerFactory)

with

null

passed as the missing member handler factory, resulting in
the default behavior for linking and evaluating missing members.

- BeansLinker

```java
public BeansLinker​(
MissingMemberHandlerFactory
missingMemberHandlerFactory)
```

Creates a new beans linker with the specified factory for creating
missing member handlers. The passed factory can be null if the default
behavior is adequate. See

MissingMemberHandlerFactory

for details.

**Parameters:** missingMemberHandlerFactory

- a factory for creating handlers for
operations on missing members.

---

#### Constructor Detail

BeansLinker

```java
public BeansLinker()
```

Creates a new beans linker. Equivalent to

BeansLinker(MissingMemberHandlerFactory)

with

null

passed as the missing member handler factory, resulting in
the default behavior for linking and evaluating missing members.

---

#### BeansLinker

public BeansLinker()

Creates a new beans linker. Equivalent to

BeansLinker(MissingMemberHandlerFactory)

with

null

passed as the missing member handler factory, resulting in
the default behavior for linking and evaluating missing members.

BeansLinker

```java
public BeansLinker​(
MissingMemberHandlerFactory
missingMemberHandlerFactory)
```

Creates a new beans linker with the specified factory for creating
missing member handlers. The passed factory can be null if the default
behavior is adequate. See

MissingMemberHandlerFactory

for details.

**Parameters:** missingMemberHandlerFactory

- a factory for creating handlers for
operations on missing members.

---

#### BeansLinker

public BeansLinker​(

MissingMemberHandlerFactory

missingMemberHandlerFactory)

Creates a new beans linker with the specified factory for creating
missing member handlers. The passed factory can be null if the default
behavior is adequate. See

MissingMemberHandlerFactory

for details.

Method Detail

- getLinkerForClass

```java
public
TypeBasedGuardingDynamicLinker
getLinkerForClass​(
Class
<?> clazz)
```

Returns a bean linker for a particular single class. Useful when you need
to override or extend the behavior of linking for some classes in your
language runtime's linker, but still want to delegate to the default
behavior in some cases.

**Parameters:** clazz

- the class
**Returns:** a bean linker for that class

- isDynamicMethod

```java
public static boolean isDynamicMethod​(
Object
obj)
```

Returns true if the object is a Java dynamic method (e.g., one
obtained through a

GET:METHOD

operation on a Java object or

StaticClass

or through

getConstructorMethod(Class, String)

.

**Parameters:** obj

- the object we want to test for being a Java dynamic method.
**Returns:** true if it is a dynamic method, false otherwise.

- isDynamicConstructor

```java
public static boolean isDynamicConstructor​(
Object
obj)
```

Returns true if the object is a Java constructor (obtained through

getConstructorMethod(Class, String)

}.

**Parameters:** obj

- the object we want to test for being a Java constructor.
**Returns:** true if it is a constructor, false otherwise.

- getConstructorMethod

```java
public static
Object
getConstructorMethod​(
Class
<?> clazz,

String
signature)
```

Return the dynamic method of constructor of the given class and the given
signature. This method is useful for exposing a functionality for
selecting an overloaded constructor based on an explicit signature, as
this functionality is not otherwise exposed by Dynalink as

StaticClass

objects act as overloaded constructors without
explicit signature selection. Example usage would be:

getConstructorMethod(java.awt.Color.class, "int, int, int")

.

**Parameters:** clazz

- the class
**Parameters:** signature

- full signature of the constructor. Note how you can use
names of primitive types, array names with normal Java notation (e.g.

"int[]"

), and normally you can even use unqualified class names
(e.g.

"String, List"

instead of

"java.lang.String, java.util.List"

as long as they don't cause
ambiguity in the specific parameter position.
**Returns:** dynamic method for the constructor or null if no constructor with
the specified signature exists.

- getReadableInstancePropertyNames

```java
public static
Set
<
String
> getReadableInstancePropertyNames​(
Class
<?> clazz)
```

Returns a set of names of all readable instance properties of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all readable instance properties of a class.

- getWritableInstancePropertyNames

```java
public static
Set
<
String
> getWritableInstancePropertyNames​(
Class
<?> clazz)
```

Returns a set of names of all writable instance properties of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all writable instance properties of a class.

- getInstanceMethodNames

```java
public static
Set
<
String
> getInstanceMethodNames​(
Class
<?> clazz)
```

Returns a set of names of all instance methods of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all instance methods of a class.

- getReadableStaticPropertyNames

```java
public static
Set
<
String
> getReadableStaticPropertyNames​(
Class
<?> clazz)
```

Returns a set of names of all readable static properties of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all readable static properties of a class.

- getWritableStaticPropertyNames

```java
public static
Set
<
String
> getWritableStaticPropertyNames​(
Class
<?> clazz)
```

Returns a set of names of all writable static properties of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all writable static properties of a class.

- getStaticMethodNames

```java
public static
Set
<
String
> getStaticMethodNames​(
Class
<?> clazz)
```

Returns a set of names of all static methods of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all static methods of a class.

---

#### Method Detail

getLinkerForClass

```java
public
TypeBasedGuardingDynamicLinker
getLinkerForClass​(
Class
<?> clazz)
```

Returns a bean linker for a particular single class. Useful when you need
to override or extend the behavior of linking for some classes in your
language runtime's linker, but still want to delegate to the default
behavior in some cases.

**Parameters:** clazz

- the class
**Returns:** a bean linker for that class

---

#### getLinkerForClass

public

TypeBasedGuardingDynamicLinker

getLinkerForClass​(

Class

<?> clazz)

Returns a bean linker for a particular single class. Useful when you need
to override or extend the behavior of linking for some classes in your
language runtime's linker, but still want to delegate to the default
behavior in some cases.

isDynamicMethod

```java
public static boolean isDynamicMethod​(
Object
obj)
```

Returns true if the object is a Java dynamic method (e.g., one
obtained through a

GET:METHOD

operation on a Java object or

StaticClass

or through

getConstructorMethod(Class, String)

.

**Parameters:** obj

- the object we want to test for being a Java dynamic method.
**Returns:** true if it is a dynamic method, false otherwise.

---

#### isDynamicMethod

public static boolean isDynamicMethod​(

Object

obj)

Returns true if the object is a Java dynamic method (e.g., one
obtained through a

GET:METHOD

operation on a Java object or

StaticClass

or through

getConstructorMethod(Class, String)

.

isDynamicConstructor

```java
public static boolean isDynamicConstructor​(
Object
obj)
```

Returns true if the object is a Java constructor (obtained through

getConstructorMethod(Class, String)

}.

**Parameters:** obj

- the object we want to test for being a Java constructor.
**Returns:** true if it is a constructor, false otherwise.

---

#### isDynamicConstructor

public static boolean isDynamicConstructor​(

Object

obj)

Returns true if the object is a Java constructor (obtained through

getConstructorMethod(Class, String)

}.

getConstructorMethod

```java
public static
Object
getConstructorMethod​(
Class
<?> clazz,

String
signature)
```

Return the dynamic method of constructor of the given class and the given
signature. This method is useful for exposing a functionality for
selecting an overloaded constructor based on an explicit signature, as
this functionality is not otherwise exposed by Dynalink as

StaticClass

objects act as overloaded constructors without
explicit signature selection. Example usage would be:

getConstructorMethod(java.awt.Color.class, "int, int, int")

.

**Parameters:** clazz

- the class
**Parameters:** signature

- full signature of the constructor. Note how you can use
names of primitive types, array names with normal Java notation (e.g.

"int[]"

), and normally you can even use unqualified class names
(e.g.

"String, List"

instead of

"java.lang.String, java.util.List"

as long as they don't cause
ambiguity in the specific parameter position.
**Returns:** dynamic method for the constructor or null if no constructor with
the specified signature exists.

---

#### getConstructorMethod

public static

Object

getConstructorMethod​(

Class

<?> clazz,

String

signature)

Return the dynamic method of constructor of the given class and the given
signature. This method is useful for exposing a functionality for
selecting an overloaded constructor based on an explicit signature, as
this functionality is not otherwise exposed by Dynalink as

StaticClass

objects act as overloaded constructors without
explicit signature selection. Example usage would be:

getConstructorMethod(java.awt.Color.class, "int, int, int")

.

getReadableInstancePropertyNames

```java
public static
Set
<
String
> getReadableInstancePropertyNames​(
Class
<?> clazz)
```

Returns a set of names of all readable instance properties of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all readable instance properties of a class.

---

#### getReadableInstancePropertyNames

public static

Set

<

String

> getReadableInstancePropertyNames​(

Class

<?> clazz)

Returns a set of names of all readable instance properties of a class.

getWritableInstancePropertyNames

```java
public static
Set
<
String
> getWritableInstancePropertyNames​(
Class
<?> clazz)
```

Returns a set of names of all writable instance properties of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all writable instance properties of a class.

---

#### getWritableInstancePropertyNames

public static

Set

<

String

> getWritableInstancePropertyNames​(

Class

<?> clazz)

Returns a set of names of all writable instance properties of a class.

getInstanceMethodNames

```java
public static
Set
<
String
> getInstanceMethodNames​(
Class
<?> clazz)
```

Returns a set of names of all instance methods of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all instance methods of a class.

---

#### getInstanceMethodNames

public static

Set

<

String

> getInstanceMethodNames​(

Class

<?> clazz)

Returns a set of names of all instance methods of a class.

getReadableStaticPropertyNames

```java
public static
Set
<
String
> getReadableStaticPropertyNames​(
Class
<?> clazz)
```

Returns a set of names of all readable static properties of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all readable static properties of a class.

---

#### getReadableStaticPropertyNames

public static

Set

<

String

> getReadableStaticPropertyNames​(

Class

<?> clazz)

Returns a set of names of all readable static properties of a class.

getWritableStaticPropertyNames

```java
public static
Set
<
String
> getWritableStaticPropertyNames​(
Class
<?> clazz)
```

Returns a set of names of all writable static properties of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all writable static properties of a class.

---

#### getWritableStaticPropertyNames

public static

Set

<

String

> getWritableStaticPropertyNames​(

Class

<?> clazz)

Returns a set of names of all writable static properties of a class.

getStaticMethodNames

```java
public static
Set
<
String
> getStaticMethodNames​(
Class
<?> clazz)
```

Returns a set of names of all static methods of a class.

**Parameters:** clazz

- the class
**Returns:** a set of names of all static methods of a class.

---

#### getStaticMethodNames

public static

Set

<

String

> getStaticMethodNames​(

Class

<?> clazz)

Returns a set of names of all static methods of a class.

---

