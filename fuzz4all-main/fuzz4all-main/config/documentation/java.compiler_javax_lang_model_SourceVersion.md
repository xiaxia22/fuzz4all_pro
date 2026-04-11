# Enum SourceVersion

**Source:** `java.compiler\javax\lang\model\SourceVersion.html`

### Class Description

```java
public enum
SourceVersion

extends
Enum
<
SourceVersion
>
```

Source versions of the Java™ programming language.

See the appropriate edition of

The Java™ Language Specification

for information about a particular source version.

Note that additional source version constants will be added to
model future releases of the language.

**All Implemented Interfaces:** Serializable

,

Comparable

<

SourceVersion

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
SourceVersion
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SourceVersion c : SourceVersion.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
SourceVersion
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

#### public static
SourceVersion
latest()

Returns the latest source version that can be modeled.

**Returns:**
- the latest source version that can be modeled

---

#### public static
SourceVersion
latestSupported()

Returns the latest source version fully supported by the
current execution environment.

RELEASE_5

or later must
be returned.

**Returns:**
- the latest source version that is fully supported

---

#### public static boolean isIdentifier​(
CharSequence
name)

Returns whether or not

name

is a syntactically valid
identifier (simple name) or keyword in the latest source
version. The method returns

true

if the name consists
of an initial character for which

Character.isJavaIdentifierStart(int)

returns

true

,
followed only by characters for which

Character.isJavaIdentifierPart(int)

returns

true

.
This pattern matches regular identifiers, keywords, restricted
keywords, and the literals

"true"

,

"false"

,

"null"

, and

"var"

.

The method returns

false

for all other strings.

**Parameters:**
- name

- the string to check

**Returns:**
- true

if this string is a
syntactically valid identifier or keyword,

false

otherwise.

---

#### public static boolean isName​(
CharSequence
name)

Returns whether or not

name

is a syntactically valid
qualified name in the latest source version. Unlike

isIdentifier

, this method returns

false

for keywords, boolean literals, and the null literal.

This method returns

true

for

restricted
keywords

and

"var"

.

**Parameters:**
- name

- the string to check

**Returns:**
- true

if this string is a
syntactically valid name,

false

otherwise.

**See The Java™ Language Specification :**
- 3.9 Keywords, 6.2 Names and Identifiers

---

#### public static boolean isName​(
CharSequence
name,

SourceVersion
version)

Returns whether or not

name

is a syntactically valid
qualified name in the given source version. Unlike

isIdentifier

, this method returns

false

for keywords, boolean literals, and the null literal.

This method returns

true

for

restricted
keywords

and

"var"

.

**Parameters:**
- name

- the string to check
- version

- the version to use

**Returns:**
- true

if this string is a
syntactically valid name,

false

otherwise.

**Since:**
- 9

**See The Java™ Language Specification :**
- 3.9 Keywords, 6.2 Names and Identifiers

---

#### public static boolean isKeyword​(
CharSequence
s)

Returns whether or not

s

is a keyword, boolean literal,
or null literal in the latest source version.
This method returns

false

for

restricted
keywords

and

"var"

.

**Parameters:**
- s

- the string to check

**Returns:**
- true

if

s

is a keyword, or boolean
literal, or null literal,

false

otherwise.

**See The Java™ Language Specification :**
- 3.9 Keywords, 3.10.3 Boolean Literals, 3.10.7 The Null Literal

---

#### public static boolean isKeyword​(
CharSequence
s,

SourceVersion
version)

Returns whether or not

s

is a keyword, boolean literal,
or null literal in the given source version.
This method returns

false

for

restricted
keywords

and

"var"

.

**Parameters:**
- s

- the string to check
- version

- the version to use

**Returns:**
- true

if

s

is a keyword, or boolean
literal, or null literal,

false

otherwise.

**Since:**
- 9

**See The Java™ Language Specification :**
- 3.9 Keywords, 3.10.3 Boolean Literals, 3.10.7 The Null Literal

---

### Additional Sections

#### Enum SourceVersion

java.lang.Object

- java.lang.Enum

<

SourceVersion

>
- - javax.lang.model.SourceVersion

