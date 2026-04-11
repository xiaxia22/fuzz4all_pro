# Class Boolean

**Source:** `java.base\java\lang\Boolean.html`

### Class Description

```java
public final class
Boolean

extends
Object

implements
Serializable
,
Comparable
<
Boolean
>
```

The Boolean class wraps a value of the primitive type

boolean

in an object. An object of type

Boolean

contains a single field whose type is

boolean

.

In addition, this class provides many methods for
converting a

boolean

to a

String

and a

String

to a

boolean

, as well as other
constants and methods useful when dealing with a

boolean

.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Boolean

>

---

### Field Details

#### public static final
Boolean
TRUE

The

Boolean

object corresponding to the primitive
value

true

.

---

#### public static final
Boolean
FALSE

The

Boolean

object corresponding to the primitive
value

false

.

---

#### public static final
Class
<
Boolean
> TYPE

The Class object representing the primitive type boolean.

**Since:**
- 1.1

---

### Constructor Details

#### @Deprecated
(
since
="9")
public Boolean​(boolean value)

Allocates a

Boolean

object representing the

value

argument.

**Parameters:**
- value

- the value of the

Boolean

.

---

#### @Deprecated
(
since
="9")
public Boolean​(
String
s)

Allocates a

Boolean

object representing the value

true

if the string argument is not

null

and is equal, ignoring case, to the string

"true"

.
Otherwise, allocates a

Boolean

object representing the
value

false

.

**Parameters:**
- s

- the string to be converted to a

Boolean

.

---

### Method Details

#### public static boolean parseBoolean​(
String
s)

Parses the string argument as a boolean. The

boolean

returned represents the value

true

if the string argument
is not

null

and is equal, ignoring case, to the string

"true"

.
Otherwise, a false value is returned, including for a null
argument.

Example:

Boolean.parseBoolean("True")

returns

true

.

Example:

Boolean.parseBoolean("yes")

returns

false

.

**Parameters:**
- s

- the

String

containing the boolean
representation to be parsed

**Returns:**
- the boolean represented by the string argument

**Since:**
- 1.5

---

#### public boolean booleanValue()

Returns the value of this

Boolean

object as a boolean
primitive.

**Returns:**
- the primitive

boolean

value of this object.

---

#### public static
Boolean
valueOf​(boolean b)

Returns a

Boolean

instance representing the specified

boolean

value. If the specified

boolean

value
is

true

, this method returns

Boolean.TRUE

;
if it is

false

, this method returns

Boolean.FALSE

.
If a new

Boolean

instance is not required, this method
should generally be used in preference to the constructor

Boolean(boolean)

, as this method is likely to yield
significantly better space and time performance.

**Parameters:**
- b

- a boolean value.

**Returns:**
- a

Boolean

instance representing

b

.

**Since:**
- 1.4

---

#### public static
Boolean
valueOf​(
String
s)

Returns a

Boolean

with a value represented by the
specified string. The

Boolean

returned represents a
true value if the string argument is not

null

and is equal, ignoring case, to the string

"true"

.
Otherwise, a false value is returned, including for a null
argument.

**Parameters:**
- s

- a string.

**Returns:**
- the

Boolean

value represented by the string.

---

#### public static
String
toString​(boolean b)

Returns a

String

object representing the specified
boolean. If the specified boolean is

true

, then
the string

"true"

will be returned, otherwise the
string

"false"

will be returned.

**Parameters:**
- b

- the boolean to be converted

**Returns:**
- the string representation of the specified

boolean

**Since:**
- 1.4

---

#### public
String
toString()

Returns a

String

object representing this Boolean's
value. If this object represents the value

true

,
a string equal to

"true"

is returned. Otherwise, a
string equal to

"false"

is returned.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this object.

---

#### public int hashCode()

Returns a hash code for this

Boolean

object.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the integer

1231

if this object represents

true

; returns the integer

1237

if this
object represents

false

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public static int hashCode​(boolean value)

Returns a hash code for a

boolean

value; compatible with

Boolean.hashCode()

.

**Parameters:**
- value

- the value to hash

**Returns:**
- a hash code value for a

boolean

value.

**Since:**
- 1.8

---

#### public boolean equals​(
Object
obj)

Returns

true

if and only if the argument is not

null

and is a

Boolean

object that
represents the same

boolean

value as this object.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to compare with.

**Returns:**
- true

if the Boolean objects represent the
same value;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public static boolean getBoolean​(
String
name)

Returns

true

if and only if the system property named
by the argument exists and is equal to, ignoring case, the
string

"true"

.
A system property is accessible through

getProperty

, a
method defined by the

System

class.

If there is no
property with the specified name, or if the specified name is
empty or null, then

false

is returned.

**Parameters:**
- name

- the system property name.

**Returns:**
- the

boolean

value of the system property.

**Throws:**
- SecurityException

- for the same reasons as

System.getProperty

**See Also:**
- System.getProperty(java.lang.String)

