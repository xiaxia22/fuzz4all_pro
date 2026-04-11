# Enum LayoutStyle.ComponentPlacement

**Source:** `java.desktop\javax\swing\LayoutStyle.ComponentPlacement.html`

### Class Description

```java
public static enum
LayoutStyle.ComponentPlacement

extends
Enum
<
LayoutStyle.ComponentPlacement
>
```

ComponentPlacement

is an enumeration of the
possible ways two components can be placed relative to each
other.

ComponentPlacement

is used by the

LayoutStyle

method

getPreferredGap

. Refer to

LayoutStyle

for more information.

**All Implemented Interfaces:** Serializable

,

Comparable

<

LayoutStyle.ComponentPlacement

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
LayoutStyle.ComponentPlacement
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LayoutStyle.ComponentPlacement c : LayoutStyle.ComponentPlacement.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
LayoutStyle.ComponentPlacement
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

#### Enum LayoutStyle.ComponentPlacement

java.lang.Object

- java.lang.Enum

<

LayoutStyle.ComponentPlacement

>
- - javax.swing.LayoutStyle.ComponentPlacement

java.lang.Enum

<

LayoutStyle.ComponentPlacement

>

- javax.swing.LayoutStyle.ComponentPlacement

javax.swing.LayoutStyle.ComponentPlacement

**All Implemented Interfaces:** Serializable

,

Comparable

<

LayoutStyle.ComponentPlacement

>

**Enclosing class:** LayoutStyle

```java
public static enum
LayoutStyle.ComponentPlacement

extends
Enum
<
LayoutStyle.ComponentPlacement
>
```

ComponentPlacement

is an enumeration of the
possible ways two components can be placed relative to each
other.

ComponentPlacement

is used by the

LayoutStyle

method

getPreferredGap

. Refer to

LayoutStyle

for more information.

**Since:** 1.6
**See Also:** LayoutStyle.getPreferredGap(JComponent,JComponent,
ComponentPlacement,int,Container)

public static enum

LayoutStyle.ComponentPlacement

extends

Enum

<

LayoutStyle.ComponentPlacement

>

ComponentPlacement

is an enumeration of the
possible ways two components can be placed relative to each
other.

ComponentPlacement

is used by the

LayoutStyle

method

getPreferredGap

. Refer to

LayoutStyle

for more information.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

INDENT

Enumeration value indicating the distance to indent a component
is being requested.

RELATED

Enumeration value indicating the two components are
visually related and will be placed in the same parent.

UNRELATED

Enumeration value indicating the two components are
visually unrelated and will be placed in the same parent.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

LayoutStyle.ComponentPlacement

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

LayoutStyle.ComponentPlacement

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

INDENT

Enumeration value indicating the distance to indent a component
is being requested.

RELATED

Enumeration value indicating the two components are
visually related and will be placed in the same parent.

UNRELATED

Enumeration value indicating the two components are
visually unrelated and will be placed in the same parent.

---

#### Enum Constant Summary

Enumeration value indicating the distance to indent a component
is being requested.

Enumeration value indicating the two components are
visually related and will be placed in the same parent.

Enumeration value indicating the two components are
visually unrelated and will be placed in the same parent.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

LayoutStyle.ComponentPlacement

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

LayoutStyle.ComponentPlacement

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

- RELATED

```java
public static final
LayoutStyle.ComponentPlacement
RELATED
```

Enumeration value indicating the two components are
visually related and will be placed in the same parent.
For example, a

JLabel

providing a label for a

JTextField

is typically visually associated
with the

JTextField

; the constant

RELATED

is used for this.

- UNRELATED

```java
public static final
LayoutStyle.ComponentPlacement
UNRELATED
```

Enumeration value indicating the two components are
visually unrelated and will be placed in the same parent.
For example, groupings of components are usually visually
separated; the constant

UNRELATED

is used for this.

- INDENT

```java
public static final
LayoutStyle.ComponentPlacement
INDENT
```

