# Enum Modifier

**Source:** `java.compiler\javax\lang\model\element\Modifier.html`

### Class Description

```java
public enum
Modifier

extends
Enum
<
Modifier
>
```

Represents a modifier on a program element such
as a class, method, or field.

Not all modifiers are applicable to all kinds of elements.
When two or more modifiers appear in the source code of an element
then it is customary, though not required, that they appear in the same
order as the constants listed in the detail section below.

Note that it is possible additional modifiers will be added in
future versions of the platform.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Modifier

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Modifier
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Modifier c : Modifier.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Modifier
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

#### public
String
toString()

Returns this modifier's name in lowercase.

**Overrides:**
- toString

in class

Enum

<

Modifier

>

**Returns:**
- the name of this enum constant

---

### Additional Sections

#### Enum Modifier

java.lang.Object

- java.lang.Enum

<

Modifier

>
- - javax.lang.model.element.Modifier

java.lang.Enum

<

Modifier

>

- javax.lang.model.element.Modifier

javax.lang.model.element.Modifier

**All Implemented Interfaces:** Serializable

,

Comparable

<

Modifier

>

```java
public enum
Modifier

extends
Enum
<
Modifier
>
```

Represents a modifier on a program element such
as a class, method, or field.

Not all modifiers are applicable to all kinds of elements.
When two or more modifiers appear in the source code of an element
then it is customary, though not required, that they appear in the same
order as the constants listed in the detail section below.

Note that it is possible additional modifiers will be added in
future versions of the platform.

**Since:** 1.6

public enum

Modifier

extends

Enum

<

Modifier

>

Represents a modifier on a program element such
as a class, method, or field.

Not all modifiers are applicable to all kinds of elements.
When two or more modifiers appear in the source code of an element
then it is customary, though not required, that they appear in the same
order as the constants listed in the detail section below.

Note that it is possible additional modifiers will be added in
future versions of the platform.

Not all modifiers are applicable to all kinds of elements.
When two or more modifiers appear in the source code of an element
then it is customary, though not required, that they appear in the same
order as the constants listed in the detail section below.

Note that it is possible additional modifiers will be added in
future versions of the platform.

Note that it is possible additional modifiers will be added in
future versions of the platform.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ABSTRACT

The modifier

abstract

DEFAULT

The modifier

default

FINAL

The modifier

final

NATIVE

The modifier

native

PRIVATE

The modifier

private

PROTECTED

The modifier

protected

PUBLIC

The modifier

public

STATIC

The modifier

static

STRICTFP

The modifier

strictfp

SYNCHRONIZED

The modifier

synchronized

TRANSIENT

The modifier

transient

VOLATILE

The modifier

volatile

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

toString

()

Returns this modifier's name in lowercase.

static

Modifier

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Modifier

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

ABSTRACT

The modifier

abstract

DEFAULT

The modifier

default

FINAL

The modifier

final

NATIVE

The modifier

native

PRIVATE

The modifier

private

PROTECTED

The modifier

protected

PUBLIC

The modifier

public

STATIC

The modifier

static

STRICTFP

The modifier

strictfp

SYNCHRONIZED

The modifier

synchronized

TRANSIENT

The modifier

transient

VOLATILE

The modifier

volatile

---

#### Enum Constant Summary

The modifier

abstract

The modifier

default

The modifier

final

The modifier

native

The modifier

private

The modifier

protected

The modifier

public

The modifier

static

The modifier

strictfp

The modifier

synchronized

The modifier

transient

The modifier

volatile

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

toString

()

Returns this modifier's name in lowercase.

static

Modifier

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Modifier

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

Returns this modifier's name in lowercase.

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

- PUBLIC

```java
public static final
Modifier
PUBLIC
```

The modifier

public

- PROTECTED

```java
public static final
Modifier
PROTECTED
```

The modifier

protected

- PRIVATE

```java
public static final
Modifier
PRIVATE
```

The modifier

private

- ABSTRACT

```java
public static final
Modifier
ABSTRACT
```

The modifier

abstract

- DEFAULT

```java
public static final
Modifier
DEFAULT
```

The modifier

default

**Since:** 1.8

- STATIC

```java
public static final
Modifier
STATIC
```

The modifier

static

- FINAL

```java
public static final
Modifier
FINAL
```

The modifier

final

- TRANSIENT

```java
public static final
Modifier
TRANSIENT
```

The modifier

transient

- VOLATILE

```java
public static final
Modifier
VOLATILE
```

The modifier

volatile

- SYNCHRONIZED

```java
public static final
Modifier
SYNCHRONIZED
```

The modifier

synchronized

- NATIVE

