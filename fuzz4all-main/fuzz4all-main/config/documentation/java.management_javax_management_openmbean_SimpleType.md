# Class SimpleType<T>

**Source:** `java.management\javax\management\openmbean\SimpleType.html`

### Class Description

```java
public final class
SimpleType<T>

extends
OpenType
<T>
```

The

SimpleType

class is the

open type

class whose instances describe
all

open data

values which are neither arrays,
nor

CompositeData

values,
nor

TabularData

values.
It predefines all its possible instances as static fields, and has no public constructor.

Given a

SimpleType

instance describing values whose Java class name is

className

,
the internal fields corresponding to the name and description of this

SimpleType

instance
are also set to

className

.
In other words, its methods

getClassName

,

getTypeName

and

getDescription

all return the same string value

className

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final
SimpleType
<
Void
> VOID

The

SimpleType

instance describing values whose
Java class name is

java.lang.Void

.

---

#### public static final
SimpleType
<
Boolean
> BOOLEAN

The

SimpleType

instance describing values whose
Java class name is

java.lang.Boolean

.

---

#### public static final
SimpleType
<
Character
> CHARACTER

The

SimpleType

instance describing values whose
Java class name is

java.lang.Character

.

---

#### public static final
SimpleType
<
Byte
> BYTE

The

SimpleType

instance describing values whose
Java class name is

java.lang.Byte

.

---

#### public static final
SimpleType
<
Short
> SHORT

The

SimpleType

instance describing values whose
Java class name is

java.lang.Short

.

---

#### public static final
SimpleType
<
Integer
> INTEGER

The

SimpleType

instance describing values whose
Java class name is

java.lang.Integer

.

---

#### public static final
SimpleType
<
Long
> LONG

The

SimpleType

instance describing values whose
Java class name is

java.lang.Long

.

---

#### public static final
SimpleType
<
Float
> FLOAT

The

SimpleType

instance describing values whose
Java class name is

java.lang.Float

.

---

#### public static final
SimpleType
<
Double
> DOUBLE

The

SimpleType

instance describing values whose
Java class name is

java.lang.Double

.

---

#### public static final
SimpleType
<
String
> STRING

The

SimpleType

instance describing values whose
Java class name is

java.lang.String

.

---

#### public static final
SimpleType
<
BigDecimal
> BIGDECIMAL

The

SimpleType

instance describing values whose
Java class name is

java.math.BigDecimal

.

---

#### public static final
SimpleType
<
BigInteger
> BIGINTEGER

The

SimpleType

instance describing values whose
Java class name is

java.math.BigInteger

.

---

#### public static final
SimpleType
<
Date
> DATE

The

SimpleType

instance describing values whose
Java class name is

java.util.Date

.

---

#### public static final
SimpleType
<
ObjectName
> OBJECTNAME

The

SimpleType

instance describing values whose
Java class name is

javax.management.ObjectName

.

---

### Constructor Details

*No entries found.*

### Method Details

#### public boolean isValue​(
Object
obj)

Tests whether

obj

is a value for this

SimpleType

instance.

This method returns

true

if and only if

obj

is not null and

obj

's class name is the same as the className field
defined for this

SimpleType

instance (ie the class
name returned by the

getClassName

method).

**Specified by:**
- isValue

in class

OpenType

<

T

>

**Parameters:**
- obj

- the object to be tested.

**Returns:**
- true

if

obj

is a value for this

SimpleType

instance.

---

#### public boolean equals​(
Object
obj)

Compares the specified

obj

parameter with this

SimpleType

instance for equality.

Two

SimpleType

instances are equal if and only if their

getClassName

methods return the same value.

**Specified by:**
- equals

in class

OpenType

<

T

>

**Parameters:**
- obj

- the object to be compared for equality with this

SimpleType

instance;
if

obj

is

null

or is not an instance of the class

SimpleType

,

equals

returns

false

.

**Returns:**
- true

if the specified object is equal to this

SimpleType

instance.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this

SimpleType

instance.
The hash code of a

SimpleType

