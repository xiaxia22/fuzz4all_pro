# Enum MemberReferenceTree.ReferenceMode

**Source:** `jdk.compiler\com\sun\source\tree\MemberReferenceTree.ReferenceMode.html`

### Class Description

```java
public static enum
MemberReferenceTree.ReferenceMode

extends
Enum
<
MemberReferenceTree.ReferenceMode
>
```

There are two kinds of member references: (i) method references and
(ii) constructor references

**All Implemented Interfaces:** Serializable

,

Comparable

<

MemberReferenceTree.ReferenceMode

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
MemberReferenceTree.ReferenceMode
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MemberReferenceTree.ReferenceMode c : MemberReferenceTree.ReferenceMode.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
MemberReferenceTree.ReferenceMode
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

#### Enum MemberReferenceTree.ReferenceMode

java.lang.Object

- java.lang.Enum

<

MemberReferenceTree.ReferenceMode

>
- - com.sun.source.tree.MemberReferenceTree.ReferenceMode

java.lang.Enum

<

MemberReferenceTree.ReferenceMode

>

- com.sun.source.tree.MemberReferenceTree.ReferenceMode

com.sun.source.tree.MemberReferenceTree.ReferenceMode

**All Implemented Interfaces:** Serializable

,

Comparable

<

MemberReferenceTree.ReferenceMode

>

**Enclosing interface:** MemberReferenceTree

```java
public static enum
MemberReferenceTree.ReferenceMode

extends
Enum
<
MemberReferenceTree.ReferenceMode
>
```

There are two kinds of member references: (i) method references and
(ii) constructor references

public static enum

MemberReferenceTree.ReferenceMode

extends

Enum

<

MemberReferenceTree.ReferenceMode

>

There are two kinds of member references: (i) method references and
(ii) constructor references

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

INVOKE

enum constant for method references.

NEW

enum constant for constructor references.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

MemberReferenceTree.ReferenceMode

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

MemberReferenceTree.ReferenceMode

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

INVOKE

enum constant for method references.

NEW

enum constant for constructor references.

---

#### Enum Constant Summary

enum constant for method references.

enum constant for constructor references.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

MemberReferenceTree.ReferenceMode

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

MemberReferenceTree.ReferenceMode

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

- INVOKE

```java
public static final
MemberReferenceTree.ReferenceMode
INVOKE
```

enum constant for method references.

- NEW

```java
public static final
MemberReferenceTree.ReferenceMode
NEW
```

enum constant for constructor references.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
MemberReferenceTree.ReferenceMode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MemberReferenceTree.ReferenceMode c : MemberReferenceTree.ReferenceMode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
MemberReferenceTree.ReferenceMode
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

- INVOKE

```java
public static final
MemberReferenceTree.ReferenceMode
INVOKE
```

enum constant for method references.

- NEW

```java
public static final
MemberReferenceTree.ReferenceMode
NEW
```

enum constant for constructor references.

---

#### Enum Constant Detail

INVOKE

```java
public static final
MemberReferenceTree.ReferenceMode
INVOKE
```

enum constant for method references.

---

#### INVOKE

public static final

MemberReferenceTree.ReferenceMode

INVOKE

enum constant for method references.

NEW

```java
public static final
MemberReferenceTree.ReferenceMode
NEW
```

enum constant for constructor references.

---

#### NEW

public static final

MemberReferenceTree.ReferenceMode

NEW

enum constant for constructor references.

Method Detail

- values

```java
public static
MemberReferenceTree.ReferenceMode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MemberReferenceTree.ReferenceMode c : MemberReferenceTree.ReferenceMode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
MemberReferenceTree.ReferenceMode
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
MemberReferenceTree.ReferenceMode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MemberReferenceTree.ReferenceMode c : MemberReferenceTree.ReferenceMode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

MemberReferenceTree.ReferenceMode

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MemberReferenceTree.ReferenceMode c : MemberReferenceTree.ReferenceMode.values())
System.out.println(c);
```

for (MemberReferenceTree.ReferenceMode c : MemberReferenceTree.ReferenceMode.values())
System.out.println(c);

valueOf

```java
public static
MemberReferenceTree.ReferenceMode
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

MemberReferenceTree.ReferenceMode

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