,

System.getProperty(java.lang.String, java.lang.String)

---

#### public int compareTo​(
Boolean
b)

Compares this

Boolean

instance with another.

**Specified by:**
- compareTo

in interface

Comparable

<

Boolean

>

**Parameters:**
- b

- the

Boolean

instance to be compared

**Returns:**
- zero if this object represents the same boolean value as the
argument; a positive value if this object represents true
and the argument represents false; and a negative value if
this object represents false and the argument represents true

**Throws:**
- NullPointerException

- if the argument is

null

**See Also:**
- Comparable

**Since:**
- 1.5

---

#### public static int compare​(boolean x,
boolean y)

Compares two

boolean

values.
The value returned is identical to what would be returned by:

```java
Boolean.valueOf(x).compareTo(Boolean.valueOf(y))
```

**Parameters:**
- x

- the first

boolean

to compare
- y

- the second

boolean

to compare

**Returns:**
- the value

0

if

x == y

;
a value less than

0

if

!x && y

; and
a value greater than

0

if

x && !y

**Since:**
- 1.7

---

#### public static boolean logicalAnd​(boolean a,
boolean b)

Returns the result of applying the logical AND operator to the
specified

boolean

operands.

**Parameters:**
- a

- the first operand
- b

- the second operand

**Returns:**
- the logical AND of

a

and

b

**See Also:**
- BinaryOperator

**Since:**
- 1.8

---

#### public static boolean logicalOr​(boolean a,
boolean b)

Returns the result of applying the logical OR operator to the
specified

boolean

operands.

**Parameters:**
- a

- the first operand
- b

- the second operand

**Returns:**
- the logical OR of

a

and

b

**See Also:**
- BinaryOperator

**Since:**
- 1.8

---

#### public static boolean logicalXor​(boolean a,
boolean b)

Returns the result of applying the logical XOR operator to the
specified

boolean

operands.

**Parameters:**
- a

- the first operand
- b

- the second operand

**Returns:**
- the logical XOR of

a

and

b

**See Also:**
- BinaryOperator

**Since:**
- 1.8

---

### Additional Sections

#### Class Boolean

java.lang.Object

- java.lang.Boolean

java.lang.Boolean

**All Implemented Interfaces:** Serializable

,

Comparable

<

Boolean

>

```java
public final class
Boolean

extends
Object

implements
Serializable
,
Comparable
<
Boolean
>
```

The Boolean class wraps a value of the primitive type

boolean

in an object. An object of type

Boolean

contains a single field whose type is

boolean

.

In addition, this class provides many methods for
converting a

boolean

to a

String

and a

String

to a

boolean

, as well as other
constants and methods useful when dealing with a

boolean

.

**Since:** 1.0
**See Also:** Serialized Form

public final class

Boolean

extends

Object

implements

Serializable

,

Comparable

<

Boolean

>

The Boolean class wraps a value of the primitive type

boolean

in an object. An object of type

Boolean

contains a single field whose type is

boolean

.

In addition, this class provides many methods for
converting a

boolean

to a

String

and a

String

to a

boolean

, as well as other
constants and methods useful when dealing with a

boolean

.

In addition, this class provides many methods for
converting a

boolean

to a

String

and a

String

to a

boolean

, as well as other
constants and methods useful when dealing with a

boolean

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

Boolean

FALSE

The

Boolean

object corresponding to the primitive
value

false

.

static

Boolean

TRUE

The

Boolean

object corresponding to the primitive
value

true

.

static

Class

<

Boolean

>

TYPE

The Class object representing the primitive type boolean.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Boolean

​(boolean value)

Deprecated.

It is rarely appropriate to use this constructor.

Boolean

​(

String

s)

Deprecated.

It is rarely appropriate to use this constructor.

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

booleanValue

()

Returns the value of this

Boolean

object as a boolean
primitive.

static int

compare

​(boolean x,
boolean y)

Compares two

boolean

values.

int

compareTo

​(

Boolean

b)

Compares this

Boolean

instance with another.

boolean

equals

​(

Object

obj)

Returns

true

if and only if the argument is not

null

and is a

Boolean

object that
represents the same

boolean

value as this object.

static boolean

getBoolean

​(

String

name)

Returns

true

if and only if the system property named
by the argument exists and is equal to, ignoring case, the
string

"true"

.

int

hashCode

()

Returns a hash code for this

Boolean

object.

static int

hashCode

​(boolean value)

Returns a hash code for a

boolean

value; compatible with

Boolean.hashCode()

.

static boolean

logicalAnd

​(boolean a,
boolean b)

Returns the result of applying the logical AND operator to the
specified

boolean

operands.

static boolean

logicalOr

​(boolean a,
boolean b)

Returns the result of applying the logical OR operator to the
specified

boolean

operands.

static boolean

logicalXor

​(boolean a,
boolean b)

Returns the result of applying the logical XOR operator to the
specified