java.lang.Enum

<

SourceVersion

>

- javax.lang.model.SourceVersion

javax.lang.model.SourceVersion

**All Implemented Interfaces:** Serializable

,

Comparable

<

SourceVersion

>

```java
public enum
SourceVersion

extends
Enum
<
SourceVersion
>
```

Source versions of the Java™ programming language.

See the appropriate edition of

The Java™ Language Specification

for information about a particular source version.

Note that additional source version constants will be added to
model future releases of the language.

**Since:** 1.6

public enum

SourceVersion

extends

Enum

<

SourceVersion

>

Source versions of the Java™ programming language.

See the appropriate edition of

The Java™ Language Specification

for information about a particular source version.

Note that additional source version constants will be added to
model future releases of the language.

Note that additional source version constants will be added to
model future releases of the language.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

RELEASE_0

The original version.

RELEASE_1

The version recognized by the Java Platform 1.1.

RELEASE_10

The version recognized by the Java Platform, Standard Edition
10.

RELEASE_11

The version recognized by the Java Platform, Standard Edition
11.

RELEASE_2

The version recognized by the Java 2 Platform, Standard Edition,
v 1.2.

RELEASE_3

The version recognized by the Java 2 Platform, Standard Edition,
v 1.3.

RELEASE_4

The version recognized by the Java 2 Platform, Standard Edition,
v 1.4.

RELEASE_5

The version recognized by the Java 2 Platform, Standard
Edition 5.0.

RELEASE_6

The version recognized by the Java Platform, Standard Edition
6.

RELEASE_7

The version recognized by the Java Platform, Standard Edition
7.

RELEASE_8

The version recognized by the Java Platform, Standard Edition
8.

RELEASE_9

The version recognized by the Java Platform, Standard Edition
9.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static boolean

isIdentifier

​(

CharSequence

name)

Returns whether or not

name

is a syntactically valid
identifier (simple name) or keyword in the latest source
version.

static boolean

isKeyword

​(

CharSequence

s)

Returns whether or not

s

is a keyword, boolean literal,
or null literal in the latest source version.

static boolean

isKeyword

​(

CharSequence

s,

SourceVersion

version)

Returns whether or not

s

is a keyword, boolean literal,
or null literal in the given source version.

static boolean

isName

​(

CharSequence

name)

Returns whether or not

name

is a syntactically valid
qualified name in the latest source version.

static boolean

isName

​(

CharSequence

name,

SourceVersion

version)

Returns whether or not

name

is a syntactically valid
qualified name in the given source version.

static

SourceVersion

latest

()

Returns the latest source version that can be modeled.

static

SourceVersion

latestSupported

()

Returns the latest source version fully supported by the
current execution environment.

static

SourceVersion

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

SourceVersion

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

RELEASE_0

The original version.

RELEASE_1

The version recognized by the Java Platform 1.1.

RELEASE_10

The version recognized by the Java Platform, Standard Edition
10.

RELEASE_11

The version recognized by the Java Platform, Standard Edition
11.

RELEASE_2

The version recognized by the Java 2 Platform, Standard Edition,
v 1.2.

RELEASE_3

The version recognized by the Java 2 Platform, Standard Edition,
v 1.3.

RELEASE_4

The version recognized by the Java 2 Platform, Standard Edition,
v 1.4.

RELEASE_5

The version recognized by the Java 2 Platform, Standard
Edition 5.0.

RELEASE_6

The version recognized by the Java Platform, Standard Edition
6.

RELEASE_7

The version recognized by the Java Platform, Standard Edition
7.

RELEASE_8

The version recognized by the Java Platform, Standard Edition
8.

RELEASE_9

The version recognized by the Java Platform, Standard Edition
9.

---

#### Enum Constant Summary

The original version.

The version recognized by the Java Platform 1.1.

The version recognized by the Java Platform, Standard Edition
10.

The version recognized by the Java Platform, Standard Edition
11.

The version recognized by the Java 2 Platform, Standard Edition,
v 1.2.

The version recognized by the Java 2 Platform, Standard Edition,
v 1.3.

The version recognized by the Java 2 Platform, Standard Edition,
v 1.4.

