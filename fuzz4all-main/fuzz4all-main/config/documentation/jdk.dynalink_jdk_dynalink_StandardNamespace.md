# Enum StandardNamespace

**Source:** `jdk.dynalink\jdk\dynalink\StandardNamespace.html`

### Class Description

```java
public enum
StandardNamespace

extends
Enum
<
StandardNamespace
>
implements
Namespace
```

An enumeration of standard namespaces defined by Dynalink.

**All Implemented Interfaces:** Serializable

,

Comparable

<

StandardNamespace

>

,

Namespace

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
StandardNamespace
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardNamespace c : StandardNamespace.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
StandardNamespace
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

#### public static
StandardNamespace
findFirst​(
Operation
op)

If the passed in operation is a

NamespaceOperation

, or a

NamedOperation

wrapping a

NamespaceOperation

, then it
returns the first (if any)

StandardNamespace

in its namespace
list. If the passed operation is not a namespace operation (optionally
wrapped in a named operation), or if it doesn't have any standard
namespaces in it, returns

null

.

**Parameters:**
- op

- the operation

**Returns:**
- the first standard namespace in the operation's namespace list

---

### Additional Sections

#### Enum StandardNamespace

java.lang.Object

- java.lang.Enum

<

StandardNamespace

>
- - jdk.dynalink.StandardNamespace

java.lang.Enum

<

StandardNamespace

>

- jdk.dynalink.StandardNamespace

jdk.dynalink.StandardNamespace

**All Implemented Interfaces:** Serializable

,

Comparable

<

StandardNamespace

>

,

Namespace

```java
public enum
StandardNamespace

extends
Enum
<
StandardNamespace
>
implements
Namespace
```

An enumeration of standard namespaces defined by Dynalink.

public enum

StandardNamespace

extends

Enum

<

StandardNamespace

>
implements

Namespace

An enumeration of standard namespaces defined by Dynalink.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ELEMENT

Standard namespace for elements of a collection object.

METHOD

Standard namespace for methods of an object.

PROPERTY

Standard namespace for properties of an object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

StandardNamespace

findFirst

​(

Operation

op)

If the passed in operation is a

NamespaceOperation

, or a

NamedOperation

wrapping a

NamespaceOperation

, then it
returns the first (if any)

StandardNamespace

in its namespace
list.

static

StandardNamespace

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

StandardNamespace

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Enum Constant Summary

Enum Constants

Enum Constant

Description

ELEMENT

Standard namespace for elements of a collection object.

METHOD

Standard namespace for methods of an object.

PROPERTY

Standard namespace for properties of an object.

---

#### Enum Constant Summary

Standard namespace for elements of a collection object.

Standard namespace for methods of an object.

Standard namespace for properties of an object.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

StandardNamespace

findFirst

​(

Operation

op)

If the passed in operation is a

NamespaceOperation

, or a

NamedOperation

wrapping a

NamespaceOperation

, then it
returns the first (if any)

StandardNamespace

in its namespace
list.

static

StandardNamespace

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

StandardNamespace

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

If the passed in operation is a

NamespaceOperation

, or a

NamedOperation

wrapping a

NamespaceOperation

, then it
returns the first (if any)

StandardNamespace

in its namespace
list.

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- PROPERTY

```java
public static final
StandardNamespace
PROPERTY
```

Standard namespace for properties of an object.

- ELEMENT

```java
public static final
StandardNamespace
ELEMENT
```

Standard namespace for elements of a collection object.

- METHOD

```java
public static final
StandardNamespace
METHOD
```

Standard namespace for methods of an object. The method objects retrieved
through a

StandardOperation.GET

on this namespace can be (and where
object semantics allows they should be) unbound, that is: not bound to the
object they were retrieved through. When they are used with

StandardOperation.CALL

an explicit "this" receiver argument is always
passed to them. Of course bound methods can be returned if the object semantics
requires them and such methods are free to ignore the receiver passed in the

CALL

operation or even raise an error when it is different from the one
the method is bound to, or exhibit any other behavior their semantics requires
in such case.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
StandardNamespace
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardNamespace c : StandardNamespace.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
StandardNamespace
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- findFirst

```java
public static
StandardNamespace
findFirst​(
Operation
op)
```

If the passed in operation is a

NamespaceOperation

, or a

NamedOperation

wrapping a

NamespaceOperation

, then it
returns the first (if any)

StandardNamespace

in its namespace
list. If the passed operation is not a namespace operation (optionally
wrapped in a named operation), or if it doesn't have any standard
namespaces in it, returns

