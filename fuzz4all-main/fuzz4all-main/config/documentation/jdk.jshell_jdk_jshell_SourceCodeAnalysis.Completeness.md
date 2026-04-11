# Enum SourceCodeAnalysis.Completeness

**Source:** `jdk.jshell\jdk\jshell\SourceCodeAnalysis.Completeness.html`

### Class Description

```java
public static enum
SourceCodeAnalysis.Completeness

extends
Enum
<
SourceCodeAnalysis.Completeness
>
```

Describes the completeness of the given input.

**All Implemented Interfaces:** Serializable

,

Comparable

<

SourceCodeAnalysis.Completeness

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
SourceCodeAnalysis.Completeness
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SourceCodeAnalysis.Completeness c : SourceCodeAnalysis.Completeness.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
SourceCodeAnalysis.Completeness
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

#### public boolean isComplete()

Indicates whether the first snippet of source is complete.
For example, "

x=

" is not
complete, but "

x=2

" is complete, even though a subsequent line could
make it "

x=2+2

". Already erroneous code is marked complete.

**Returns:**
- true

if the input is or begins a complete Snippet;
otherwise

false

---

### Additional Sections

#### Enum SourceCodeAnalysis.Completeness

java.lang.Object

- java.lang.Enum

<

SourceCodeAnalysis.Completeness

>
- - jdk.jshell.SourceCodeAnalysis.Completeness

java.lang.Enum

<

SourceCodeAnalysis.Completeness

>

- jdk.jshell.SourceCodeAnalysis.Completeness

jdk.jshell.SourceCodeAnalysis.Completeness

**All Implemented Interfaces:** Serializable

,

Comparable

<

SourceCodeAnalysis.Completeness

>

**Enclosing class:** SourceCodeAnalysis

```java
public static enum
SourceCodeAnalysis.Completeness

extends
Enum
<
SourceCodeAnalysis.Completeness
>
```

Describes the completeness of the given input.

public static enum

SourceCodeAnalysis.Completeness

extends

Enum

<

SourceCodeAnalysis.Completeness

>

Describes the completeness of the given input.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

COMPLETE

The input is a complete source snippet (declaration or statement) as is.

COMPLETE_WITH_SEMI

With this addition of a semicolon the input is a complete source snippet.

CONSIDERED_INCOMPLETE

A statement with a trailing (non-terminated) empty statement.

DEFINITELY_INCOMPLETE

There must be further source beyond the given input in order for it
to be complete.

EMPTY

An empty input.

UNKNOWN

The completeness of the input could not be determined because it
contains errors.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isComplete

()

Indicates whether the first snippet of source is complete.

static

SourceCodeAnalysis.Completeness

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

SourceCodeAnalysis.Completeness

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

COMPLETE

The input is a complete source snippet (declaration or statement) as is.

COMPLETE_WITH_SEMI

With this addition of a semicolon the input is a complete source snippet.

CONSIDERED_INCOMPLETE

A statement with a trailing (non-terminated) empty statement.

DEFINITELY_INCOMPLETE

There must be further source beyond the given input in order for it
to be complete.

EMPTY

An empty input.

UNKNOWN

The completeness of the input could not be determined because it
contains errors.

---

#### Enum Constant Summary

The input is a complete source snippet (declaration or statement) as is.

With this addition of a semicolon the input is a complete source snippet.

A statement with a trailing (non-terminated) empty statement.

There must be further source beyond the given input in order for it
to be complete.

An empty input.

The completeness of the input could not be determined because it
contains errors.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isComplete

()

Indicates whether the first snippet of source is complete.

static

SourceCodeAnalysis.Completeness

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

SourceCodeAnalysis.Completeness

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

Indicates whether the first snippet of source is complete.

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

- COMPLETE

```java
public static final
SourceCodeAnalysis.Completeness
COMPLETE
```

The input is a complete source snippet (declaration or statement) as is.

- COMPLETE_WITH_SEMI

```java
public static final
SourceCodeAnalysis.Completeness
COMPLETE_WITH_SEMI
```

