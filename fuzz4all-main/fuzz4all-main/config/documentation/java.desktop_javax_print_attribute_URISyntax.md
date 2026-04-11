# Class URISyntax

**Source:** `java.desktop\javax\print\attribute\URISyntax.html`

### Class Description

```java
public abstract class
URISyntax

extends
Object

implements
Serializable
,
Cloneable
```

Class

URISyntax

is an abstract base class providing the common
implementation of all attributes whose value is a Uniform Resource Identifier
(URI). Once constructed, a

URI

attribute's value is immutable.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected URISyntax​(
URI
uri)

Constructs a

URI

attribute with the specified

URI

.

**Parameters:**
- uri

- the

URI

**Throws:**
- NullPointerException

- if

uri

is

null

---

### Method Details

#### public
URI
getURI()

Returns this

URI

attribute's

URI

value.

**Returns:**
- the

URI

---

#### public int hashCode()

Returns a hashcode for this

URI

attribute.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hashcode value for this object

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
object)

Returns whether this

URI

attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

URISyntax

.

This

URI

attribute's underlying

URI

and

object

's underlying

URI

are equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- object

-

Object

to compare to

**Returns:**
- true

if

object

is equivalent to this

URI

attribute,

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
toString()

Returns a

String

identifying this

URI

attribute. The

String

is the string representation of the attribute's underlying

URI

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a

String

identifying this object

---

### Additional Sections

#### Class URISyntax

java.lang.Object

- javax.print.attribute.URISyntax

javax.print.attribute.URISyntax

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** Destination

,

PrinterMoreInfo

,

PrinterMoreInfoManufacturer

,

PrinterURI

```java
public abstract class
URISyntax

extends
Object

implements
Serializable
,
Cloneable
```

Class

URISyntax

is an abstract base class providing the common
implementation of all attributes whose value is a Uniform Resource Identifier
(URI). Once constructed, a

URI

attribute's value is immutable.

**See Also:** Serialized Form

public abstract class

URISyntax

extends

Object

implements

Serializable

,

Cloneable

Class

URISyntax

is an abstract base class providing the common
implementation of all attributes whose value is a Uniform Resource Identifier
(URI). Once constructed, a

URI

attribute's value is immutable.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

URISyntax

​(

URI

uri)

Constructs a

URI

attribute with the specified

URI

.

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

object)

Returns whether this

URI

attribute is equivalent to the passed in
object.

URI

getURI

()

Returns this

URI

attribute's

URI

value.

int

hashCode

()

Returns a hashcode for this

URI

attribute.

String

toString

()

Returns a

String

identifying this

URI

attribute.

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

URISyntax

​(

URI

uri)

Constructs a

URI

attribute with the specified

URI

.

---

#### Constructor Summary

Constructs a

URI

attribute with the specified

URI

.

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

object)

Returns whether this

URI

attribute is equivalent to the passed in
object.

URI

getURI

()

Returns this

URI

attribute's

URI

value.

int

hashCode

()

Returns a hashcode for this

URI

attribute.

String

toString

()

Returns a

String

identifying this

URI

attribute.

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

Returns whether this

URI

attribute is equivalent to the passed in
object.

Returns this

URI

attribute's

URI

value.

Returns a hashcode for this

URI

attribute.

Returns a

String

identifying this

URI

attribute.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- URISyntax

```java
protected URISyntax​(
URI
uri)
```

Constructs a

URI

attribute with the specified

URI

.

**Parameters:** uri

- the

URI
**Throws:** NullPointerException

- if

uri

is

null

============ METHOD DETAIL ==========

- Method Detail

- getURI

```java
public
URI
getURI()
```

Returns this

URI

attribute's

URI

value.

**Returns:** the

URI

- hashCode

```java
public int hashCode()
```

Returns a hashcode for this

URI

attribute.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode value for this object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this

URI

attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

URISyntax

.

This

URI

attribute's underlying

URI

and

object

's underlying

URI

are equal.

**Overrides:** equals

in class

Object
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this

URI

attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a

String

identifying this

URI

attribute. The

String

is the string representation of the attribute's underlying

URI

.

**Overrides:** toString

in class

Object
**Returns:** a

String

identifying this object

Constructor Detail

- URISyntax

```java
protected URISyntax​(
URI
uri)
```

Constructs a

URI

attribute with the specified

URI

.

**Parameters:** uri

- the

URI
**Throws:** NullPointerException

- if

uri

is

null

---

#### Constructor Detail

URISyntax

```java
protected URISyntax​(
URI
uri)
```

Constructs a

URI

attribute with the specified

URI

.

**Parameters:** uri

- the

URI
**Throws:** NullPointerException

- if

uri

is

null

---

#### URISyntax

protected URISyntax​(

URI

uri)

Constructs a

URI

attribute with the specified

URI

.

Method Detail

- getURI

```java
public
URI
getURI()
```

Returns this

URI

attribute's

URI

value.

**Returns:** the

URI

- hashCode

```java
public int hashCode()
```

Returns a hashcode for this

URI

attribute.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode value for this object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this

URI

attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

URISyntax

.

This

URI

attribute's underlying

URI

and

object

's underlying

URI

are equal.

**Overrides:** equals

in class

Object
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this

URI

attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a

String

identifying this

URI

attribute. The

String

is the string representation of the attribute's underlying

URI

.

**Overrides:** toString

in class

Object
**Returns:** a

String

identifying this object

---

#### Method Detail

getURI

```java
public
URI
getURI()
```

Returns this

URI

attribute's

URI

value.

**Returns:** the

URI

---

#### getURI

public

URI

getURI()

Returns this

URI

attribute's

URI

value.

hashCode

```java
public int hashCode()
```

Returns a hashcode for this

URI

attribute.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode value for this object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hashcode for this

URI

attribute.

equals

```java
public boolean equals​(
Object
object)
```

Returns whether this

URI

attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

URISyntax

.

This

URI

attribute's underlying

URI

and

object

's underlying

URI

are equal.

**Overrides:** equals

in class

Object
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this

URI

attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

object)

Returns whether this

URI

attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

URISyntax

.

This

URI

attribute's underlying

URI

and

object

's underlying

URI

are equal.

object

is not

null

.

object

is an instance of class

URISyntax

.

This

URI

attribute's underlying

URI

and

object

's underlying

URI

are equal.

toString

```java
public
String
toString()
```

Returns a

String

identifying this

URI

attribute. The

String

is the string representation of the attribute's underlying

URI

.

**Overrides:** toString

in class

Object
**Returns:** a

String

identifying this object

---

#### toString

public

String

toString()

Returns a

String

identifying this

URI

attribute. The

String

is the string representation of the attribute's underlying

URI

.

---