boolean

operands.

static boolean

parseBoolean

​(

String

s)

Parses the string argument as a boolean.

String

toString

()

Returns a

String

object representing this Boolean's
value.

static

String

toString

​(boolean b)

Returns a

String

object representing the specified
boolean.

static

Boolean

valueOf

​(boolean b)

Returns a

Boolean

instance representing the specified

boolean

value.

static

Boolean

valueOf

​(

String

s)

Returns a

Boolean

with a value represented by the
specified string.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

Field Summary

Fields

Modifier and Type

Field

Description

static

Boolean

FALSE

The

Boolean

object corresponding to the primitive
value

false

.

static

Boolean

TRUE

The

Boolean

object corresponding to the primitive
value

true

.

static

Class

<

Boolean

>

TYPE

The Class object representing the primitive type boolean.

---

#### Field Summary

The

Boolean

object corresponding to the primitive
value

false

.

The

Boolean

object corresponding to the primitive
value

true

.

The Class object representing the primitive type boolean.

Constructor Summary

Constructors

Constructor

Description

Boolean

​(boolean value)

Deprecated.

It is rarely appropriate to use this constructor.

Boolean

​(

String

s)

Deprecated.

It is rarely appropriate to use this constructor.

---

#### Constructor Summary

Deprecated.

It is rarely appropriate to use this constructor.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

booleanValue

()

Returns the value of this

Boolean

object as a boolean
primitive.

static int

compare

​(boolean x,
boolean y)

Compares two

boolean

values.

int

compareTo

​(

Boolean

b)

Compares this

Boolean

instance with another.

boolean

equals

​(

Object

obj)

Returns

true

if and only if the argument is not

null

and is a

Boolean

object that
represents the same

boolean

value as this object.

static boolean

getBoolean

​(

String

name)

Returns

true

if and only if the system property named
by the argument exists and is equal to, ignoring case, the
string

"true"

.

int

hashCode

()

Returns a hash code for this

Boolean

object.

static int

hashCode

​(boolean value)

Returns a hash code for a

boolean

value; compatible with

Boolean.hashCode()

.

static boolean

logicalAnd

​(boolean a,
boolean b)

Returns the result of applying the logical AND operator to the
specified

boolean

operands.

static boolean

logicalOr

​(boolean a,
boolean b)

Returns the result of applying the logical OR operator to the
specified

boolean

operands.

static boolean

logicalXor

​(boolean a,
boolean b)

Returns the result of applying the logical XOR operator to the
specified

boolean

operands.

static boolean

parseBoolean

​(

String

s)

Parses the string argument as a boolean.

String

toString

()

Returns a

String

object representing this Boolean's
value.

static

String

toString

​(boolean b)

Returns a

String

object representing the specified
boolean.

static

Boolean

valueOf

​(boolean b)

Returns a

Boolean

instance representing the specified

boolean

value.

static

Boolean

valueOf

​(

String

s)

Returns a

Boolean

with a value represented by the
specified string.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

Returns the value of this

Boolean

object as a boolean
primitive.

Compares two

boolean

values.

Compares this

Boolean

instance with another.

Returns

true

if and only if the argument is not

null

and is a

Boolean

object that
represents the same

boolean

value as this object.

Returns

true

if and only if the system property named
by the argument exists and is equal to, ignoring case, the
string

"true"

.

Returns a hash code for this

Boolean

object.

Returns a hash code for a

boolean

value; compatible with

Boolean.hashCode()

.

Returns the result of applying the logical AND operator to the
specified

boolean

operands.

Returns the result of applying the logical OR operator to the
specified

boolean

operands.

Returns the result of applying the logical XOR operator to the
specified

boolean

operands.

Parses the string argument as a boolean.

Returns a

String

object representing this Boolean's
value.

Returns a

String

object representing the specified
boolean.

Returns a

Boolean

instance representing the specified

boolean

value.

Returns a

Boolean

with a value represented by the
specified string.

Methods declared in class java.lang.

Object

clone

,

finalize

,

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

============ FIELD DETAIL ===========

- Field Detail

- TRUE

```java
public static final
Boolean
TRUE
```

The

Boolean

object corresponding to the primitive
value

true

.

- FALSE

```java
public static final
Boolean
FALSE
```

The

Boolean

object corresponding to the primitive
value

false

.

- TYPE

```java
public static final
Class
<
Boolean
> TYPE
```

The Class object representing the primitive type boolean.

**Since:** 1.1

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Boolean

```java
@Deprecated
(
since
="9")
public Boolean​(boolean value)
```

Deprecated.

It is rarely appropriate to use this constructor. The static factory

valueOf(boolean)

is generally a better choice, as it is
likely to yield significantly better space and time performance.
Also consider using the final fields

TRUE

and

FALSE

if possible.

Allocates a

Boolean

object representing the

value

argument.

**Parameters:** value

- the value of the

Boolean

.

- Boolean

