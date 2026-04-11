# Class RefAddr

**Source:** `java.naming\javax\naming\RefAddr.html`

### Class Description

```java
public abstract class
RefAddr

extends
Object

implements
Serializable
```

This class represents the address of a communications end-point.
It consists of a type that describes the communication mechanism
and an address contents determined by an RefAddr subclass.

For example, an address type could be "BSD Printer Address",
which specifies that it is an address to be used with the BSD printing
protocol. Its contents could be the machine name identifying the
location of the printer server that understands this protocol.

A RefAddr is contained within a Reference.

RefAddr is an abstract class. Concrete implementations of it
determine its synchronization properties.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected
String
addrType

Contains the type of this address.

---

### Constructor Details

#### protected RefAddr​(
String
addrType)

Constructs a new instance of RefAddr using its address type.

**Parameters:**
- addrType

- A non-null string describing the type of the address.

---

### Method Details

#### public
String
getType()

Retrieves the address type of this address.

**Returns:**
- The non-null address type of this address.

---

#### public abstract
Object
getContent()

Retrieves the contents of this address.

**Returns:**
- The possibly null address contents.

---

#### public boolean equals​(
Object
obj)

Determines whether obj is equal to this RefAddr.

obj is equal to this RefAddr if all of these conditions are true

- non-null

instance of RefAddr

obj has the same address type as this RefAddr (using String.compareTo())

both obj and this RefAddr's contents are null or they are equal
(using the equals() test).

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- possibly null obj to check.

**Returns:**
- true if obj is equal to this refaddr; false otherwise.

**See Also:**
- getContent()

,

getType()

---

#### public int hashCode()

Computes the hash code of this address using its address type and contents.
The hash code is the sum of the hash code of the address type and
the hash code of the address contents.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- The hash code of this address as an int.

**See Also:**
- Object.hashCode()

---

#### public
String
toString()

Generates the string representation of this address.
The string consists of the address's type and contents with labels.
This representation is intended for display only and not to be parsed.

**Overrides:**
- toString

in class

Object

**Returns:**
- The non-null string representation of this address.

---

### Additional Sections

#### Class RefAddr

java.lang.Object

- javax.naming.RefAddr

javax.naming.RefAddr

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** BinaryRefAddr

,

StringRefAddr

```java
public abstract class
RefAddr

extends
Object

implements
Serializable
```

This class represents the address of a communications end-point.
It consists of a type that describes the communication mechanism
and an address contents determined by an RefAddr subclass.

For example, an address type could be "BSD Printer Address",
which specifies that it is an address to be used with the BSD printing
protocol. Its contents could be the machine name identifying the
location of the printer server that understands this protocol.

A RefAddr is contained within a Reference.

RefAddr is an abstract class. Concrete implementations of it
determine its synchronization properties.

**Since:** 1.3
**See Also:** Reference

,

LinkRef

,

StringRefAddr

,

BinaryRefAddr

,

Serialized Form

public abstract class

RefAddr

extends

Object

implements

Serializable

This class represents the address of a communications end-point.
It consists of a type that describes the communication mechanism
and an address contents determined by an RefAddr subclass.

For example, an address type could be "BSD Printer Address",
which specifies that it is an address to be used with the BSD printing
protocol. Its contents could be the machine name identifying the
location of the printer server that understands this protocol.

A RefAddr is contained within a Reference.

RefAddr is an abstract class. Concrete implementations of it
determine its synchronization properties.

For example, an address type could be "BSD Printer Address",
which specifies that it is an address to be used with the BSD printing
protocol. Its contents could be the machine name identifying the
location of the printer server that understands this protocol.

A RefAddr is contained within a Reference.

RefAddr is an abstract class. Concrete implementations of it
determine its synchronization properties.

A RefAddr is contained within a Reference.

RefAddr is an abstract class. Concrete implementations of it
determine its synchronization properties.

RefAddr is an abstract class. Concrete implementations of it
determine its synchronization properties.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

String

addrType

Contains the type of this address.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

RefAddr

​(

String

addrType)

Constructs a new instance of RefAddr using its address type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Determines whether obj is equal to this RefAddr.

abstract

Object

getContent

()

Retrieves the contents of this address.

String

getType

()

Retrieves the address type of this address.

int

hashCode

()

Computes the hash code of this address using its address type and contents.

String

toString

()

Generates the string representation of this address.

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

protected

String

addrType

Contains the type of this address.

---

#### Field Summary

Contains the type of this address.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

RefAddr

​(

String

addrType)

Constructs a new instance of RefAddr using its address type.

---

#### Constructor Summary

Constructs a new instance of RefAddr using its address type.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Determines whether obj is equal to this RefAddr.

abstract

Object

getContent

()

Retrieves the contents of this address.

String

getType

()

Retrieves the address type of this address.

int

hashCode

()

Computes the hash code of this address using its address type and contents.

String

toString

()

Generates the string representation of this address.

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

Determines whether obj is equal to this RefAddr.

Retrieves the contents of this address.

Retrieves the address type of this address.

Computes the hash code of this address using its address type and contents.

Generates the string representation of this address.

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

- addrType

```java
protected
String
addrType
```

Contains the type of this address.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RefAddr

```java
protected RefAddr​(
String
addrType)
```

Constructs a new instance of RefAddr using its address type.

**Parameters:** addrType