instance is the hash code of
the string value returned by the

getClassName

method.

As

SimpleType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this

SimpleType

instance

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string representation of this

SimpleType

instance.

The string representation consists of
the name of this class (ie

javax.management.openmbean.SimpleType

) and the type name
for this instance (which is the java class name of the values this

SimpleType

instance represents).

As

SimpleType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

**Specified by:**
- toString

in class

OpenType

<

T

>

**Returns:**
- a string representation of this

SimpleType

instance

---

#### public
Object
readResolve()
throws
ObjectStreamException

Replace an object read from an

ObjectInputStream

with the unique instance for that
value.

**Returns:**
- the replacement object.

**Throws:**
- ObjectStreamException

- if the read object cannot be
resolved.

---

### Additional Sections

#### Class SimpleType<T>

java.lang.Object

- javax.management.openmbean.OpenType

<T>
- - javax.management.openmbean.SimpleType<T>

javax.management.openmbean.OpenType

<T>

- javax.management.openmbean.SimpleType<T>

javax.management.openmbean.SimpleType<T>

**All Implemented Interfaces:** Serializable

```java
public final class
SimpleType<T>

extends
OpenType
<T>
```

The

SimpleType

class is the

open type

class whose instances describe
all

open data

values which are neither arrays,
nor

CompositeData

values,
nor

TabularData

values.
It predefines all its possible instances as static fields, and has no public constructor.

Given a

SimpleType

instance describing values whose Java class name is

className

,
the internal fields corresponding to the name and description of this

SimpleType

instance
are also set to

className

.
In other words, its methods

getClassName

,

getTypeName

and

getDescription

all return the same string value

className

.

**Since:** 1.5
**See Also:** Serialized Form

public final class

SimpleType<T>

extends

OpenType

<T>

The

SimpleType

class is the

open type

class whose instances describe
all

open data

values which are neither arrays,
nor

CompositeData

values,
nor

TabularData

values.
It predefines all its possible instances as static fields, and has no public constructor.

Given a

SimpleType

instance describing values whose Java class name is

className

,
the internal fields corresponding to the name and description of this

SimpleType

instance
are also set to

className

.
In other words, its methods

getClassName

,

getTypeName

and

getDescription

all return the same string value

className

.

Given a

SimpleType

instance describing values whose Java class name is

className

,
the internal fields corresponding to the name and description of this

SimpleType

instance
are also set to

className

.
In other words, its methods

getClassName

,

getTypeName

and

getDescription

all return the same string value

className

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

SimpleType

<

BigDecimal

>

BIGDECIMAL

The

SimpleType

instance describing values whose
Java class name is

java.math.BigDecimal

.

static

SimpleType

<

BigInteger

>

BIGINTEGER

The

SimpleType

instance describing values whose
Java class name is

java.math.BigInteger

.

static

SimpleType

<

Boolean

>

BOOLEAN

The

SimpleType

instance describing values whose
Java class name is

java.lang.Boolean

.

static

SimpleType

<

Byte

>

BYTE

The

SimpleType

instance describing values whose
Java class name is

java.lang.Byte

.

static

SimpleType

<

Character

>

CHARACTER

The

SimpleType

instance describing values whose
Java class name is

java.lang.Character

.

static

SimpleType

<

Date

>

DATE

The

SimpleType

instance describing values whose
Java class name is

java.util.Date

.

static

SimpleType

<

Double

>

DOUBLE

The

SimpleType

instance describing values whose
Java class name is

java.lang.Double

.

static

SimpleType

<

Float

>

FLOAT

The

SimpleType

instance describing values whose
Java class name is

java.lang.Float

.

static

SimpleType

<

Integer

>

INTEGER

The

SimpleType

instance describing values whose
Java class name is

java.lang.Integer

.

static

SimpleType

<

Long

>

LONG

The

SimpleType

instance describing values whose
Java class name is

java.lang.Long

.

static

SimpleType

<

ObjectName

>

OBJECTNAME

The

SimpleType

instance describing values whose
Java class name is

javax.management.ObjectName

