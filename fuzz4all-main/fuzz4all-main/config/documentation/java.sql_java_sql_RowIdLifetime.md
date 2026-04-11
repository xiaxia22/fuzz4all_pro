# Enum RowIdLifetime

**Source:** `java.sql\java\sql\RowIdLifetime.html`

### Class Description

```java
public enum
RowIdLifetime

extends
Enum
<
RowIdLifetime
>
```

Enumeration for RowId life-time values.

**All Implemented Interfaces:** Serializable

,

Comparable

<

RowIdLifetime

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
RowIdLifetime
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RowIdLifetime c : RowIdLifetime.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
RowIdLifetime
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

#### Enum RowIdLifetime

java.lang.Object

- java.lang.Enum

<

RowIdLifetime

>
- - java.sql.RowIdLifetime

java.lang.Enum

<

RowIdLifetime

>

- java.sql.RowIdLifetime

java.sql.RowIdLifetime

**All Implemented Interfaces:** Serializable

,

Comparable

<

RowIdLifetime

>

```java
public enum
RowIdLifetime

extends
Enum
<
RowIdLifetime
>
```

Enumeration for RowId life-time values.

**Since:** 1.6

public enum

RowIdLifetime

extends

Enum

<

RowIdLifetime

>

Enumeration for RowId life-time values.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ROWID_UNSUPPORTED

Indicates that this data source does not support the ROWID type.

ROWID_VALID_FOREVER

Indicates that the lifetime of a RowId from this data source is, effectively,
unlimited.

ROWID_VALID_OTHER

Indicates that the lifetime of a RowId from this data source is indeterminate;
but not one of ROWID_VALID_TRANSACTION, ROWID_VALID_SESSION, or,
ROWID_VALID_FOREVER.

ROWID_VALID_SESSION

Indicates that the lifetime of a RowId from this data source is at least the
containing session.

ROWID_VALID_TRANSACTION

Indicates that the lifetime of a RowId from this data source is at least the
containing transaction.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

RowIdLifetime

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

RowIdLifetime

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

ROWID_UNSUPPORTED

Indicates that this data source does not support the ROWID type.

ROWID_VALID_FOREVER

Indicates that the lifetime of a RowId from this data source is, effectively,
unlimited.

ROWID_VALID_OTHER

Indicates that the lifetime of a RowId from this data source is indeterminate;
but not one of ROWID_VALID_TRANSACTION, ROWID_VALID_SESSION, or,
ROWID_VALID_FOREVER.

ROWID_VALID_SESSION

Indicates that the lifetime of a RowId from this data source is at least the
containing session.

ROWID_VALID_TRANSACTION

Indicates that the lifetime of a RowId from this data source is at least the
containing transaction.

---

#### Enum Constant Summary

Indicates that this data source does not support the ROWID type.

Indicates that the lifetime of a RowId from this data source is, effectively,
unlimited.

Indicates that the lifetime of a RowId from this data source is indeterminate;
but not one of ROWID_VALID_TRANSACTION, ROWID_VALID_SESSION, or,
ROWID_VALID_FOREVER.

Indicates that the lifetime of a RowId from this data source is at least the
containing session.

Indicates that the lifetime of a RowId from this data source is at least the
containing transaction.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

RowIdLifetime

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

RowIdLifetime

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

- ROWID_UNSUPPORTED

```java
public static final
RowIdLifetime
ROWID_UNSUPPORTED
```

Indicates that this data source does not support the ROWID type.

- ROWID_VALID_OTHER

```java
public static final
RowIdLifetime
ROWID_VALID_OTHER
```

Indicates that the lifetime of a RowId from this data source is indeterminate;
but not one of ROWID_VALID_TRANSACTION, ROWID_VALID_SESSION, or,
ROWID_VALID_FOREVER.

- ROWID_VALID_SESSION

```java
public static final
RowIdLifetime
ROWID_VALID_SESSION
```

Indicates that the lifetime of a RowId from this data source is at least the
containing session.

- ROWID_VALID_TRANSACTION

```java
public static final
RowIdLifetime
ROWID_VALID_TRANSACTION
```

Indicates that the lifetime of a RowId from this data source is at least the
containing transaction.