```java
public static final
Modifier
NATIVE
```

The modifier

native

- STRICTFP

```java
public static final
Modifier
STRICTFP
```

The modifier

strictfp

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Modifier
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Modifier c : Modifier.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Modifier
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

- toString

```java
public
String
toString()
```

Returns this modifier's name in lowercase.

**Overrides:** toString

in class

Enum

<

Modifier

>
**Returns:** the name of this enum constant

Enum Constant Detail

- PUBLIC

```java
public static final
Modifier
PUBLIC
```

The modifier

public

- PROTECTED

```java
public static final
Modifier
PROTECTED
```

The modifier

protected

- PRIVATE

```java
public static final
Modifier
PRIVATE
```

The modifier

private

- ABSTRACT

```java
public static final
Modifier
ABSTRACT
```

The modifier

abstract

- DEFAULT

```java
public static final
Modifier
DEFAULT
```

The modifier

default

**Since:** 1.8

- STATIC

```java
public static final
Modifier
STATIC
```

The modifier

static

- FINAL

```java
public static final
Modifier
FINAL
```

The modifier

final

- TRANSIENT

```java
public static final
Modifier
TRANSIENT
```

The modifier

transient

- VOLATILE

```java
public static final
Modifier
VOLATILE
```

The modifier

volatile

- SYNCHRONIZED

```java
public static final
Modifier
SYNCHRONIZED
```

The modifier

synchronized

- NATIVE

```java
public static final
Modifier
NATIVE
```

The modifier

native

- STRICTFP

```java
public static final
Modifier
STRICTFP
```

The modifier

strictfp

---

#### Enum Constant Detail

PUBLIC

```java
public static final
Modifier
PUBLIC
```

The modifier

public

---

#### PUBLIC

public static final

Modifier

PUBLIC

The modifier

public

PROTECTED

```java
public static final
Modifier
PROTECTED
```

The modifier

protected

---

#### PROTECTED

public static final

Modifier

PROTECTED

The modifier

protected

PRIVATE

```java
public static final
Modifier
PRIVATE
```

The modifier

private

---

#### PRIVATE

public static final

Modifier

PRIVATE

The modifier

private

ABSTRACT

```java
public static final
Modifier
ABSTRACT
```

The modifier

abstract

---

#### ABSTRACT

public static final

Modifier

ABSTRACT

The modifier

abstract

DEFAULT

```java
public static final
Modifier
DEFAULT
```

The modifier

default

**Since:** 1.8

---

#### DEFAULT

public static final

Modifier

DEFAULT

The modifier

default

STATIC

```java
public static final
Modifier
STATIC
```

The modifier

static

---

#### STATIC

public static final

Modifier

STATIC

The modifier

static

FINAL

```java
public static final
Modifier
FINAL
```

The modifier

final

---

#### FINAL

public static final

Modifier

FINAL

The modifier

final

TRANSIENT

```java
public static final
Modifier
TRANSIENT
```

The modifier

transient

---

#### TRANSIENT

public static final

Modifier

TRANSIENT

The modifier

transient

VOLATILE

```java
public static final
Modifier
VOLATILE
```

The modifier

volatile

---

#### VOLATILE

public static final

Modifier

VOLATILE

The modifier

volatile

SYNCHRONIZED

```java
public static final
Modifier
SYNCHRONIZED
```

The modifier

synchronized

---

#### SYNCHRONIZED

public static final

Modifier

SYNCHRONIZED

The modifier

synchronized

NATIVE

```java
public static final
Modifier
NATIVE
```

The modifier

native

---

#### NATIVE

public static final

Modifier

NATIVE

The modifier

native

STRICTFP

```java
public static final
Modifier
STRICTFP
```

The modifier

strictfp

---

#### STRICTFP

public static final

Modifier

STRICTFP

The modifier

strictfp

Method Detail

- values

```java
public static
Modifier
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Modifier c : Modifier.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Modifier
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

- toString

```java
public
String
toString()
```

Returns this modifier's name in lowercase.

**Overrides:** toString

in class

Enum

<

Modifier

>
**Returns:** the name of this enum constant

---

#### Method Detail

values

```java
public static
Modifier
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Modifier c : Modifier.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Modifier

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Modifier c : Modifier.values())
System.out.println(c);
```

for (Modifier c : Modifier.values())
System.out.println(c);

valueOf

```java
public static
Modifier
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

Modifier

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

toString

```java
public
String
toString()
```

Returns this modifier's name in lowercase.

**Overrides:** toString

in class

Enum

<

Modifier

>
**Returns:** the name of this enum constant

---

#### toString

public

String

toString()

Returns this modifier's name in lowercase.

---