```java
@Deprecated
(
since
="9")
public Boolean​(
String
s)
```

Deprecated.

It is rarely appropriate to use this constructor.
Use

parseBoolean(String)

to convert a string to a

boolean

primitive, or use

valueOf(String)

to convert a string to a

Boolean

object.

Allocates a

Boolean

object representing the value

true

if the string argument is not

null

and is equal, ignoring case, to the string

"true"

.
Otherwise, allocates a

Boolean

object representing the
value

false

.

**Parameters:** s

- the string to be converted to a

Boolean

.

============ METHOD DETAIL ==========

- Method Detail

- parseBoolean

```java
public static boolean parseBoolean​(
String
s)
```

Parses the string argument as a boolean. The

boolean

returned represents the value

true

if the string argument
is not

null

and is equal, ignoring case, to the string

"true"

.
Otherwise, a false value is returned, including for a null
argument.

Example:

Boolean.parseBoolean("True")

returns

true

.

Example:

Boolean.parseBoolean("yes")

returns

false

.

**Parameters:** s

- the

String

containing the boolean
representation to be parsed
**Returns:** the boolean represented by the string argument
**Since:** 1.5

- booleanValue

```java
public boolean booleanValue()
```

Returns the value of this

Boolean

object as a boolean
primitive.

**Returns:** the primitive

boolean

value of this object.

- valueOf

```java
public static
Boolean
valueOf​(boolean b)
```

Returns a

Boolean

instance representing the specified

boolean

value. If the specified

boolean

value
is

true

, this method returns

Boolean.TRUE

;
if it is

false

, this method returns

Boolean.FALSE

.
If a new

Boolean

instance is not required, this method
should generally be used in preference to the constructor

Boolean(boolean)

, as this method is likely to yield
significantly better space and time performance.

**Parameters:** b

- a boolean value.
**Returns:** a

Boolean

instance representing

b

.
**Since:** 1.4

- valueOf

```java
public static
Boolean
valueOf​(
String
s)
```

Returns a

Boolean

with a value represented by the
specified string. The

Boolean

returned represents a
true value if the string argument is not

null

and is equal, ignoring case, to the string

"true"

.
Otherwise, a false value is returned, including for a null
argument.

**Parameters:** s

- a string.
**Returns:** the

Boolean

value represented by the string.

- toString

```java
public static
String
toString​(boolean b)
```

Returns a

String

object representing the specified
boolean. If the specified boolean is

true

, then
the string

"true"

will be returned, otherwise the
string

"false"

will be returned.

**Parameters:** b

- the boolean to be converted
**Returns:** the string representation of the specified

boolean
**Since:** 1.4

- toString

```java
public
String
toString()
```

Returns a

String

object representing this Boolean's
value. If this object represents the value

true

,
a string equal to

"true"

is returned. Otherwise, a
string equal to

"false"

is returned.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object.

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

Boolean

object.

**Overrides:** hashCode

in class

Object
**Returns:** the integer

1231

if this object represents

true

; returns the integer

1237

if this
object represents

false

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- hashCode

```java
public static int hashCode​(boolean value)
```

Returns a hash code for a

boolean

value; compatible with

Boolean.hashCode()

.

**Parameters:** value

- the value to hash
**Returns:** a hash code value for a

boolean

value.
**Since:** 1.8

- equals

```java
public boolean equals​(
Object
obj)
```

Returns

true

if and only if the argument is not

null

and is a

Boolean

object that
represents the same

boolean

value as this object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare with.
**Returns:** true

if the Boolean objects represent the
same value;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- getBoolean

```java
public static boolean getBoolean​(
String
name)
```

Returns

true

if and only if the system property named
by the argument exists and is equal to, ignoring case, the
string

"true"

.
A system property is accessible through

getProperty

, a
method defined by the

System

class.

If there is no
property with the specified name, or if the specified name is
empty or null, then

false

is returned.

**Parameters:** name

- the system property name.
**Returns:** the

boolean

value of the system property.
**Throws:** SecurityException

- for the same reasons as

System.getProperty
**See Also:** System.getProperty(java.lang.String)

,

System.getProperty(java.lang.String, java.lang.String)

- compareTo

```java
public int compareTo​(
Boolean
b)
```

Compares this

Boolean

instance with another.

**Specified by:** compareTo

in interface

Comparable

<

Boolean

>
**Parameters:** b

- the

Boolean

instance to be compared
**Returns:** zero if this object represents the same boolean value as the
argument; a positive value if this object represents true
and the argument represents false; and a negative value if
this object represents false and the argument represents true
**Throws:** NullPointerException

- if the argument is

null
**Since:** 1.5
**See Also:** Comparable

- compare

```java
public static int compare​(boolean x,
boolean y)
```

Compares two

boolean

values.
The value returned is identical to what would be returned by:

```java
Boolean.valueOf(x).compareTo(Boolean.valueOf(y))
```

**Parameters:** x

