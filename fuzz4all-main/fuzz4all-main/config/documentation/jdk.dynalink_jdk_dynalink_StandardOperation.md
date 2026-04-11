# Enum StandardOperation

**Source:** `jdk.dynalink\jdk\dynalink\StandardOperation.html`

### Class Description

```java
public enum
StandardOperation

extends
Enum
<
StandardOperation
>
implements
Operation
```

Defines the standard dynamic operations. The operations

GET

and

SET

must
be used as part of a

NamespaceOperation

.

NamedOperation

can then be further used on these

NamespaceOperation

s to bind the name parameter of

GET

and

SET

operations, in which case it
disappears from their type signature.

NamedOperation

can also be used to decorate

CALL

and

NEW

operations with a
diagnostic name, and as such it does not affect their type signature.

**All Implemented Interfaces:** Serializable

,

Comparable

<

StandardOperation

>

,

Operation

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
StandardOperation
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardOperation c : StandardOperation.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
StandardOperation
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

### Additional Sections

#### Enum StandardOperation

java.lang.Object

- java.lang.Enum

<

StandardOperation

>
- - jdk.dynalink.StandardOperation

java.lang.Enum

<

StandardOperation

>

- jdk.dynalink.StandardOperation

jdk.dynalink.StandardOperation

**All Implemented Interfaces:** Serializable

,

Comparable

<

StandardOperation

>

,

Operation

```java
public enum
StandardOperation

extends
Enum
<
StandardOperation
>
implements
Operation
```

Defines the standard dynamic operations. The operations

GET

and

SET

must
be used as part of a

NamespaceOperation

.

NamedOperation

can then be further used on these

NamespaceOperation

s to bind the name parameter of

GET

and

SET

operations, in which case it
disappears from their type signature.

NamedOperation

can also be used to decorate

CALL

and

NEW

operations with a
diagnostic name, and as such it does not affect their type signature.

public enum

StandardOperation

extends

Enum

<

StandardOperation

>
implements

Operation

Defines the standard dynamic operations. The operations

GET

and

SET

must
be used as part of a

NamespaceOperation

.

NamedOperation

can then be further used on these

NamespaceOperation

s to bind the name parameter of

GET

and

SET

operations, in which case it
disappears from their type signature.

NamedOperation

can also be used to decorate

CALL

and

NEW

operations with a
diagnostic name, and as such it does not affect their type signature.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

CALL

Call a callable object.

GET

Get the value from a namespace defined on an object.

NEW

Call a constructor object.

REMOVE

Removes the value from a namespace defined on an object.

SET

Set the value in a namespace defined on an object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

StandardOperation

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

StandardOperation

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

- Methods declared in interface jdk.dynalink.

Operation

named

,

withNamespace

,

withNamespaces

Enum Constant Summary

Enum Constants

Enum Constant

Description

CALL

Call a callable object.

GET

Get the value from a namespace defined on an object.

NEW

Call a constructor object.

REMOVE

Removes the value from a namespace defined on an object.

SET

Set the value in a namespace defined on an object.

---

#### Enum Constant Summary

Call a callable object.

Get the value from a namespace defined on an object.

Call a constructor object.

Removes the value from a namespace defined on an object.

Set the value in a namespace defined on an object.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

StandardOperation

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

StandardOperation

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

- Methods declared in interface jdk.dynalink.

Operation

named

,

withNamespace

,

withNamespaces

---

#### Method Summary

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

Methods declared in interface jdk.dynalink.

Operation

named

,

withNamespace

,

withNamespaces

---

#### Methods declared in interface jdk.dynalink. Operation

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- GET

```java
public static final
StandardOperation
GET
```

Get the value from a namespace defined on an object. Call sites with this
operation should have a signature of

(receiver, name)→value

or

(receiver)→value

when used with

NamedOperation

, with
all parameters and return type being of any type (either primitive or
reference). This operation must always be used as part of a

NamespaceOperation

.

- SET

```java
public static final
StandardOperation
SET
```

Set the value in a namespace defined on an object. Call sites with this
operation should have a signature of

(receiver, name, value)→void

or

