# Class OpenType<T>

**Source:** `java.management\javax\management\openmbean\OpenType.html`

### Class Description

```java
public abstract class
OpenType<T>

extends
Object

implements
Serializable
```

The

OpenType

class is the parent abstract class of all classes which describe the actual

open type

of open data values.

An

open type

is defined by:

- the fully qualified Java class name of the open data values this type describes;
note that only a limited set of Java classes is allowed for open data values
(see

ALLOWED_CLASSNAMES_LIST

),
- its name,
- its description.

**Type Parameters:** T

- the Java type that instances described by this type must
have. For example,

SimpleType.INTEGER

is a

SimpleType<Integer>

which is a subclass of

OpenType<Integer>

,
meaning that an attribute, parameter, or return value that is described
as a

SimpleType.INTEGER

must have Java type

Integer

.

---

### Field Details

#### public static final
List
<
String
> ALLOWED_CLASSNAMES_LIST

List of the fully qualified names of the Java classes allowed for open
data values. A multidimensional array of any one of these classes or
their corresponding primitive types is also an allowed class for open
data values.

```java
ALLOWED_CLASSNAMES_LIST = {
"java.lang.Void",
"java.lang.Boolean",
"java.lang.Character",
"java.lang.Byte",
"java.lang.Short",
"java.lang.Integer",
"java.lang.Long",
"java.lang.Float",
"java.lang.Double",
"java.lang.String",
"java.math.BigDecimal",
"java.math.BigInteger",
"java.util.Date",
"javax.management.ObjectName",
CompositeData.class.getName(),
TabularData.class.getName() } ;
```

---

#### @Deprecated

public static final
String
[] ALLOWED_CLASSNAMES

*No description found.*

---

### Constructor Details

#### protected OpenType​(
String
className,

String
typeName,

String
description)
throws
OpenDataException

Constructs an

OpenType

instance (actually a subclass instance as

OpenType

is abstract),
checking for the validity of the given parameters.
The validity constraints are described below for each parameter.

**Parameters:**
- className

- The fully qualified Java class name of the open data values this open type describes.
The valid Java class names allowed for open data values are listed in

ALLOWED_CLASSNAMES_LIST

.
A multidimensional array of any one of these classes
or their corresponding primitive types is also an allowed class,
in which case the class name follows the rules defined by the method

getName()

of

java.lang.Class

.
For example, a 3-dimensional array of Strings has for class name
"

