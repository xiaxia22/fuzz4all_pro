# Enum Doclet.Option.Kind

**Source:** `jdk.javadoc\jdk\javadoc\doclet\Doclet.Option.Kind.html`

### Class Description

```java
public static enum
Doclet.Option.Kind

extends
Enum
<
Doclet.Option.Kind
>
```

The kind of an option.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Doclet.Option.Kind

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Doclet.Option.Kind
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Doclet.Option.Kind c : Doclet.Option.Kind.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Doclet.Option.Kind
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

#### Enum Doclet.Option.Kind

java.lang.Object

- java.lang.Enum

<

Doclet.Option.Kind

>
- - jdk.javadoc.doclet.Doclet.Option.Kind

java.lang.Enum

<

Doclet.Option.Kind

>

- jdk.javadoc.doclet.Doclet.Option.Kind

jdk.javadoc.doclet.Doclet.Option.Kind

**All Implemented Interfaces:** Serializable

,

Comparable

<

Doclet.Option.Kind

>

**Enclosing interface:** Doclet.Option

```java
public static enum
Doclet.Option.Kind

extends
Enum
<
Doclet.Option.Kind
>
```

The kind of an option.

public static enum

Doclet.Option.Kind

extends

Enum

<

Doclet.Option.Kind

>

The kind of an option.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

EXTENDED

an extended option, such as those prefixed with -X

OTHER

an implementation reserved option

STANDARD

a standard option

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Doclet.Option.Kind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Doclet.Option.Kind

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

EXTENDED

an extended option, such as those prefixed with -X

OTHER

an implementation reserved option

STANDARD

a standard option

---

#### Enum Constant Summary

an extended option, such as those prefixed with -X

an implementation reserved option

a standard option

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Doclet.Option.Kind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Doclet.Option.Kind

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

- EXTENDED

```java
public static final
Doclet.Option.Kind
EXTENDED
```

an extended option, such as those prefixed with -X

- STANDARD

```java
public static final
Doclet.Option.Kind
STANDARD
```

a standard option

- OTHER

```java
public static final
Doclet.Option.Kind
OTHER
```

an implementation reserved option

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Doclet.Option.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Doclet.Option.Kind c : Doclet.Option.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Doclet.Option.Kind
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

- EXTENDED

```java
public static final
Doclet.Option.Kind
EXTENDED
```

an extended option, such as those prefixed with -X

- STANDARD

```java
public static final
Doclet.Option.Kind
STANDARD
```

a standard option

- OTHER

```java
public static final
Doclet.Option.Kind
OTHER
```

an implementation reserved option

---

#### Enum Constant Detail

EXTENDED

```java
public static final
Doclet.Option.Kind
EXTENDED
```

an extended option, such as those prefixed with -X

---

#### EXTENDED

public static final

Doclet.Option.Kind

EXTENDED

an extended option, such as those prefixed with -X

STANDARD

```java
public static final
Doclet.Option.Kind
STANDARD
```

a standard option

---

#### STANDARD

public static final

Doclet.Option.Kind

STANDARD

a standard option

OTHER

```java
public static final
Doclet.Option.Kind
OTHER
```

an implementation reserved option

---

#### OTHER

public static final

Doclet.Option.Kind

OTHER

an implementation reserved option

Method Detail

- values

```java
public static
Doclet.Option.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Doclet.Option.Kind c : Doclet.Option.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Doclet.Option.Kind
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
Doclet.Option.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Doclet.Option.Kind c : Doclet.Option.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Doclet.Option.Kind

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Doclet.Option.Kind c : Doclet.Option.Kind.values())
System.out.println(c);
```

for (Doclet.Option.Kind c : Doclet.Option.Kind.values())
System.out.println(c);

valueOf

```java
public static
Doclet.Option.Kind
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

Doclet.Option.Kind

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

