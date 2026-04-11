# Enum Diagnostic.Kind

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\Diagnostic.Kind.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public static enum
Diagnostic.Kind

extends
Enum
<
Diagnostic.Kind
>
```

Kinds of diagnostics, for example, error or warning.

The kind of a diagnostic can be used to determine how the
diagnostic should be presented to the user. For example,
errors might be colored red or prefixed with the word "Error",
while warnings might be colored yellow or prefixed with the
word "Warning". There is no requirement that the Kind
should imply any inherent semantic meaning to the message
of the diagnostic: for example, a tool might provide an
option to report all warnings as errors.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Diagnostic.Kind

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Diagnostic.Kind
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Diagnostic.Kind c : Diagnostic.Kind.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Diagnostic.Kind
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

#### Enum Diagnostic.Kind

java.lang.Object

- java.lang.Enum

<

Diagnostic.Kind

>
- - jdk.nashorn.api.tree.Diagnostic.Kind

java.lang.Enum

<

Diagnostic.Kind

>

- jdk.nashorn.api.tree.Diagnostic.Kind

jdk.nashorn.api.tree.Diagnostic.Kind

**All Implemented Interfaces:** Serializable

,

Comparable

<

Diagnostic.Kind

>

**Enclosing interface:** Diagnostic

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public static enum
Diagnostic.Kind

extends
Enum
<
Diagnostic.Kind
>
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

Kinds of diagnostics, for example, error or warning.

The kind of a diagnostic can be used to determine how the
diagnostic should be presented to the user. For example,
errors might be colored red or prefixed with the word "Error",
while warnings might be colored yellow or prefixed with the
word "Warning". There is no requirement that the Kind
should imply any inherent semantic meaning to the message
of the diagnostic: for example, a tool might provide an
option to report all warnings as errors.

@Deprecated

(

since

="11",

forRemoval

=true)
public static enum

Diagnostic.Kind

extends

Enum

<

Diagnostic.Kind

>

Kinds of diagnostics, for example, error or warning.

The kind of a diagnostic can be used to determine how the
diagnostic should be presented to the user. For example,
errors might be colored red or prefixed with the word "Error",
while warnings might be colored yellow or prefixed with the
word "Warning". There is no requirement that the Kind
should imply any inherent semantic meaning to the message
of the diagnostic: for example, a tool might provide an
option to report all warnings as errors.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ERROR

Deprecated, for removal: This API element is subject to removal in a future version.

Problem which prevents the tool's normal completion.

MANDATORY_WARNING

Deprecated, for removal: This API element is subject to removal in a future version.

Problem similar to a warning, but is mandated by the tool's
specification.

NOTE

Deprecated, for removal: This API element is subject to removal in a future version.

Informative message from the tool.

OTHER

Deprecated, for removal: This API element is subject to removal in a future version.

Diagnostic which does not fit within the other kinds.

WARNING

Deprecated, for removal: This API element is subject to removal in a future version.

Problem which does not usually prevent the tool from
completing normally.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

Diagnostic.Kind

valueOf

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the enum constant of this type with the specified name.

static

Diagnostic.Kind

[]

values

()

Deprecated, for removal: This API element is subject to removal in a future version.

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

ERROR

Deprecated, for removal: This API element is subject to removal in a future version.

Problem which prevents the tool's normal completion.

MANDATORY_WARNING

Deprecated, for removal: This API element is subject to removal in a future version.

Problem similar to a warning, but is mandated by the tool's
specification.

NOTE

Deprecated, for removal: This API element is subject to removal in a future version.

Informative message from the tool.

OTHER

Deprecated, for removal: This API element is subject to removal in a future version.

Diagnostic which does not fit within the other kinds.

WARNING

Deprecated, for removal: This API element is subject to removal in a future version.

Problem which does not usually prevent the tool from
completing normally.

---

#### Enum Constant Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Problem which prevents the tool's normal completion.

Problem similar to a warning, but is mandated by the tool's
specification.

Informative message from the tool.

Diagnostic which does not fit within the other kinds.

Problem which does not usually prevent the tool from
completing normally.

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

Diagnostic.Kind

valueOf

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the enum constant of this type with the specified name.

static

Diagnostic.Kind

[]

values

()

Deprecated, for removal: This API element is subject to removal in a future version.

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

Deprecated, for removal: This API element is subject to removal in a future version.

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

- ERROR

```java
public static final
Diagnostic.Kind
ERROR
```

Deprecated, for removal: This API element is subject to removal in a future version.

Problem which prevents the tool's normal completion.

- WARNING

```java
public static final
Diagnostic.Kind
WARNING
```

Deprecated, for removal: This API element is subject to removal in a future version.

Problem which does not usually prevent the tool from
completing normally.

- MANDATORY_WARNING

```java
public static final
Diagnostic.Kind
MANDATORY_WARNING
```

Deprecated, for removal: This API element is subject to removal in a future version.

Problem similar to a warning, but is mandated by the tool's
specification. For example, the Java™ Language
Specification mandates warnings on certain
unchecked operations and the use of deprecated methods.

- NOTE

```java
public static final
Diagnostic.Kind
NOTE
```

Deprecated, for removal: This API element is subject to removal in a future version.

Informative message from the tool.

- OTHER

```java
public static final
Diagnostic.Kind
OTHER
```

Deprecated, for removal: This API element is subject to removal in a future version.

Diagnostic which does not fit within the other kinds.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Diagnostic.Kind
[] values()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Diagnostic.Kind c : Diagnostic.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Diagnostic.Kind
valueOf​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

- ERROR

```java
public static final
Diagnostic.Kind
ERROR
```

Deprecated, for removal: This API element is subject to removal in a future version.

Problem which prevents the tool's normal completion.

- WARNING

```java
public static final
Diagnostic.Kind
WARNING
```

Deprecated, for removal: This API element is subject to removal in a future version.

Problem which does not usually prevent the tool from
completing normally.

- MANDATORY_WARNING

```java
public static final
Diagnostic.Kind
MANDATORY_WARNING
```

Deprecated, for removal: This API element is subject to removal in a future version.

Problem similar to a warning, but is mandated by the tool's
specification. For example, the Java™ Language
Specification mandates warnings on certain
unchecked operations and the use of deprecated methods.

- NOTE

```java
public static final
Diagnostic.Kind
NOTE
```

Deprecated, for removal: This API element is subject to removal in a future version.

Informative message from the tool.

- OTHER

```java
public static final
Diagnostic.Kind
OTHER
```

Deprecated, for removal: This API element is subject to removal in a future version.

Diagnostic which does not fit within the other kinds.

---

#### Enum Constant Detail

ERROR

```java
public static final
Diagnostic.Kind
ERROR
```

Deprecated, for removal: This API element is subject to removal in a future version.

Problem which prevents the tool's normal completion.

---

#### ERROR

public static final

Diagnostic.Kind

ERROR

Problem which prevents the tool's normal completion.

WARNING

```java
public static final
Diagnostic.Kind
WARNING
```

Deprecated, for removal: This API element is subject to removal in a future version.

Problem which does not usually prevent the tool from
completing normally.

---

#### WARNING

public static final

Diagnostic.Kind

WARNING

Problem which does not usually prevent the tool from
completing normally.

MANDATORY_WARNING

```java
public static final
Diagnostic.Kind
MANDATORY_WARNING
```

Deprecated, for removal: This API element is subject to removal in a future version.

Problem similar to a warning, but is mandated by the tool's
specification. For example, the Java™ Language
Specification mandates warnings on certain
unchecked operations and the use of deprecated methods.

---

#### MANDATORY_WARNING

public static final

Diagnostic.Kind

MANDATORY_WARNING

Problem similar to a warning, but is mandated by the tool's
specification. For example, the Java™ Language
Specification mandates warnings on certain
unchecked operations and the use of deprecated methods.

NOTE

```java
public static final
Diagnostic.Kind
NOTE
```

Deprecated, for removal: This API element is subject to removal in a future version.

Informative message from the tool.

---

#### NOTE

public static final

Diagnostic.Kind

NOTE

Informative message from the tool.

OTHER

```java
public static final
Diagnostic.Kind
OTHER
```

Deprecated, for removal: This API element is subject to removal in a future version.

Diagnostic which does not fit within the other kinds.

---

#### OTHER

public static final

Diagnostic.Kind

OTHER

Diagnostic which does not fit within the other kinds.

Method Detail

- values

```java
public static
Diagnostic.Kind
[] values()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Diagnostic.Kind c : Diagnostic.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Diagnostic.Kind
valueOf​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

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
Diagnostic.Kind
[] values()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Diagnostic.Kind c : Diagnostic.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Diagnostic.Kind

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Diagnostic.Kind c : Diagnostic.Kind.values())
System.out.println(c);
```

for (Diagnostic.Kind c : Diagnostic.Kind.values())
System.out.println(c);

valueOf

```java
public static
Diagnostic.Kind
valueOf​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

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

Diagnostic.Kind

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