.

static

SimpleType

<

Short

>

SHORT

The

SimpleType

instance describing values whose
Java class name is

java.lang.Short

.

static

SimpleType

<

String

>

STRING

The

SimpleType

instance describing values whose
Java class name is

java.lang.String

.

static

SimpleType

<

Void

>

VOID

The

SimpleType

instance describing values whose
Java class name is

java.lang.Void

.

- Fields declared in class javax.management.openmbean.

OpenType

ALLOWED_CLASSNAMES

,

ALLOWED_CLASSNAMES_LIST

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares the specified

obj

parameter with this

SimpleType

instance for equality.

int

hashCode

()

Returns the hash code value for this

SimpleType

instance.

boolean

isValue

​(

Object

obj)

Tests whether

obj

is a value for this

SimpleType

instance.

Object

readResolve

()

Replace an object read from an

ObjectInputStream

with the unique instance for that
value.

String

toString

()

Returns a string representation of this

SimpleType

instance.

- Methods declared in class javax.management.openmbean.

OpenType

getClassName

,

getDescription

,

getTypeName

,

isArray

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

SimpleType

<

BigDecimal

>

BIGDECIMAL

The

SimpleType

instance describing values whose
Java class name is

java.math.BigDecimal

.

static

SimpleType

<

BigInteger

>

BIGINTEGER

The

SimpleType

instance describing values whose
Java class name is

java.math.BigInteger

.

static

SimpleType

<

Boolean

>

BOOLEAN

The

SimpleType

instance describing values whose
Java class name is

java.lang.Boolean

.

static

SimpleType

<

Byte

>

BYTE

The

SimpleType

instance describing values whose
Java class name is

java.lang.Byte

.

static

SimpleType

<

Character

>

CHARACTER

The

SimpleType

instance describing values whose
Java class name is

java.lang.Character

.

static

SimpleType

<

Date

>

DATE

The

SimpleType

instance describing values whose
Java class name is

java.util.Date

.

static

SimpleType

<

Double

>

DOUBLE

The

SimpleType

instance describing values whose
Java class name is

java.lang.Double

.

static

SimpleType

<

Float

>

FLOAT

The

SimpleType

instance describing values whose
Java class name is

java.lang.Float

.

static

SimpleType

<

Integer

>

INTEGER

The

SimpleType

instance describing values whose
Java class name is

java.lang.Integer

.

static

SimpleType

<

Long

>

LONG

The

SimpleType

instance describing values whose
Java class name is

java.lang.Long

.

static

SimpleType

<

ObjectName

>

OBJECTNAME

The

SimpleType

instance describing values whose
Java class name is

javax.management.ObjectName

.

static

SimpleType

<

Short

>

SHORT

The

SimpleType

instance describing values whose
Java class name is

java.lang.Short

.

static

SimpleType

<

String

>

STRING

The

SimpleType

instance describing values whose
Java class name is

java.lang.String

.

static

SimpleType

<

Void

>

VOID

The

SimpleType

instance describing values whose
Java class name is

java.lang.Void

.

- Fields declared in class javax.management.openmbean.

OpenType

ALLOWED_CLASSNAMES

,

ALLOWED_CLASSNAMES_LIST

---

#### Field Summary

The

SimpleType

instance describing values whose
Java class name is

java.math.BigDecimal

.

The

SimpleType

instance describing values whose
Java class name is

java.math.BigInteger

.

The

SimpleType

instance describing values whose
Java class name is

java.lang.Boolean

.

The

SimpleType

instance describing values whose
Java class name is

java.lang.Byte

.

The

SimpleType

instance describing values whose
Java class name is

java.lang.Character

.

The

SimpleType

instance describing values whose
Java class name is

java.util.Date

.

The

SimpleType

instance describing values whose
Java class name is

java.lang.Double

.

The

SimpleType

instance describing values whose
Java class name is

java.lang.Float

.

The

SimpleType

instance describing values whose
Java class name is

java.lang.Integer

.

The

SimpleType

instance describing values whose
Java class name is

java.lang.Long

