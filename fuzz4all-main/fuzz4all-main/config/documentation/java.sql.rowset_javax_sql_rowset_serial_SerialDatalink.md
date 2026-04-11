# Class SerialDatalink

**Source:** `java.sql.rowset\javax\sql\rowset\serial\SerialDatalink.html`

### Class Description

```java
public class
SerialDatalink

extends
Object

implements
Serializable
,
Cloneable
```

A serialized mapping in the Java programming language of an SQL

DATALINK

value. A

DATALINK

value
references a file outside of the underlying data source that the
data source manages.

RowSet

implementations can use the method

RowSet.getURL

to retrieve a

java.net.URL

object, which can be used
to manipulate the external data.

```java
java.net.URL url = rowset.getURL(1);
```

Thread safety

A SerialDatalink is not safe for use by multiple concurrent threads. If a
SerialDatalink is to be used by more than one thread then access to the
SerialDatalink should be controlled by appropriate synchronization.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SerialDatalink​(
URL
url)
throws
SerialException

Constructs a new

SerialDatalink

object from the given

java.net.URL

object.

**Parameters:**
- url

- the

URL

to create the

SerialDataLink

from

**Throws:**
- SerialException

- if url parameter is a null

---

### Method Details

#### public
URL
getDatalink()
throws
SerialException

Returns a new URL that is a copy of this

SerialDatalink

object.

**Returns:**
- a copy of this

SerialDatalink

object as a

URL

object in the Java programming language.

**Throws:**
- SerialException

- if the

URL

object cannot be de-serialized

---

#### public boolean equals​(
Object
obj)

Compares this

SerialDatalink

to the specified object.
The result is

true

if and only if the argument is not

null

and is a

SerialDatalink

object whose URL is
identical to this object's URL

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- The object to compare this

SerialDatalink

against

**Returns:**
- true

if the given object represents a

SerialDatalink

equivalent to this SerialDatalink,

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code for this

SerialDatalink

. The hash code for a

SerialDatalink

object is taken as the hash code of
the

URL

it stores

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
Object
clone()

Returns a clone of this

SerialDatalink

.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this SerialDatalink

**See Also:**
- Cloneable

---

### Additional Sections

#### Class SerialDatalink

java.lang.Object

- javax.sql.rowset.serial.SerialDatalink

javax.sql.rowset.serial.SerialDatalink

**All Implemented Interfaces:** Serializable

,

Cloneable

```java
public class
SerialDatalink

extends
Object

implements
Serializable
,
Cloneable
```

A serialized mapping in the Java programming language of an SQL

DATALINK

value. A

DATALINK

value
references a file outside of the underlying data source that the
data source manages.

RowSet

implementations can use the method

RowSet.getURL

to retrieve a

java.net.URL

object, which can be used
to manipulate the external data.

```java
java.net.URL url = rowset.getURL(1);
```

Thread safety

A SerialDatalink is not safe for use by multiple concurrent threads. If a
SerialDatalink is to be used by more than one thread then access to the
SerialDatalink should be controlled by appropriate synchronization.

**Since:** 1.5
**See Also:** Serialized Form

public class

SerialDatalink

extends

Object

implements

Serializable

,

Cloneable

A serialized mapping in the Java programming language of an SQL

DATALINK

value. A

DATALINK

value
references a file outside of the underlying data source that the
data source manages.

RowSet

implementations can use the method

RowSet.getURL

to retrieve a

java.net.URL

object, which can be used
to manipulate the external data.

```java
java.net.URL url = rowset.getURL(1);
```

Thread safety

A SerialDatalink is not safe for use by multiple concurrent threads. If a
SerialDatalink is to be used by more than one thread then access to the
SerialDatalink should be controlled by appropriate synchronization.

RowSet

implementations can use the method

RowSet.getURL

to retrieve a

java.net.URL

object, which can be used
to manipulate the external data.

```java
java.net.URL url = rowset.getURL(1);
```

Thread safety

A SerialDatalink is not safe for use by multiple concurrent threads. If a
SerialDatalink is to be used by more than one thread then access to the
SerialDatalink should be controlled by appropriate synchronization.

java.net.URL url = rowset.getURL(1);

---

#### Thread safety

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SerialDatalink

​(

URL

url)

Constructs a new

SerialDatalink

object from the given

java.net.URL

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone of this

SerialDatalink

.

boolean

equals

​(

Object

obj)

Compares this

SerialDatalink

to the specified object.

URL

getDatalink

()

Returns a new URL that is a copy of this

SerialDatalink

object.

int

hashCode

()

Returns a hash code for this

SerialDatalink

.

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

SerialDatalink

​(

URL

url)

Constructs a new

SerialDatalink

object from the given

java.net.URL

object.

---

#### Constructor Summary

Constructs a new

SerialDatalink

object from the given

java.net.URL

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone of this

SerialDatalink

.

boolean

equals

​(

Object

obj)

