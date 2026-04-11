# Enum ConversionComparator.Comparison

**Source:** `jdk.dynalink\jdk\dynalink\linker\ConversionComparator.Comparison.html`

### Class Description

```java
public static enum
ConversionComparator.Comparison

extends
Enum
<
ConversionComparator.Comparison
>
```

Enumeration of possible outcomes of comparing one conversion to another.

**All Implemented Interfaces:** Serializable

,

Comparable

<

ConversionComparator.Comparison

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ConversionComparator.Comparison
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ConversionComparator.Comparison c : ConversionComparator.Comparison.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
ConversionComparator.Comparison
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

#### Enum ConversionComparator.Comparison

java.lang.Object

- java.lang.Enum

<

ConversionComparator.Comparison

>
- - jdk.dynalink.linker.ConversionComparator.Comparison

java.lang.Enum

<

ConversionComparator.Comparison

>

- jdk.dynalink.linker.ConversionComparator.Comparison

jdk.dynalink.linker.ConversionComparator.Comparison

**All Implemented Interfaces:** Serializable

,

Comparable

<

ConversionComparator.Comparison

>

**Enclosing interface:** ConversionComparator

```java
public static enum
ConversionComparator.Comparison

extends
Enum
<
ConversionComparator.Comparison
>
```

Enumeration of possible outcomes of comparing one conversion to another.

public static enum

ConversionComparator.Comparison

extends

Enum

<

ConversionComparator.Comparison

>

Enumeration of possible outcomes of comparing one conversion to another.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

INDETERMINATE

The conversions cannot be compared.

TYPE_1_BETTER

The first conversion is better than the second one.

TYPE_2_BETTER

The second conversion is better than the first one.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ConversionComparator.Comparison

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ConversionComparator.Comparison

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

INDETERMINATE

The conversions cannot be compared.

TYPE_1_BETTER

The first conversion is better than the second one.

TYPE_2_BETTER

The second conversion is better than the first one.

---

#### Enum Constant Summary

The conversions cannot be compared.

The first conversion is better than the second one.

The second conversion is better than the first one.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ConversionComparator.Comparison

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ConversionComparator.Comparison

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

- INDETERMINATE

```java
public static final
ConversionComparator.Comparison
INDETERMINATE
```

The conversions cannot be compared.

- TYPE_1_BETTER

```java
public static final
ConversionComparator.Comparison
TYPE_1_BETTER
```

The first conversion is better than the second one.

- TYPE_2_BETTER

```java
public static final
ConversionComparator.Comparison
TYPE_2_BETTER
```

The second conversion is better than the first one.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
ConversionComparator.Comparison
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ConversionComparator.Comparison c : ConversionComparator.Comparison.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ConversionComparator.Comparison
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

- INDETERMINATE

```java
public static final
ConversionComparator.Comparison
INDETERMINATE
```

The conversions cannot be compared.

- TYPE_1_BETTER

```java
public static final
ConversionComparator.Comparison
TYPE_1_BETTER
```

The first conversion is better than the second one.

- TYPE_2_BETTER

```java
public static final
ConversionComparator.Comparison
TYPE_2_BETTER
```

The second conversion is better than the first one.

---

#### Enum Constant Detail

INDETERMINATE

```java
public static final
ConversionComparator.Comparison
INDETERMINATE
```

The conversions cannot be compared.

---

#### INDETERMINATE

public static final

ConversionComparator.Comparison

INDETERMINATE

The conversions cannot be compared.

TYPE_1_BETTER

```java
public static final
ConversionComparator.Comparison
TYPE_1_BETTER
```

The first conversion is better than the second one.

---

#### TYPE_1_BETTER

public static final

ConversionComparator.Comparison

TYPE_1_BETTER

The first conversion is better than the second one.

TYPE_2_BETTER

```java
public static final
ConversionComparator.Comparison
TYPE_2_BETTER
```

The second conversion is better than the first one.

---

#### TYPE_2_BETTER

public static final

ConversionComparator.Comparison

TYPE_2_BETTER

The second conversion is better than the first one.

Method Detail

- values

```java
public static
ConversionComparator.Comparison
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ConversionComparator.Comparison c : ConversionComparator.Comparison.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ConversionComparator.Comparison
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
ConversionComparator.Comparison
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ConversionComparator.Comparison c : ConversionComparator.Comparison.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

ConversionComparator.Comparison

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ConversionComparator.Comparison c : ConversionComparator.Comparison.values())
System.out.println(c);
```

for (ConversionComparator.Comparison c : ConversionComparator.Comparison.values())
System.out.println(c);

valueOf

```java
public static
ConversionComparator.Comparison
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

ConversionComparator.Comparison

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