- A non-null string describing the type of the address.

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
public
String
getType()
```

Retrieves the address type of this address.

**Returns:** The non-null address type of this address.

- getContent

```java
public abstract
Object
getContent()
```

Retrieves the contents of this address.

**Returns:** The possibly null address contents.

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether obj is equal to this RefAddr.

obj is equal to this RefAddr if all of these conditions are true

- non-null

instance of RefAddr

obj has the same address type as this RefAddr (using String.compareTo())

both obj and this RefAddr's contents are null or they are equal
(using the equals() test).

**Overrides:** equals

in class

Object
**Parameters:** obj

- possibly null obj to check.
**Returns:** true if obj is equal to this refaddr; false otherwise.
**See Also:** getContent()

,

getType()

- hashCode

```java
public int hashCode()
```

Computes the hash code of this address using its address type and contents.
The hash code is the sum of the hash code of the address type and
the hash code of the address contents.

**Overrides:** hashCode

in class

Object
**Returns:** The hash code of this address as an int.
**See Also:** Object.hashCode()

- toString

```java
public
String
toString()
```

Generates the string representation of this address.
The string consists of the address's type and contents with labels.
This representation is intended for display only and not to be parsed.

**Overrides:** toString

in class

Object
**Returns:** The non-null string representation of this address.

Field Detail

- addrType

```java
protected
String
addrType
```

Contains the type of this address.

---

#### Field Detail

addrType

```java
protected
String
addrType
```

Contains the type of this address.

---

#### addrType

protected

String

addrType

Contains the type of this address.

Constructor Detail

- RefAddr

```java
protected RefAddr​(
String
addrType)
```

Constructs a new instance of RefAddr using its address type.

**Parameters:** addrType

- A non-null string describing the type of the address.

---

#### Constructor Detail

RefAddr

```java
protected RefAddr​(
String
addrType)
```

Constructs a new instance of RefAddr using its address type.

**Parameters:** addrType

- A non-null string describing the type of the address.

---

#### RefAddr

protected RefAddr​(

String

addrType)

Constructs a new instance of RefAddr using its address type.

Method Detail

- getType

```java
public
String
getType()
```

Retrieves the address type of this address.

**Returns:** The non-null address type of this address.

- getContent

```java
public abstract
Object
getContent()
```

Retrieves the contents of this address.

**Returns:** The possibly null address contents.

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether obj is equal to this RefAddr.

obj is equal to this RefAddr if all of these conditions are true

- non-null

instance of RefAddr

obj has the same address type as this RefAddr (using String.compareTo())

both obj and this RefAddr's contents are null or they are equal
(using the equals() test).

**Overrides:** equals

in class

Object
**Parameters:** obj

- possibly null obj to check.
**Returns:** true if obj is equal to this refaddr; false otherwise.
**See Also:** getContent()

,

getType()

- hashCode

```java
public int hashCode()
```

Computes the hash code of this address using its address type and contents.
The hash code is the sum of the hash code of the address type and
the hash code of the address contents.

**Overrides:** hashCode

in class

Object
**Returns:** The hash code of this address as an int.
**See Also:** Object.hashCode()

- toString

```java
public
String
toString()
```

Generates the string representation of this address.
The string consists of the address's type and contents with labels.
This representation is intended for display only and not to be parsed.

**Overrides:** toString

in class

Object
**Returns:** The non-null string representation of this address.

---

#### Method Detail

getType

```java
public
String
getType()
```

Retrieves the address type of this address.

**Returns:** The non-null address type of this address.

---

#### getType

public

String

getType()

Retrieves the address type of this address.

getContent

```java
public abstract
Object
getContent()
```

Retrieves the contents of this address.

**Returns:** The possibly null address contents.

---

#### getContent

public abstract

Object

getContent()

Retrieves the contents of this address.

equals

```java
public boolean equals​(
Object
obj)
```

Determines whether obj is equal to this RefAddr.

obj is equal to this RefAddr if all of these conditions are true

- non-null

instance of RefAddr

obj has the same address type as this RefAddr (using String.compareTo())

both obj and this RefAddr's contents are null or they are equal
(using the equals() test).

**Overrides:** equals

in class

Object
**Parameters:** obj

- possibly null obj to check.
**Returns:** true if obj is equal to this refaddr; false otherwise.
**See Also:** getContent()

,

getType()

---

#### equals

public boolean equals​(

Object

obj)

Determines whether obj is equal to this RefAddr.

obj is equal to this RefAddr if all of these conditions are true

- non-null

instance of RefAddr

obj has the same address type as this RefAddr (using String.compareTo())

both obj and this RefAddr's contents are null or they are equal
(using the equals() test).

obj is equal to this RefAddr if all of these conditions are true

- non-null

instance of RefAddr

obj has the same address type as this RefAddr (using String.compareTo())

both obj and this RefAddr's contents are null or they are equal
(using the equals() test).

non-null

instance of RefAddr

obj has the same address type as this RefAddr (using String.compareTo())

both obj and this RefAddr's contents are null or they are equal
(using the equals() test).

hashCode

```java
public int hashCode()
```

Computes the hash code of this address using its address type and contents.
The hash code is the sum of the hash code of the address type and
the hash code of the address contents.

**Overrides:** hashCode

in class

Object
**Returns:** The hash code of this address as an int.
**See Also:** Object.hashCode()

---

#### hashCode

public int hashCode()

Computes the hash code of this address using its address type and contents.
The hash code is the sum of the hash code of the address type and
the hash code of the address contents.

toString

```java
public
String
toString()
```

Generates the string representation of this address.
The string consists of the address's type and contents with labels.
This representation is intended for display only and not to be parsed.

**Overrides:** toString

in class

Object
**Returns:** The non-null string representation of this address.

---

#### toString

public

String

toString()

Generates the string representation of this address.
The string consists of the address's type and contents with labels.
This representation is intended for display only and not to be parsed.

---

