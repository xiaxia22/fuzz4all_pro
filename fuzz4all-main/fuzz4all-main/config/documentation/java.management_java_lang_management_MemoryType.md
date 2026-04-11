# Enum MemoryType

**Source:** `java.management\java\lang\management\MemoryType.html`

### Class Description

```java
public enum
MemoryType

extends
Enum
<
MemoryType
>
```

Types of

memory pools

.

**All Implemented Interfaces:** Serializable

,

Comparable

<

MemoryType

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
MemoryType
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MemoryType c : MemoryType.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
MemoryType
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

Returns the string representation of this

MemoryType

.

**Overrides:**
- toString

in class

Enum

<

MemoryType

>

**Returns:**
- the string representation of this

MemoryType

.

---

### Additional Sections

#### Enum MemoryType

java.lang.Object

- java.lang.Enum

<

MemoryType

>
- - java.lang.management.MemoryType

java.lang.Enum

<

MemoryType

>

- java.lang.management.MemoryType

java.lang.management.MemoryType

**All Implemented Interfaces:** Serializable

,

Comparable

<

MemoryType

>

```java
public enum
MemoryType

extends
Enum
<
MemoryType
>
```

Types of

memory pools

.

**Since:** 1.5

public enum

MemoryType

extends

Enum

<

MemoryType

>

Types of

memory pools

.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

HEAP

Heap memory type.

NON_HEAP

Non-heap memory type.

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

Returns the string representation of this

MemoryType

.

static

MemoryType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

MemoryType

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

HEAP

Heap memory type.

NON_HEAP

Non-heap memory type.

---

#### Enum Constant Summary

Heap memory type.

Non-heap memory type.

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

Returns the string representation of this

MemoryType

.

static

MemoryType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

MemoryType

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

Returns the string representation of this

MemoryType

.

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

- HEAP

```java
public static final
MemoryType
HEAP
```

Heap memory type.

The Java virtual machine has a

heap

that is the runtime data area from which
memory for all class instances and arrays are allocated.

- NON_HEAP

```java
public static final
MemoryType
NON_HEAP
```

Non-heap memory type.

The Java virtual machine manages memory other than the heap
(referred as

non-heap memory

). The non-heap memory includes
the

method area

and memory required for the internal
processing or optimization for the Java virtual machine.
It stores per-class structures such as a runtime
constant pool, field and method data, and the code for
methods and constructors.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
MemoryType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MemoryType c : MemoryType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
MemoryType
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

Returns the string representation of this

MemoryType

.

**Overrides:** toString

in class

Enum

<

MemoryType

>
**Returns:** the string representation of this

MemoryType

.

Enum Constant Detail

- HEAP

```java
public static final
MemoryType
HEAP
```

Heap memory type.

The Java virtual machine has a

heap

that is the runtime data area from which
memory for all class instances and arrays are allocated.

- NON_HEAP

```java
public static final
MemoryType
NON_HEAP
```

Non-heap memory type.

The Java virtual machine manages memory other than the heap
(referred as

non-heap memory

). The non-heap memory includes
the

method area

and memory required for the internal
processing or optimization for the Java virtual machine.
It stores per-class structures such as a runtime
constant pool, field and method data, and the code for
methods and constructors.

---

#### Enum Constant Detail

HEAP

```java
public static final
MemoryType
HEAP
```

Heap memory type.

The Java virtual machine has a

heap

that is the runtime data area from which
memory for all class instances and arrays are allocated.

---

#### HEAP

public static final

MemoryType

HEAP

Heap memory type.

The Java virtual machine has a

heap

that is the runtime data area from which
memory for all class instances and arrays are allocated.

The Java virtual machine has a

heap

that is the runtime data area from which
memory for all class instances and arrays are allocated.

NON_HEAP

```java
public static final
MemoryType
NON_HEAP
```

Non-heap memory type.

The Java virtual machine manages memory other than the heap
(referred as

non-heap memory

). The non-heap memory includes
the

method area

and memory required for the internal
processing or optimization for the Java virtual machine.
It stores per-class structures such as a runtime
constant pool, field and method data, and the code for
methods and constructors.

---

#### NON_HEAP

public static final

MemoryType

NON_HEAP

Non-heap memory type.

The Java virtual machine manages memory other than the heap
(referred as

non-heap memory

). The non-heap memory includes
the

method area

and memory required for the internal
processing or optimization for the Java virtual machine.
It stores per-class structures such as a runtime
constant pool, field and method data, and the code for
methods and constructors.

The Java virtual machine manages memory other than the heap
(referred as

non-heap memory

). The non-heap memory includes
the

method area

and memory required for the internal
processing or optimization for the Java virtual machine.
It stores per-class structures such as a runtime
constant pool, field and method data, and the code for
methods and constructors.

Method Detail

- values

```java
public static
MemoryType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MemoryType c : MemoryType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
MemoryType
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

Returns the string representation of this

MemoryType

.

**Overrides:** toString

in class

Enum

<

MemoryType

>
**Returns:** the string representation of this

MemoryType

.

---

#### Method Detail

values

```java
public static
MemoryType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MemoryType c : MemoryType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

MemoryType

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MemoryType c : MemoryType.values())
System.out.println(c);
```

for (MemoryType c : MemoryType.values())
System.out.println(c);

valueOf

```java
public static
MemoryType
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

MemoryType

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

Returns the string representation of this

MemoryType

.

**Overrides:** toString

in class

Enum

<

MemoryType

>
**Returns:** the string representation of this

MemoryType

.

---

#### toString

public

String

toString()

Returns the string representation of this

MemoryType

.

---