- the first

boolean

to compare
**Parameters:** y

- the second

boolean

to compare
**Returns:** the value

0

if

x == y

;
a value less than

0

if

!x && y

; and
a value greater than

0

if

x && !y
**Since:** 1.7

- logicalAnd

```java
public static boolean logicalAnd​(boolean a,
boolean b)
```

Returns the result of applying the logical AND operator to the
specified

boolean

operands.

**Parameters:** a

- the first operand
**Parameters:** b

- the second operand
**Returns:** the logical AND of

a

and

b
**Since:** 1.8
**See Also:** BinaryOperator

- logicalOr

```java
public static boolean logicalOr​(boolean a,
boolean b)
```

Returns the result of applying the logical OR operator to the
specified

boolean

operands.

**Parameters:** a

- the first operand
**Parameters:** b

- the second operand
**Returns:** the logical OR of

a

and

b
**Since:** 1.8
**See Also:** BinaryOperator

- logicalXor

```java
public static boolean logicalXor​(boolean a,
boolean b)
```

Returns the result of applying the logical XOR operator to the
specified

boolean

operands.

**Parameters:** a

- the first operand
**Parameters:** b

- the second operand
**Returns:** the logical XOR of

a

and

b
**Since:** 1.8
**See Also:** BinaryOperator

Field Detail

- TRUE

```java
public static final
Boolean
TRUE
```

The

Boolean

object corresponding to the primitive
value

true

.

- FALSE

```java
public static final
Boolean
FALSE
```

The

Boolean

object corresponding to the primitive
value

false

.

- TYPE

```java
public static final
Class
<
Boolean
> TYPE
```

The Class object representing the primitive type boolean.

**Since:** 1.1

---

#### Field Detail

TRUE

```java
public static final
Boolean
TRUE
```

The

Boolean

object corresponding to the primitive
value

true

.

---

#### TRUE

public static final

Boolean

TRUE

The

Boolean

object corresponding to the primitive
value

true

.

FALSE

```java
public static final
Boolean
FALSE
```

The

Boolean

object corresponding to the primitive
value

false

.

---

#### FALSE

public static final

Boolean

FALSE

The

Boolean

object corresponding to the primitive
value

false

.

TYPE

```java
public static final
Class
<
Boolean
> TYPE
```

The Class object representing the primitive type boolean.

**Since:** 1.1

---

#### TYPE

public static final

Class

<

Boolean

> TYPE

The Class object representing the primitive type boolean.

Constructor Detail

- Boolean

```java
@Deprecated
(
since
="9")
public Boolean​(boolean value)
```

Deprecated.

It is rarely appropriate to use this constructor. The static factory

valueOf(boolean)

is generally a better choice, as it is
likely to yield significantly better space and time performance.
Also consider using the final fields

TRUE

and

FALSE

if possible.

Allocates a

Boolean

object representing the

value

argument.

**Parameters:** value

- the value of the

Boolean

.

- Boolean

```java
@Deprecated
(
since
="9")
public Boolean​(
String
s)
```

Deprecated.

It is rarely appropriate to use this constructor.
Use

parseBoolean(String)

to convert a string to a

boolean

primitive, or use

valueOf(String)

to convert a string to a

Boolean

object.

Allocates a

Boolean

object representing the value

true

if the string argument is not

null

and is equal, ignoring case, to the string

"true"

.
Otherwise, allocates a

Boolean

object representing the
value

false

.

**Parameters:** s

- the string to be converted to a

Boolean

.

---

#### Constructor Detail

Boolean

```java
@Deprecated
(
since
="9")
public Boolean​(boolean value)
```

Deprecated.

It is rarely appropriate to use this constructor. The static factory

valueOf(boolean)

is generally a better choice, as it is
likely to yield significantly better space and time performance.
Also consider using the final fields

TRUE

and

FALSE

if possible.

Allocates a

Boolean

object representing the

value

argument.

**Parameters:** value

- the value of the

Boolean

.

---

#### Boolean

@Deprecated

(

since

="9")
public Boolean​(boolean value)

Allocates a

Boolean

object representing the

value

argument.

Boolean

```java
@Deprecated
(
since
="9")
public Boolean​(
String
s)
```

Deprecated.

It is rarely appropriate to use this constructor.
Use

parseBoolean(String)

to convert a string to a

boolean

primitive, or use

valueOf(String)

to convert a string to a

Boolean

object.

Allocates a

Boolean

object representing the value

true

if the string argument is not

null

and is equal, ignoring case, to the string

"true"

.
Otherwise, allocates a

Boolean

object representing the
value

false

.

**Parameters:** s

- the string to be converted to a

Boolean

.

---

#### Boolean

@Deprecated

(

since

="9")
public Boolean​(

String

s)

Allocates a

Boolean

object representing the value

true

if the string argument is not

null

and is equal, ignoring case, to the string

"true"

.
Otherwise, allocates a

Boolean

