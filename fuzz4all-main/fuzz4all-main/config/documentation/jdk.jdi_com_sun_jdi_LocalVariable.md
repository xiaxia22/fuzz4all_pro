# Interface LocalVariable

**Source:** `jdk.jdi\com\sun\jdi\LocalVariable.html`

### Class Description

```java
public interface
LocalVariable

extends
Mirror
,
Comparable
<
LocalVariable
>
```

A local variable in the target VM. Each variable declared within a

Method

has its own LocalVariable object. Variables of the same
name declared in different scopes have different LocalVariable objects.
LocalVariables can be used alone to retrieve static information
about their declaration, or can be used in conjunction with a

StackFrame

to set and get values.

**All Superinterfaces:** Comparable

<

LocalVariable

>

,

Mirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
name()

Gets the name of the local variable.

**Returns:**
- a string containing the name.

---

#### String
typeName()

Returns a text representation of the type
of this variable.
Where the type is the type specified in the declaration
of this local variable.

This type name is always available even if
the type has not yet been created or loaded.

**Returns:**
- a String representing the
type of this local variable.

---

#### Type
type()
throws
ClassNotLoadedException

Returns the type of this variable.
Where the type is the type specified in the declaration
of this local variable.

Note: if the type of this variable is a reference type (class,
interface, or array) and it has not been created or loaded
by the class loader of the enclosing class,
then ClassNotLoadedException will be thrown.
Also, a reference type may have been loaded but not yet prepared,
in which case the type will be returned
but attempts to perform some operations on the returned type
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

**Returns:**
- the

Type

of this local variable.

**Throws:**
- ClassNotLoadedException

- if the type has not yet been loaded
through the appropriate class loader.

**See Also:**
- Type

,

Field.type() - for usage examples

---

#### String
signature()

Gets the JNI signature of the local variable.

**Returns:**
- a string containing the signature.

**See Also:**
- Type Signatures

---

#### String
genericSignature()

Gets the generic signature for this variable if there is one.
Generic signatures are described in the

The Java™ Virtual Machine Specification

.

**Returns:**
- a string containing the generic signature, or

null

if there is no generic signature.

**Since:**
- 1.5

---

#### boolean isVisible​(
StackFrame
frame)

Determines whether this variable can be accessed from the given

StackFrame

.

See

StackFrame.visibleVariables()

for a complete description
variable visibility in this interface.

**Parameters:**
- frame

- the StackFrame querying visibility

**Returns:**
- true

if this variable is visible;

false

otherwise.

**Throws:**
- IllegalArgumentException

- if the stack frame's method
does not match this variable's method.

---

#### boolean isArgument()

Determines if this variable is an argument to its method.

**Returns:**
- true

if this variable is an argument;

false

otherwise.

---

#### boolean equals​(
Object
obj)

Compares the specified Object with this LocalVariable for equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true if the Object is a LocalVariable, if both LocalVariables
are contained in the same method (as determined by

Method.equals(java.lang.Object)

), and if both LocalVariables mirror
the same declaration within that method

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this LocalVariable.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the integer hash code

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Interface LocalVariable

**All Superinterfaces:** Comparable

<

LocalVariable

>

,

Mirror

```java
public interface
LocalVariable

extends
Mirror
,
Comparable
<
LocalVariable
>
```

A local variable in the target VM. Each variable declared within a

Method

has its own LocalVariable object. Variables of the same
name declared in different scopes have different LocalVariable objects.
LocalVariables can be used alone to retrieve static information
about their declaration, or can be used in conjunction with a

StackFrame

to set and get values.

**Since:** 1.3
**See Also:** StackFrame

,

Method

public interface

LocalVariable

extends

Mirror

,

Comparable

<

LocalVariable

>

A local variable in the target VM. Each variable declared within a

Method

has its own LocalVariable object. Variables of the same
name declared in different scopes have different LocalVariable objects.
LocalVariables can be used alone to retrieve static information
about their declaration, or can be used in conjunction with a

StackFrame

to set and get values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares the specified Object with this LocalVariable for equality.

String

genericSignature

()

Gets the generic signature for this variable if there is one.

int

hashCode

()

Returns the hash code value for this LocalVariable.

boolean

isArgument

()

Determines if this variable is an argument to its method.

boolean

isVisible

​(

StackFrame

frame)

Determines whether this variable can be accessed from the given

StackFrame

.

String

name

()

Gets the name of the local variable.

String

signature

()

Gets the JNI signature of the local variable.

Type

type

()

Returns the type of this variable.

String

typeName

()

Returns a text representation of the type
of this variable.

- Methods declared in interface java.lang.

Comparable

compareTo

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares the specified Object with this LocalVariable for equality.

String

genericSignature

()

Gets the generic signature for this variable if there is one.

int

hashCode

()

Returns the hash code value for this LocalVariable.

boolean

