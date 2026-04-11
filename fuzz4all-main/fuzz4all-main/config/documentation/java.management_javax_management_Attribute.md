# Class Attribute

**Source:** `java.management\javax\management\Attribute.html`

### Class Description

```java
public class
Attribute

extends
Object

implements
Serializable
```

Represents an MBean attribute by associating its name with its value.
The MBean server and other objects use this class to get and set attributes values.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public Attribute​(
String
name,

Object
value)

Constructs an Attribute object which associates the given attribute name with the given value.

**Parameters:**
- name

- A String containing the name of the attribute to be created. Cannot be null.
- value

- The Object which is assigned to the attribute. This object must be of the same type as the attribute.

---

### Method Details

#### public
String
getName()

Returns a String containing the name of the attribute.

**Returns:**
- the name of the attribute.

---

#### public
Object
getValue()

Returns an Object that is the value of this attribute.

**Returns:**
- the value of the attribute.

---

#### public boolean equals​(
Object
object)

Compares the current Attribute Object with another Attribute Object.

**Overrides:**
- equals

in class

Object

**Parameters:**
- object

- The Attribute that the current Attribute is to be compared with.

**Returns:**
- True if the two Attribute objects are equal, otherwise false.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this attribute.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this attribute.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a String object representing this Attribute's value. The format of this
string is not specified, but users can expect that two Attributes return the
same string if and only if they are equal.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class Attribute

java.lang.Object

- javax.management.Attribute

javax.management.Attribute

**All Implemented Interfaces:** Serializable

```java
public class
Attribute

extends
Object

implements
Serializable
```

Represents an MBean attribute by associating its name with its value.
The MBean server and other objects use this class to get and set attributes values.

**Since:** 1.5
**See Also:** Serialized Form

public class

Attribute

extends

Object

implements

Serializable

Represents an MBean attribute by associating its name with its value.
The MBean server and other objects use this class to get and set attributes values.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Attribute

​(

String

name,

Object

value)

Constructs an Attribute object which associates the given attribute name with the given value.

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

Compares the current Attribute Object with another Attribute Object.

String

getName

()

Returns a String containing the name of the attribute.

Object

getValue

()

Returns an Object that is the value of this attribute.

int

hashCode

()

Returns a hash code value for this attribute.

String

toString

()

Returns a String object representing this Attribute's value.

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

Attribute

​(

String

name,

Object

value)

Constructs an Attribute object which associates the given attribute name with the given value.

---

#### Constructor Summary

Constructs an Attribute object which associates the given attribute name with the given value.

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

Compares the current Attribute Object with another Attribute Object.

String

getName

()

Returns a String containing the name of the attribute.

Object

getValue

()

Returns an Object that is the value of this attribute.

int

hashCode

()

Returns a hash code value for this attribute.

String

toString

()

Returns a String object representing this Attribute's value.

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

Compares the current Attribute Object with another Attribute Object.

Returns a String containing the name of the attribute.

Returns an Object that is the value of this attribute.

Returns a hash code value for this attribute.

Returns a String object representing this Attribute's value.

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

- Attribute

```java
public Attribute​(
String
name,

Object
value)
```

Constructs an Attribute object which associates the given attribute name with the given value.

**Parameters:** name

- A String containing the name of the attribute to be created. Cannot be null.
**Parameters:** value

- The Object which is assigned to the attribute. This object must be of the same type as the attribute.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Returns a String containing the name of the attribute.

**Returns:** the name of the attribute.

- getValue

```java
public
Object
getValue()
```

Returns an Object that is the value of this attribute.

**Returns:** the value of the attribute.

- equals

```java
public boolean equals​(
Object
object)
```

Compares the current Attribute Object with another Attribute Object.

**Overrides:** equals

in class

Object
**Parameters:** object

- The Attribute that the current Attribute is to be compared with.
**Returns:** True if the two Attribute objects are equal, otherwise false.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this attribute.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this attribute.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a String object representing this Attribute's value. The format of this
string is not specified, but users can expect that two Attributes return the
same string if and only if they are equal.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- Attribute

```java
public Attribute​(
String
name,

Object
value)
```

Constructs an Attribute object which associates the given attribute name with the given value.

**Parameters:** name

- A String containing the name of the attribute to be created. Cannot be null.
**Parameters:** value

- The Object which is assigned to the attribute. This object must be of the same type as the attribute.

---

#### Constructor Detail

Attribute

```java
public Attribute​(
String
name,

Object
value)
```

Constructs an Attribute object which associates the given attribute name with the given value.

**Parameters:** name

- A String containing the name of the attribute to be created. Cannot be null.
**Parameters:** value

- The Object which is assigned to the attribute. This object must be of the same type as the attribute.

---

#### Attribute

public Attribute​(

String

name,

Object

value)

Constructs an Attribute object which associates the given attribute name with the given value.

Method Detail

- getName

```java
public
String
getName()
```

Returns a String containing the name of the attribute.

**Returns:** the name of the attribute.

- getValue

```java
public
Object
getValue()
```

Returns an Object that is the value of this attribute.

**Returns:** the value of the attribute.

- equals

```java
public boolean equals​(
Object
object)
```

Compares the current Attribute Object with another Attribute Object.

**Overrides:** equals

in class

Object
**Parameters:** object

- The Attribute that the current Attribute is to be compared with.
**Returns:** True if the two Attribute objects are equal, otherwise false.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this attribute.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this attribute.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a String object representing this Attribute's value. The format of this
string is not specified, but users can expect that two Attributes return the
same string if and only if they are equal.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

getName

```java
public
String
getName()
```

Returns a String containing the name of the attribute.

**Returns:** the name of the attribute.

---

#### getName

public

String

getName()

Returns a String containing the name of the attribute.

getValue

```java
public
Object
getValue()
```

Returns an Object that is the value of this attribute.

**Returns:** the value of the attribute.

---

#### getValue

public

Object

getValue()

Returns an Object that is the value of this attribute.

equals

```java
public boolean equals​(
Object
object)
```

Compares the current Attribute Object with another Attribute Object.

**Overrides:** equals

in class

Object
**Parameters:** object

- The Attribute that the current Attribute is to be compared with.
**Returns:** True if the two Attribute objects are equal, otherwise false.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

object)

Compares the current Attribute Object with another Attribute Object.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this attribute.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this attribute.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this attribute.

toString

```java
public
String
toString()
```

Returns a String object representing this Attribute's value. The format of this
string is not specified, but users can expect that two Attributes return the
same string if and only if they are equal.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a String object representing this Attribute's value. The format of this
string is not specified, but users can expect that two Attributes return the
same string if and only if they are equal.

---

