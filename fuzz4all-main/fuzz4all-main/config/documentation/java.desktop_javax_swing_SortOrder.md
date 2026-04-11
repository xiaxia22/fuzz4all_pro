# Enum SortOrder

**Source:** `java.desktop\javax\swing\SortOrder.html`

### Class Description

```java
public enum
SortOrder

extends
Enum
<
SortOrder
>
```

SortOrder is an enumeration of the possible sort orderings.

**All Implemented Interfaces:** Serializable

,

Comparable

<

SortOrder

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
SortOrder
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SortOrder c : SortOrder.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
SortOrder
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

#### Enum SortOrder

java.lang.Object

- java.lang.Enum

<

SortOrder

>
- - javax.swing.SortOrder

java.lang.Enum

<

SortOrder

>

- javax.swing.SortOrder

javax.swing.SortOrder

**All Implemented Interfaces:** Serializable

,

Comparable

<

SortOrder

>

```java
public enum
SortOrder

extends
Enum
<
SortOrder
>
```

SortOrder is an enumeration of the possible sort orderings.

**Since:** 1.6
**See Also:** RowSorter

public enum

SortOrder

extends

Enum

<

SortOrder

>

SortOrder is an enumeration of the possible sort orderings.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ASCENDING

Enumeration value indicating the items are sorted in increasing order.

DESCENDING

Enumeration value indicating the items are sorted in decreasing order.

UNSORTED

Enumeration value indicating the items are unordered.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

SortOrder

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

SortOrder

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

ASCENDING

Enumeration value indicating the items are sorted in increasing order.

DESCENDING

Enumeration value indicating the items are sorted in decreasing order.

UNSORTED

Enumeration value indicating the items are unordered.

---

#### Enum Constant Summary

Enumeration value indicating the items are sorted in increasing order.

Enumeration value indicating the items are sorted in decreasing order.

Enumeration value indicating the items are unordered.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

SortOrder

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

SortOrder

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

- ASCENDING

```java
public static final
SortOrder
ASCENDING
```

Enumeration value indicating the items are sorted in increasing order.
For example, the set

1, 4, 0

sorted in

ASCENDING

order is

0, 1, 4

.

- DESCENDING

```java
public static final
SortOrder
DESCENDING
```

Enumeration value indicating the items are sorted in decreasing order.
For example, the set

1, 4, 0

sorted in

DESCENDING

order is

4, 1, 0

.

- UNSORTED

```java
public static final
SortOrder
UNSORTED
```

Enumeration value indicating the items are unordered.
For example, the set

1, 4, 0

in

UNSORTED

order is

1, 4, 0

.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
SortOrder
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SortOrder c : SortOrder.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
SortOrder
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

- ASCENDING

```java
public static final
SortOrder
ASCENDING
```

Enumeration value indicating the items are sorted in increasing order.
For example, the set

1, 4, 0

sorted in

ASCENDING

order is

0, 1, 4

.

- DESCENDING

```java
public static final
SortOrder
DESCENDING
```

Enumeration value indicating the items are sorted in decreasing order.
For example, the set

1, 4, 0

sorted in

DESCENDING

order is

4, 1, 0

.

- UNSORTED

```java
public static final
SortOrder
UNSORTED
```

Enumeration value indicating the items are unordered.
For example, the set

1, 4, 0

in

UNSORTED

order is

1, 4, 0

.

---

#### Enum Constant Detail

ASCENDING

```java
public static final
SortOrder
ASCENDING
```

Enumeration value indicating the items are sorted in increasing order.
For example, the set

1, 4, 0

sorted in

ASCENDING

order is

0, 1, 4

.

---

#### ASCENDING

public static final

SortOrder

ASCENDING

Enumeration value indicating the items are sorted in increasing order.
For example, the set

1, 4, 0

sorted in

ASCENDING

order is

0, 1, 4

.

DESCENDING

```java
public static final
SortOrder
DESCENDING
```

Enumeration value indicating the items are sorted in decreasing order.
For example, the set

1, 4, 0

sorted in

DESCENDING

order is

4, 1, 0

.

---

#### DESCENDING

public static final

SortOrder

DESCENDING

Enumeration value indicating the items are sorted in decreasing order.
For example, the set

1, 4, 0

sorted in

DESCENDING

order is

4, 1, 0

.

UNSORTED

```java
public static final
SortOrder
UNSORTED
```

Enumeration value indicating the items are unordered.
For example, the set

1, 4, 0

in

UNSORTED

order is

1, 4, 0

.

---

#### UNSORTED

public static final

SortOrder

UNSORTED

Enumeration value indicating the items are unordered.
For example, the set

1, 4, 0

in

UNSORTED

order is

1, 4, 0

.

Method Detail

- values

```java
public static
SortOrder
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SortOrder c : SortOrder.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
SortOrder
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
SortOrder
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SortOrder c : SortOrder.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

SortOrder

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SortOrder c : SortOrder.values())
System.out.println(c);
```

for (SortOrder c : SortOrder.values())
System.out.println(c);

valueOf

```java
public static
SortOrder
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

SortOrder

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