object representing the
value

false

.

Method Detail

- parseBoolean

```java
public static boolean parseBoolean​(
String
s)
```

Parses the string argument as a boolean. The

boolean

returned represents the value

true

if the string argument
is not

null

and is equal, ignoring case, to the string

"true"

.
Otherwise, a false value is returned, including for a null
argument.

Example:

Boolean.parseBoolean("True")

returns

true

.

Example:

Boolean.parseBoolean("yes")

returns

false

.

**Parameters:** s

- the

String

containing the boolean
representation to be parsed
**Returns:** the boolean represented by the string argument
**Since:** 1.5

- booleanValue

```java
public boolean booleanValue()
```

Returns the value of this

Boolean

object as a boolean
primitive.

**Returns:** the primitive

boolean

value of this object.

- valueOf

```java
public static
Boolean
valueOf​(boolean b)
```

Returns a

Boolean

instance representing the specified

boolean

value. If the specified

boolean

value
is

true

, this method returns

Boolean.TRUE

;
if it is

false

, this method returns

Boolean.FALSE

.
If a new

Boolean

instance is not required, this method
should generally be used in preference to the constructor

Boolean(boolean)

, as this method is likely to yield
significantly better space and time performance.

**Parameters:** b

- a boolean value.
**Returns:** a

Boolean

instance representing

b

.
**Since:** 1.4

- valueOf

```java
public static
Boolean
valueOf​(
String
s)
```

Returns a

Boolean

with a value represented by the
specified string. The

Boolean

returned represents a
true value if the string argument is not

null

and is equal, ignoring case, to the string

"true"

.
Otherwise, a false value is returned, including for a null
argument.

**Parameters:** s

- a string.
**Returns:** the

Boolean

value represented by the string.

- toString

```java
public static
String
toString​(boolean b)
```

Returns a

String

object representing the specified
boolean. If the specified boolean is

true

, then
the string

"true"

will be returned, otherwise the
string

"false"

will be returned.

**Parameters:** b

- the boolean to be converted
**Returns:** the string representation of the specified

boolean
**Since:** 1.4

- toString

```java
public
String
toString()
```

Returns a

String

object representing this Boolean's
value. If this object represents the value

true

,
a string equal to

"true"

is returned. Otherwise, a
string equal to

"false"

is returned.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object.

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

Boolean

object.

**Overrides:** hashCode

in class

Object
**Returns:** the integer

1231

if this object represents

true

; returns the integer

1237

if this
object represents

false

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- hashCode

```java
public static int hashCode​(boolean value)
```

Returns a hash code for a

boolean

value; compatible with

Boolean.hashCode()

.

**Parameters:** value

- the value to hash
**Returns:** a hash code value for a

boolean

value.
**Since:** 1.8

- equals

```java
public boolean equals​(
Object
obj)
```

Returns

true

if and only if the argument is not

null

and is a

Boolean

object that
represents the same

boolean

value as this object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare with.
**Returns:** true

if the Boolean objects represent the
same value;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- getBoolean

```java
public static boolean getBoolean​(
String
name)
```

Returns

true

if and only if the system property named
by the argument exists and is equal to, ignoring case, the
string

"true"

.
A system property is accessible through

getProperty

, a
method defined by the

System

class.

If there is no
property with the specified name, or if the specified name is
empty or null, then

false

is returned.

**Parameters:** name

- the system property name.
**Returns:** the

boolean

value of the system property.
**Throws:** SecurityException

- for the same reasons as

System.getProperty
**See Also:** System.getProperty(java.lang.String)

,

System.getProperty(java.lang.String, java.lang.String)

- compareTo

```java
public int compareTo​(
Boolean
b)
```

Compares this

Boolean

instance with another.

**Specified by:** compareTo

in interface

Comparable

<

Boolean

>
**Parameters:** b

- the

Boolean

instance to be compared
**Returns:** zero if this object represents the same boolean value as the
argument; a positive value if this object represents true
and the argument represents false; and a negative value if
this object represents false and the argument represents true
**Throws:** NullPointerException

- if the argument is

null
**Since:** 1.5
**See Also:** Comparable

- compare

```java
public static int compare​(boolean x,
boolean y)
```

Compares two

boolean

values.
The value returned is identical to what would be returned by:

```java
Boolean.valueOf(x).compareTo(Boolean.valueOf(y))
```

**Parameters:** x

- the first

boolean

to compare
**Parameters:** y

- the second

boolean

to compare
**Returns:** the value

0

if

x == y

;
a value less than

0

if

!x && y

; and
a value greater than

0

if

x && !y
**Since:** 1.7

- logicalAnd

```java
public static boolean logicalAnd​(boolean a,
boolean b)
```

Returns the result of applying the logical AND operator to the
specified

boolean

operands.

**Parameters:** a

- the first operand
**Parameters:** b

- the second operand
**Returns:** the logical AND of

a

and

