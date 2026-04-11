# Class SctpStandardSocketOptions.InitMaxStreams

**Source:** `jdk.sctp\com\sun\nio\sctp\SctpStandardSocketOptions.InitMaxStreams.html`

### Class Description

```java
public static class
SctpStandardSocketOptions.InitMaxStreams

extends
Object
```

This class is used to set the maximum number of inbound/outbound streams
used by the local endpoint during association initialization. An
instance of this class is used to set the

SCTP_INIT_MAXSTREAMS

socket option.

**Enclosing class:** SctpStandardSocketOptions

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
SctpStandardSocketOptions.InitMaxStreams
create​(int maxInStreams,
int maxOutStreams)

Creates an InitMaxStreams instance.

**Parameters:**
- maxInStreams

- The maximum number of inbound streams, where

0 <= maxInStreams <= 65536
- maxOutStreams

- The maximum number of outbound streams, where

0 <= maxOutStreams <= 65536

**Returns:**
- An

InitMaxStreams

instance

**Throws:**
- IllegalArgumentException

- If an argument is outside of specified bounds

---

#### public int maxInStreams()

Returns the maximum number of inbound streams.

**Returns:**
- Maximum inbound streams

---

#### public int maxOutStreams()

Returns the maximum number of outbound streams.

**Returns:**
- Maximum outbound streams

---

#### public
String
toString()

Returns a string representation of this init max streams, including
the maximum in and out bound streams.

**Overrides:**
- toString

in class

Object

**Returns:**
- A string representation of this init max streams

---

#### public boolean equals​(
Object
obj)

Returns true if the specified object is another

InitMaxStreams

instance with the same number of in and out bound streams.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- The object to be compared with this init max streams

**Returns:**
- true if the specified object is another

InitMaxStreams

instance with the same number of in
and out bound streams

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this init max streams.

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

### Additional Sections

#### Class SctpStandardSocketOptions.InitMaxStreams

java.lang.Object

- com.sun.nio.sctp.SctpStandardSocketOptions.InitMaxStreams

com.sun.nio.sctp.SctpStandardSocketOptions.InitMaxStreams

**Enclosing class:** SctpStandardSocketOptions

```java
public static class
SctpStandardSocketOptions.InitMaxStreams

extends
Object
```

This class is used to set the maximum number of inbound/outbound streams
used by the local endpoint during association initialization. An
instance of this class is used to set the

SCTP_INIT_MAXSTREAMS

socket option.

**Since:** 1.7

public static class

SctpStandardSocketOptions.InitMaxStreams

extends

Object

This class is used to set the maximum number of inbound/outbound streams
used by the local endpoint during association initialization. An
instance of this class is used to set the

SCTP_INIT_MAXSTREAMS

socket option.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

SctpStandardSocketOptions.InitMaxStreams

create

​(int maxInStreams,
int maxOutStreams)

Creates an InitMaxStreams instance.

boolean

equals

​(

Object

obj)

Returns true if the specified object is another

InitMaxStreams

instance with the same number of in and out bound streams.

int

hashCode

()

Returns a hash code value for this init max streams.

int

maxInStreams

()

Returns the maximum number of inbound streams.

int

maxOutStreams

()

Returns the maximum number of outbound streams.

String

toString

()

Returns a string representation of this init max streams, including
the maximum in and out bound streams.

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

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

SctpStandardSocketOptions.InitMaxStreams

create

​(int maxInStreams,
int maxOutStreams)

Creates an InitMaxStreams instance.

boolean

equals

​(

Object

obj)

Returns true if the specified object is another

InitMaxStreams

instance with the same number of in and out bound streams.

int

hashCode

()

Returns a hash code value for this init max streams.

int

maxInStreams

()

Returns the maximum number of inbound streams.

int

maxOutStreams

()

Returns the maximum number of outbound streams.

String

toString

()

Returns a string representation of this init max streams, including
the maximum in and out bound streams.

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

Creates an InitMaxStreams instance.

Returns true if the specified object is another

InitMaxStreams

instance with the same number of in and out bound streams.

Returns a hash code value for this init max streams.

Returns the maximum number of inbound streams.

Returns the maximum number of outbound streams.

Returns a string representation of this init max streams, including
the maximum in and out bound streams.

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

============ METHOD DETAIL ==========

- Method Detail

- create

```java
public static
SctpStandardSocketOptions.InitMaxStreams
create​(int maxInStreams,
int maxOutStreams)
```

