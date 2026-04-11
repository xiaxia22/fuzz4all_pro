# Enum GroupLayout.Alignment

**Source:** `java.desktop\javax\swing\GroupLayout.Alignment.html`

### Class Description

```java
public static enum
GroupLayout.Alignment

extends
Enum
<
GroupLayout.Alignment
>
```

Enumeration of the possible ways

ParallelGroup

can align
its children.

**All Implemented Interfaces:** Serializable

,

Comparable

<

GroupLayout.Alignment

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
GroupLayout.Alignment
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (GroupLayout.Alignment c : GroupLayout.Alignment.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
GroupLayout.Alignment
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

#### Enum GroupLayout.Alignment

java.lang.Object

- java.lang.Enum

<

GroupLayout.Alignment

>
- - javax.swing.GroupLayout.Alignment

java.lang.Enum

<

GroupLayout.Alignment

>

- javax.swing.GroupLayout.Alignment

javax.swing.GroupLayout.Alignment

**All Implemented Interfaces:** Serializable

,

Comparable

<

GroupLayout.Alignment

>

**Enclosing class:** GroupLayout

```java
public static enum
GroupLayout.Alignment

extends
Enum
<
GroupLayout.Alignment
>
```

Enumeration of the possible ways

ParallelGroup

can align
its children.

**Since:** 1.6
**See Also:** GroupLayout.createParallelGroup(Alignment)

public static enum

GroupLayout.Alignment

extends

Enum

<

GroupLayout.Alignment

>

Enumeration of the possible ways

ParallelGroup

can align
its children.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

BASELINE

Indicates the elements should be aligned along
their baseline.

CENTER

Indicates the elements should be centered in
the region.

LEADING

Indicates the elements should be
aligned to the origin.

TRAILING

Indicates the elements should be aligned to the end of the
region.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

GroupLayout.Alignment

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

GroupLayout.Alignment

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

BASELINE

Indicates the elements should be aligned along
their baseline.

CENTER

Indicates the elements should be centered in
the region.

LEADING

Indicates the elements should be
aligned to the origin.

TRAILING

Indicates the elements should be aligned to the end of the
region.

---

#### Enum Constant Summary

Indicates the elements should be aligned along
their baseline.

Indicates the elements should be centered in
the region.

Indicates the elements should be
aligned to the origin.

Indicates the elements should be aligned to the end of the
region.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

GroupLayout.Alignment

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

GroupLayout.Alignment

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

- LEADING

```java
public static final
GroupLayout.Alignment
LEADING
```

Indicates the elements should be
aligned to the origin. For the horizontal axis with a left to
right orientation this means aligned to the left edge. For the
vertical axis leading means aligned to the top edge.

**See Also:** GroupLayout.createParallelGroup(Alignment)

- TRAILING

```java
public static final
GroupLayout.Alignment
TRAILING
```

Indicates the elements should be aligned to the end of the
region. For the horizontal axis with a left to right
orientation this means aligned to the right edge. For the
vertical axis trailing means aligned to the bottom edge.

**See Also:** GroupLayout.createParallelGroup(Alignment)

- CENTER

```java
public static final
GroupLayout.Alignment
CENTER
```

Indicates the elements should be centered in
the region.

**See Also:** GroupLayout.createParallelGroup(Alignment)

- BASELINE

```java
public static final
GroupLayout.Alignment
BASELINE
```

Indicates the elements should be aligned along
their baseline.

**See Also:** GroupLayout.createParallelGroup(Alignment)

,

GroupLayout.createBaselineGroup(boolean,boolean)

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
GroupLayout.Alignment
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (GroupLayout.Alignment c : GroupLayout.Alignment.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
GroupLayout.Alignment
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

- LEADING

```java
public static final
GroupLayout.Alignment
LEADING
```

Indicates the elements should be
aligned to the origin. For the horizontal axis with a left to
right orientation this means aligned to the left edge. For the
vertical axis leading means aligned to the top edge.

**See Also:** GroupLayout.createParallelGroup(Alignment)

- TRAILING

```java
public static final
GroupLayout.Alignment
TRAILING
```

Indicates the elements should be aligned to the end of the
region. For the horizontal axis with a left to right
orientation this means aligned to the right edge. For the
vertical axis trailing means aligned to the bottom edge.

**See Also:** GroupLayout.createParallelGroup(Alignment)

- CENTER

```java
public static final
GroupLayout.Alignment
CENTER
```

Indicates the elements should be centered in
the region.

**See Also:** GroupLayout.createParallelGroup(Alignment)

- BASELINE

```java
public static final
GroupLayout.Alignment
BASELINE
```

Indicates the elements should be aligned along
their baseline.

**See Also:** GroupLayout.createParallelGroup(Alignment)

,

GroupLayout.createBaselineGroup(boolean,boolean)

---

#### Enum Constant Detail

LEADING

```java
public static final
GroupLayout.Alignment
LEADING
```

Indicates the elements should be
aligned to the origin. For the horizontal axis with a left to
right orientation this means aligned to the left edge. For the
vertical axis leading means aligned to the top edge.

**See Also:** GroupLayout.createParallelGroup(Alignment)

---

#### LEADING

public static final

GroupLayout.Alignment

LEADING

Indicates the elements should be
aligned to the origin. For the horizontal axis with a left to
right orientation this means aligned to the left edge. For the
vertical axis leading means aligned to the top edge.

TRAILING

```java
public static final
GroupLayout.Alignment
TRAILING
```

Indicates the elements should be aligned to the end of the
region. For the horizontal axis with a left to right
orientation this means aligned to the right edge. For the
vertical axis trailing means aligned to the bottom edge.

**See Also:** GroupLayout.createParallelGroup(Alignment)

---

#### TRAILING

public static final

GroupLayout.Alignment

TRAILING

Indicates the elements should be aligned to the end of the
region. For the horizontal axis with a left to right
orientation this means aligned to the right edge. For the
vertical axis trailing means aligned to the bottom edge.

CENTER

```java
public static final
GroupLayout.Alignment
CENTER
```

Indicates the elements should be centered in
the region.

**See Also:** GroupLayout.createParallelGroup(Alignment)

---

#### CENTER

public static final

GroupLayout.Alignment

CENTER

Indicates the elements should be centered in
the region.

BASELINE

```java
public static final
GroupLayout.Alignment
BASELINE
```

Indicates the elements should be aligned along
their baseline.

**See Also:** GroupLayout.createParallelGroup(Alignment)

,

GroupLayout.createBaselineGroup(boolean,boolean)

---

#### BASELINE

public static final

GroupLayout.Alignment

BASELINE

Indicates the elements should be aligned along
their baseline.

Method Detail

- values

```java
public static
GroupLayout.Alignment
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (GroupLayout.Alignment c : GroupLayout.Alignment.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
GroupLayout.Alignment
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
GroupLayout.Alignment
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (GroupLayout.Alignment c : GroupLayout.Alignment.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

GroupLayout.Alignment

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (GroupLayout.Alignment c : GroupLayout.Alignment.values())
System.out.println(c);
```

for (GroupLayout.Alignment c : GroupLayout.Alignment.values())
System.out.println(c);

valueOf

```java
public static
GroupLayout.Alignment
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

GroupLayout.Alignment

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

