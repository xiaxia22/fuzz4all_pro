# Enum ObjectInputFilter.Status

**Source:** `java.base\java\io\ObjectInputFilter.Status.html`

### Class Description

```java
public static enum
ObjectInputFilter.Status

extends
Enum
<
ObjectInputFilter.Status
>
```

The status of a check on the class, array length, number of references,
depth, and stream size.

**All Implemented Interfaces:** Serializable

,

Comparable

<

ObjectInputFilter.Status

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ObjectInputFilter.Status
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ObjectInputFilter.Status c : ObjectInputFilter.Status.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
ObjectInputFilter.Status
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

#### Enum ObjectInputFilter.Status

java.lang.Object

- java.lang.Enum

<

ObjectInputFilter.Status

>
- - java.io.ObjectInputFilter.Status

java.lang.Enum

<

ObjectInputFilter.Status

>

- java.io.ObjectInputFilter.Status

java.io.ObjectInputFilter.Status

**All Implemented Interfaces:** Serializable

,

Comparable

<

ObjectInputFilter.Status

>

**Enclosing interface:** ObjectInputFilter

```java
public static enum
ObjectInputFilter.Status

extends
Enum
<
ObjectInputFilter.Status
>
```

The status of a check on the class, array length, number of references,
depth, and stream size.

**Since:** 9

public static enum

ObjectInputFilter.Status

extends

Enum

<

ObjectInputFilter.Status

>

The status of a check on the class, array length, number of references,
depth, and stream size.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ALLOWED

The status is allowed.

REJECTED

The status is rejected.

UNDECIDED

The status is undecided, not allowed and not rejected.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ObjectInputFilter.Status

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ObjectInputFilter.Status

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

ALLOWED

The status is allowed.

REJECTED

The status is rejected.

UNDECIDED

The status is undecided, not allowed and not rejected.

---

#### Enum Constant Summary

The status is allowed.

The status is rejected.

The status is undecided, not allowed and not rejected.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ObjectInputFilter.Status

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ObjectInputFilter.Status

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

- UNDECIDED

```java
public static final
ObjectInputFilter.Status
UNDECIDED
```

The status is undecided, not allowed and not rejected.

- ALLOWED

```java
public static final
ObjectInputFilter.Status
ALLOWED
```

The status is allowed.

- REJECTED

```java
public static final
ObjectInputFilter.Status
REJECTED
```

The status is rejected.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
ObjectInputFilter.Status
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ObjectInputFilter.Status c : ObjectInputFilter.Status.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ObjectInputFilter.Status
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

- UNDECIDED

```java
public static final
ObjectInputFilter.Status
UNDECIDED
```

The status is undecided, not allowed and not rejected.

- ALLOWED

```java
public static final
ObjectInputFilter.Status
ALLOWED
```

The status is allowed.

- REJECTED

```java
public static final
ObjectInputFilter.Status
REJECTED
```

The status is rejected.

---

#### Enum Constant Detail

UNDECIDED

```java
public static final
ObjectInputFilter.Status
UNDECIDED
```

The status is undecided, not allowed and not rejected.

---

#### UNDECIDED

public static final

ObjectInputFilter.Status

UNDECIDED

The status is undecided, not allowed and not rejected.

ALLOWED

```java
public static final
ObjectInputFilter.Status
ALLOWED
```

The status is allowed.

---

#### ALLOWED

public static final

ObjectInputFilter.Status

ALLOWED

The status is allowed.

REJECTED

```java
public static final
ObjectInputFilter.Status
REJECTED
```

The status is rejected.

---

#### REJECTED

public static final

ObjectInputFilter.Status

REJECTED

The status is rejected.

Method Detail

- values

```java
public static
ObjectInputFilter.Status
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ObjectInputFilter.Status c : ObjectInputFilter.Status.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ObjectInputFilter.Status
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
ObjectInputFilter.Status
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ObjectInputFilter.Status c : ObjectInputFilter.Status.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

ObjectInputFilter.Status

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ObjectInputFilter.Status c : ObjectInputFilter.Status.values())
System.out.println(c);
```

for (ObjectInputFilter.Status c : ObjectInputFilter.Status.values())
System.out.println(c);

valueOf

```java
public static
ObjectInputFilter.Status
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

ObjectInputFilter.Status

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

