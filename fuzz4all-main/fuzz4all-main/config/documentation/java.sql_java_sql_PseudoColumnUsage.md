# Enum PseudoColumnUsage

**Source:** `java.sql\java\sql\PseudoColumnUsage.html`

### Class Description

```java
public enum
PseudoColumnUsage

extends
Enum
<
PseudoColumnUsage
>
```

Enumeration for pseudo/hidden column usage.

**All Implemented Interfaces:** Serializable

,

Comparable

<

PseudoColumnUsage

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
PseudoColumnUsage
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PseudoColumnUsage c : PseudoColumnUsage.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
PseudoColumnUsage
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

#### Enum PseudoColumnUsage

java.lang.Object

- java.lang.Enum

<

PseudoColumnUsage

>
- - java.sql.PseudoColumnUsage

java.lang.Enum

<

PseudoColumnUsage

>

- java.sql.PseudoColumnUsage

java.sql.PseudoColumnUsage

**All Implemented Interfaces:** Serializable

,

Comparable

<

PseudoColumnUsage

>

```java
public enum
PseudoColumnUsage

extends
Enum
<
PseudoColumnUsage
>
```

Enumeration for pseudo/hidden column usage.

**Since:** 1.7
**See Also:** DatabaseMetaData.getPseudoColumns(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

public enum

PseudoColumnUsage

extends

Enum

<

PseudoColumnUsage

>

Enumeration for pseudo/hidden column usage.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

NO_USAGE_RESTRICTIONS

There are no restrictions on the usage of the pseudo/hidden columns.

SELECT_LIST_ONLY

The pseudo/hidden column may only be used in a SELECT list.

USAGE_UNKNOWN

The usage of the pseudo/hidden column cannot be determined.

WHERE_CLAUSE_ONLY

The pseudo/hidden column may only be used in a WHERE clause.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

PseudoColumnUsage

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

PseudoColumnUsage

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

NO_USAGE_RESTRICTIONS

There are no restrictions on the usage of the pseudo/hidden columns.

SELECT_LIST_ONLY

The pseudo/hidden column may only be used in a SELECT list.

USAGE_UNKNOWN

The usage of the pseudo/hidden column cannot be determined.

WHERE_CLAUSE_ONLY

The pseudo/hidden column may only be used in a WHERE clause.

---

#### Enum Constant Summary

There are no restrictions on the usage of the pseudo/hidden columns.

The pseudo/hidden column may only be used in a SELECT list.

The usage of the pseudo/hidden column cannot be determined.

The pseudo/hidden column may only be used in a WHERE clause.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

PseudoColumnUsage

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

PseudoColumnUsage

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

- SELECT_LIST_ONLY

```java
public static final
PseudoColumnUsage
SELECT_LIST_ONLY
```

The pseudo/hidden column may only be used in a SELECT list.

- WHERE_CLAUSE_ONLY

```java
public static final
PseudoColumnUsage
WHERE_CLAUSE_ONLY
```

The pseudo/hidden column may only be used in a WHERE clause.

- NO_USAGE_RESTRICTIONS

```java
public static final
PseudoColumnUsage
NO_USAGE_RESTRICTIONS
```

There are no restrictions on the usage of the pseudo/hidden columns.

- USAGE_UNKNOWN

```java
public static final
PseudoColumnUsage
USAGE_UNKNOWN
```

The usage of the pseudo/hidden column cannot be determined.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
PseudoColumnUsage
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PseudoColumnUsage c : PseudoColumnUsage.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
PseudoColumnUsage
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

- SELECT_LIST_ONLY

```java
public static final
PseudoColumnUsage
SELECT_LIST_ONLY
```

The pseudo/hidden column may only be used in a SELECT list.

- WHERE_CLAUSE_ONLY

```java
public static final
PseudoColumnUsage
WHERE_CLAUSE_ONLY
```

The pseudo/hidden column may only be used in a WHERE clause.

- NO_USAGE_RESTRICTIONS

```java
public static final
PseudoColumnUsage
NO_USAGE_RESTRICTIONS
```

There are no restrictions on the usage of the pseudo/hidden columns.

- USAGE_UNKNOWN

```java
public static final
PseudoColumnUsage
USAGE_UNKNOWN
```

The usage of the pseudo/hidden column cannot be determined.

---

#### Enum Constant Detail

SELECT_LIST_ONLY

```java
public static final
PseudoColumnUsage
SELECT_LIST_ONLY
```

The pseudo/hidden column may only be used in a SELECT list.

---

#### SELECT_LIST_ONLY

public static final

PseudoColumnUsage

SELECT_LIST_ONLY

The pseudo/hidden column may only be used in a SELECT list.

WHERE_CLAUSE_ONLY

```java
public static final
PseudoColumnUsage
WHERE_CLAUSE_ONLY
```

The pseudo/hidden column may only be used in a WHERE clause.

---

#### WHERE_CLAUSE_ONLY

public static final

PseudoColumnUsage

WHERE_CLAUSE_ONLY

The pseudo/hidden column may only be used in a WHERE clause.

NO_USAGE_RESTRICTIONS

```java
public static final
PseudoColumnUsage
NO_USAGE_RESTRICTIONS
```

There are no restrictions on the usage of the pseudo/hidden columns.

---

#### NO_USAGE_RESTRICTIONS

public static final

PseudoColumnUsage

NO_USAGE_RESTRICTIONS

There are no restrictions on the usage of the pseudo/hidden columns.

USAGE_UNKNOWN

```java
public static final
PseudoColumnUsage
USAGE_UNKNOWN
```

The usage of the pseudo/hidden column cannot be determined.

---

#### USAGE_UNKNOWN

public static final

PseudoColumnUsage

USAGE_UNKNOWN

The usage of the pseudo/hidden column cannot be determined.

Method Detail

- values

```java
public static
PseudoColumnUsage
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PseudoColumnUsage c : PseudoColumnUsage.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
PseudoColumnUsage
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
PseudoColumnUsage
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PseudoColumnUsage c : PseudoColumnUsage.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

PseudoColumnUsage

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PseudoColumnUsage c : PseudoColumnUsage.values())
System.out.println(c);
```

for (PseudoColumnUsage c : PseudoColumnUsage.values())
System.out.println(c);

valueOf

```java
public static
PseudoColumnUsage
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

PseudoColumnUsage

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

