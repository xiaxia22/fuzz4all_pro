# Class StringRefAddr

**Source:** `java.naming\javax\naming\StringRefAddr.html`

### Class Description

```java
public class
StringRefAddr

extends
RefAddr
```

This class represents the string form of the address of
a communications end-point.
It consists of a type that describes the communication mechanism
and a string contents specific to that communication mechanism.
The format and interpretation of
the address type and the contents of the address are based on
the agreement of three parties: the client that uses the address,
the object/server that can be reached using the address, and the
administrator or program that creates the address.

An example of a string reference address is a host name.
Another example of a string reference address is a URL.

A string reference address is immutable:
once created, it cannot be changed. Multithreaded access to
a single StringRefAddr need not be synchronized.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public StringRefAddr​(
String
addrType,

String
addr)

Constructs a new instance of StringRefAddr using its address type
and contents.

**Parameters:**
- addrType

- A non-null string describing the type of the address.
- addr

- The possibly null contents of the address in the form of a string.

---

### Method Details

#### public
Object
getContent()

Retrieves the contents of this address. The result is a string.

**Specified by:**
- getContent

in class

RefAddr

**Returns:**
- The possibly null address contents.

---

### Additional Sections

#### Class StringRefAddr

java.lang.Object

- javax.naming.RefAddr
- - javax.naming.StringRefAddr

javax.naming.RefAddr

- javax.naming.StringRefAddr

javax.naming.StringRefAddr

**All Implemented Interfaces:** Serializable

```java
public class
StringRefAddr

extends
RefAddr
```

This class represents the string form of the address of
a communications end-point.
It consists of a type that describes the communication mechanism
and a string contents specific to that communication mechanism.
The format and interpretation of
the address type and the contents of the address are based on
the agreement of three parties: the client that uses the address,
the object/server that can be reached using the address, and the
administrator or program that creates the address.

An example of a string reference address is a host name.
Another example of a string reference address is a URL.

A string reference address is immutable:
once created, it cannot be changed. Multithreaded access to
a single StringRefAddr need not be synchronized.

**Since:** 1.3
**See Also:** RefAddr

,

BinaryRefAddr

,

Serialized Form

public class

StringRefAddr

extends

RefAddr

This class represents the string form of the address of
a communications end-point.
It consists of a type that describes the communication mechanism
and a string contents specific to that communication mechanism.
The format and interpretation of
the address type and the contents of the address are based on
the agreement of three parties: the client that uses the address,
the object/server that can be reached using the address, and the
administrator or program that creates the address.

An example of a string reference address is a host name.
Another example of a string reference address is a URL.

A string reference address is immutable:
once created, it cannot be changed. Multithreaded access to
a single StringRefAddr need not be synchronized.

An example of a string reference address is a host name.
Another example of a string reference address is a URL.

A string reference address is immutable:
once created, it cannot be changed. Multithreaded access to
a single StringRefAddr need not be synchronized.

A string reference address is immutable:
once created, it cannot be changed. Multithreaded access to
a single StringRefAddr need not be synchronized.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.naming.

RefAddr

addrType

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StringRefAddr

​(

String

addrType,

String

addr)

Constructs a new instance of StringRefAddr using its address type
and contents.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getContent

()

Retrieves the contents of this address.

- Methods declared in class javax.naming.

RefAddr

equals

,

getType

,

hashCode

,

toString

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

- Fields declared in class javax.naming.

RefAddr

addrType

---

#### Field Summary

Fields declared in class javax.naming.

RefAddr

addrType

---

#### Fields declared in class javax.naming. RefAddr

Constructor Summary

Constructors

Constructor

Description

StringRefAddr

​(

String

addrType,

String

addr)

Constructs a new instance of StringRefAddr using its address type
and contents.

---

#### Constructor Summary

Constructs a new instance of StringRefAddr using its address type
and contents.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getContent

()

Retrieves the contents of this address.

- Methods declared in class javax.naming.

RefAddr

equals

,

getType

,

hashCode

,

toString

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

Retrieves the contents of this address.

Methods declared in class javax.naming.

RefAddr

equals

,

getType

,

hashCode

,

toString

---

#### Methods declared in class javax.naming. RefAddr

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

- StringRefAddr

```java
public StringRefAddr​(
String
addrType,

String
addr)
```

Constructs a new instance of StringRefAddr using its address type
and contents.

**Parameters:** addrType

- A non-null string describing the type of the address.
**Parameters:** addr

- The possibly null contents of the address in the form of a string.

============ METHOD DETAIL ==========

- Method Detail

- getContent

```java
public
Object
getContent()
```

Retrieves the contents of this address. The result is a string.

**Specified by:** getContent

in class

RefAddr
**Returns:** The possibly null address contents.

Constructor Detail

- StringRefAddr

```java
public StringRefAddr​(
String
addrType,

String
addr)
```

Constructs a new instance of StringRefAddr using its address type
and contents.

**Parameters:** addrType

- A non-null string describing the type of the address.
**Parameters:** addr

- The possibly null contents of the address in the form of a string.

---

#### Constructor Detail

StringRefAddr

```java
public StringRefAddr​(
String
addrType,

String
addr)
```

Constructs a new instance of StringRefAddr using its address type
and contents.

**Parameters:** addrType

- A non-null string describing the type of the address.
**Parameters:** addr

- The possibly null contents of the address in the form of a string.

---

#### StringRefAddr

public StringRefAddr​(

String

addrType,

String

addr)

Constructs a new instance of StringRefAddr using its address type
and contents.

Method Detail

- getContent

```java
public
Object
getContent()
```

Retrieves the contents of this address. The result is a string.

**Specified by:** getContent

in class

RefAddr
**Returns:** The possibly null address contents.

---

#### Method Detail

getContent

```java
public
Object
getContent()
```

Retrieves the contents of this address. The result is a string.

**Specified by:** getContent

in class

RefAddr
**Returns:** The possibly null address contents.

---

#### getContent

public

Object

getContent()

Retrieves the contents of this address. The result is a string.

---

