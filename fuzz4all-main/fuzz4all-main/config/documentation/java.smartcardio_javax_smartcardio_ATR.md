# Class ATR

**Source:** `java.smartcardio\javax\smartcardio\ATR.html`

### Class Description

```java
public final class
ATR

extends
Object

implements
Serializable
```

A Smart Card's answer-to-reset bytes. A Card's ATR object can be obtained
by calling

Card.getATR()

.
This class does not attempt to verify that the ATR encodes a semantically
valid structure.

Instances of this class are immutable. Where data is passed in or out
via byte arrays, defensive cloning is performed.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ATR​(byte[] atr)

Constructs an ATR from a byte array.

**Parameters:**
- atr

- the byte array containing the answer-to-reset bytes

**Throws:**
- NullPointerException

- if

atr

is null

---

### Method Details

#### public byte[] getBytes()

Returns a copy of the bytes in this ATR.

**Returns:**
- a copy of the bytes in this ATR.

---

#### public byte[] getHistoricalBytes()

Returns a copy of the historical bytes in this ATR.
If this ATR does not contain historical bytes, an array of length
zero is returned.

**Returns:**
- a copy of the historical bytes in this ATR.

---

#### public
String
toString()

Returns a string representation of this ATR.

**Overrides:**
- toString

in class

Object

**Returns:**
- a String representation of this ATR.

---

#### public boolean equals​(
Object
obj)

Compares the specified object with this ATR for equality.
Returns true if the given object is also an ATR and its bytes are
identical to the bytes in this ATR.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to be compared for equality with this ATR

**Returns:**
- true if the specified object is equal to this ATR

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this ATR.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this ATR.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class ATR

java.lang.Object

- javax.smartcardio.ATR

javax.smartcardio.ATR

**All Implemented Interfaces:** Serializable

```java
public final class
ATR

extends
Object

implements
Serializable
```

A Smart Card's answer-to-reset bytes. A Card's ATR object can be obtained
by calling

Card.getATR()

.
This class does not attempt to verify that the ATR encodes a semantically
valid structure.

Instances of this class are immutable. Where data is passed in or out
via byte arrays, defensive cloning is performed.

**Since:** 1.6
**See Also:** Card.getATR()

,

Serialized Form

public final class

ATR

extends

Object

implements

Serializable

A Smart Card's answer-to-reset bytes. A Card's ATR object can be obtained
by calling

Card.getATR()

.
This class does not attempt to verify that the ATR encodes a semantically
valid structure.

Instances of this class are immutable. Where data is passed in or out
via byte arrays, defensive cloning is performed.

Instances of this class are immutable. Where data is passed in or out
via byte arrays, defensive cloning is performed.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ATR

​(byte[] atr)

Constructs an ATR from a byte array.

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

Compares the specified object with this ATR for equality.

byte[]

getBytes

()

Returns a copy of the bytes in this ATR.

byte[]

getHistoricalBytes

()

Returns a copy of the historical bytes in this ATR.

int

hashCode

()

Returns the hash code value for this ATR.

String

toString

()

Returns a string representation of this ATR.

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

Constructor

Description

ATR

​(byte[] atr)

Constructs an ATR from a byte array.

---

#### Constructor Summary

Constructs an ATR from a byte array.

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

Compares the specified object with this ATR for equality.

byte[]

getBytes

()

Returns a copy of the bytes in this ATR.

byte[]

getHistoricalBytes

()

Returns a copy of the historical bytes in this ATR.

int

hashCode

()

Returns the hash code value for this ATR.

String

toString

()

Returns a string representation of this ATR.

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

Compares the specified object with this ATR for equality.

Returns a copy of the bytes in this ATR.

Returns a copy of the historical bytes in this ATR.

Returns the hash code value for this ATR.

Returns a string representation of this ATR.

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

- ATR

```java
public ATR​(byte[] atr)
```

Constructs an ATR from a byte array.

**Parameters:** atr

- the byte array containing the answer-to-reset bytes
**Throws:** NullPointerException

- if

atr

is null

============ METHOD DETAIL ==========

- Method Detail

- getBytes

```java
public byte[] getBytes()
```

Returns a copy of the bytes in this ATR.

**Returns:** a copy of the bytes in this ATR.

- getHistoricalBytes

```java
public byte[] getHistoricalBytes()
```

Returns a copy of the historical bytes in this ATR.
If this ATR does not contain historical bytes, an array of length
zero is returned.

**Returns:** a copy of the historical bytes in this ATR.

- toString

```java
public
String
toString()
```

Returns a string representation of this ATR.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this ATR.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified object with this ATR for equality.
Returns true if the given object is also an ATR and its bytes are
identical to the bytes in this ATR.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this ATR
**Returns:** true if the specified object is equal to this ATR
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this ATR.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this ATR.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- ATR

```java
public ATR​(byte[] atr)
```

Constructs an ATR from a byte array.

**Parameters:** atr

- the byte array containing the answer-to-reset bytes
**Throws:** NullPointerException

- if

atr

is null

---

#### Constructor Detail

ATR

```java
public ATR​(byte[] atr)
```

Constructs an ATR from a byte array.

**Parameters:** atr

- the byte array containing the answer-to-reset bytes
**Throws:** NullPointerException

- if

atr

is null

---

#### ATR

public ATR​(byte[] atr)

Constructs an ATR from a byte array.

Method Detail

- getBytes

```java
public byte[] getBytes()
```

Returns a copy of the bytes in this ATR.

**Returns:** a copy of the bytes in this ATR.

- getHistoricalBytes

```java
public byte[] getHistoricalBytes()
```

Returns a copy of the historical bytes in this ATR.
If this ATR does not contain historical bytes, an array of length
zero is returned.

**Returns:** a copy of the historical bytes in this ATR.

- toString

```java
public
String
toString()
```

Returns a string representation of this ATR.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this ATR.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified object with this ATR for equality.
Returns true if the given object is also an ATR and its bytes are
identical to the bytes in this ATR.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this ATR
**Returns:** true if the specified object is equal to this ATR
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this ATR.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this ATR.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getBytes

```java
public byte[] getBytes()
```

Returns a copy of the bytes in this ATR.

**Returns:** a copy of the bytes in this ATR.

---

#### getBytes

public byte[] getBytes()

Returns a copy of the bytes in this ATR.

getHistoricalBytes

```java
public byte[] getHistoricalBytes()
```

Returns a copy of the historical bytes in this ATR.
If this ATR does not contain historical bytes, an array of length
zero is returned.

**Returns:** a copy of the historical bytes in this ATR.

---

#### getHistoricalBytes

public byte[] getHistoricalBytes()

Returns a copy of the historical bytes in this ATR.
If this ATR does not contain historical bytes, an array of length
zero is returned.

toString

```java
public
String
toString()
```

Returns a string representation of this ATR.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this ATR.

---

#### toString

public

String

toString()

Returns a string representation of this ATR.

equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified object with this ATR for equality.
Returns true if the given object is also an ATR and its bytes are
identical to the bytes in this ATR.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this ATR
**Returns:** true if the specified object is equal to this ATR
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares the specified object with this ATR for equality.
Returns true if the given object is also an ATR and its bytes are
identical to the bytes in this ATR.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this ATR.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this ATR.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this ATR.

---

