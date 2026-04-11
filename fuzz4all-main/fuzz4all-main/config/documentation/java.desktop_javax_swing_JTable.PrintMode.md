# Enum JTable.PrintMode

**Source:** `java.desktop\javax\swing\JTable.PrintMode.html`

### Class Description

```java
public static enum
JTable.PrintMode

extends
Enum
<
JTable.PrintMode
>
```

Printing modes, used in printing

JTable

s.

**All Implemented Interfaces:** Serializable

,

Comparable

<

JTable.PrintMode

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
JTable.PrintMode
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JTable.PrintMode c : JTable.PrintMode.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
JTable.PrintMode
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

#### Enum JTable.PrintMode

java.lang.Object

- java.lang.Enum

<

JTable.PrintMode

>
- - javax.swing.JTable.PrintMode

java.lang.Enum

<

JTable.PrintMode

>

- javax.swing.JTable.PrintMode

javax.swing.JTable.PrintMode

**All Implemented Interfaces:** Serializable

,

Comparable

<

JTable.PrintMode

>

**Enclosing class:** JTable

```java
public static enum
JTable.PrintMode

extends
Enum
<
JTable.PrintMode
>
```

Printing modes, used in printing

JTable

s.

**Since:** 1.5
**See Also:** JTable.print(JTable.PrintMode, MessageFormat, MessageFormat,
boolean, PrintRequestAttributeSet, boolean)

,

JTable.getPrintable(javax.swing.JTable.PrintMode, java.text.MessageFormat, java.text.MessageFormat)

public static enum

JTable.PrintMode

extends

Enum

<

JTable.PrintMode

>

Printing modes, used in printing

JTable

s.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

FIT_WIDTH

Printing mode that scales the output smaller, if necessary,
to fit the table's entire width (and thereby all columns) on each page;
Rows are spread across multiple pages as necessary.

NORMAL

Printing mode that prints the table at its current size,
spreading both columns and rows across multiple pages if necessary.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

JTable.PrintMode

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

JTable.PrintMode

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

FIT_WIDTH

Printing mode that scales the output smaller, if necessary,
to fit the table's entire width (and thereby all columns) on each page;
Rows are spread across multiple pages as necessary.

NORMAL

Printing mode that prints the table at its current size,
spreading both columns and rows across multiple pages if necessary.

---

#### Enum Constant Summary

Printing mode that scales the output smaller, if necessary,
to fit the table's entire width (and thereby all columns) on each page;
Rows are spread across multiple pages as necessary.

Printing mode that prints the table at its current size,
spreading both columns and rows across multiple pages if necessary.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

JTable.PrintMode

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

JTable.PrintMode

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

- NORMAL

```java
public static final
JTable.PrintMode
NORMAL
```

Printing mode that prints the table at its current size,
spreading both columns and rows across multiple pages if necessary.

- FIT_WIDTH

```java
public static final
JTable.PrintMode
FIT_WIDTH
```

Printing mode that scales the output smaller, if necessary,
to fit the table's entire width (and thereby all columns) on each page;
Rows are spread across multiple pages as necessary.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
JTable.PrintMode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JTable.PrintMode c : JTable.PrintMode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
JTable.PrintMode
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

- NORMAL

```java
public static final
JTable.PrintMode
NORMAL
```

Printing mode that prints the table at its current size,
spreading both columns and rows across multiple pages if necessary.

- FIT_WIDTH

```java
public static final
JTable.PrintMode
FIT_WIDTH
```

Printing mode that scales the output smaller, if necessary,
to fit the table's entire width (and thereby all columns) on each page;
Rows are spread across multiple pages as necessary.

---

#### Enum Constant Detail

NORMAL

```java
public static final
JTable.PrintMode
NORMAL
```

Printing mode that prints the table at its current size,
spreading both columns and rows across multiple pages if necessary.

---

#### NORMAL

public static final

JTable.PrintMode

NORMAL

Printing mode that prints the table at its current size,
spreading both columns and rows across multiple pages if necessary.

FIT_WIDTH

```java
public static final
JTable.PrintMode
FIT_WIDTH
```

Printing mode that scales the output smaller, if necessary,
to fit the table's entire width (and thereby all columns) on each page;
Rows are spread across multiple pages as necessary.

---

#### FIT_WIDTH

public static final

JTable.PrintMode

FIT_WIDTH

Printing mode that scales the output smaller, if necessary,
to fit the table's entire width (and thereby all columns) on each page;
Rows are spread across multiple pages as necessary.

Method Detail

- values

```java
public static
JTable.PrintMode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JTable.PrintMode c : JTable.PrintMode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
JTable.PrintMode
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
JTable.PrintMode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JTable.PrintMode c : JTable.PrintMode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

JTable.PrintMode

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JTable.PrintMode c : JTable.PrintMode.values())
System.out.println(c);
```

for (JTable.PrintMode c : JTable.PrintMode.values())
System.out.println(c);

valueOf

```java
public static
JTable.PrintMode
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

JTable.PrintMode

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

