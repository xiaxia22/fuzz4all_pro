# Enum Locale.Category

**Source:** `java.base\java\util\Locale.Category.html`

### Class Description

```java
public static enum
Locale.Category

extends
Enum
<
Locale.Category
>
```

Enum for locale categories. These locale categories are used to get/set
the default locale for the specific functionality represented by the
category.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Locale.Category

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Locale.Category
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Locale.Category c : Locale.Category.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Locale.Category
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

#### Enum Locale.Category

java.lang.Object

- java.lang.Enum

<

Locale.Category

>
- - java.util.Locale.Category

java.lang.Enum

<

Locale.Category

>

- java.util.Locale.Category

java.util.Locale.Category

**All Implemented Interfaces:** Serializable

,

Comparable

<

Locale.Category

>

**Enclosing class:** Locale

```java
public static enum
Locale.Category

extends
Enum
<
Locale.Category
>
```

Enum for locale categories. These locale categories are used to get/set
the default locale for the specific functionality represented by the
category.

**Since:** 1.7
**See Also:** Locale.getDefault(Locale.Category)

,

Locale.setDefault(Locale.Category, Locale)

public static enum

Locale.Category

extends

Enum

<

Locale.Category

>

Enum for locale categories. These locale categories are used to get/set
the default locale for the specific functionality represented by the
category.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

DISPLAY

Category used to represent the default locale for
displaying user interfaces.

FORMAT

Category used to represent the default locale for
formatting dates, numbers, and/or currencies.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Locale.Category

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Locale.Category

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

DISPLAY

Category used to represent the default locale for
displaying user interfaces.

FORMAT

Category used to represent the default locale for
formatting dates, numbers, and/or currencies.

---

#### Enum Constant Summary

Category used to represent the default locale for
displaying user interfaces.

Category used to represent the default locale for
formatting dates, numbers, and/or currencies.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Locale.Category

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Locale.Category

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

- DISPLAY

```java
public static final
Locale.Category
DISPLAY
```

Category used to represent the default locale for
displaying user interfaces.

- FORMAT

```java
public static final
Locale.Category
FORMAT
```

Category used to represent the default locale for
formatting dates, numbers, and/or currencies.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Locale.Category
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Locale.Category c : Locale.Category.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Locale.Category
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

- DISPLAY

```java
public static final
Locale.Category
DISPLAY
```

Category used to represent the default locale for
displaying user interfaces.

- FORMAT

```java
public static final
Locale.Category
FORMAT
```

Category used to represent the default locale for
formatting dates, numbers, and/or currencies.

---

#### Enum Constant Detail

DISPLAY

```java
public static final
Locale.Category
DISPLAY
```

Category used to represent the default locale for
displaying user interfaces.

---

#### DISPLAY

public static final

Locale.Category

DISPLAY

Category used to represent the default locale for
displaying user interfaces.

FORMAT

```java
public static final
Locale.Category
FORMAT
```

Category used to represent the default locale for
formatting dates, numbers, and/or currencies.

---

#### FORMAT

public static final

Locale.Category

FORMAT

Category used to represent the default locale for
formatting dates, numbers, and/or currencies.

Method Detail

- values

```java
public static
Locale.Category
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Locale.Category c : Locale.Category.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Locale.Category
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
Locale.Category
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Locale.Category c : Locale.Category.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Locale.Category

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Locale.Category c : Locale.Category.values())
System.out.println(c);
```

for (Locale.Category c : Locale.Category.values())
System.out.println(c);

valueOf

```java
public static
Locale.Category
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

Locale.Category

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