With this addition of a semicolon the input is a complete source snippet.
This will only be returned when the end of input is encountered.

- DEFINITELY_INCOMPLETE

```java
public static final
SourceCodeAnalysis.Completeness
DEFINITELY_INCOMPLETE
```

There must be further source beyond the given input in order for it
to be complete. A semicolon would not complete it.
This will only be returned when the end of input is encountered.

- CONSIDERED_INCOMPLETE

```java
public static final
SourceCodeAnalysis.Completeness
CONSIDERED_INCOMPLETE
```

A statement with a trailing (non-terminated) empty statement.
Though technically it would be a complete statement
with the addition of a semicolon, it is rare
that that assumption is the desired behavior.
The input is considered incomplete. Comments and white-space are
still considered empty.

- EMPTY

```java
public static final
SourceCodeAnalysis.Completeness
EMPTY
```

An empty input.
The input is considered incomplete. Comments and white-space are
still considered empty.

- UNKNOWN

```java
public static final
SourceCodeAnalysis.Completeness
UNKNOWN
```

The completeness of the input could not be determined because it
contains errors. Error detection is not a goal of completeness
analysis, however errors interfered with determining its completeness.
The input is considered complete because evaluating is the best
mechanism to get error information.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
SourceCodeAnalysis.Completeness
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SourceCodeAnalysis.Completeness c : SourceCodeAnalysis.Completeness.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
SourceCodeAnalysis.Completeness
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

- isComplete

```java
public boolean isComplete()
```

Indicates whether the first snippet of source is complete.
For example, "

x=

" is not
complete, but "

x=2

" is complete, even though a subsequent line could
make it "

x=2+2

". Already erroneous code is marked complete.

**Returns:** true

if the input is or begins a complete Snippet;
otherwise

false

Enum Constant Detail

- COMPLETE

```java
public static final
SourceCodeAnalysis.Completeness
COMPLETE
```

The input is a complete source snippet (declaration or statement) as is.

- COMPLETE_WITH_SEMI

```java
public static final
SourceCodeAnalysis.Completeness
COMPLETE_WITH_SEMI
```

With this addition of a semicolon the input is a complete source snippet.
This will only be returned when the end of input is encountered.

- DEFINITELY_INCOMPLETE

```java
public static final
SourceCodeAnalysis.Completeness
DEFINITELY_INCOMPLETE
```

There must be further source beyond the given input in order for it
to be complete. A semicolon would not complete it.
This will only be returned when the end of input is encountered.

- CONSIDERED_INCOMPLETE

```java
public static final
SourceCodeAnalysis.Completeness
CONSIDERED_INCOMPLETE
```

A statement with a trailing (non-terminated) empty statement.
Though technically it would be a complete statement
with the addition of a semicolon, it is rare
that that assumption is the desired behavior.
The input is considered incomplete. Comments and white-space are
still considered empty.

- EMPTY

```java
public static final
SourceCodeAnalysis.Completeness
EMPTY
```

An empty input.
The input is considered incomplete. Comments and white-space are
still considered empty.

- UNKNOWN

```java
public static final
SourceCodeAnalysis.Completeness
UNKNOWN
```

The completeness of the input could not be determined because it
contains errors. Error detection is not a goal of completeness
analysis, however errors interfered with determining its completeness.
The input is considered complete because evaluating is the best
mechanism to get error information.

---

#### Enum Constant Detail

COMPLETE

```java
public static final
SourceCodeAnalysis.Completeness
COMPLETE
```

The input is a complete source snippet (declaration or statement) as is.

---

#### COMPLETE

public static final

SourceCodeAnalysis.Completeness

COMPLETE

The input is a complete source snippet (declaration or statement) as is.

COMPLETE_WITH_SEMI

```java
public static final
SourceCodeAnalysis.Completeness
COMPLETE_WITH_SEMI
```

With this addition of a semicolon the input is a complete source snippet.
This will only be returned when the end of input is encountered.

---

#### COMPLETE_WITH_SEMI

public static final

SourceCodeAnalysis.Completeness

COMPLETE_WITH_SEMI