The version recognized by the Java 2 Platform, Standard
Edition 5.0.

The version recognized by the Java Platform, Standard Edition
6.

The version recognized by the Java Platform, Standard Edition
7.

The version recognized by the Java Platform, Standard Edition
8.

The version recognized by the Java Platform, Standard Edition
9.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static boolean

isIdentifier

​(

CharSequence

name)

Returns whether or not

name

is a syntactically valid
identifier (simple name) or keyword in the latest source
version.

static boolean

isKeyword

​(

CharSequence

s)

Returns whether or not

s

is a keyword, boolean literal,
or null literal in the latest source version.

static boolean

isKeyword

​(

CharSequence

s,

SourceVersion

version)

Returns whether or not

s

is a keyword, boolean literal,
or null literal in the given source version.

static boolean

isName

​(

CharSequence

name)

Returns whether or not

name

is a syntactically valid
qualified name in the latest source version.

static boolean

isName

​(

CharSequence

name,

SourceVersion

version)

Returns whether or not

name

is a syntactically valid
qualified name in the given source version.

static

SourceVersion

latest

()

Returns the latest source version that can be modeled.

static

SourceVersion

latestSupported

()

Returns the latest source version fully supported by the
current execution environment.

static

SourceVersion

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

SourceVersion

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

Returns whether or not

name

is a syntactically valid
identifier (simple name) or keyword in the latest source
version.

Returns whether or not

s

is a keyword, boolean literal,
or null literal in the latest source version.

Returns whether or not

s

is a keyword, boolean literal,
or null literal in the given source version.

Returns whether or not

name

is a syntactically valid
qualified name in the latest source version.

Returns whether or not

name

is a syntactically valid
qualified name in the given source version.

Returns the latest source version that can be modeled.

Returns the latest source version fully supported by the
current execution environment.

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

- RELEASE_0

```java
public static final
SourceVersion
RELEASE_0
```

The original version.

The language described in

The Java™ Language Specification, First Edition

.

- RELEASE_1

```java
public static final
SourceVersion
RELEASE_1
```

The version recognized by the Java Platform 1.1.

The language is

RELEASE_0

augmented with nested classes as described in the 1.1 update to

The Java™ Language Specification, First Edition

.

- RELEASE_2

```java
public static final
SourceVersion
RELEASE_2
```

The version recognized by the Java 2 Platform, Standard Edition,
v 1.2.

The language described in

The Java™ Language Specification,
Second Edition

, which includes the

strictfp

modifier.

- RELEASE_3

```java
public static final
SourceVersion
RELEASE_3
```

The version recognized by the Java 2 Platform, Standard Edition,
v 1.3.

No major changes from

RELEASE_2

.

- RELEASE_4

```java
public static final
SourceVersion
RELEASE_4
```

The version recognized by the Java 2 Platform, Standard Edition,
v 1.4.

Added a simple assertion facility.

- RELEASE_5

```java
public static final
SourceVersion
RELEASE_5
```

The version recognized by the Java 2 Platform, Standard
Edition 5.0.

The language described in

The Java™ Language Specification,
Third Edition

. First release to support
generics, annotations, autoboxing, var-args, enhanced

for

loop, and hexadecimal floating-point literals.

- RELEASE_6

```java
public static final
SourceVersion
RELEASE_6
```

The version recognized by the Java Platform, Standard Edition
6.

No major changes from

RELEASE_5

.

- RELEASE_7

```java
public static final
SourceVersion
RELEASE_7
```

The version recognized by the Java Platform, Standard Edition
7.

Additions in this release include, diamond syntax for
constructors,

try

-with-resources, strings in switch,
binary literals, and multi-catch.

**Since:** 1.7

- RELEASE_8

```java
public static final
SourceVersion
RELEASE_8
```

The version recognized by the Java Platform, Standard Edition
8.

Additions in this release include lambda expressions and default methods.

**Since:** 1.8

- RELEASE_9

```java
public static final
SourceVersion
RELEASE_9
```

The version recognized by the Java Platform, Standard Edition
9.

Additions in this release include modules and removal of a
single underscore from the set of legal identifier names.