(receiver, value)→void

when used with

NamedOperation

,
with all parameters and return type being of any type (either primitive
or reference). This operation must always be used as part of a

NamespaceOperation

.

- REMOVE

```java
public static final
StandardOperation
REMOVE
```

Removes the value from a namespace defined on an object. Call sites with this
operation should have a signature of

(receiver, name)→void

or

(receiver)→void

when used with

NamedOperation

,
with all parameters being of any type (either primitive
or reference). This operation must always be used as part of a

NamespaceOperation

.

- CALL

```java
public static final
StandardOperation
CALL
```

Call a callable object. Call sites with this operation should have a
signature of

(callable, receiver, arguments...)→value

,
with all parameters and return type being of any type (either primitive or
reference). Typically, the callables are presumed to be methods of an object, so
an explicit receiver value is always passed to the callable before the arguments.
If a callable has no concept of a receiver, it is free to ignore the value of the
receiver argument.
The

CALL

operation is allowed to be used with a

NamedOperation

even though it does not take a name. Using it with
a named operation won't affect its signature; the name is solely meant to
be used as a diagnostic description for error messages.

- NEW

```java
public static final
StandardOperation
NEW
```

Call a constructor object. Call sites with this operation should have a
signature of

(constructor, arguments...)→value

, with all
parameters and return type being of any type (either primitive or
reference). The

NEW

operation is allowed to be used with a

NamedOperation

even though it does not take a name. Using it with
a named operation won't affect its signature; the name is solely meant to
be used as a diagnostic description for error messages.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
StandardOperation
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardOperation c : StandardOperation.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
StandardOperation
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

Enum Constant Detail

- GET

```java
public static final
StandardOperation
GET
```

Get the value from a namespace defined on an object. Call sites with this
operation should have a signature of

(receiver, name)→value

or

(receiver)→value

when used with

NamedOperation

, with
all parameters and return type being of any type (either primitive or
reference). This operation must always be used as part of a

NamespaceOperation

.

- SET

```java
public static final
StandardOperation
SET
```

Set the value in a namespace defined on an object. Call sites with this
operation should have a signature of

(receiver, name, value)→void

or

(receiver, value)→void

when used with

NamedOperation

,
with all parameters and return type being of any type (either primitive
or reference). This operation must always be used as part of a

NamespaceOperation

.

- REMOVE

```java
public static final
StandardOperation
REMOVE
```

Removes the value from a namespace defined on an object. Call sites with this
operation should have a signature of

(receiver, name)→void

or

(receiver)→void

when used with

NamedOperation

,
with all parameters being of any type (either primitive
or reference). This operation must always be used as part of a

NamespaceOperation

.

- CALL

```java
public static final
StandardOperation
CALL
```

Call a callable object. Call sites with this operation should have a
signature of

(callable, receiver, arguments...)→value

,
with all parameters and return type being of any type (either primitive or
reference). Typically, the callables are presumed to be methods of an object, so
an explicit receiver value is always passed to the callable before the arguments.
If a callable has no concept of a receiver, it is free to ignore the value of the
receiver argument.
The

CALL

operation is allowed to be used with a

NamedOperation

even though it does not take a name. Using it with
a named operation won't affect its signature; the name is solely meant to
be used as a diagnostic description for error messages.

- NEW

```java
public static final
StandardOperation
NEW
```

Call a constructor object. Call sites with this operation should have a
signature of

(constructor, arguments...)→value

, with all
parameters and return type being of any type (either primitive or
reference). The

NEW

operation is allowed to be used with a

NamedOperation

even though it does not take a name. Using it with
a named operation won't affect its signature; the name is solely meant to
be used as a diagnostic description for error messages.

---

#### Enum Constant Detail

GET

```java
public static final
StandardOperation
GET
```

Get the value from a namespace defined on an object. Call sites with this
operation should have a signature of

(receiver, name)→value

or

(receiver)→value

when used with

NamedOperation

, with
all parameters and return type being of any type (either primitive or
reference). This operation must always be used as part of a

NamespaceOperation

.

---

#### GET

public static final

StandardOperation

GET

