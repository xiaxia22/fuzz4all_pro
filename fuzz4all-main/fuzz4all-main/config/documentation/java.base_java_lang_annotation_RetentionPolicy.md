# Enum RetentionPolicy

**Source:** `java.base\java\lang\annotation\RetentionPolicy.html`

### Class Description

```java
public enum
RetentionPolicy

extends
Enum
<
RetentionPolicy
>
```

Annotation retention policy. The constants of this enumerated type
describe the various policies for retaining annotations. They are used
in conjunction with the

Retention

meta-annotation type to specify
how long annotations are to be retained.

**All Implemented Interfaces:** Serializable

,

Comparable

<

RetentionPolicy

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
RetentionPolicy
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RetentionPolicy c : RetentionPolicy.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
RetentionPolicy
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

#### Enum RetentionPolicy

java.lang.Object

- java.lang.Enum

<

RetentionPolicy

>
- - java.lang.annotation.RetentionPolicy

java.lang.Enum

<

RetentionPolicy

>

- java.lang.annotation.RetentionPolicy

java.lang.annotation.RetentionPolicy

**All Implemented Interfaces:** Serializable

,

Comparable

<

RetentionPolicy

>

```java
public enum
RetentionPolicy

extends
Enum
<
RetentionPolicy
>
```

Annotation retention policy. The constants of this enumerated type
describe the various policies for retaining annotations. They are used
in conjunction with the

Retention

meta-annotation type to specify
how long annotations are to be retained.

**Since:** 1.5

public enum

RetentionPolicy

extends

Enum

<

RetentionPolicy

>

Annotation retention policy. The constants of this enumerated type
describe the various policies for retaining annotations. They are used
in conjunction with the

Retention

meta-annotation type to specify
how long annotations are to be retained.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

CLASS

Annotations are to be recorded in the class file by the compiler
but need not be retained by the VM at run time.

RUNTIME

Annotations are to be recorded in the class file by the compiler and
retained by the VM at run time, so they may be read reflectively.

SOURCE

Annotations are to be discarded by the compiler.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

RetentionPolicy

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

RetentionPolicy

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

CLASS

Annotations are to be recorded in the class file by the compiler
but need not be retained by the VM at run time.

RUNTIME

Annotations are to be recorded in the class file by the compiler and
retained by the VM at run time, so they may be read reflectively.

SOURCE

Annotations are to be discarded by the compiler.

---

#### Enum Constant Summary

Annotations are to be recorded in the class file by the compiler
but need not be retained by the VM at run time.

Annotations are to be recorded in the class file by the compiler and
retained by the VM at run time, so they may be read reflectively.

Annotations are to be discarded by the compiler.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

RetentionPolicy

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

RetentionPolicy

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

- SOURCE

```java
public static final
RetentionPolicy
SOURCE
```

Annotations are to be discarded by the compiler.

- CLASS

```java
public static final
RetentionPolicy
CLASS
```

Annotations are to be recorded in the class file by the compiler
but need not be retained by the VM at run time. This is the default
behavior.

- RUNTIME

```java
public static final
RetentionPolicy
RUNTIME
```

Annotations are to be recorded in the class file by the compiler and
retained by the VM at run time, so they may be read reflectively.

**See Also:** AnnotatedElement

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
RetentionPolicy
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RetentionPolicy c : RetentionPolicy.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
RetentionPolicy
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

- SOURCE

```java
public static final
RetentionPolicy
SOURCE
```

Annotations are to be discarded by the compiler.

- CLASS

```java
public static final
RetentionPolicy
CLASS
```

Annotations are to be recorded in the class file by the compiler
but need not be retained by the VM at run time. This is the default
behavior.

- RUNTIME

```java
public static final
RetentionPolicy
RUNTIME
```

Annotations are to be recorded in the class file by the compiler and
retained by the VM at run time, so they may be read reflectively.

**See Also:** AnnotatedElement

---

#### Enum Constant Detail

SOURCE

```java
public static final
RetentionPolicy
SOURCE
```

Annotations are to be discarded by the compiler.

---

#### SOURCE

public static final

RetentionPolicy

SOURCE

Annotations are to be discarded by the compiler.

CLASS

```java
public static final
RetentionPolicy
CLASS
```

Annotations are to be recorded in the class file by the compiler
but need not be retained by the VM at run time. This is the default
behavior.

---

#### CLASS

public static final

RetentionPolicy

CLASS

Annotations are to be recorded in the class file by the compiler
but need not be retained by the VM at run time. This is the default
behavior.

RUNTIME

```java
public static final
RetentionPolicy
RUNTIME
```

Annotations are to be recorded in the class file by the compiler and
retained by the VM at run time, so they may be read reflectively.

**See Also:** AnnotatedElement

---

#### RUNTIME

public static final

RetentionPolicy

RUNTIME

Annotations are to be recorded in the class file by the compiler and
retained by the VM at run time, so they may be read reflectively.

Method Detail

- values

```java
public static
RetentionPolicy
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RetentionPolicy c : RetentionPolicy.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
RetentionPolicy
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
RetentionPolicy
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RetentionPolicy c : RetentionPolicy.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

RetentionPolicy

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RetentionPolicy c : RetentionPolicy.values())
System.out.println(c);
```

for (RetentionPolicy c : RetentionPolicy.values())
System.out.println(c);

valueOf

```java
public static
RetentionPolicy
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

RetentionPolicy

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