**Since:** 9

- RELEASE_10

```java
public static final
SourceVersion
RELEASE_10
```

The version recognized by the Java Platform, Standard Edition
10.

Additions in this release include local-variable type inference
(

var

).

**Since:** 10

- RELEASE_11

```java
public static final
SourceVersion
RELEASE_11
```

The version recognized by the Java Platform, Standard Edition
11.

**Since:** 11

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
SourceVersion
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SourceVersion c : SourceVersion.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
SourceVersion
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

- latest

```java
public static
SourceVersion
latest()
```

Returns the latest source version that can be modeled.

**Returns:** the latest source version that can be modeled

- latestSupported

```java
public static
SourceVersion
latestSupported()
```

Returns the latest source version fully supported by the
current execution environment.

RELEASE_5

or later must
be returned.

**Returns:** the latest source version that is fully supported

- isIdentifier

```java
public static boolean isIdentifier​(
CharSequence
name)
```

Returns whether or not

name

is a syntactically valid
identifier (simple name) or keyword in the latest source
version. The method returns

true

if the name consists
of an initial character for which

Character.isJavaIdentifierStart(int)

returns

true

,
followed only by characters for which

Character.isJavaIdentifierPart(int)

returns

true

.
This pattern matches regular identifiers, keywords, restricted
keywords, and the literals

"true"

,

"false"

,

"null"

, and

"var"

.

The method returns

false

for all other strings.

**Parameters:** name

- the string to check
**Returns:** true

if this string is a
syntactically valid identifier or keyword,

false

otherwise.

- isName

```java
public static boolean isName​(
CharSequence
name)
```

Returns whether or not

name

is a syntactically valid
qualified name in the latest source version. Unlike

isIdentifier

, this method returns

false

for keywords, boolean literals, and the null literal.

This method returns

true

for

restricted
keywords

and

"var"

.

**Parameters:** name

- the string to check
**Returns:** true

if this string is a
syntactically valid name,

false

otherwise.
**See The Java™ Language Specification :** 3.9 Keywords, 6.2 Names and Identifiers

- isName

```java
public static boolean isName​(
CharSequence
name,

SourceVersion
version)
```

Returns whether or not

name

is a syntactically valid
qualified name in the given source version. Unlike

isIdentifier

, this method returns

false

for keywords, boolean literals, and the null literal.

This method returns

true

for

restricted
keywords

and

"var"

.

**Parameters:** name

- the string to check
**Parameters:** version

- the version to use
**Returns:** true

if this string is a
syntactically valid name,

false

otherwise.
**Since:** 9
**See The Java™ Language Specification :** 3.9 Keywords, 6.2 Names and Identifiers

- isKeyword

```java
public static boolean isKeyword​(
CharSequence
s)
```

Returns whether or not

s

is a keyword, boolean literal,
or null literal in the latest source version.
This method returns

false

for

restricted
keywords

and

"var"

.

**Parameters:** s

- the string to check
**Returns:** true

if

s

is a keyword, or boolean
literal, or null literal,

false

otherwise.
**See The Java™ Language Specification :** 3.9 Keywords, 3.10.3 Boolean Literals, 3.10.7 The Null Literal

- isKeyword

```java
public static boolean isKeyword​(
CharSequence
s,

SourceVersion
version)
```

Returns whether or not

s

is a keyword, boolean literal,
or null literal in the given source version.
This method returns

false

for

restricted
keywords

and

"var"

.

**Parameters:** s

- the string to check
**Parameters:** version

- the version to use
**Returns:** true

if

s

is a keyword, or boolean
literal, or null literal,

false

otherwise.
**Since:** 9
**See The Java™ Language Specification :** 3.9 Keywords, 3.10.3 Boolean Literals, 3.10.7 The Null Literal

Enum Constant Detail

- RELEASE_0

```java
public static final
SourceVersion
RELEASE_0
```

The original version.

The language described in

The Java™ Language Specification, First Edition

.

- RELEASE_1

```java
public static final
SourceVersion
RELEASE_1
```

The version recognized by the Java Platform 1.1.

The language is

RELEASE_0

augmented with nested classes as described in the 1.1 update to

