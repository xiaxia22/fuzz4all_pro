# Enum ProcessBuilder.Redirect.Type

**Source:** `java.base\java\lang\ProcessBuilder.Redirect.Type.html`

### Class Description

```java
public static enum
ProcessBuilder.Redirect.Type

extends
Enum
<
ProcessBuilder.Redirect.Type
>
```

The type of a

ProcessBuilder.Redirect

.

**All Implemented Interfaces:** Serializable

,

Comparable

<

ProcessBuilder.Redirect.Type

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ProcessBuilder.Redirect.Type
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ProcessBuilder.Redirect.Type c : ProcessBuilder.Redirect.Type.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
ProcessBuilder.Redirect.Type
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

#### Enum ProcessBuilder.Redirect.Type

java.lang.Object

- java.lang.Enum

<

ProcessBuilder.Redirect.Type

>
- - java.lang.ProcessBuilder.Redirect.Type

java.lang.Enum

<

ProcessBuilder.Redirect.Type

>

- java.lang.ProcessBuilder.Redirect.Type

java.lang.ProcessBuilder.Redirect.Type

**All Implemented Interfaces:** Serializable

,

Comparable

<

ProcessBuilder.Redirect.Type

>

**Enclosing class:** ProcessBuilder.Redirect

```java
public static enum
ProcessBuilder.Redirect.Type

extends
Enum
<
ProcessBuilder.Redirect.Type
>
```

The type of a

ProcessBuilder.Redirect

.

public static enum

ProcessBuilder.Redirect.Type

extends

Enum

<

ProcessBuilder.Redirect.Type

>

The type of a

ProcessBuilder.Redirect

.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

APPEND

The type of redirects returned from

Redirect.appendTo(File)

.

INHERIT

The type of

Redirect.INHERIT

.

PIPE

The type of

Redirect.PIPE

.

READ

The type of redirects returned from

Redirect.from(File)

.

WRITE

The type of redirects returned from

Redirect.to(File)

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ProcessBuilder.Redirect.Type

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ProcessBuilder.Redirect.Type

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

APPEND

The type of redirects returned from

Redirect.appendTo(File)

.

INHERIT

The type of

Redirect.INHERIT

.

PIPE

The type of

Redirect.PIPE

.

READ

The type of redirects returned from

Redirect.from(File)

.

WRITE

The type of redirects returned from

Redirect.to(File)

.

---

#### Enum Constant Summary

The type of redirects returned from

Redirect.appendTo(File)

.

The type of

Redirect.INHERIT

.

The type of

Redirect.PIPE

.

The type of redirects returned from

Redirect.from(File)

.

The type of redirects returned from

Redirect.to(File)

.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ProcessBuilder.Redirect.Type

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ProcessBuilder.Redirect.Type

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

- PIPE

```java
public static final
ProcessBuilder.Redirect.Type
PIPE
```

The type of

Redirect.PIPE

.

- INHERIT

```java
public static final
ProcessBuilder.Redirect.Type
INHERIT
```

The type of

Redirect.INHERIT

.

- READ

```java
public static final
ProcessBuilder.Redirect.Type
READ
```

The type of redirects returned from

Redirect.from(File)

.

- WRITE

```java
public static final
ProcessBuilder.Redirect.Type
WRITE
```

The type of redirects returned from

Redirect.to(File)

.

- APPEND

```java
public static final
ProcessBuilder.Redirect.Type
APPEND
```

The type of redirects returned from

Redirect.appendTo(File)

.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
ProcessBuilder.Redirect.Type
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ProcessBuilder.Redirect.Type c : ProcessBuilder.Redirect.Type.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ProcessBuilder.Redirect.Type
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

- PIPE

```java
public static final
ProcessBuilder.Redirect.Type
PIPE
```

The type of

Redirect.PIPE

.

- INHERIT

```java
public static final
ProcessBuilder.Redirect.Type
INHERIT
```

The type of

Redirect.INHERIT

.

- READ

```java
public static final
ProcessBuilder.Redirect.Type
READ
```

The type of redirects returned from

Redirect.from(File)

.

- WRITE

```java
public static final
ProcessBuilder.Redirect.Type
WRITE
```

The type of redirects returned from

Redirect.to(File)

.

- APPEND

```java
public static final
ProcessBuilder.Redirect.Type
APPEND
```

The type of redirects returned from

Redirect.appendTo(File)

.

---

#### Enum Constant Detail

PIPE

```java
public static final
ProcessBuilder.Redirect.Type
PIPE
```

The type of

Redirect.PIPE

.

---

#### PIPE

public static final

ProcessBuilder.Redirect.Type

PIPE

The type of

Redirect.PIPE

.

INHERIT

```java
public static final
ProcessBuilder.Redirect.Type
INHERIT
```

The type of

Redirect.INHERIT

.

---

#### INHERIT

public static final

ProcessBuilder.Redirect.Type

INHERIT

The type of

Redirect.INHERIT

.

READ

```java
public static final
ProcessBuilder.Redirect.Type
READ
```

The type of redirects returned from

Redirect.from(File)

.

---

#### READ

public static final

ProcessBuilder.Redirect.Type

READ

The type of redirects returned from

Redirect.from(File)

.

WRITE

```java
public static final
ProcessBuilder.Redirect.Type
WRITE
```

The type of redirects returned from

Redirect.to(File)

.

---

#### WRITE

public static final

ProcessBuilder.Redirect.Type

WRITE

The type of redirects returned from

Redirect.to(File)

.

APPEND

```java
public static final
ProcessBuilder.Redirect.Type
APPEND
```

The type of redirects returned from

Redirect.appendTo(File)

.

---

#### APPEND

public static final

ProcessBuilder.Redirect.Type

APPEND

The type of redirects returned from

Redirect.appendTo(File)

.

Method Detail

- values

```java
public static
ProcessBuilder.Redirect.Type
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ProcessBuilder.Redirect.Type c : ProcessBuilder.Redirect.Type.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ProcessBuilder.Redirect.Type
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
ProcessBuilder.Redirect.Type
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ProcessBuilder.Redirect.Type c : ProcessBuilder.Redirect.Type.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

ProcessBuilder.Redirect.Type

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ProcessBuilder.Redirect.Type c : ProcessBuilder.Redirect.Type.values())
System.out.println(c);
```

for (ProcessBuilder.Redirect.Type c : ProcessBuilder.Redirect.Type.values())
System.out.println(c);

valueOf

```java
public static
ProcessBuilder.Redirect.Type
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

ProcessBuilder.Redirect.Type

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