.

The

SimpleType

instance describing values whose
Java class name is

javax.management.ObjectName

.

The

SimpleType

instance describing values whose
Java class name is

java.lang.Short

.

The

SimpleType

instance describing values whose
Java class name is

java.lang.String

.

The

SimpleType

instance describing values whose
Java class name is

java.lang.Void

.

Fields declared in class javax.management.openmbean.

OpenType

ALLOWED_CLASSNAMES

,

ALLOWED_CLASSNAMES_LIST

---

#### Fields declared in class javax.management.openmbean. OpenType

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares the specified

obj

parameter with this

SimpleType

instance for equality.

int

hashCode

()

Returns the hash code value for this

SimpleType

instance.

boolean

isValue

​(

Object

obj)

Tests whether

obj

is a value for this

SimpleType

instance.

Object

readResolve

()

Replace an object read from an

ObjectInputStream

with the unique instance for that
value.

String

toString

()

Returns a string representation of this

SimpleType

instance.

- Methods declared in class javax.management.openmbean.

OpenType

getClassName

,

getDescription

,

getTypeName

,

isArray

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

Compares the specified

obj

parameter with this

SimpleType

instance for equality.

Returns the hash code value for this

SimpleType

instance.

Tests whether

obj

is a value for this

SimpleType

instance.

Replace an object read from an

ObjectInputStream

with the unique instance for that
value.

Returns a string representation of this

SimpleType

instance.

Methods declared in class javax.management.openmbean.

OpenType

getClassName

,

getDescription

,

getTypeName

,

isArray

---

#### Methods declared in class javax.management.openmbean. OpenType

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

- VOID

```java
public static final
SimpleType
<
Void
> VOID
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Void

.

- BOOLEAN

```java
public static final
SimpleType
<
Boolean
> BOOLEAN
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Boolean

.

- CHARACTER

```java
public static final
SimpleType
<
Character
> CHARACTER
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Character

.

- BYTE

```java
public static final
SimpleType
<
Byte
> BYTE
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Byte

.

- SHORT

```java
public static final
SimpleType
<
Short
> SHORT
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Short

.

- INTEGER

```java
public static final
SimpleType
<
Integer
> INTEGER
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Integer

.

- LONG

```java
public static final
SimpleType
<
Long
> LONG
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Long

.

- FLOAT

```java
public static final
SimpleType
<
Float
> FLOAT
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Float

.

- DOUBLE

```java
public static final
SimpleType
<
Double
> DOUBLE
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Double

.

- STRING

```java
public static final
SimpleType
<
String
> STRING
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.String

.

- BIGDECIMAL

```java
public static final
SimpleType
<
BigDecimal
> BIGDECIMAL
```

The

SimpleType

instance describing values whose
Java class name is

java.math.BigDecimal

.

- BIGINTEGER

```java
public static final
SimpleType
<
BigInteger
> BIGINTEGER
```

The

SimpleType

instance describing values whose
Java class name is

java.math.BigInteger

.

- DATE

```java
public static final
SimpleType
<
Date
> DATE
```

The

SimpleType

instance describing values whose
Java class name is

java.util.Date

.

- OBJECTNAME

```java
public static final
SimpleType
<
ObjectName
> OBJECTNAME
```

The

SimpleType

instance describing values whose
Java class name is

javax.management.ObjectName

.

============ METHOD DETAIL ==========

- Method Detail

- isValue

```java
public boolean isValue​(
Object
obj)
```

Tests whether

obj

is a value for this

SimpleType

instance.

This method returns

true

if and only if

obj

is not null and

obj

's class name is the same as the className field
defined for this

SimpleType

instance (ie the class
name returned by the

getClassName

method).

**Specified by:** isValue

in class

OpenType

<

T

>
**Parameters:** obj

- the object to be tested.
**Returns:** true

if

obj

is a value for this

SimpleType

instance.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

SimpleType

instance for equality.

Two

SimpleType

instances are equal if and only if their

getClassName

methods return the same value.

**Specified by:** equals

in class

OpenType