Enumeration value indicating the distance to indent a component
is being requested. For example, often times the children of
a label will be horizontally indented from the label. To determine
the preferred distance for such a gap use the

INDENT

type.

This value is typically only useful with a direction of

EAST

or

WEST

.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
LayoutStyle.ComponentPlacement
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LayoutStyle.ComponentPlacement c : LayoutStyle.ComponentPlacement.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
LayoutStyle.ComponentPlacement
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

- RELATED

```java
public static final
LayoutStyle.ComponentPlacement
RELATED
```

Enumeration value indicating the two components are
visually related and will be placed in the same parent.
For example, a

JLabel

providing a label for a

JTextField

is typically visually associated
with the

JTextField

; the constant

RELATED

is used for this.

- UNRELATED

```java
public static final
LayoutStyle.ComponentPlacement
UNRELATED
```

Enumeration value indicating the two components are
visually unrelated and will be placed in the same parent.
For example, groupings of components are usually visually
separated; the constant

UNRELATED

is used for this.

- INDENT

```java
public static final
LayoutStyle.ComponentPlacement
INDENT
```

Enumeration value indicating the distance to indent a component
is being requested. For example, often times the children of
a label will be horizontally indented from the label. To determine
the preferred distance for such a gap use the

INDENT

type.

This value is typically only useful with a direction of

EAST

or

WEST

.

---

#### Enum Constant Detail

RELATED

```java
public static final
LayoutStyle.ComponentPlacement
RELATED
```

Enumeration value indicating the two components are
visually related and will be placed in the same parent.
For example, a

JLabel

providing a label for a

JTextField

is typically visually associated
with the

JTextField

; the constant

RELATED

is used for this.

---

#### RELATED

public static final

LayoutStyle.ComponentPlacement

RELATED

Enumeration value indicating the two components are
visually related and will be placed in the same parent.
For example, a

JLabel

providing a label for a

JTextField

is typically visually associated
with the

JTextField

; the constant

RELATED

is used for this.

UNRELATED

```java
public static final
LayoutStyle.ComponentPlacement
UNRELATED
```

Enumeration value indicating the two components are
visually unrelated and will be placed in the same parent.
For example, groupings of components are usually visually
separated; the constant

UNRELATED

is used for this.

---

#### UNRELATED

public static final

LayoutStyle.ComponentPlacement

UNRELATED

Enumeration value indicating the two components are
visually unrelated and will be placed in the same parent.
For example, groupings of components are usually visually
separated; the constant

UNRELATED

is used for this.

INDENT

```java
public static final
LayoutStyle.ComponentPlacement
INDENT
```

Enumeration value indicating the distance to indent a component
is being requested. For example, often times the children of
a label will be horizontally indented from the label. To determine
the preferred distance for such a gap use the

INDENT

type.

This value is typically only useful with a direction of

EAST

or

WEST

.

---

#### INDENT

public static final

LayoutStyle.ComponentPlacement

INDENT

Enumeration value indicating the distance to indent a component
is being requested. For example, often times the children of
a label will be horizontally indented from the label. To determine
the preferred distance for such a gap use the

INDENT

type.

This value is typically only useful with a direction of

EAST

or

WEST

.

This value is typically only useful with a direction of

EAST

or

WEST

.

Method Detail

- values

```java
public static
LayoutStyle.ComponentPlacement
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LayoutStyle.ComponentPlacement c : LayoutStyle.ComponentPlacement.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
LayoutStyle.ComponentPlacement
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
LayoutStyle.ComponentPlacement
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LayoutStyle.ComponentPlacement c : LayoutStyle.ComponentPlacement.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

LayoutStyle.ComponentPlacement

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LayoutStyle.ComponentPlacement c : LayoutStyle.ComponentPlacement.values())
System.out.println(c);
```

for (LayoutStyle.ComponentPlacement c : LayoutStyle.ComponentPlacement.values())
System.out.println(c);

valueOf

```java
public static
LayoutStyle.ComponentPlacement
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

LayoutStyle.ComponentPlacement

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

