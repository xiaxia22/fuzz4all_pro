# Enum MultipleGradientPaint.CycleMethod

**Source:** `java.desktop\java\awt\MultipleGradientPaint.CycleMethod.html`

### Class Description

```java
public static enum
MultipleGradientPaint.CycleMethod

extends
Enum
<
MultipleGradientPaint.CycleMethod
>
```

The method to use when painting outside the gradient bounds.

**All Implemented Interfaces:** Serializable

,

Comparable

<

MultipleGradientPaint.CycleMethod

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
MultipleGradientPaint.CycleMethod
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MultipleGradientPaint.CycleMethod c : MultipleGradientPaint.CycleMethod.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
MultipleGradientPaint.CycleMethod
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

#### Enum MultipleGradientPaint.CycleMethod

java.lang.Object

- java.lang.Enum

<

MultipleGradientPaint.CycleMethod

>
- - java.awt.MultipleGradientPaint.CycleMethod

java.lang.Enum

<

MultipleGradientPaint.CycleMethod

>

- java.awt.MultipleGradientPaint.CycleMethod

java.awt.MultipleGradientPaint.CycleMethod

**All Implemented Interfaces:** Serializable

,

Comparable

<

MultipleGradientPaint.CycleMethod

>

**Enclosing class:** MultipleGradientPaint

```java
public static enum
MultipleGradientPaint.CycleMethod

extends
Enum
<
MultipleGradientPaint.CycleMethod
>
```

The method to use when painting outside the gradient bounds.

**Since:** 1.6

public static enum

MultipleGradientPaint.CycleMethod

extends

Enum

<

MultipleGradientPaint.CycleMethod

>

The method to use when painting outside the gradient bounds.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

NO_CYCLE

Use the terminal colors to fill the remaining area.

REFLECT

Cycle the gradient colors start-to-end, end-to-start
to fill the remaining area.

REPEAT

Cycle the gradient colors start-to-end, start-to-end
to fill the remaining area.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

MultipleGradientPaint.CycleMethod

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

MultipleGradientPaint.CycleMethod

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

NO_CYCLE

Use the terminal colors to fill the remaining area.

REFLECT

Cycle the gradient colors start-to-end, end-to-start
to fill the remaining area.

REPEAT

Cycle the gradient colors start-to-end, start-to-end
to fill the remaining area.

---

#### Enum Constant Summary

Use the terminal colors to fill the remaining area.

Cycle the gradient colors start-to-end, end-to-start
to fill the remaining area.

Cycle the gradient colors start-to-end, start-to-end
to fill the remaining area.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

MultipleGradientPaint.CycleMethod

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

MultipleGradientPaint.CycleMethod

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

- NO_CYCLE

```java
public static final
MultipleGradientPaint.CycleMethod
NO_CYCLE
```

Use the terminal colors to fill the remaining area.

- REFLECT

```java
public static final
MultipleGradientPaint.CycleMethod
REFLECT
```

Cycle the gradient colors start-to-end, end-to-start
to fill the remaining area.

- REPEAT

```java
public static final
MultipleGradientPaint.CycleMethod
REPEAT
```

Cycle the gradient colors start-to-end, start-to-end
to fill the remaining area.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
MultipleGradientPaint.CycleMethod
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MultipleGradientPaint.CycleMethod c : MultipleGradientPaint.CycleMethod.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
MultipleGradientPaint.CycleMethod
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

- NO_CYCLE

```java
public static final
MultipleGradientPaint.CycleMethod
NO_CYCLE
```

Use the terminal colors to fill the remaining area.

- REFLECT

```java
public static final
MultipleGradientPaint.CycleMethod
REFLECT
```

Cycle the gradient colors start-to-end, end-to-start
to fill the remaining area.

- REPEAT

```java
public static final
MultipleGradientPaint.CycleMethod
REPEAT
```

Cycle the gradient colors start-to-end, start-to-end
to fill the remaining area.

---

#### Enum Constant Detail

NO_CYCLE

```java
public static final
MultipleGradientPaint.CycleMethod
NO_CYCLE
```

Use the terminal colors to fill the remaining area.

---

#### NO_CYCLE

public static final

MultipleGradientPaint.CycleMethod

NO_CYCLE

Use the terminal colors to fill the remaining area.

REFLECT

```java
public static final
MultipleGradientPaint.CycleMethod
REFLECT
```

Cycle the gradient colors start-to-end, end-to-start
to fill the remaining area.

---

#### REFLECT

public static final

MultipleGradientPaint.CycleMethod

REFLECT

Cycle the gradient colors start-to-end, end-to-start
to fill the remaining area.

REPEAT

```java
public static final
MultipleGradientPaint.CycleMethod
REPEAT
```

Cycle the gradient colors start-to-end, start-to-end
to fill the remaining area.

---

#### REPEAT

public static final

MultipleGradientPaint.CycleMethod

REPEAT

Cycle the gradient colors start-to-end, start-to-end
to fill the remaining area.

Method Detail

- values

```java
public static
MultipleGradientPaint.CycleMethod
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MultipleGradientPaint.CycleMethod c : MultipleGradientPaint.CycleMethod.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
MultipleGradientPaint.CycleMethod
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
MultipleGradientPaint.CycleMethod
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MultipleGradientPaint.CycleMethod c : MultipleGradientPaint.CycleMethod.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

MultipleGradientPaint.CycleMethod

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MultipleGradientPaint.CycleMethod c : MultipleGradientPaint.CycleMethod.values())
System.out.println(c);
```

for (MultipleGradientPaint.CycleMethod c : MultipleGradientPaint.CycleMethod.values())
System.out.println(c);

valueOf

```java
public static
MultipleGradientPaint.CycleMethod
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

MultipleGradientPaint.CycleMethod

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