<

T

>
**Parameters:** obj

- the object to be compared for equality with this

SimpleType

instance;
if

obj

is

null

or is not an instance of the class

SimpleType

,

equals

returns

false

.
**Returns:** true

if the specified object is equal to this

SimpleType

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

SimpleType

instance.
The hash code of a

SimpleType

instance is the hash code of
the string value returned by the

getClassName

method.

As

SimpleType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

SimpleType

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this

SimpleType

instance.

The string representation consists of
the name of this class (ie

javax.management.openmbean.SimpleType

) and the type name
for this instance (which is the java class name of the values this

SimpleType

instance represents).

As

SimpleType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

**Specified by:** toString

in class

OpenType

<

T

>
**Returns:** a string representation of this

SimpleType

instance

- readResolve

```java
public
Object
readResolve()
throws
ObjectStreamException
```

Replace an object read from an

ObjectInputStream

with the unique instance for that
value.

**Returns:** the replacement object.
**Throws:** ObjectStreamException

- if the read object cannot be
resolved.

Field Detail

- VOID

```java
public static final
SimpleType
<
Void
> VOID
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Void

.

- BOOLEAN

```java
public static final
SimpleType
<
Boolean
> BOOLEAN
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Boolean

.

- CHARACTER

```java
public static final
SimpleType
<
Character
> CHARACTER
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Character

.

- BYTE

```java
public static final
SimpleType
<
Byte
> BYTE
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Byte

.

- SHORT

```java
public static final
SimpleType
<
Short
> SHORT
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Short

.

- INTEGER

```java
public static final
SimpleType
<
Integer
> INTEGER
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Integer

.

- LONG

```java
public static final
SimpleType
<
Long
> LONG
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Long

.

- FLOAT

```java
public static final
SimpleType
<
Float
> FLOAT
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Float

.

- DOUBLE

```java
public static final
SimpleType
<
Double
> DOUBLE
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Double

.

- STRING

```java
public static final
SimpleType
<
String
> STRING
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.String

.

- BIGDECIMAL

```java
public static final
SimpleType
<
BigDecimal
> BIGDECIMAL
```

The

SimpleType

instance describing values whose
Java class name is

java.math.BigDecimal

.

- BIGINTEGER

```java
public static final
SimpleType
<
BigInteger
> BIGINTEGER
```

The

SimpleType

instance describing values whose
Java class name is

java.math.BigInteger

.

- DATE

```java
public static final
SimpleType
<
Date
> DATE
```

The

SimpleType

instance describing values whose
Java class name is

java.util.Date

.

- OBJECTNAME

```java
public static final
SimpleType
<
ObjectName
> OBJECTNAME
```

The

SimpleType

instance describing values whose
Java class name is

javax.management.ObjectName

.

---

#### Field Detail

VOID

```java
public static final
SimpleType
<
Void
> VOID
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Void

.

---

#### VOID

public static final

SimpleType

<

Void

> VOID

The

SimpleType

instance describing values whose
Java class name is

java.lang.Void

.

BOOLEAN

```java
public static final
SimpleType
<
Boolean
> BOOLEAN
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Boolean

.

---

#### BOOLEAN

public static final

SimpleType

<

Boolean

> BOOLEAN

The

SimpleType

instance describing values whose
Java class name is

java.lang.Boolean

.

CHARACTER

```java
public static final
SimpleType
<
Character
> CHARACTER
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Character

.

---

#### CHARACTER

public static final

SimpleType

<

Character

> CHARACTER

The

SimpleType

instance describing values whose
Java class name is

java.lang.Character

.

BYTE

```java
public static final
SimpleType
<
Byte
> BYTE
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Byte

.

---

#### BYTE

public static final

SimpleType

<

Byte

> BYTE

The

SimpleType

instance describing values whose
Java class name is

java.lang.Byte

.

SHORT

```java
public static final
SimpleType
<
Short
> SHORT
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Short

.

---

#### SHORT

public static final

SimpleType

<

Short

> SHORT

The

SimpleType

instance describing values whose
Java class name is

java.lang.Short

.

INTEGER

```java
public static final
SimpleType
<
Integer
> INTEGER
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Integer