With this addition of a semicolon the input is a complete source snippet.
This will only be returned when the end of input is encountered.

DEFINITELY_INCOMPLETE

```java
public static final
SourceCodeAnalysis.Completeness
DEFINITELY_INCOMPLETE
```

There must be further source beyond the given input in order for it
to be complete. A semicolon would not complete it.
This will only be returned when the end of input is encountered.

---

#### DEFINITELY_INCOMPLETE

public static final

SourceCodeAnalysis.Completeness

DEFINITELY_INCOMPLETE

There must be further source beyond the given input in order for it
to be complete. A semicolon would not complete it.
This will only be returned when the end of input is encountered.

CONSIDERED_INCOMPLETE

```java
public static final
SourceCodeAnalysis.Completeness
CONSIDERED_INCOMPLETE
```

A statement with a trailing (non-terminated) empty statement.
Though technically it would be a complete statement
with the addition of a semicolon, it is rare
that that assumption is the desired behavior.
The input is considered incomplete. Comments and white-space are
still considered empty.

---

#### CONSIDERED_INCOMPLETE

public static final

SourceCodeAnalysis.Completeness

CONSIDERED_INCOMPLETE

A statement with a trailing (non-terminated) empty statement.
Though technically it would be a complete statement
with the addition of a semicolon, it is rare
that that assumption is the desired behavior.
The input is considered incomplete. Comments and white-space are
still considered empty.

EMPTY

```java
public static final
SourceCodeAnalysis.Completeness
EMPTY
```

An empty input.
The input is considered incomplete. Comments and white-space are
still considered empty.

---

#### EMPTY

public static final

SourceCodeAnalysis.Completeness

EMPTY

An empty input.
The input is considered incomplete. Comments and white-space are
still considered empty.

UNKNOWN

```java
public static final
SourceCodeAnalysis.Completeness
UNKNOWN
```

The completeness of the input could not be determined because it
contains errors. Error detection is not a goal of completeness
analysis, however errors interfered with determining its completeness.
The input is considered complete because evaluating is the best
mechanism to get error information.

---

#### UNKNOWN

public static final

SourceCodeAnalysis.Completeness

UNKNOWN

The completeness of the input could not be determined because it
contains errors. Error detection is not a goal of completeness
analysis, however errors interfered with determining its completeness.
The input is considered complete because evaluating is the best
mechanism to get error information.

Method Detail

- values

```java
public static
SourceCodeAnalysis.Completeness
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SourceCodeAnalysis.Completeness c : SourceCodeAnalysis.Completeness.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
SourceCodeAnalysis.Completeness
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

- isComplete

```java
public boolean isComplete()
```

Indicates whether the first snippet of source is complete.
For example, "

x=

" is not
complete, but "

x=2

" is complete, even though a subsequent line could
make it "

x=2+2

". Already erroneous code is marked complete.

**Returns:** true

if the input is or begins a complete Snippet;
otherwise

false

---

#### Method Detail

values

```java
public static
SourceCodeAnalysis.Completeness
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SourceCodeAnalysis.Completeness c : SourceCodeAnalysis.Completeness.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

SourceCodeAnalysis.Completeness

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SourceCodeAnalysis.Completeness c : SourceCodeAnalysis.Completeness.values())
System.out.println(c);
```

for (SourceCodeAnalysis.Completeness c : SourceCodeAnalysis.Completeness.values())
System.out.println(c);

valueOf

```java
public static
SourceCodeAnalysis.Completeness
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

SourceCodeAnalysis.Completeness

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

isComplete

```java
public boolean isComplete()
```

Indicates whether the first snippet of source is complete.
For example, "

x=

" is not
complete, but "

x=2

" is complete, even though a subsequent line could
make it "

x=2+2

". Already erroneous code is marked complete.

**Returns:** true

if the input is or begins a complete Snippet;
otherwise

false

---

#### isComplete

public boolean isComplete()

Indicates whether the first snippet of source is complete.
For example, "

x=

" is not
complete, but "

x=2

" is complete, even though a subsequent line could
make it "

x=2+2

". Already erroneous code is marked complete.

---