The Java™ Language Specification, First Edition

.

- RELEASE_2

```java
public static final
SourceVersion
RELEASE_2
```

The version recognized by the Java 2 Platform, Standard Edition,
v 1.2.

The language described in

The Java™ Language Specification,
Second Edition

, which includes the

strictfp

modifier.

- RELEASE_3

```java
public static final
SourceVersion
RELEASE_3
```

The version recognized by the Java 2 Platform, Standard Edition,
v 1.3.

No major changes from

RELEASE_2

.

- RELEASE_4

```java
public static final
SourceVersion
RELEASE_4
```

The version recognized by the Java 2 Platform, Standard Edition,
v 1.4.

Added a simple assertion facility.

- RELEASE_5

```java
public static final
SourceVersion
RELEASE_5
```

The version recognized by the Java 2 Platform, Standard
Edition 5.0.

The language described in

The Java™ Language Specification,
Third Edition

. First release to support
generics, annotations, autoboxing, var-args, enhanced

for

loop, and hexadecimal floating-point literals.

- RELEASE_6

```java
public static final
SourceVersion
RELEASE_6
```

The version recognized by the Java Platform, Standard Edition
6.

No major changes from

RELEASE_5

.

- RELEASE_7

```java
public static final
SourceVersion
RELEASE_7
```

The version recognized by the Java Platform, Standard Edition
7.

Additions in this release include, diamond syntax for
constructors,

try

-with-resources, strings in switch,
binary literals, and multi-catch.

**Since:** 1.7

- RELEASE_8

```java
public static final
SourceVersion
RELEASE_8
```

The version recognized by the Java Platform, Standard Edition
8.

Additions in this release include lambda expressions and default methods.

**Since:** 1.8

- RELEASE_9

```java
public static final
SourceVersion
RELEASE_9
```

The version recognized by the Java Platform, Standard Edition
9.

Additions in this release include modules and removal of a
single underscore from the set of legal identifier names.

**Since:** 9

- RELEASE_10

```java
public static final
SourceVersion
RELEASE_10
```

The version recognized by the Java Platform, Standard Edition
10.

Additions in this release include local-variable type inference
(

var

).

**Since:** 10

- RELEASE_11

```java
public static final
SourceVersion
RELEASE_11
```

The version recognized by the Java Platform, Standard Edition
11.

**Since:** 11

---

#### Enum Constant Detail

RELEASE_0

```java
public static final
SourceVersion
RELEASE_0
```

The original version.

The language described in

The Java™ Language Specification, First Edition

.

---

#### RELEASE_0

public static final

SourceVersion

RELEASE_0

The original version.

The language described in

The Java™ Language Specification, First Edition

.

RELEASE_1

```java
public static final
SourceVersion
RELEASE_1
```

The version recognized by the Java Platform 1.1.

The language is

RELEASE_0

augmented with nested classes as described in the 1.1 update to

The Java™ Language Specification, First Edition

.

---

#### RELEASE_1

public static final

SourceVersion

RELEASE_1

The version recognized by the Java Platform 1.1.

The language is

RELEASE_0

augmented with nested classes as described in the 1.1 update to

The Java™ Language Specification, First Edition

.

RELEASE_2

```java
public static final
SourceVersion
RELEASE_2
```

The version recognized by the Java 2 Platform, Standard Edition,
v 1.2.

The language described in

The Java™ Language Specification,
Second Edition

, which includes the

strictfp

modifier.

---

#### RELEASE_2

public static final

SourceVersion

RELEASE_2

The version recognized by the Java 2 Platform, Standard Edition,
v 1.2.

The language described in

The Java™ Language Specification,
Second Edition

, which includes the

strictfp

modifier.

RELEASE_3

```java
public static final
SourceVersion
RELEASE_3
```

The version recognized by the Java 2 Platform, Standard Edition,
v 1.3.

No major changes from

RELEASE_2

.

---

#### RELEASE_3

public static final

SourceVersion

RELEASE_3

The version recognized by the Java 2 Platform, Standard Edition,
v 1.3.

No major changes from

RELEASE_2

.

RELEASE_4