isArgument

()

Determines if this variable is an argument to its method.

boolean

isVisible

​(

StackFrame

frame)

Determines whether this variable can be accessed from the given

StackFrame

.

String

name

()

Gets the name of the local variable.

String

signature

()

Gets the JNI signature of the local variable.

Type

type

()

Returns the type of this variable.

String

typeName

()

Returns a text representation of the type
of this variable.

- Methods declared in interface java.lang.

Comparable

compareTo

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Method Summary

Compares the specified Object with this LocalVariable for equality.

Gets the generic signature for this variable if there is one.

Returns the hash code value for this LocalVariable.

Determines if this variable is an argument to its method.

Determines whether this variable can be accessed from the given

StackFrame

.

Gets the name of the local variable.

Gets the JNI signature of the local variable.

Returns the type of this variable.

Returns a text representation of the type
of this variable.

Methods declared in interface java.lang.

Comparable

compareTo

---

#### Methods declared in interface java.lang. Comparable

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Gets the name of the local variable.

**Returns:** a string containing the name.

- typeName

```java
String
typeName()
```

Returns a text representation of the type
of this variable.
Where the type is the type specified in the declaration
of this local variable.

This type name is always available even if
the type has not yet been created or loaded.

**Returns:** a String representing the
type of this local variable.

- type

```java
Type
type()
throws
ClassNotLoadedException
```

Returns the type of this variable.
Where the type is the type specified in the declaration
of this local variable.

Note: if the type of this variable is a reference type (class,
interface, or array) and it has not been created or loaded
by the class loader of the enclosing class,
then ClassNotLoadedException will be thrown.
Also, a reference type may have been loaded but not yet prepared,
in which case the type will be returned
but attempts to perform some operations on the returned type
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

**Returns:** the

Type

of this local variable.
**Throws:** ClassNotLoadedException

- if the type has not yet been loaded
through the appropriate class loader.
**See Also:** Type

,

Field.type() - for usage examples

- signature

```java
String
signature()
```

Gets the JNI signature of the local variable.

**Returns:** a string containing the signature.
**See Also:** Type Signatures

- genericSignature

```java
String
genericSignature()
```

Gets the generic signature for this variable if there is one.
Generic signatures are described in the

The Java™ Virtual Machine Specification

.

**Returns:** a string containing the generic signature, or

null

if there is no generic signature.
**Since:** 1.5

- isVisible

```java
boolean isVisible​(
StackFrame
frame)
```

Determines whether this variable can be accessed from the given

StackFrame

.

See

StackFrame.visibleVariables()

for a complete description
variable visibility in this interface.

**Parameters:** frame

- the StackFrame querying visibility
**Returns:** true

if this variable is visible;

false

otherwise.
**Throws:** IllegalArgumentException

- if the stack frame's method
does not match this variable's method.

- isArgument

```java
boolean isArgument()
```

Determines if this variable is an argument to its method.

**Returns:** true

if this variable is an argument;

false

otherwise.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this LocalVariable for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a LocalVariable, if both LocalVariables
are contained in the same method (as determined by

Method.equals(java.lang.Object)

), and if both LocalVariables mirror
the same declaration within that method
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this LocalVariable.

**Overrides:** hashCode

in class

Object
**Returns:** the integer hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Method Detail

- name

```java
String
name()
```

Gets the name of the local variable.

**Returns:** a string containing the name.

- typeName

```java
String
typeName()
```

Returns a text representation of the type
of this variable.
Where the type is the type specified in the declaration
of this local variable.

This type name is always available even if
the type has not yet been created or loaded.

**Returns:** a String representing the
type of this local variable.

- type

```java
Type
type()
throws
ClassNotLoadedException
```

Returns the type of this variable.
Where the type is the type specified in the declaration
of this local variable.

Note: if the type of this variable is a reference type (class,
interface, or array) and it has not been created or loaded
by the class loader of the enclosing class,
then ClassNotLoadedException will be thrown.
Also, a reference type may have been loaded but not yet prepared,
in which case the type will be returned
but attempts to perform some operations on the returned type
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

**Returns:** the

Type

of this local variable.
**Throws:** ClassNotLoadedException

- if the type has not yet been loaded
through the appropriate class loader.
**See Also:** Type

,

Field.type() - for usage examples

- signature

```java
String
signature()
```

Gets the JNI signature of the local variable.

**Returns:** a string containing the signature.
**See Also:** Type Signatures

- genericSignature

```java
String
genericSignature()
```

Gets the generic signature for this variable if there is one.
Generic signatures are described in the

The Java™ Virtual Machine Specification

.

**Returns:** a string containing the generic signature, or

null

if there is no generic signature.
**Since:** 1.5

- isVisible

```java
boolean isVisible​(
StackFrame
frame)
```

Determines whether this variable can be accessed from the given

StackFrame

.

See