Get the value from a namespace defined on an object. Call sites with this
operation should have a signature of

(receiver, name)→value

or

(receiver)→value

when used with

NamedOperation

, with
all parameters and return type being of any type (either primitive or
reference). This operation must always be used as part of a

NamespaceOperation

.

SET

```java
public static final
StandardOperation
SET
```

Set the value in a namespace defined on an object. Call sites with this
operation should have a signature of

(receiver, name, value)→void

or

(receiver, value)→void

when used with

NamedOperation

,
with all parameters and return type being of any type (either primitive
or reference). This operation must always be used as part of a

NamespaceOperation

.

---

#### SET

public static final

StandardOperation

SET

Set the value in a namespace defined on an object. Call sites with this
operation should have a signature of

(receiver, name, value)→void

or

(receiver, value)→void

when used with

NamedOperation

,
with all parameters and return type being of any type (either primitive
or reference). This operation must always be used as part of a

NamespaceOperation

.

REMOVE

```java
public static final
StandardOperation
REMOVE
```

Removes the value from a namespace defined on an object. Call sites with this
operation should have a signature of

(receiver, name)→void

or

(receiver)→void

when used with

NamedOperation

,
with all parameters being of any type (either primitive
or reference). This operation must always be used as part of a

NamespaceOperation

.

---

#### REMOVE

public static final

StandardOperation

REMOVE

Removes the value from a namespace defined on an object. Call sites with this
operation should have a signature of

(receiver, name)→void

or

(receiver)→void

when used with

NamedOperation

,
with all parameters being of any type (either primitive
or reference). This operation must always be used as part of a

NamespaceOperation

.

CALL

```java
public static final
StandardOperation
CALL
```

Call a callable object. Call sites with this operation should have a
signature of

(callable, receiver, arguments...)→value

,
with all parameters and return type being of any type (either primitive or
reference). Typically, the callables are presumed to be methods of an object, so
an explicit receiver value is always passed to the callable before the arguments.
If a callable has no concept of a receiver, it is free to ignore the value of the
receiver argument.
The

CALL

operation is allowed to be used with a

NamedOperation

even though it does not take a name. Using it with
a named operation won't affect its signature; the name is solely meant to
be used as a diagnostic description for error messages.

---

#### CALL

public static final

StandardOperation

CALL

Call a callable object. Call sites with this operation should have a
signature of

(callable, receiver, arguments...)→value

,
with all parameters and return type being of any type (either primitive or
reference). Typically, the callables are presumed to be methods of an object, so
an explicit receiver value is always passed to the callable before the arguments.
If a callable has no concept of a receiver, it is free to ignore the value of the
receiver argument.
The

CALL

operation is allowed to be used with a

NamedOperation

even though it does not take a name. Using it with
a named operation won't affect its signature; the name is solely meant to
be used as a diagnostic description for error messages.

NEW

```java
public static final
StandardOperation
NEW
```

Call a constructor object. Call sites with this operation should have a
signature of

(constructor, arguments...)→value

, with all
parameters and return type being of any type (either primitive or
reference). The

NEW

operation is allowed to be used with a

NamedOperation

even though it does not take a name. Using it with
a named operation won't affect its signature; the name is solely meant to
be used as a diagnostic description for error messages.

---

#### NEW

public static final

StandardOperation

NEW

Call a constructor object. Call sites with this operation should have a
signature of

(constructor, arguments...)→value

, with all
parameters and return type being of any type (either primitive or
reference). The

NEW

operation is allowed to be used with a

NamedOperation

even though it does not take a name. Using it with
a named operation won't affect its signature; the name is solely meant to
be used as a diagnostic description for error messages.

Method Detail

- values

```java
public static
StandardOperation
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardOperation c : StandardOperation.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
StandardOperation
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

#### Method Detail

values

```java
public static
StandardOperation
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardOperation c : StandardOperation.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

StandardOperation

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardOperation c : StandardOperation.values())
System.out.println(c);
```

for (StandardOperation c : StandardOperation.values())
System.out.println(c);

valueOf

```java
public static
StandardOperation
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

StandardOperation

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

---