Compares this

SerialDatalink

to the specified object.

URL

getDatalink

()

Returns a new URL that is a copy of this

SerialDatalink

object.

int

hashCode

()

Returns a hash code for this

SerialDatalink

.

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns a clone of this

SerialDatalink

.

Compares this

SerialDatalink

to the specified object.

Returns a new URL that is a copy of this

SerialDatalink

object.

Returns a hash code for this

SerialDatalink

.

Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

toString

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

- SerialDatalink

```java
public SerialDatalink​(
URL
url)
throws
SerialException
```

Constructs a new

SerialDatalink

object from the given

java.net.URL

object.

**Parameters:** url

- the

URL

to create the

SerialDataLink

from
**Throws:** SerialException

- if url parameter is a null

============ METHOD DETAIL ==========

- Method Detail

- getDatalink

```java
public
URL
getDatalink()
throws
SerialException
```

Returns a new URL that is a copy of this

SerialDatalink

object.

**Returns:** a copy of this

SerialDatalink

object as a

URL

object in the Java programming language.
**Throws:** SerialException

- if the

URL

object cannot be de-serialized

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this

SerialDatalink

to the specified object.
The result is

true

if and only if the argument is not

null

and is a

SerialDatalink

object whose URL is
identical to this object's URL

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to compare this

SerialDatalink

against
**Returns:** true

if the given object represents a

SerialDatalink

equivalent to this SerialDatalink,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

SerialDatalink

. The hash code for a

SerialDatalink

object is taken as the hash code of
the

URL

it stores

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Returns a clone of this

SerialDatalink

.

**Overrides:** clone

in class

Object
**Returns:** a clone of this SerialDatalink
**See Also:** Cloneable

Constructor Detail

- SerialDatalink

```java
public SerialDatalink​(
URL
url)
throws
SerialException
```

Constructs a new

SerialDatalink

object from the given

java.net.URL

object.

**Parameters:** url

- the

URL

to create the

SerialDataLink

from
**Throws:** SerialException

- if url parameter is a null

---

#### Constructor Detail

SerialDatalink

```java
public SerialDatalink​(
URL
url)
throws
SerialException
```

Constructs a new

SerialDatalink

object from the given

java.net.URL

object.

**Parameters:** url

- the

URL

to create the

SerialDataLink

from
**Throws:** SerialException

- if url parameter is a null

---

#### SerialDatalink

public SerialDatalink​(

URL

url)
throws

SerialException

Constructs a new

SerialDatalink

object from the given

java.net.URL

object.

Method Detail

- getDatalink

```java
public
URL
getDatalink()
throws
SerialException
```

Returns a new URL that is a copy of this

SerialDatalink

object.

**Returns:** a copy of this

SerialDatalink

object as a

URL

object in the Java programming language.
**Throws:** SerialException

- if the

URL

object cannot be de-serialized

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this

SerialDatalink

to the specified object.
The result is

true

if and only if the argument is not

null

and is a

SerialDatalink

object whose URL is
identical to this object's URL

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to compare this

SerialDatalink

against
**Returns:** true

if the given object represents a

SerialDatalink

equivalent to this SerialDatalink,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

SerialDatalink

. The hash code for a

SerialDatalink

object is taken as the hash code of
the

URL

it stores

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Returns a clone of this

SerialDatalink

.

**Overrides:** clone

in class

Object
**Returns:** a clone of this SerialDatalink
**See Also:** Cloneable

---

#### Method Detail

getDatalink

```java
public
URL
getDatalink()
throws
SerialException
```

Returns a new URL that is a copy of this

SerialDatalink

object.

**Returns:** a copy of this

SerialDatalink

object as a

URL

object in the Java programming language.
**Throws:** SerialException

- if the

URL

object cannot be de-serialized

---

#### getDatalink

public

URL

getDatalink()
throws

SerialException

Returns a new URL that is a copy of this

SerialDatalink

object.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this

SerialDatalink

to the specified object.
The result is

true

if and only if the argument is not

null

and is a

SerialDatalink

object whose URL is
identical to this object's URL

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to compare this

SerialDatalink

against
**Returns:** true

if the given object represents a

SerialDatalink

equivalent to this SerialDatalink,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares this

SerialDatalink

to the specified object.
The result is

true

if and only if the argument is not

null

and is a

SerialDatalink

object whose URL is
identical to this object's URL

hashCode

```java
public int hashCode()
```

Returns a hash code for this

SerialDatalink

. The hash code for a

SerialDatalink

object is taken as the hash code of
the

URL

it stores

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code for this

SerialDatalink

. The hash code for a

SerialDatalink

object is taken as the hash code of
the

URL

it stores

clone

```java
public
Object
clone()
```

Returns a clone of this

SerialDatalink

.

**Overrides:** clone

in class

Object
**Returns:** a clone of this SerialDatalink
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a clone of this

SerialDatalink

.

---