null

.

**Parameters:** op

- the operation
**Returns:** the first standard namespace in the operation's namespace list

Enum Constant Detail

- PROPERTY

```java
public static final
StandardNamespace
PROPERTY
```

Standard namespace for properties of an object.

- ELEMENT

```java
public static final
StandardNamespace
ELEMENT
```

Standard namespace for elements of a collection object.

- METHOD

```java
public static final
StandardNamespace
METHOD
```

Standard namespace for methods of an object. The method objects retrieved
through a

StandardOperation.GET

on this namespace can be (and where
object semantics allows they should be) unbound, that is: not bound to the
object they were retrieved through. When they are used with

StandardOperation.CALL

an explicit "this" receiver argument is always
passed to them. Of course bound methods can be returned if the object semantics
requires them and such methods are free to ignore the receiver passed in the

CALL

operation or even raise an error when it is different from the one
the method is bound to, or exhibit any other behavior their semantics requires
in such case.

---

#### Enum Constant Detail

PROPERTY

```java
public static final
StandardNamespace
PROPERTY
```

Standard namespace for properties of an object.

---

#### PROPERTY

public static final

StandardNamespace

PROPERTY

Standard namespace for properties of an object.

ELEMENT

```java
public static final
StandardNamespace
ELEMENT
```

Standard namespace for elements of a collection object.

---

#### ELEMENT

public static final

StandardNamespace

ELEMENT

Standard namespace for elements of a collection object.

METHOD

```java
public static final
StandardNamespace
METHOD
```

Standard namespace for methods of an object. The method objects retrieved
through a

StandardOperation.GET

on this namespace can be (and where
object semantics allows they should be) unbound, that is: not bound to the
object they were retrieved through. When they are used with

StandardOperation.CALL

an explicit "this" receiver argument is always
passed to them. Of course bound methods can be returned if the object semantics
requires them and such methods are free to ignore the receiver passed in the

CALL

operation or even raise an error when it is different from the one
the method is bound to, or exhibit any other behavior their semantics requires
in such case.

---

#### METHOD

public static final

StandardNamespace

METHOD

Standard namespace for methods of an object. The method objects retrieved
through a

StandardOperation.GET

on this namespace can be (and where
object semantics allows they should be) unbound, that is: not bound to the
object they were retrieved through. When they are used with

StandardOperation.CALL

an explicit "this" receiver argument is always
passed to them. Of course bound methods can be returned if the object semantics
requires them and such methods are free to ignore the receiver passed in the

CALL

operation or even raise an error when it is different from the one
the method is bound to, or exhibit any other behavior their semantics requires
in such case.

Method Detail

- values

```java
public static
StandardNamespace
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardNamespace c : StandardNamespace.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
StandardNamespace
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- findFirst

```java
public static
StandardNamespace
findFirst​(
Operation
op)
```

If the passed in operation is a

NamespaceOperation

, or a

NamedOperation

wrapping a

NamespaceOperation

, then it
returns the first (if any)

StandardNamespace

in its namespace
list. If the passed operation is not a namespace operation (optionally
wrapped in a named operation), or if it doesn't have any standard
namespaces in it, returns

null

.

**Parameters:** op

- the operation
**Returns:** the first standard namespace in the operation's namespace list

---

#### Method Detail

values

```java
public static
StandardNamespace
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardNamespace c : StandardNamespace.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

StandardNamespace

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardNamespace c : StandardNamespace.values())
System.out.println(c);
```

for (StandardNamespace c : StandardNamespace.values())
System.out.println(c);

valueOf

```java
public static
StandardNamespace
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

StandardNamespace

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

findFirst

```java
public static
StandardNamespace
findFirst​(
Operation
op)
```

If the passed in operation is a

NamespaceOperation

, or a

NamedOperation

wrapping a

NamespaceOperation

, then it
returns the first (if any)

StandardNamespace

in its namespace
list. If the passed operation is not a namespace operation (optionally
wrapped in a named operation), or if it doesn't have any standard
namespaces in it, returns

null

.

**Parameters:** op

- the operation
**Returns:** the first standard namespace in the operation's namespace list

---

#### findFirst

public static

StandardNamespace

findFirst​(

Operation

op)

If the passed in operation is a

NamespaceOperation

, or a

NamedOperation

wrapping a

NamespaceOperation

, then it
returns the first (if any)

StandardNamespace

in its namespace
list. If the passed operation is not a namespace operation (optionally
wrapped in a named operation), or if it doesn't have any standard
namespaces in it, returns

null

.

---