```java
public static final
SourceVersion
RELEASE_4
```

The version recognized by the Java 2 Platform, Standard Edition,
v 1.4.

Added a simple assertion facility.

---

#### RELEASE_4

public static final

SourceVersion

RELEASE_4

The version recognized by the Java 2 Platform, Standard Edition,
v 1.4.

Added a simple assertion facility.

RELEASE_5

```java
public static final
SourceVersion
RELEASE_5
```

The version recognized by the Java 2 Platform, Standard
Edition 5.0.

The language described in

The Java™ Language Specification,
Third Edition

. First release to support
generics, annotations, autoboxing, var-args, enhanced

for

loop, and hexadecimal floating-point literals.

---

#### RELEASE_5

public static final

SourceVersion

RELEASE_5

The version recognized by the Java 2 Platform, Standard
Edition 5.0.

The language described in

The Java™ Language Specification,
Third Edition

. First release to support
generics, annotations, autoboxing, var-args, enhanced

for

loop, and hexadecimal floating-point literals.

RELEASE_6

```java
public static final
SourceVersion
RELEASE_6
```

The version recognized by the Java Platform, Standard Edition
6.

No major changes from

RELEASE_5

.

---

#### RELEASE_6

public static final

SourceVersion

RELEASE_6

The version recognized by the Java Platform, Standard Edition
6.

No major changes from

RELEASE_5

.

RELEASE_7

```java
public static final
SourceVersion
RELEASE_7
```

The version recognized by the Java Platform, Standard Edition
7.

Additions in this release include, diamond syntax for
constructors,

try

-with-resources, strings in switch,
binary literals, and multi-catch.

**Since:** 1.7

---

#### RELEASE_7

public static final

SourceVersion

RELEASE_7

The version recognized by the Java Platform, Standard Edition
7.

Additions in this release include, diamond syntax for
constructors,

try

-with-resources, strings in switch,
binary literals, and multi-catch.

RELEASE_8

```java
public static final
SourceVersion
RELEASE_8
```

The version recognized by the Java Platform, Standard Edition
8.

Additions in this release include lambda expressions and default methods.

**Since:** 1.8

---

#### RELEASE_8

public static final

SourceVersion

RELEASE_8

The version recognized by the Java Platform, Standard Edition
8.

Additions in this release include lambda expressions and default methods.

RELEASE_9

```java
public static final
SourceVersion
RELEASE_9
```

The version recognized by the Java Platform, Standard Edition
9.

Additions in this release include modules and removal of a
single underscore from the set of legal identifier names.

**Since:** 9

---

#### RELEASE_9

public static final

SourceVersion

RELEASE_9

The version recognized by the Java Platform, Standard Edition
9.

Additions in this release include modules and removal of a
single underscore from the set of legal identifier names.

RELEASE_10

```java
public static final
SourceVersion
RELEASE_10
```

The version recognized by the Java Platform, Standard Edition
10.

Additions in this release include local-variable type inference
(

var

).

**Since:** 10

---

#### RELEASE_10

public static final

SourceVersion

RELEASE_10

The version recognized by the Java Platform, Standard Edition
10.

Additions in this release include local-variable type inference
(

var

).

RELEASE_11

```java
public static final
SourceVersion
RELEASE_11
```

The version recognized by the Java Platform, Standard Edition
11.

**Since:** 11

---

#### RELEASE_11

public static final

SourceVersion

RELEASE_11

The version recognized by the Java Platform, Standard Edition
11.

Method Detail

- values