StackFrame.visibleVariables()

for a complete description
variable visibility in this interface.

**Parameters:** frame

- the StackFrame querying visibility
**Returns:** true

if this variable is visible;

false

otherwise.
**Throws:** IllegalArgumentException

- if the stack frame's method
does not match this variable's method.

- isArgument

```java
boolean isArgument()
```

Determines if this variable is an argument to its method.

**Returns:** true

if this variable is an argument;

false

otherwise.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this LocalVariable for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a LocalVariable, if both LocalVariables
are contained in the same method (as determined by

Method.equals(java.lang.Object)

), and if both LocalVariables mirror
the same declaration within that method
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this LocalVariable.

**Overrides:** hashCode

in class

Object
**Returns:** the integer hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

name

```java
String
name()
```

Gets the name of the local variable.

**Returns:** a string containing the name.

---

#### name

String

name()

Gets the name of the local variable.

typeName

```java
String
typeName()
```

Returns a text representation of the type
of this variable.
Where the type is the type specified in the declaration
of this local variable.

This type name is always available even if
the type has not yet been created or loaded.

**Returns:** a String representing the
type of this local variable.

---

#### typeName

String

typeName()

Returns a text representation of the type
of this variable.
Where the type is the type specified in the declaration
of this local variable.

This type name is always available even if
the type has not yet been created or loaded.

This type name is always available even if
the type has not yet been created or loaded.

type

```java
Type
type()
throws
ClassNotLoadedException
```

Returns the type of this variable.
Where the type is the type specified in the declaration
of this local variable.

Note: if the type of this variable is a reference type (class,
interface, or array) and it has not been created or loaded
by the class loader of the enclosing class,
then ClassNotLoadedException will be thrown.
Also, a reference type may have been loaded but not yet prepared,
in which case the type will be returned
but attempts to perform some operations on the returned type
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

**Returns:** the

Type

of this local variable.
**Throws:** ClassNotLoadedException

- if the type has not yet been loaded
through the appropriate class loader.
**See Also:** Type

,

Field.type() - for usage examples

---

#### type

Type

type()
throws

ClassNotLoadedException

Returns the type of this variable.
Where the type is the type specified in the declaration
of this local variable.

Note: if the type of this variable is a reference type (class,
interface, or array) and it has not been created or loaded
by the class loader of the enclosing class,
then ClassNotLoadedException will be thrown.
Also, a reference type may have been loaded but not yet prepared,
in which case the type will be returned
but attempts to perform some operations on the returned type
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

Note: if the type of this variable is a reference type (class,
interface, or array) and it has not been created or loaded
by the class loader of the enclosing class,
then ClassNotLoadedException will be thrown.
Also, a reference type may have been loaded but not yet prepared,
in which case the type will be returned
but attempts to perform some operations on the returned type
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

signature

```java
String
signature()
```

Gets the JNI signature of the local variable.

**Returns:** a string containing the signature.
**See Also:** Type Signatures

---

#### signature

String

signature()

Gets the JNI signature of the local variable.

genericSignature

```java
String
genericSignature()
```

Gets the generic signature for this variable if there is one.
Generic signatures are described in the

The Java™ Virtual Machine Specification

.

**Returns:** a string containing the generic signature, or

null

if there is no generic signature.
**Since:** 1.5

---

#### genericSignature

String

genericSignature()

Gets the generic signature for this variable if there is one.
Generic signatures are described in the

The Java™ Virtual Machine Specification

.

isVisible

```java
boolean isVisible​(
StackFrame
frame)
```

Determines whether this variable can be accessed from the given

StackFrame

.

See

StackFrame.visibleVariables()

for a complete description
variable visibility in this interface.

**Parameters:** frame

- the StackFrame querying visibility
**Returns:** true

if this variable is visible;

false

otherwise.
**Throws:** IllegalArgumentException

- if the stack frame's method
does not match this variable's method.

---

#### isVisible

boolean isVisible​(

StackFrame

frame)

Determines whether this variable can be accessed from the given

StackFrame

.

See

StackFrame.visibleVariables()

for a complete description
variable visibility in this interface.

isArgument

```java
boolean isArgument()
```

Determines if this variable is an argument to its method.

**Returns:** true

if this variable is an argument;

false

otherwise.

---

#### isArgument

boolean isArgument()

Determines if this variable is an argument to its method.

equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this LocalVariable for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a LocalVariable, if both LocalVariables
are contained in the same method (as determined by

Method.equals(java.lang.Object)

), and if both LocalVariables mirror
the same declaration within that method
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

boolean equals​(

Object

obj)

Compares the specified Object with this LocalVariable for equality.

hashCode

```java
int hashCode()
```

Returns the hash code value for this LocalVariable.

**Overrides:** hashCode

in class

Object
**Returns:** the integer hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

int hashCode()

Returns the hash code value for this LocalVariable.

---