b
**Since:** 1.8
**See Also:** BinaryOperator

- logicalOr

```java
public static boolean logicalOr​(boolean a,
boolean b)
```

Returns the result of applying the logical OR operator to the
specified

boolean

operands.

**Parameters:** a

- the first operand
**Parameters:** b

- the second operand
**Returns:** the logical OR of

a

and

b
**Since:** 1.8
**See Also:** BinaryOperator

- logicalXor

```java
public static boolean logicalXor​(boolean a,
boolean b)
```

Returns the result of applying the logical XOR operator to the
specified

boolean

operands.

**Parameters:** a

- the first operand
**Parameters:** b

- the second operand
**Returns:** the logical XOR of

a

and

b
**Since:** 1.8
**See Also:** BinaryOperator

---

#### Method Detail

parseBoolean

```java
public static boolean parseBoolean​(
String
s)
```

Parses the string argument as a boolean. The

boolean

returned represents the value

true

if the string argument
is not

null

and is equal, ignoring case, to the string

"true"

.
Otherwise, a false value is returned, including for a null
argument.

Example:

Boolean.parseBoolean("True")

returns

true

.

Example:

Boolean.parseBoolean("yes")

returns

false

.

**Parameters:** s

- the

String

containing the boolean
representation to be parsed
**Returns:** the boolean represented by the string argument
**Since:** 1.5

---

#### parseBoolean

public static boolean parseBoolean​(

String

s)

Parses the string argument as a boolean. The

boolean

returned represents the value

true

if the string argument
is not

null

and is equal, ignoring case, to the string

"true"

.
Otherwise, a false value is returned, including for a null
argument.

Example:

Boolean.parseBoolean("True")

returns

true

.

Example:

Boolean.parseBoolean("yes")

returns

false

.

Example:

Boolean.parseBoolean("True")

returns

true

.

Example:

Boolean.parseBoolean("yes")

returns

false

.

booleanValue

```java
public boolean booleanValue()
```

Returns the value of this

Boolean

object as a boolean
primitive.

**Returns:** the primitive

boolean

value of this object.

---

#### booleanValue

public boolean booleanValue()

Returns the value of this

Boolean

object as a boolean
primitive.

valueOf

```java
public static
Boolean
valueOf​(boolean b)
```

Returns a

Boolean

instance representing the specified

boolean

value. If the specified

boolean

value
is

true

, this method returns

Boolean.TRUE

;
if it is

false

, this method returns

Boolean.FALSE

.
If a new

Boolean

instance is not required, this method
should generally be used in preference to the constructor

Boolean(boolean)

, as this method is likely to yield
significantly better space and time performance.

**Parameters:** b

- a boolean value.
**Returns:** a

Boolean

instance representing

b

.
**Since:** 1.4

---

#### valueOf

public static

Boolean

valueOf​(boolean b)

Returns a

Boolean

instance representing the specified

boolean

value. If the specified

boolean

value
is

true

, this method returns

Boolean.TRUE

;
if it is

false

, this method returns

Boolean.FALSE

.
If a new

Boolean

instance is not required, this method
should generally be used in preference to the constructor

Boolean(boolean)

, as this method is likely to yield
significantly better space and time performance.

valueOf

```java
public static
Boolean
valueOf​(
String
s)
```

Returns a

Boolean

with a value represented by the
specified string. The

Boolean

returned represents a
true value if the string argument is not

null

and is equal, ignoring case, to the string

"true"

.
Otherwise, a false value is returned, including for a null
argument.

**Parameters:** s

- a string.
**Returns:** the

Boolean

value represented by the string.

---

#### valueOf

public static

Boolean

valueOf​(

String

s)

Returns a

Boolean

with a value represented by the
specified string. The

Boolean

returned represents a
true value if the string argument is not

null

and is equal, ignoring case, to the string

"true"

.
Otherwise, a false value is returned, including for a null
argument.

toString

```java
public static
String
toString​(boolean b)
```

Returns a

String

object representing the specified
boolean. If the specified boolean is

true

, then
the string

"true"

will be returned, otherwise the
string

"false"

will be returned.

**Parameters:** b

- the boolean to be converted
**Returns:** the string representation of the specified

boolean
**Since:** 1.4

---

#### toString

public static

String

toString​(boolean b)

Returns a

String

object representing the specified
boolean. If the specified boolean is

true

, then
the string

"true"

will be returned, otherwise the
string

"false"

will be returned.

toString

```java
public
String
toString()
```

Returns a

String

object representing this Boolean's
value. If this object represents the value

true

,
a string equal to

"true"

is returned. Otherwise, a
string equal to

"false"

is returned.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object.

---

#### toString

public

String

toString()

Returns a

String

object representing this Boolean's
value. If this object represents the value

true

,
a string equal to

"true"

is returned. Otherwise, a
string equal to

"false"

is returned.

hashCode

```java
public int hashCode()
```

Returns a hash code for this

Boolean

object.

