# Enum AttributeTree.ValueKind

**Source:** `jdk.compiler\com\sun\source\doctree\AttributeTree.ValueKind.html`

### Class Description

```java
public static enum
AttributeTree.ValueKind

extends
Enum
<
AttributeTree.ValueKind
>
```

The kind of an attribute value.

**All Implemented Interfaces:** Serializable

,

Comparable

<

AttributeTree.ValueKind

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
AttributeTree.ValueKind
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AttributeTree.ValueKind c : AttributeTree.ValueKind.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
AttributeTree.ValueKind
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

#### Enum AttributeTree.ValueKind

java.lang.Object

- java.lang.Enum

<

AttributeTree.ValueKind

>
- - com.sun.source.doctree.AttributeTree.ValueKind

java.lang.Enum

<

AttributeTree.ValueKind

>

- com.sun.source.doctree.AttributeTree.ValueKind

com.sun.source.doctree.AttributeTree.ValueKind

**All Implemented Interfaces:** Serializable

,

Comparable

<

AttributeTree.ValueKind

>

**Enclosing interface:** AttributeTree

```java
public static enum
AttributeTree.ValueKind

extends
Enum
<
AttributeTree.ValueKind
>
```

The kind of an attribute value.

public static enum

AttributeTree.ValueKind

extends

Enum

<

AttributeTree.ValueKind

>

The kind of an attribute value.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

DOUBLE

The attribute value is enclosed in double quotation marks.

EMPTY

The attribute value is empty.

SINGLE

The attribute value is enclosed in single quotation marks.

UNQUOTED

The attribute value is not enclosed in quotes.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

AttributeTree.ValueKind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

AttributeTree.ValueKind

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

DOUBLE

The attribute value is enclosed in double quotation marks.

EMPTY

The attribute value is empty.

SINGLE

The attribute value is enclosed in single quotation marks.

UNQUOTED

The attribute value is not enclosed in quotes.

---

#### Enum Constant Summary

The attribute value is enclosed in double quotation marks.

The attribute value is empty.

The attribute value is enclosed in single quotation marks.

The attribute value is not enclosed in quotes.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

AttributeTree.ValueKind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

AttributeTree.ValueKind

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

- EMPTY

```java
public static final
AttributeTree.ValueKind
EMPTY
```

The attribute value is empty.

- UNQUOTED

```java
public static final
AttributeTree.ValueKind
UNQUOTED
```

The attribute value is not enclosed in quotes.

- SINGLE

```java
public static final
AttributeTree.ValueKind
SINGLE
```

The attribute value is enclosed in single quotation marks.

- DOUBLE

```java
public static final
AttributeTree.ValueKind
DOUBLE
```

The attribute value is enclosed in double quotation marks.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
AttributeTree.ValueKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AttributeTree.ValueKind c : AttributeTree.ValueKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
AttributeTree.ValueKind
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

- EMPTY

```java
public static final
AttributeTree.ValueKind
EMPTY
```

The attribute value is empty.

- UNQUOTED

```java
public static final
AttributeTree.ValueKind
UNQUOTED
```

The attribute value is not enclosed in quotes.

- SINGLE

```java
public static final
AttributeTree.ValueKind
SINGLE
```

The attribute value is enclosed in single quotation marks.

- DOUBLE

```java
public static final
AttributeTree.ValueKind
DOUBLE
```

The attribute value is enclosed in double quotation marks.

---

#### Enum Constant Detail

EMPTY

```java
public static final
AttributeTree.ValueKind
EMPTY
```

The attribute value is empty.

---

#### EMPTY

public static final

AttributeTree.ValueKind

EMPTY

The attribute value is empty.

UNQUOTED

```java
public static final
AttributeTree.ValueKind
UNQUOTED
```

The attribute value is not enclosed in quotes.

---

#### UNQUOTED

public static final

AttributeTree.ValueKind

UNQUOTED

The attribute value is not enclosed in quotes.

SINGLE

```java
public static final
AttributeTree.ValueKind
SINGLE
```

The attribute value is enclosed in single quotation marks.

---

#### SINGLE

public static final

AttributeTree.ValueKind

SINGLE

The attribute value is enclosed in single quotation marks.

DOUBLE

```java
public static final
AttributeTree.ValueKind
DOUBLE
```

The attribute value is enclosed in double quotation marks.

---

#### DOUBLE

public static final

AttributeTree.ValueKind

DOUBLE

The attribute value is enclosed in double quotation marks.

Method Detail

- values

```java
public static
AttributeTree.ValueKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AttributeTree.ValueKind c : AttributeTree.ValueKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
AttributeTree.ValueKind
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
AttributeTree.ValueKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AttributeTree.ValueKind c : AttributeTree.ValueKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

AttributeTree.ValueKind

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AttributeTree.ValueKind c : AttributeTree.ValueKind.values())
System.out.println(c);
```

for (AttributeTree.ValueKind c : AttributeTree.ValueKind.values())
System.out.println(c);

valueOf

```java
public static
AttributeTree.ValueKind
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

AttributeTree.ValueKind

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