- ROWID_VALID_FOREVER

```java
public static final
RowIdLifetime
ROWID_VALID_FOREVER
```

Indicates that the lifetime of a RowId from this data source is, effectively,
unlimited.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
RowIdLifetime
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RowIdLifetime c : RowIdLifetime.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
RowIdLifetime
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

- ROWID_UNSUPPORTED

```java
public static final
RowIdLifetime
ROWID_UNSUPPORTED
```

Indicates that this data source does not support the ROWID type.

- ROWID_VALID_OTHER

```java
public static final
RowIdLifetime
ROWID_VALID_OTHER
```

Indicates that the lifetime of a RowId from this data source is indeterminate;
but not one of ROWID_VALID_TRANSACTION, ROWID_VALID_SESSION, or,
ROWID_VALID_FOREVER.

- ROWID_VALID_SESSION

```java
public static final
RowIdLifetime
ROWID_VALID_SESSION
```

Indicates that the lifetime of a RowId from this data source is at least the
containing session.

- ROWID_VALID_TRANSACTION

```java
public static final
RowIdLifetime
ROWID_VALID_TRANSACTION
```

Indicates that the lifetime of a RowId from this data source is at least the
containing transaction.

- ROWID_VALID_FOREVER

```java
public static final
RowIdLifetime
ROWID_VALID_FOREVER
```

Indicates that the lifetime of a RowId from this data source is, effectively,
unlimited.

---

#### Enum Constant Detail

ROWID_UNSUPPORTED

```java
public static final
RowIdLifetime
ROWID_UNSUPPORTED
```

Indicates that this data source does not support the ROWID type.

---

#### ROWID_UNSUPPORTED

public static final

RowIdLifetime

ROWID_UNSUPPORTED

Indicates that this data source does not support the ROWID type.

ROWID_VALID_OTHER

```java
public static final
RowIdLifetime
ROWID_VALID_OTHER
```

Indicates that the lifetime of a RowId from this data source is indeterminate;
but not one of ROWID_VALID_TRANSACTION, ROWID_VALID_SESSION, or,
ROWID_VALID_FOREVER.

---

#### ROWID_VALID_OTHER

public static final

RowIdLifetime

ROWID_VALID_OTHER

Indicates that the lifetime of a RowId from this data source is indeterminate;
but not one of ROWID_VALID_TRANSACTION, ROWID_VALID_SESSION, or,
ROWID_VALID_FOREVER.

ROWID_VALID_SESSION

```java
public static final
RowIdLifetime
ROWID_VALID_SESSION
```

Indicates that the lifetime of a RowId from this data source is at least the
containing session.

---

#### ROWID_VALID_SESSION

public static final

RowIdLifetime

ROWID_VALID_SESSION

Indicates that the lifetime of a RowId from this data source is at least the
containing session.

ROWID_VALID_TRANSACTION

```java
public static final
RowIdLifetime
ROWID_VALID_TRANSACTION
```

Indicates that the lifetime of a RowId from this data source is at least the
containing transaction.

---

#### ROWID_VALID_TRANSACTION

public static final

RowIdLifetime

ROWID_VALID_TRANSACTION

Indicates that the lifetime of a RowId from this data source is at least the
containing transaction.

ROWID_VALID_FOREVER

```java
public static final
RowIdLifetime
ROWID_VALID_FOREVER
```

Indicates that the lifetime of a RowId from this data source is, effectively,
unlimited.

---

#### ROWID_VALID_FOREVER

public static final

RowIdLifetime

ROWID_VALID_FOREVER

Indicates that the lifetime of a RowId from this data source is, effectively,
unlimited.

Method Detail

- values

```java
public static
RowIdLifetime
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RowIdLifetime c : RowIdLifetime.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
RowIdLifetime
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
RowIdLifetime
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RowIdLifetime c : RowIdLifetime.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

RowIdLifetime

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RowIdLifetime c : RowIdLifetime.values())
System.out.println(c);
```

for (RowIdLifetime c : RowIdLifetime.values())
System.out.println(c);

valueOf

```java
public static
RowIdLifetime
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

RowIdLifetime

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

