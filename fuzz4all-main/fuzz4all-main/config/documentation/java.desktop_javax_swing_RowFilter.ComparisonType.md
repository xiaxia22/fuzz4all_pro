# Enum RowFilter.ComparisonType

**Source:** `java.desktop\javax\swing\RowFilter.ComparisonType.html`

### Class Description

```java
public static enum
RowFilter.ComparisonType

extends
Enum
<
RowFilter.ComparisonType
>
```

Enumeration of the possible comparison values supported by
some of the default

RowFilter

s.

**All Implemented Interfaces:** Serializable

,

Comparable

<

RowFilter.ComparisonType

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
RowFilter.ComparisonType
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RowFilter.ComparisonType c : RowFilter.ComparisonType.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
RowFilter.ComparisonType
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

#### Enum RowFilter.ComparisonType

java.lang.Object

- java.lang.Enum

<

RowFilter.ComparisonType

>
- - javax.swing.RowFilter.ComparisonType

java.lang.Enum

<

RowFilter.ComparisonType

>

- javax.swing.RowFilter.ComparisonType

javax.swing.RowFilter.ComparisonType

**All Implemented Interfaces:** Serializable

,

Comparable

<

RowFilter.ComparisonType

>

**Enclosing class:** RowFilter

<

M

,​

I

>

```java
public static enum
RowFilter.ComparisonType

extends
Enum
<
RowFilter.ComparisonType
>
```

Enumeration of the possible comparison values supported by
some of the default

RowFilter

s.

**Since:** 1.6
**See Also:** RowFilter

public static enum

RowFilter.ComparisonType

extends

Enum

<

RowFilter.ComparisonType

>

Enumeration of the possible comparison values supported by
some of the default

RowFilter

s.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

AFTER

Indicates that entries with a value after the supplied
value should be included.

BEFORE

Indicates that entries with a value before the supplied
value should be included.

EQUAL

Indicates that entries with a value equal to the supplied
value should be included.

NOT_EQUAL

Indicates that entries with a value not equal to the supplied
value should be included.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

RowFilter.ComparisonType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

RowFilter.ComparisonType

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

AFTER

Indicates that entries with a value after the supplied
value should be included.

BEFORE

Indicates that entries with a value before the supplied
value should be included.

EQUAL

Indicates that entries with a value equal to the supplied
value should be included.

NOT_EQUAL

Indicates that entries with a value not equal to the supplied
value should be included.

---

#### Enum Constant Summary

Indicates that entries with a value after the supplied
value should be included.

Indicates that entries with a value before the supplied
value should be included.

Indicates that entries with a value equal to the supplied
value should be included.

Indicates that entries with a value not equal to the supplied
value should be included.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

RowFilter.ComparisonType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

RowFilter.ComparisonType

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

- BEFORE

```java
public static final
RowFilter.ComparisonType
BEFORE
```

Indicates that entries with a value before the supplied
value should be included.

- AFTER

```java
public static final
RowFilter.ComparisonType
AFTER
```

Indicates that entries with a value after the supplied
value should be included.

- EQUAL

```java
public static final
RowFilter.ComparisonType
EQUAL
```

Indicates that entries with a value equal to the supplied
value should be included.

- NOT_EQUAL

```java
public static final
RowFilter.ComparisonType
NOT_EQUAL
```

Indicates that entries with a value not equal to the supplied
value should be included.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
RowFilter.ComparisonType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RowFilter.ComparisonType c : RowFilter.ComparisonType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
RowFilter.ComparisonType
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

- BEFORE

```java
public static final
RowFilter.ComparisonType
BEFORE
```

Indicates that entries with a value before the supplied
value should be included.

- AFTER

```java
public static final
RowFilter.ComparisonType
AFTER
```

Indicates that entries with a value after the supplied
value should be included.

- EQUAL

```java
public static final
RowFilter.ComparisonType
EQUAL
```

Indicates that entries with a value equal to the supplied
value should be included.

- NOT_EQUAL

```java
public static final
RowFilter.ComparisonType
NOT_EQUAL
```

Indicates that entries with a value not equal to the supplied
value should be included.

---

#### Enum Constant Detail

BEFORE

```java
public static final
RowFilter.ComparisonType
BEFORE
```

Indicates that entries with a value before the supplied
value should be included.

---

#### BEFORE

public static final

RowFilter.ComparisonType

BEFORE

Indicates that entries with a value before the supplied
value should be included.

AFTER

```java
public static final
RowFilter.ComparisonType
AFTER
```

Indicates that entries with a value after the supplied
value should be included.

---

#### AFTER

public static final

RowFilter.ComparisonType

AFTER

Indicates that entries with a value after the supplied
value should be included.

EQUAL

```java
public static final
RowFilter.ComparisonType
EQUAL
```

Indicates that entries with a value equal to the supplied
value should be included.

---

#### EQUAL

public static final

RowFilter.ComparisonType

EQUAL

Indicates that entries with a value equal to the supplied
value should be included.

NOT_EQUAL

```java
public static final
RowFilter.ComparisonType
NOT_EQUAL
```

Indicates that entries with a value not equal to the supplied
value should be included.

---

#### NOT_EQUAL

public static final

RowFilter.ComparisonType

NOT_EQUAL

Indicates that entries with a value not equal to the supplied
value should be included.

Method Detail

- values

```java
public static
RowFilter.ComparisonType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RowFilter.ComparisonType c : RowFilter.ComparisonType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
RowFilter.ComparisonType
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
RowFilter.ComparisonType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RowFilter.ComparisonType c : RowFilter.ComparisonType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

RowFilter.ComparisonType

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RowFilter.ComparisonType c : RowFilter.ComparisonType.values())
System.out.println(c);
```

for (RowFilter.ComparisonType c : RowFilter.ComparisonType.values())
System.out.println(c);

valueOf

```java
public static
RowFilter.ComparisonType
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

RowFilter.ComparisonType

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