**Overrides:** hashCode

in class

Object
**Returns:** the integer

1231

if this object represents

true

; returns the integer

1237

if this
object represents

false

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code for this

Boolean

object.

hashCode

```java
public static int hashCode​(boolean value)
```

Returns a hash code for a

boolean

value; compatible with

Boolean.hashCode()

.

**Parameters:** value

- the value to hash
**Returns:** a hash code value for a

boolean

value.
**Since:** 1.8

---

#### hashCode

public static int hashCode​(boolean value)

Returns a hash code for a

boolean

value; compatible with

Boolean.hashCode()

.

equals

```java
public boolean equals​(
Object
obj)
```

Returns

true

if and only if the argument is not

null

and is a

Boolean

object that
represents the same

boolean

value as this object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare with.
**Returns:** true

if the Boolean objects represent the
same value;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Returns

true

if and only if the argument is not

null

and is a

Boolean

object that
represents the same

boolean

value as this object.

getBoolean

```java
public static boolean getBoolean​(
String
name)
```

Returns

true

if and only if the system property named
by the argument exists and is equal to, ignoring case, the
string

"true"

.
A system property is accessible through

getProperty

, a
method defined by the

System

class.

If there is no
property with the specified name, or if the specified name is
empty or null, then

false

is returned.

**Parameters:** name

- the system property name.
**Returns:** the

boolean

value of the system property.
**Throws:** SecurityException

- for the same reasons as

System.getProperty
**See Also:** System.getProperty(java.lang.String)

,

System.getProperty(java.lang.String, java.lang.String)

---

#### getBoolean

public static boolean getBoolean​(

String

name)

Returns

true

if and only if the system property named
by the argument exists and is equal to, ignoring case, the
string

"true"

.
A system property is accessible through

getProperty

, a
method defined by the

System

class.

If there is no
property with the specified name, or if the specified name is
empty or null, then

false

is returned.

If there is no
property with the specified name, or if the specified name is
empty or null, then

false

is returned.

compareTo

```java
public int compareTo​(
Boolean
b)
```

Compares this

Boolean

instance with another.

**Specified by:** compareTo

in interface

Comparable

<

Boolean

>
**Parameters:** b

- the

Boolean

instance to be compared
**Returns:** zero if this object represents the same boolean value as the
argument; a positive value if this object represents true
and the argument represents false; and a negative value if
this object represents false and the argument represents true
**Throws:** NullPointerException

- if the argument is

null
**Since:** 1.5
**See Also:** Comparable

---

#### compareTo

public int compareTo​(

Boolean

b)

Compares this

Boolean

instance with another.

compare

```java
public static int compare​(boolean x,
boolean y)
```

Compares two

boolean

values.
The value returned is identical to what would be returned by:

```java
Boolean.valueOf(x).compareTo(Boolean.valueOf(y))
```

**Parameters:** x

- the first

boolean

to compare
**Parameters:** y

- the second

boolean

to compare
**Returns:** the value

0

if

x == y

;
a value less than

0

if

!x && y

; and
a value greater than

0

if

x && !y
**Since:** 1.7

---

#### compare

public static int compare​(boolean x,
boolean y)

Compares two

boolean

values.
The value returned is identical to what would be returned by:

```java
Boolean.valueOf(x).compareTo(Boolean.valueOf(y))
```

Boolean.valueOf(x).compareTo(Boolean.valueOf(y))

logicalAnd

```java
public static boolean logicalAnd​(boolean a,
boolean b)
```

Returns the result of applying the logical AND operator to the
specified

boolean

operands.

**Parameters:** a

- the first operand
**Parameters:** b

- the second operand
**Returns:** the logical AND of

a

and

b
**Since:** 1.8
**See Also:** BinaryOperator

---

#### logicalAnd

public static boolean logicalAnd​(boolean a,
boolean b)

Returns the result of applying the logical AND operator to the
specified

boolean

operands.

logicalOr

```java
public static boolean logicalOr​(boolean a,
boolean b)
```

Returns the result of applying the logical OR operator to the
specified

boolean

operands.

**Parameters:** a

- the first operand
**Parameters:** b

- the second operand
**Returns:** the logical OR of

a

and

b
**Since:** 1.8
**See Also:** BinaryOperator

---

#### logicalOr

public static boolean logicalOr​(boolean a,
boolean b)

Returns the result of applying the logical OR operator to the
specified

boolean

operands.

logicalXor

```java
public static boolean logicalXor​(boolean a,
boolean b)
```

Returns the result of applying the logical XOR operator to the
specified

boolean

operands.

**Parameters:** a

- the first operand
**Parameters:** b

- the second operand
**Returns:** the logical XOR of

a

and

b
**Since:** 1.8
**See Also:** BinaryOperator

---

#### logicalXor

public static boolean logicalXor​(boolean a,
boolean b)

Returns the result of applying the logical XOR operator to the
specified

boolean

operands.

---