```java
public static
SourceVersion
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SourceVersion c : SourceVersion.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
SourceVersion
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

- latest

```java
public static
SourceVersion
latest()
```

Returns the latest source version that can be modeled.

**Returns:** the latest source version that can be modeled

- latestSupported

```java
public static
SourceVersion
latestSupported()
```

Returns the latest source version fully supported by the
current execution environment.

RELEASE_5

or later must
be returned.

**Returns:** the latest source version that is fully supported

- isIdentifier

```java
public static boolean isIdentifier​(
CharSequence
name)
```

Returns whether or not

name

is a syntactically valid
identifier (simple name) or keyword in the latest source
version. The method returns

true

if the name consists
of an initial character for which

Character.isJavaIdentifierStart(int)

returns

true

,
followed only by characters for which

Character.isJavaIdentifierPart(int)

returns

true

.
This pattern matches regular identifiers, keywords, restricted
keywords, and the literals

"true"

,

"false"

,

"null"

, and

"var"

.

The method returns

false

for all other strings.

**Parameters:** name

- the string to check
**Returns:** true

if this string is a
syntactically valid identifier or keyword,

false

otherwise.

- isName

```java
public static boolean isName​(
CharSequence
name)
```

Returns whether or not

name

is a syntactically valid
qualified name in the latest source version. Unlike

isIdentifier

, this method returns

false

for keywords, boolean literals, and the null literal.

This method returns

true

for

restricted
keywords

and

"var"

.

**Parameters:** name

- the string to check
**Returns:** true

if this string is a
syntactically valid name,

false

otherwise.
**See The Java™ Language Specification :** 3.9 Keywords, 6.2 Names and Identifiers

- isName

```java
public static boolean isName​(
CharSequence
name,

SourceVersion
version)
```

Returns whether or not

name

is a syntactically valid
qualified name in the given source version. Unlike

isIdentifier

, this method returns

false

for keywords, boolean literals, and the null literal.

This method returns

true

for

restricted
keywords

and

"var"

.

**Parameters:** name

- the string to check
**Parameters:** version

- the version to use
**Returns:** true

if this string is a
syntactically valid name,

false

otherwise.
**Since:** 9
**See The Java™ Language Specification :** 3.9 Keywords, 6.2 Names and Identifiers

- isKeyword

```java
public static boolean isKeyword​(
CharSequence
s)
```

Returns whether or not

s

is a keyword, boolean literal,
or null literal in the latest source version.
This method returns

false

for

restricted
keywords

and

"var"

.

**Parameters:** s

- the string to check
**Returns:** true

if

s

is a keyword, or boolean
literal, or null literal,

false

otherwise.
**See The Java™ Language Specification :** 3.9 Keywords, 3.10.3 Boolean Literals, 3.10.7 The Null Literal

- isKeyword

```java
public static boolean isKeyword​(
CharSequence
s,

SourceVersion
version)
```

Returns whether or not

s

is a keyword, boolean literal,
or null literal in the given source version.
This method returns

false

for

restricted
keywords

and

"var"

.

**Parameters:** s

- the string to check
**Parameters:** version

- the version to use
**Returns:** true

if

s

is a keyword, or boolean
literal, or null literal,

false

otherwise.
**Since:** 9
**See The Java™ Language Specification :** 3.9 Keywords, 3.10.3 Boolean Literals, 3.10.7 The Null Literal

---

#### Method Detail

values

```java
public static
SourceVersion
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SourceVersion c : SourceVersion.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

SourceVersion

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SourceVersion c : SourceVersion.values())
System.out.println(c);
```

for (SourceVersion c : SourceVersion.values())
System.out.println(c);

valueOf

```java
public static
SourceVersion
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

SourceVersion

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

latest

```java
public static
SourceVersion
latest()
```

Returns the latest source version that can be modeled.

**Returns:** the latest source version that can be modeled

---

#### latest

public static

SourceVersion

latest()

Returns the latest source version that can be modeled.

latestSupported

```java
public static
SourceVersion
latestSupported()
```

Returns the latest source version fully supported by the
current execution environment.

RELEASE_5

or later must
be returned.

**Returns:** the latest source version that is fully supported

---

#### latestSupported

public static

SourceVersion

latestSupported()

Returns the latest source version fully supported by the
current execution environment.

RELEASE_5

or later must
be returned.

isIdentifier

```java
public static boolean isIdentifier​(
CharSequence
name)
```

Returns whether or not

name

is a syntactically valid
identifier (simple name) or keyword in the latest source
version. The method returns

true

if the name consists
of an initial character for which

Character.isJavaIdentifierStart(int)

returns

true

,
followed only by characters for which

Character.isJavaIdentifierPart(int)

returns

true

.
This pattern matches regular identifiers, keywords, restricted
keywords, and the literals

