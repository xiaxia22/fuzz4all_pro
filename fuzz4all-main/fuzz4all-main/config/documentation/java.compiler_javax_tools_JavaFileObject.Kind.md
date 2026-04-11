# Enum JavaFileObject.Kind

**Source:** `java.compiler\javax\tools\JavaFileObject.Kind.html`

### Class Description

```java
public static enum
JavaFileObject.Kind

extends
Enum
<
JavaFileObject.Kind
>
```

Kinds of JavaFileObjects.

**All Implemented Interfaces:** Serializable

,

Comparable

<

JavaFileObject.Kind

>

---

### Field Details

#### public final
String
extension

The extension which (by convention) is normally used for
this kind of file object. If no convention exists, the
empty string (

""

) is used.

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
JavaFileObject.Kind
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JavaFileObject.Kind c : JavaFileObject.Kind.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
JavaFileObject.Kind
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

#### Enum JavaFileObject.Kind

java.lang.Object

- java.lang.Enum

<

JavaFileObject.Kind

>
- - javax.tools.JavaFileObject.Kind

java.lang.Enum

<

JavaFileObject.Kind

>

- javax.tools.JavaFileObject.Kind

javax.tools.JavaFileObject.Kind

**All Implemented Interfaces:** Serializable

,

Comparable

<

JavaFileObject.Kind

>

**Enclosing interface:** JavaFileObject

```java
public static enum
JavaFileObject.Kind

extends
Enum
<
JavaFileObject.Kind
>
```

Kinds of JavaFileObjects.

public static enum

JavaFileObject.Kind

extends

Enum

<

JavaFileObject.Kind

>

Kinds of JavaFileObjects.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

CLASS

Class files for the Java Virtual Machine.

HTML

HTML files.

OTHER

Any other kind.

SOURCE

Source files written in the Java programming language.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

String

extension

The extension which (by convention) is normally used for
this kind of file object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

JavaFileObject.Kind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

JavaFileObject.Kind

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

Class files for the Java Virtual Machine.

HTML

HTML files.

OTHER

Any other kind.

SOURCE

Source files written in the Java programming language.

---

#### Enum Constant Summary

Class files for the Java Virtual Machine.

HTML files.

Any other kind.

Source files written in the Java programming language.

Field Summary

Fields

Modifier and Type

Field

Description

String

extension

The extension which (by convention) is normally used for
this kind of file object.

---

#### Field Summary

The extension which (by convention) is normally used for
this kind of file object.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

JavaFileObject.Kind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

JavaFileObject.Kind

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
JavaFileObject.Kind
SOURCE
```

Source files written in the Java programming language. For
example, regular files ending with

.java

.

- CLASS

```java
public static final
JavaFileObject.Kind
CLASS
```

Class files for the Java Virtual Machine. For example,
regular files ending with

.class

.

- HTML

```java
public static final
JavaFileObject.Kind
HTML
```

HTML files. For example, regular files ending with

.html

.

- OTHER

```java
public static final
JavaFileObject.Kind
OTHER
```

Any other kind.

============ FIELD DETAIL ===========

- Field Detail

- extension

```java
public final
String
extension
```

The extension which (by convention) is normally used for
this kind of file object. If no convention exists, the
empty string (

""

) is used.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
JavaFileObject.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JavaFileObject.Kind c : JavaFileObject.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
JavaFileObject.Kind
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
JavaFileObject.Kind
SOURCE
```

Source files written in the Java programming language. For
example, regular files ending with

.java

.

- CLASS

```java
public static final
JavaFileObject.Kind
CLASS
```

Class files for the Java Virtual Machine. For example,
regular files ending with

.class

.

- HTML

```java
public static final
JavaFileObject.Kind
HTML
```

HTML files. For example, regular files ending with

.html

.

- OTHER

```java
public static final
JavaFileObject.Kind
OTHER
```

Any other kind.

---

#### Enum Constant Detail

SOURCE

```java
public static final
JavaFileObject.Kind
SOURCE
```

Source files written in the Java programming language. For
example, regular files ending with

.java

.

---

#### SOURCE

public static final

JavaFileObject.Kind

SOURCE

Source files written in the Java programming language. For
example, regular files ending with

.java

.

CLASS

```java
public static final
JavaFileObject.Kind
CLASS
```

Class files for the Java Virtual Machine. For example,
regular files ending with

.class

.

---

#### CLASS

public static final

JavaFileObject.Kind

CLASS

Class files for the Java Virtual Machine. For example,
regular files ending with

.class

.

HTML

```java
public static final
JavaFileObject.Kind
HTML
```

HTML files. For example, regular files ending with

.html

.

---

#### HTML

public static final

JavaFileObject.Kind

HTML

HTML files. For example, regular files ending with

.html

.

OTHER

```java
public static final
JavaFileObject.Kind
OTHER
```

Any other kind.

---

#### OTHER

public static final

JavaFileObject.Kind

OTHER

Any other kind.

Field Detail

- extension

```java
public final
String
extension
```

The extension which (by convention) is normally used for
this kind of file object. If no convention exists, the
empty string (

""

) is used.

---

#### Field Detail

extension

```java
public final
String
extension
```

The extension which (by convention) is normally used for
this kind of file object. If no convention exists, the
empty string (

""

) is used.

---

#### extension

public final

String

extension

The extension which (by convention) is normally used for
this kind of file object. If no convention exists, the
empty string (

""

) is used.

Method Detail

- values

```java
public static
JavaFileObject.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JavaFileObject.Kind c : JavaFileObject.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
JavaFileObject.Kind
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
JavaFileObject.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JavaFileObject.Kind c : JavaFileObject.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

JavaFileObject.Kind

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JavaFileObject.Kind c : JavaFileObject.Kind.values())
System.out.println(c);
```

for (JavaFileObject.Kind c : JavaFileObject.Kind.values())
System.out.println(c);

valueOf

```java
public static
JavaFileObject.Kind
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

JavaFileObject.Kind

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

