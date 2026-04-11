# Enum DocumentationTool.Location

**Source:** `java.compiler\javax\tools\DocumentationTool.Location.html`

### Class Description

```java
public static enum
DocumentationTool.Location

extends
Enum
<
DocumentationTool.Location
>
implements
JavaFileManager.Location
```

Locations specific to

DocumentationTool

.

**All Implemented Interfaces:** Serializable

,

Comparable

<

DocumentationTool.Location

>

,

JavaFileManager.Location

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
DocumentationTool.Location
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DocumentationTool.Location c : DocumentationTool.Location.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
DocumentationTool.Location
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

#### Enum DocumentationTool.Location

java.lang.Object

- java.lang.Enum

<

DocumentationTool.Location

>
- - javax.tools.DocumentationTool.Location

java.lang.Enum

<

DocumentationTool.Location

>

- javax.tools.DocumentationTool.Location

javax.tools.DocumentationTool.Location

**All Implemented Interfaces:** Serializable

,

Comparable

<

DocumentationTool.Location

>

,

JavaFileManager.Location

**Enclosing interface:** DocumentationTool

```java
public static enum
DocumentationTool.Location

extends
Enum
<
DocumentationTool.Location
>
implements
JavaFileManager.Location
```

Locations specific to

DocumentationTool

.

**See Also:** StandardLocation

public static enum

DocumentationTool.Location

extends

Enum

<

DocumentationTool.Location

>
implements

JavaFileManager.Location

Locations specific to

DocumentationTool

.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

DOCLET_PATH

Location to search for doclets.

DOCUMENTATION_OUTPUT

Location of new documentation files.

TAGLET_PATH

Location to search for taglets.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

DocumentationTool.Location

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

DocumentationTool.Location

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

- Methods declared in interface javax.tools.

JavaFileManager.Location

getName

,

isModuleOrientedLocation

,

isOutputLocation

Enum Constant Summary

Enum Constants

Enum Constant

Description

DOCLET_PATH

Location to search for doclets.

DOCUMENTATION_OUTPUT

Location of new documentation files.

TAGLET_PATH

Location to search for taglets.

---

#### Enum Constant Summary

Location to search for doclets.

Location of new documentation files.

Location to search for taglets.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

DocumentationTool.Location

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

DocumentationTool.Location

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

- Methods declared in interface javax.tools.

JavaFileManager.Location

getName

,

isModuleOrientedLocation

,

isOutputLocation

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

Methods declared in interface javax.tools.

JavaFileManager.Location

getName

,

isModuleOrientedLocation

,

isOutputLocation

---

#### Methods declared in interface javax.tools. JavaFileManager.Location

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- DOCUMENTATION_OUTPUT

```java
public static final
DocumentationTool.Location
DOCUMENTATION_OUTPUT
```

Location of new documentation files.

- DOCLET_PATH

```java
public static final
DocumentationTool.Location
DOCLET_PATH
```

Location to search for doclets.

- TAGLET_PATH

```java
public static final
DocumentationTool.Location
TAGLET_PATH
```

Location to search for taglets.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
DocumentationTool.Location
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DocumentationTool.Location c : DocumentationTool.Location.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
DocumentationTool.Location
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

- DOCUMENTATION_OUTPUT

```java
public static final
DocumentationTool.Location
DOCUMENTATION_OUTPUT
```

Location of new documentation files.

- DOCLET_PATH

```java
public static final
DocumentationTool.Location
DOCLET_PATH
```

Location to search for doclets.

- TAGLET_PATH

```java
public static final
DocumentationTool.Location
TAGLET_PATH
```

Location to search for taglets.

---

#### Enum Constant Detail

DOCUMENTATION_OUTPUT

```java
public static final
DocumentationTool.Location
DOCUMENTATION_OUTPUT
```

Location of new documentation files.

---

#### DOCUMENTATION_OUTPUT

public static final

DocumentationTool.Location

DOCUMENTATION_OUTPUT

Location of new documentation files.

DOCLET_PATH

```java
public static final
DocumentationTool.Location
DOCLET_PATH
```

Location to search for doclets.

---

#### DOCLET_PATH

public static final

DocumentationTool.Location

DOCLET_PATH

Location to search for doclets.

TAGLET_PATH

```java
public static final
DocumentationTool.Location
TAGLET_PATH
```

Location to search for taglets.

---

#### TAGLET_PATH

public static final

DocumentationTool.Location

TAGLET_PATH

Location to search for taglets.

Method Detail

- values

```java
public static
DocumentationTool.Location
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DocumentationTool.Location c : DocumentationTool.Location.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
DocumentationTool.Location
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
DocumentationTool.Location
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DocumentationTool.Location c : DocumentationTool.Location.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

DocumentationTool.Location

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DocumentationTool.Location c : DocumentationTool.Location.values())
System.out.println(c);
```

for (DocumentationTool.Location c : DocumentationTool.Location.values())
System.out.println(c);

valueOf

```java
public static
DocumentationTool.Location
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

DocumentationTool.Location

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