.

---

#### INTEGER

public static final

SimpleType

<

Integer

> INTEGER

The

SimpleType

instance describing values whose
Java class name is

java.lang.Integer

.

LONG

```java
public static final
SimpleType
<
Long
> LONG
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Long

.

---

#### LONG

public static final

SimpleType

<

Long

> LONG

The

SimpleType

instance describing values whose
Java class name is

java.lang.Long

.

FLOAT

```java
public static final
SimpleType
<
Float
> FLOAT
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Float

.

---

#### FLOAT

public static final

SimpleType

<

Float

> FLOAT

The

SimpleType

instance describing values whose
Java class name is

java.lang.Float

.

DOUBLE

```java
public static final
SimpleType
<
Double
> DOUBLE
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.Double

.

---

#### DOUBLE

public static final

SimpleType

<

Double

> DOUBLE

The

SimpleType

instance describing values whose
Java class name is

java.lang.Double

.

STRING

```java
public static final
SimpleType
<
String
> STRING
```

The

SimpleType

instance describing values whose
Java class name is

java.lang.String

.

---

#### STRING

public static final

SimpleType

<

String

> STRING

The

SimpleType

instance describing values whose
Java class name is

java.lang.String

.

BIGDECIMAL

```java
public static final
SimpleType
<
BigDecimal
> BIGDECIMAL
```

The

SimpleType

instance describing values whose
Java class name is

java.math.BigDecimal

.

---

#### BIGDECIMAL

public static final

SimpleType

<

BigDecimal

> BIGDECIMAL

The

SimpleType

instance describing values whose
Java class name is

java.math.BigDecimal

.

BIGINTEGER

```java
public static final
SimpleType
<
BigInteger
> BIGINTEGER
```

The

SimpleType

instance describing values whose
Java class name is

java.math.BigInteger

.

---

#### BIGINTEGER

public static final

SimpleType

<

BigInteger

> BIGINTEGER

The

SimpleType

instance describing values whose
Java class name is

java.math.BigInteger

.

DATE

```java
public static final
SimpleType
<
Date
> DATE
```

The

SimpleType

instance describing values whose
Java class name is

java.util.Date

.

---

#### DATE

public static final

SimpleType

<

Date

> DATE

The

SimpleType

instance describing values whose
Java class name is

java.util.Date

.

OBJECTNAME

```java
public static final
SimpleType
<
ObjectName
> OBJECTNAME
```

The

SimpleType

instance describing values whose
Java class name is

javax.management.ObjectName

.

---

#### OBJECTNAME

public static final

SimpleType

<

ObjectName

> OBJECTNAME

The

SimpleType

instance describing values whose
Java class name is

javax.management.ObjectName

.

Method Detail

- isValue

```java
public boolean isValue​(
Object
obj)
```

Tests whether

obj

is a value for this

SimpleType

instance.

This method returns

true

if and only if

obj

is not null and

obj

's class name is the same as the className field
defined for this

SimpleType

instance (ie the class
name returned by the

getClassName

method).

**Specified by:** isValue

in class

OpenType

<

T

>
**Parameters:** obj

- the object to be tested.
**Returns:** true

if

obj

is a value for this

SimpleType

instance.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

SimpleType

instance for equality.

Two

SimpleType

instances are equal if and only if their

getClassName

methods return the same value.

**Specified by:** equals

in class

OpenType

<

T

>
**Parameters:** obj

- the object to be compared for equality with this

SimpleType

instance;
if

obj

is

null

or is not an instance of the class

SimpleType

,

equals

returns

false

.
**Returns:** true

if the specified object is equal to this

SimpleType

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

SimpleType

instance.
The hash code of a

SimpleType

instance is the hash code of
the string value returned by the

getClassName

method.

As

SimpleType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

SimpleType

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this

SimpleType

instance.

The string representation consists of
the name of this class (ie

javax.management.openmbean.SimpleType

) and the type name
for this instance (which is the java class name of the values this

SimpleType

instance represents).

As

SimpleType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

**Specified by:** toString

in class

OpenType

<

T

>
**Returns:** a string representation of this

SimpleType

instance

- readResolve

```java
public
Object
readResolve()
throws
ObjectStreamException
```

Replace an object read from an

ObjectInputStream

with the unique instance for that
value.

**Returns:** the replacement object.
**Throws:** ObjectStreamException

- if the read object cannot be
resolved.

---

#### Method Detail

isValue

```java
public boolean isValue​(
Object
obj)
```

Tests whether

obj

is a value for this

SimpleType

instance.

This method returns

true

if and only if

obj

is not null and

obj

's class name is the same as the className field
defined for this

SimpleType

instance (ie the class
name returned by the

getClassName

method).

**Specified by:** isValue

in class

OpenType

<

T

>
**Parameters:** obj

- the object to be tested.
**Returns:** true

if

obj

is a value for this

SimpleType

instance.

---

#### isValue

public boolean isValue​(

Object

obj)

Tests whether

obj

is a value for this

SimpleType

instance.

This method returns

true

if and only if

obj

is not null and

obj

's class name is the same as the className field
defined for this

SimpleType

instance (ie the class
name returned by the

getClassName

method).

This method returns

true

if and only if

obj

is not null and

obj

's class name is the same as the className field
defined for this

SimpleType

instance (ie the class
name returned by the

getClassName

method).

equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

SimpleType

instance for equality.

Two

SimpleType

instances are equal if and only if their

getClassName

methods return the same value.

**Specified by:** equals

in class

OpenType

<

T

>
**Parameters:** obj

- the object to be compared for equality with this

SimpleType

instance;
if

obj

is

null

or is not an instance of the class

SimpleType

,

equals

returns

false

.
**Returns:** true

if the specified object is equal to this

SimpleType

instance.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares the specified

obj

parameter with this

SimpleType

instance for equality.

Two

SimpleType

instances are equal if and only if their

getClassName

methods return the same value.

Two

SimpleType

instances are equal if and only if their

getClassName

methods return the same value.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this

SimpleType

instance.
The hash code of a

SimpleType

instance is the hash code of
the string value returned by the

getClassName

method.

As

SimpleType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

SimpleType

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this

SimpleType

instance.
The hash code of a

SimpleType

instance is the hash code of
the string value returned by the

getClassName

method.

As

SimpleType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

As

SimpleType

instances are immutable, the hash code for this instance is calculated once,
on the first call to

hashCode

, and then the same value is returned for subsequent calls.

toString

```java
public
String
toString()
```

Returns a string representation of this

SimpleType

instance.

The string representation consists of
the name of this class (ie

javax.management.openmbean.SimpleType

) and the type name
for this instance (which is the java class name of the values this

SimpleType

instance represents).

As

SimpleType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

**Specified by:** toString

in class

OpenType

<

T

>
**Returns:** a string representation of this

SimpleType

instance

---

#### toString

public

String

toString()

Returns a string representation of this

SimpleType

instance.

The string representation consists of
the name of this class (ie

javax.management.openmbean.SimpleType

) and the type name
for this instance (which is the java class name of the values this

SimpleType

instance represents).

As

SimpleType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

The string representation consists of
the name of this class (ie

javax.management.openmbean.SimpleType

) and the type name
for this instance (which is the java class name of the values this

SimpleType

instance represents).

As

SimpleType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

As

SimpleType

instances are immutable, the string representation for this instance is calculated once,
on the first call to

toString

, and then the same value is returned for subsequent calls.

readResolve

```java
public
Object
readResolve()
throws
ObjectStreamException
```

Replace an object read from an

ObjectInputStream

with the unique instance for that
value.

**Returns:** the replacement object.
**Throws:** ObjectStreamException

- if the read object cannot be
resolved.

---

#### readResolve

public

Object

readResolve()
throws

ObjectStreamException

Replace an object read from an

ObjectInputStream

with the unique instance for that
value.

---