[[[Ljava.lang.String;

" (without the quotes).
- typeName

- The name given to the open type this instance represents; cannot be a null or empty string.
- description

- The human readable description of the open type this instance represents;
cannot be a null or empty string.

**Throws:**
- IllegalArgumentException

- if

className

,

typeName

or

description

is a null or empty string
- OpenDataException

- if

className

is not one of the allowed Java class names for open data

---

### Method Details

#### public
String
getClassName()

Returns the fully qualified Java class name of the open data values
this open type describes.
The only possible Java class names for open data values are listed in

ALLOWED_CLASSNAMES_LIST

.
A multidimensional array of any one of these classes or their
corresponding primitive types is also an allowed class,
in which case the class name follows the rules defined by the method

getName()

of

java.lang.Class

.
For example, a 3-dimensional array of Strings has for class name
"

[[[Ljava.lang.String;

" (without the quotes),
a 3-dimensional array of Integers has for class name
"

[[[Ljava.lang.Integer;

" (without the quotes),
and a 3-dimensional array of int has for class name
"

[[[I

" (without the quotes)

**Returns:**
- the class name.

---

#### public
String
getTypeName()

Returns the name of this

OpenType

instance.

**Returns:**
- the type name.

---

#### public
String
getDescription()

Returns the text description of this

OpenType

instance.

**Returns:**
- the description.

---

#### public boolean isArray()

Returns

true

if the open data values this open
type describes are arrays,

false

otherwise.

**Returns:**
- true if this is an array type.

---

#### public abstract boolean isValue​(
Object
obj)

Tests whether

obj

is a value for this open type.

**Parameters:**
- obj

- the object to be tested for validity.

**Returns:**
- true

if

obj

is a value for this
open type,

false

otherwise.

---

#### public abstract boolean equals​(
Object
obj)

Compares the specified

obj

parameter with this
open type instance for equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to compare to.

**Returns:**
- true if this object and

obj

are equal.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public abstract
String
toString()

Returns a string representation of this open type instance.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string representation.

---

### Additional Sections

#### Class OpenType<T>

java.lang.Object

- javax.management.openmbean.OpenType<T>

javax.management.openmbean.OpenType<T>

**Type Parameters:** T

- the Java type that instances described by this type must
have. For example,

SimpleType.INTEGER

is a

SimpleType<Integer>

which is a subclass of

OpenType<Integer>

,
meaning that an attribute, parameter, or return value that is described
as a

SimpleType.INTEGER

must have Java type

Integer

.

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** ArrayType

,

CompositeType

,

SimpleType

,

TabularType

```java
public abstract class
OpenType<T>

extends
Object

implements
Serializable
```

The

OpenType

class is the parent abstract class of all classes which describe the actual

open type

of open data values.

An

open type

is defined by:

- the fully qualified Java class name of the open data values this type describes;
note that only a limited set of Java classes is allowed for open data values
(see

ALLOWED_CLASSNAMES_LIST

),
- its name,
- its description.

**Since:** 1.5
**See Also:** Serialized Form

public abstract class

OpenType<T>

extends

Object

implements

Serializable

The

OpenType

class is the parent abstract class of all classes which describe the actual

open type

of open data values.

An

open type

is defined by:

- the fully qualified Java class name of the open data values this type describes;
note that only a limited set of Java classes is allowed for open data values
(see

ALLOWED_CLASSNAMES_LIST

),
- its name,
- its description.

An

open type

is defined by:

- the fully qualified Java class name of the open data values this type describes;
note that only a limited set of Java classes is allowed for open data values
(see

ALLOWED_CLASSNAMES_LIST

),
- its name,
- its description.

the fully qualified Java class name of the open data values this type describes;
note that only a limited set of Java classes is allowed for open data values
(see

ALLOWED_CLASSNAMES_LIST

),

its name,

its description.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

[]

ALLOWED_CLASSNAMES

Deprecated.

Use

ALLOWED_CLASSNAMES_LIST

instead.

static

List

<

String

>

ALLOWED_CLASSNAMES_LIST

List of the fully qualified names of the Java classes allowed for open
data values.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

OpenType

​(

String

className,

String

typeName,

String

description)

Constructs an

OpenType

instance (actually a subclass instance as

OpenType

is abstract),
checking for the validity of the given parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract boolean

equals

​(

Object

obj)

Compares the specified

obj

parameter with this
open type instance for equality.

String

getClassName

()

Returns the fully qualified Java class name of the open data values
this open type describes.

String

getDescription

()

Returns the text description of this

OpenType

instance.

String

getTypeName

()

Returns the name of this

OpenType

instance.

boolean

isArray

()

Returns

true

if the open data values this open
type describes are arrays,

false

otherwise.

abstract boolean

isValue

​(

Object

obj)

Tests whether

obj

is a value for this open type.

abstract

String

toString

()

Returns a string representation of this open type instance.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

hashCode

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

String

[]

ALLOWED_CLASSNAMES

Deprecated.

Use

ALLOWED_CLASSNAMES_LIST

instead.

static

List

<

String

>

ALLOWED_CLASSNAMES_LIST

List of the fully qualified names of the Java classes allowed for open
data values.

---

#### Field Summary

Deprecated.

Use

ALLOWED_CLASSNAMES_LIST

instead.

List of the fully qualified names of the Java classes allowed for open
data values.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

OpenType

​(

String

className,

String

typeName,

String

description)

Constructs an

OpenType

instance (actually a subclass instance as

OpenType

is abstract),
checking for the validity of the given parameters.

---

#### Constructor Summary

Constructs an

OpenType

instance (actually a subclass instance as

OpenType

is abstract),
checking for the validity of the given parameters.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract boolean

equals

​(

Object

obj)

Compares the specified

obj

parameter with this
open type instance for equality.

String

getClassName

()

Returns the fully qualified Java class name of the open data values
this open type describes.

String

getDescription

()

Returns the text description of this

OpenType

instance.

String

getTypeName

()

Returns the name of this

OpenType

instance.

boolean

isArray

()

Returns

true

if the open data values this open
type describes are arrays,

false

otherwise.

abstract boolean

isValue

​(

Object

obj)

Tests whether

obj

is a value for this open type.

abstract

String

toString

()

Returns a string representation of this open type instance.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

hashCode

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
open type instance for equality.

Returns the fully qualified Java class name of the open data values
this open type describes.

Returns the text description of this

OpenType

instance.

Returns the name of this

OpenType

instance.

Returns

true

if the open data values this open
type describes are arrays,

false

otherwise.

Tests whether

obj

is a value for this open type.

Returns a string representation of this open type instance.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

hashCode

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

- ALLOWED_CLASSNAMES_LIST

```java
public static final
List
<
String
> ALLOWED_CLASSNAMES_LIST
```

List of the fully qualified names of the Java classes allowed for open
data values. A multidimensional array of any one of these classes or
their corresponding primitive types is also an allowed class for open
data values.

```java
ALLOWED_CLASSNAMES_LIST = {
"java.lang.Void",
"java.lang.Boolean",
"java.lang.Character",
"java.lang.Byte",
"java.lang.Short",
"java.lang.Integer",
"java.lang.Long",
"java.lang.Float",
"java.lang.Double",
"java.lang.String",
"java.math.BigDecimal",
"java.math.BigInteger",
"java.util.Date",
"javax.management.ObjectName",
CompositeData.class.getName(),
TabularData.class.getName() } ;
```

- ALLOWED_CLASSNAMES

```java
@Deprecated

public static final
String
[] ALLOWED_CLASSNAMES
```

Deprecated.

Use

ALLOWED_CLASSNAMES_LIST

instead.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- OpenType

```java
protected OpenType​(
String
className,

String
typeName,

String
description)
throws
OpenDataException
```

Constructs an

OpenType

instance (actually a subclass instance as

OpenType

is abstract),
checking for the validity of the given parameters.
The validity constraints are described below for each parameter.

**Parameters:** className

- The fully qualified Java class name of the open data values this open type describes.
The valid Java class names allowed for open data values are listed in

ALLOWED_CLASSNAMES_LIST

.
A multidimensional array of any one of these classes
or their corresponding primitive types is also an allowed class,
in which case the class name follows the rules defined by the method

getName()

of

java.lang.Class

.
For example, a 3-dimensional array of Strings has for class name
"

[[[Ljava.lang.String;

" (without the quotes).
**Parameters:** typeName

- The name given to the open type this instance represents; cannot be a null or empty string.
**Parameters:** description

- The human readable description of the open type this instance represents;
cannot be a null or empty string.
**Throws:** IllegalArgumentException

- if

className

,

typeName

or

description

is a null or empty string
**Throws:** OpenDataException

- if

className

is not one of the allowed Java class names for open data

============ METHOD DETAIL ==========

- Method Detail

- getClassName

```java
public
String
getClassName()
```

Returns the fully qualified Java class name of the open data values
this open type describes.
The only possible Java class names for open data values are listed in

ALLOWED_CLASSNAMES_LIST

.
A multidimensional array of any one of these classes or their
corresponding primitive types is also an allowed class,
in which case the class name follows the rules defined by the method

getName()

of

java.lang.Class

.
For example, a 3-dimensional array of Strings has for class name
"

[[[Ljava.lang.String;

" (without the quotes),
a 3-dimensional array of Integers has for class name
"

[[[Ljava.lang.Integer;

" (without the quotes),
and a 3-dimensional array of int has for class name
"

[[[I

" (without the quotes)

**Returns:** the class name.

- getTypeName

```java
public
String
getTypeName()
```

Returns the name of this

OpenType

instance.

**Returns:** the type name.

- getDescription

```java
public
String
getDescription()
```

Returns the text description of this

OpenType

instance.

**Returns:** the description.

- isArray

```java
public boolean isArray()
```

Returns

true

if the open data values this open
type describes are arrays,

false

otherwise.

**Returns:** true if this is an array type.

- isValue

```java
public abstract boolean isValue​(
Object
obj)
```

Tests whether

obj

is a value for this open type.

**Parameters:** obj

- the object to be tested for validity.
**Returns:** true

if

obj

is a value for this
open type,

false

otherwise.

- equals

```java
public abstract boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this
open type instance for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare to.
**Returns:** true if this object and

obj

are equal.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public abstract
String
toString()
```

Returns a string representation of this open type instance.

**Overrides:** toString

in class

Object
**Returns:** the string representation.

Field Detail

- ALLOWED_CLASSNAMES_LIST

```java
public static final
List
<
String
> ALLOWED_CLASSNAMES_LIST
```

List of the fully qualified names of the Java classes allowed for open
data values. A multidimensional array of any one of these classes or
their corresponding primitive types is also an allowed class for open
data values.

```java
ALLOWED_CLASSNAMES_LIST = {
"java.lang.Void",
"java.lang.Boolean",
"java.lang.Character",
"java.lang.Byte",
"java.lang.Short",
"java.lang.Integer",
"java.lang.Long",
"java.lang.Float",
"java.lang.Double",
"java.lang.String",
"java.math.BigDecimal",
"java.math.BigInteger",
"java.util.Date",
"javax.management.ObjectName",
CompositeData.class.getName(),
TabularData.class.getName() } ;
```

- ALLOWED_CLASSNAMES

```java
@Deprecated

public static final
String
[] ALLOWED_CLASSNAMES
```

Deprecated.

Use

ALLOWED_CLASSNAMES_LIST

instead.

---

#### Field Detail

ALLOWED_CLASSNAMES_LIST

```java
public static final
List
<
String
> ALLOWED_CLASSNAMES_LIST
```

List of the fully qualified names of the Java classes allowed for open
data values. A multidimensional array of any one of these classes or
their corresponding primitive types is also an allowed class for open
data values.

```java
ALLOWED_CLASSNAMES_LIST = {
"java.lang.Void",
"java.lang.Boolean",
"java.lang.Character",
"java.lang.Byte",
"java.lang.Short",
"java.lang.Integer",
"java.lang.Long",
"java.lang.Float",
"java.lang.Double",
"java.lang.String",
"java.math.BigDecimal",
"java.math.BigInteger",
"java.util.Date",
"javax.management.ObjectName",
CompositeData.class.getName(),
TabularData.class.getName() } ;
```

---

#### ALLOWED_CLASSNAMES_LIST

public static final

List

<

String

> ALLOWED_CLASSNAMES_LIST

List of the fully qualified names of the Java classes allowed for open
data values. A multidimensional array of any one of these classes or
their corresponding primitive types is also an allowed class for open
data values.

```java
ALLOWED_CLASSNAMES_LIST = {
"java.lang.Void",
"java.lang.Boolean",
"java.lang.Character",
"java.lang.Byte",
"java.lang.Short",
"java.lang.Integer",
"java.lang.Long",
"java.lang.Float",
"java.lang.Double",
"java.lang.String",
"java.math.BigDecimal",
"java.math.BigInteger",
"java.util.Date",
"javax.management.ObjectName",
CompositeData.class.getName(),
TabularData.class.getName() } ;
```

ALLOWED_CLASSNAMES_LIST = {
"java.lang.Void",
"java.lang.Boolean",
"java.lang.Character",
"java.lang.Byte",
"java.lang.Short",
"java.lang.Integer",
"java.lang.Long",
"java.lang.Float",
"java.lang.Double",
"java.lang.String",
"java.math.BigDecimal",
"java.math.BigInteger",
"java.util.Date",
"javax.management.ObjectName",
CompositeData.class.getName(),
TabularData.class.getName() } ;

ALLOWED_CLASSNAMES

```java
@Deprecated

public static final
String
[] ALLOWED_CLASSNAMES
```

Deprecated.

Use

ALLOWED_CLASSNAMES_LIST

instead.

---

#### ALLOWED_CLASSNAMES

@Deprecated

public static final

String

[] ALLOWED_CLASSNAMES

Constructor Detail

- OpenType

```java
protected OpenType​(
String
className,

String
typeName,

String
description)
throws
OpenDataException
```

Constructs an

OpenType

instance (actually a subclass instance as

OpenType

is abstract),
checking for the validity of the given parameters.
The validity constraints are described below for each parameter.

**Parameters:** className

- The fully qualified Java class name of the open data values this open type describes.
The valid Java class names allowed for open data values are listed in

ALLOWED_CLASSNAMES_LIST

.
A multidimensional array of any one of these classes
or their corresponding primitive types is also an allowed class,
in which case the class name follows the rules defined by the method

getName()

of

java.lang.Class

.
For example, a 3-dimensional array of Strings has for class name
"

[[[Ljava.lang.String;

" (without the quotes).
**Parameters:** typeName

- The name given to the open type this instance represents; cannot be a null or empty string.
**Parameters:** description

- The human readable description of the open type this instance represents;
cannot be a null or empty string.
**Throws:** IllegalArgumentException

- if

className

,

typeName

or

description

is a null or empty string
**Throws:** OpenDataException

- if

className

is not one of the allowed Java class names for open data

---

#### Constructor Detail

OpenType

```java
protected OpenType​(
String
className,

String
typeName,

String
description)
throws
OpenDataException
```

Constructs an

OpenType

instance (actually a subclass instance as

OpenType

is abstract),
checking for the validity of the given parameters.
The validity constraints are described below for each parameter.

**Parameters:** className

- The fully qualified Java class name of the open data values this open type describes.
The valid Java class names allowed for open data values are listed in

ALLOWED_CLASSNAMES_LIST

.
A multidimensional array of any one of these classes
or their corresponding primitive types is also an allowed class,
in which case the class name follows the rules defined by the method

getName()

of

java.lang.Class

.
For example, a 3-dimensional array of Strings has for class name
"

[[[Ljava.lang.String;

" (without the quotes).
**Parameters:** typeName

- The name given to the open type this instance represents; cannot be a null or empty string.
**Parameters:** description

- The human readable description of the open type this instance represents;
cannot be a null or empty string.
**Throws:** IllegalArgumentException

- if

className

,

typeName

or

description

is a null or empty string
**Throws:** OpenDataException

- if

className

is not one of the allowed Java class names for open data

---

#### OpenType

protected OpenType​(

String

className,

String

typeName,

String

description)
throws

OpenDataException

Constructs an

OpenType

instance (actually a subclass instance as

OpenType

is abstract),
checking for the validity of the given parameters.
The validity constraints are described below for each parameter.

Method Detail

- getClassName

```java
public
String
getClassName()
```

Returns the fully qualified Java class name of the open data values
this open type describes.
The only possible Java class names for open data values are listed in

ALLOWED_CLASSNAMES_LIST

.
A multidimensional array of any one of these classes or their
corresponding primitive types is also an allowed class,
in which case the class name follows the rules defined by the method

getName()

of

java.lang.Class

.
For example, a 3-dimensional array of Strings has for class name
"

[[[Ljava.lang.String;

" (without the quotes),
a 3-dimensional array of Integers has for class name
"

[[[Ljava.lang.Integer;

" (without the quotes),
and a 3-dimensional array of int has for class name
"

[[[I

" (without the quotes)

**Returns:** the class name.

- getTypeName

```java
public
String
getTypeName()
```

Returns the name of this

OpenType

instance.

**Returns:** the type name.

- getDescription

```java
public
String
getDescription()
```

Returns the text description of this

OpenType

instance.

**Returns:** the description.

- isArray

```java
public boolean isArray()
```

Returns

true

if the open data values this open
type describes are arrays,

false

otherwise.

**Returns:** true if this is an array type.

- isValue

```java
public abstract boolean isValue​(
Object
obj)
```

Tests whether

obj

is a value for this open type.

**Parameters:** obj

- the object to be tested for validity.
**Returns:** true

if

obj

is a value for this
open type,

false

otherwise.

- equals

```java
public abstract boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this
open type instance for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare to.
**Returns:** true if this object and

obj

are equal.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public abstract
String
toString()
```

Returns a string representation of this open type instance.

**Overrides:** toString

in class

Object
**Returns:** the string representation.

---

#### Method Detail

getClassName

```java
public
String
getClassName()
```

Returns the fully qualified Java class name of the open data values
this open type describes.
The only possible Java class names for open data values are listed in

ALLOWED_CLASSNAMES_LIST

.
A multidimensional array of any one of these classes or their
corresponding primitive types is also an allowed class,
in which case the class name follows the rules defined by the method

getName()

of

java.lang.Class

.
For example, a 3-dimensional array of Strings has for class name
"

[[[Ljava.lang.String;

" (without the quotes),
a 3-dimensional array of Integers has for class name
"

[[[Ljava.lang.Integer;

" (without the quotes),
and a 3-dimensional array of int has for class name
"

[[[I

" (without the quotes)

**Returns:** the class name.

---

#### getClassName

public

String

getClassName()

Returns the fully qualified Java class name of the open data values
this open type describes.
The only possible Java class names for open data values are listed in

ALLOWED_CLASSNAMES_LIST

.
A multidimensional array of any one of these classes or their
corresponding primitive types is also an allowed class,
in which case the class name follows the rules defined by the method

getName()

of

java.lang.Class

.
For example, a 3-dimensional array of Strings has for class name
"

[[[Ljava.lang.String;

" (without the quotes),
a 3-dimensional array of Integers has for class name
"

[[[Ljava.lang.Integer;

" (without the quotes),
and a 3-dimensional array of int has for class name
"

[[[I

" (without the quotes)

getTypeName

```java
public
String
getTypeName()
```

Returns the name of this

OpenType

instance.

**Returns:** the type name.

---

#### getTypeName

public

String

getTypeName()

Returns the name of this

OpenType

instance.

getDescription

```java
public
String
getDescription()
```

Returns the text description of this

OpenType

instance.

**Returns:** the description.

---

#### getDescription

public

String

getDescription()

Returns the text description of this

OpenType

instance.

isArray

```java
public boolean isArray()
```

Returns

true

if the open data values this open
type describes are arrays,

false

otherwise.

**Returns:** true if this is an array type.

---

#### isArray

public boolean isArray()

Returns

true

if the open data values this open
type describes are arrays,

false

otherwise.

isValue

```java
public abstract boolean isValue​(
Object
obj)
```

Tests whether

obj

is a value for this open type.

**Parameters:** obj

- the object to be tested for validity.
**Returns:** true

if

obj

is a value for this
open type,

false

otherwise.

---

#### isValue

public abstract boolean isValue​(

Object

obj)

Tests whether

obj

is a value for this open type.

equals

```java
public abstract boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this
open type instance for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare to.
**Returns:** true if this object and

obj

are equal.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public abstract boolean equals​(

Object

obj)

Compares the specified

obj

parameter with this
open type instance for equality.

toString

```java
public abstract
String
toString()
```

Returns a string representation of this open type instance.

**Overrides:** toString

in class

Object
**Returns:** the string representation.

---

#### toString

public abstract

String

toString()

Returns a string representation of this open type instance.

---