"true"

,

"false"

,

"null"

, and

"var"

.

The method returns

false

for all other strings.

**Parameters:** name

- the string to check
**Returns:** true

if this string is a
syntactically valid identifier or keyword,

false

otherwise.

---

#### isIdentifier

public static boolean isIdentifier​(

CharSequence

name)

Returns whether or not

name

is a syntactically valid
identifier (simple name) or keyword in the latest source
version. The method returns

true

if the name consists
of an initial character for which

Character.isJavaIdentifierStart(int)

returns

true

,
followed only by characters for which

Character.isJavaIdentifierPart(int)

returns

true

.
This pattern matches regular identifiers, keywords, restricted
keywords, and the literals

"true"

,

"false"

,

"null"

, and

"var"

.

The method returns

false

for all other strings.

isName

```java
public static boolean isName​(
CharSequence
name)
```

Returns whether or not

name

is a syntactically valid
qualified name in the latest source version. Unlike

isIdentifier

, this method returns

false

for keywords, boolean literals, and the null literal.

This method returns

true

for

restricted
keywords

and

"var"

.

**Parameters:** name

- the string to check
**Returns:** true

if this string is a
syntactically valid name,

false

otherwise.
**See The Java™ Language Specification :** 3.9 Keywords, 6.2 Names and Identifiers

---

#### isName

public static boolean isName​(

CharSequence

name)

Returns whether or not

name

is a syntactically valid
qualified name in the latest source version. Unlike

isIdentifier

, this method returns

false

for keywords, boolean literals, and the null literal.

This method returns

true

for

restricted
keywords

and

"var"

.

isName

```java
public static boolean isName​(
CharSequence
name,

SourceVersion
version)
```

Returns whether or not

name

is a syntactically valid
qualified name in the given source version. Unlike

isIdentifier

, this method returns

false

for keywords, boolean literals, and the null literal.

This method returns

true

for

restricted
keywords

and

"var"

.

**Parameters:** name

- the string to check
**Parameters:** version

- the version to use
**Returns:** true

if this string is a
syntactically valid name,

false

otherwise.
**Since:** 9
**See The Java™ Language Specification :** 3.9 Keywords, 6.2 Names and Identifiers

---

#### isName

public static boolean isName​(

CharSequence

name,

SourceVersion

version)

Returns whether or not

name

is a syntactically valid
qualified name in the given source version. Unlike

isIdentifier

, this method returns

false

for keywords, boolean literals, and the null literal.

This method returns

true

for

restricted
keywords

and

"var"

.

isKeyword

```java
public static boolean isKeyword​(
CharSequence
s)
```

Returns whether or not

s

is a keyword, boolean literal,
or null literal in the latest source version.
This method returns

false

for

restricted
keywords

and

"var"

.

**Parameters:** s

- the string to check
**Returns:** true

if

s

is a keyword, or boolean
literal, or null literal,

false

otherwise.
**See The Java™ Language Specification :** 3.9 Keywords, 3.10.3 Boolean Literals, 3.10.7 The Null Literal

---

#### isKeyword

public static boolean isKeyword​(

CharSequence

s)

Returns whether or not

s

is a keyword, boolean literal,
or null literal in the latest source version.
This method returns

false

for

restricted
keywords

and

"var"

.

isKeyword

```java
public static boolean isKeyword​(
CharSequence
s,

SourceVersion
version)
```

Returns whether or not

s

is a keyword, boolean literal,
or null literal in the given source version.
This method returns

false

for

restricted
keywords

and

"var"

.

**Parameters:** s

- the string to check
**Parameters:** version

- the version to use
**Returns:** true

if

s

is a keyword, or boolean
literal, or null literal,

false

otherwise.
**Since:** 9
**See The Java™ Language Specification :** 3.9 Keywords, 3.10.3 Boolean Literals, 3.10.7 The Null Literal

---

#### isKeyword

public static boolean isKeyword​(

CharSequence

s,

SourceVersion

version)

Returns whether or not

s

is a keyword, boolean literal,
or null literal in the given source version.
This method returns

false

for

restricted
keywords

and

"var"

.

---