Creates an InitMaxStreams instance.

**Parameters:** maxInStreams

- The maximum number of inbound streams, where

0 <= maxInStreams <= 65536
**Parameters:** maxOutStreams

- The maximum number of outbound streams, where

0 <= maxOutStreams <= 65536
**Returns:** An

InitMaxStreams

instance
**Throws:** IllegalArgumentException

- If an argument is outside of specified bounds

- maxInStreams

```java
public int maxInStreams()
```

Returns the maximum number of inbound streams.

**Returns:** Maximum inbound streams

- maxOutStreams

```java
public int maxOutStreams()
```

Returns the maximum number of outbound streams.

**Returns:** Maximum outbound streams

- toString

```java
public
String
toString()
```

Returns a string representation of this init max streams, including
the maximum in and out bound streams.

**Overrides:** toString

in class

Object
**Returns:** A string representation of this init max streams

- equals

```java
public boolean equals​(
Object
obj)
```

Returns true if the specified object is another

InitMaxStreams

instance with the same number of in and out bound streams.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to be compared with this init max streams
**Returns:** true if the specified object is another

InitMaxStreams

instance with the same number of in
and out bound streams
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this init max streams.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Method Detail

- create

```java
public static
SctpStandardSocketOptions.InitMaxStreams
create​(int maxInStreams,
int maxOutStreams)
```

Creates an InitMaxStreams instance.

**Parameters:** maxInStreams

- The maximum number of inbound streams, where

0 <= maxInStreams <= 65536
**Parameters:** maxOutStreams

- The maximum number of outbound streams, where

0 <= maxOutStreams <= 65536
**Returns:** An

InitMaxStreams

instance
**Throws:** IllegalArgumentException

- If an argument is outside of specified bounds

- maxInStreams

```java
public int maxInStreams()
```

Returns the maximum number of inbound streams.

**Returns:** Maximum inbound streams

- maxOutStreams

```java
public int maxOutStreams()
```

Returns the maximum number of outbound streams.

**Returns:** Maximum outbound streams

- toString

```java
public
String
toString()
```

Returns a string representation of this init max streams, including
the maximum in and out bound streams.

**Overrides:** toString

in class

Object
**Returns:** A string representation of this init max streams

- equals

```java
public boolean equals​(
Object
obj)
```

Returns true if the specified object is another

InitMaxStreams

instance with the same number of in and out bound streams.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to be compared with this init max streams
**Returns:** true if the specified object is another

InitMaxStreams

instance with the same number of in
and out bound streams
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this init max streams.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

create

```java
public static
SctpStandardSocketOptions.InitMaxStreams
create​(int maxInStreams,
int maxOutStreams)
```

Creates an InitMaxStreams instance.

**Parameters:** maxInStreams

- The maximum number of inbound streams, where

0 <= maxInStreams <= 65536
**Parameters:** maxOutStreams

- The maximum number of outbound streams, where

0 <= maxOutStreams <= 65536
**Returns:** An

InitMaxStreams

instance
**Throws:** IllegalArgumentException

- If an argument is outside of specified bounds

---

#### create

public static

SctpStandardSocketOptions.InitMaxStreams

create​(int maxInStreams,
int maxOutStreams)

Creates an InitMaxStreams instance.

maxInStreams

```java
public int maxInStreams()
```

Returns the maximum number of inbound streams.

**Returns:** Maximum inbound streams

---

#### maxInStreams

public int maxInStreams()

Returns the maximum number of inbound streams.

maxOutStreams

```java
public int maxOutStreams()
```

Returns the maximum number of outbound streams.

**Returns:** Maximum outbound streams

---

#### maxOutStreams

public int maxOutStreams()

Returns the maximum number of outbound streams.

toString

```java
public
String
toString()
```

Returns a string representation of this init max streams, including
the maximum in and out bound streams.

**Overrides:** toString

in class

Object
**Returns:** A string representation of this init max streams

---

#### toString

public

String

toString()

Returns a string representation of this init max streams, including
the maximum in and out bound streams.

equals

```java
public boolean equals​(
Object
obj)
```

Returns true if the specified object is another

InitMaxStreams

instance with the same number of in and out bound streams.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to be compared with this init max streams
**Returns:** true if the specified object is another

InitMaxStreams

instance with the same number of in
and out bound streams
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Returns true if the specified object is another

InitMaxStreams

instance with the same number of in and out bound streams.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this init max streams.

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

Returns a hash code value for this init max streams.

---

