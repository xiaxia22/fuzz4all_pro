# Class ObjectInstance

**Source:** `java.management\javax\management\ObjectInstance.html`

### Class Description

```java
public class
ObjectInstance

extends
Object

implements
Serializable
```

Used to represent the object name of an MBean and its class name.
If the MBean is a Dynamic MBean the class name should be retrieved from
the

MBeanInfo

it provides.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ObjectInstance​(
String
objectName,

String
className)
throws
MalformedObjectNameException

Allows an object instance to be created given a string representation of
an object name and the full class name, including the package name.

**Parameters:**
- objectName

- A string representation of the object name.
- className

- The full class name, including the package
name, of the object instance. If the MBean is a Dynamic MBean
the class name corresponds to its

getMBeanInfo()

.getClassName()

.

**Throws:**
- MalformedObjectNameException

- The string passed as a
parameter does not have the right format.

---

#### public ObjectInstance​(
ObjectName
objectName,

String
className)

Allows an object instance to be created given an object name and
the full class name, including the package name.

**Parameters:**
- objectName

- The object name.
- className

- The full class name, including the package
name, of the object instance. If the MBean is a Dynamic MBean
the class name corresponds to its

getMBeanInfo()

.getClassName()

.
If the MBean is a Dynamic MBean the class name should be retrieved
from the

MBeanInfo

it provides.

---

### Method Details

#### public boolean equals​(
Object
object)

Compares the current object instance with another object instance.

**Overrides:**
- equals

in class

Object

**Parameters:**
- object

- The object instance that the current object instance is
to be compared with.

**Returns:**
- True if the two object instances are equal, otherwise false.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
ObjectName
getObjectName()

Returns the object name part.

**Returns:**
- the object name.

---

#### public
String
getClassName()

Returns the class part.

**Returns:**
- the class name.

---

#### public
String
toString()

Returns a string representing this ObjectInstance object. The format of this string
is not specified, but users can expect that two ObjectInstances return the same
string if and only if they are equal.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class ObjectInstance

java.lang.Object

- javax.management.ObjectInstance

javax.management.ObjectInstance

**All Implemented Interfaces:** Serializable

```java
public class
ObjectInstance

extends
Object

implements
Serializable
```

Used to represent the object name of an MBean and its class name.
If the MBean is a Dynamic MBean the class name should be retrieved from
the

MBeanInfo

it provides.

**Since:** 1.5
**See Also:** Serialized Form

public class

ObjectInstance

extends

Object

implements

Serializable

Used to represent the object name of an MBean and its class name.
If the MBean is a Dynamic MBean the class name should be retrieved from
the

MBeanInfo

it provides.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ObjectInstance

​(

String

objectName,

String

className)

Allows an object instance to be created given a string representation of
an object name and the full class name, including the package name.

ObjectInstance

​(

ObjectName

objectName,

String

className)

Allows an object instance to be created given an object name and
the full class name, including the package name.

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

Compares the current object instance with another object instance.

String

getClassName

()

Returns the class part.

ObjectName

getObjectName

()

Returns the object name part.

String

toString

()

Returns a string representing this ObjectInstance object.

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

Constructor Summary

Constructors

Constructor

Description

ObjectInstance

​(

String

objectName,

String

className)

Allows an object instance to be created given a string representation of
an object name and the full class name, including the package name.

ObjectInstance

​(

ObjectName

objectName,

String

className)

Allows an object instance to be created given an object name and
the full class name, including the package name.

---

#### Constructor Summary

Allows an object instance to be created given a string representation of
an object name and the full class name, including the package name.

Allows an object instance to be created given an object name and
the full class name, including the package name.

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

Compares the current object instance with another object instance.

String

getClassName

()

Returns the class part.

ObjectName

getObjectName

()

Returns the object name part.

String

toString

()

Returns a string representing this ObjectInstance object.

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

Compares the current object instance with another object instance.

Returns the class part.

Returns the object name part.

Returns a string representing this ObjectInstance object.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ObjectInstance

```java
public ObjectInstance​(
String
objectName,

String
className)
throws
MalformedObjectNameException
```

Allows an object instance to be created given a string representation of
an object name and the full class name, including the package name.

**Parameters:** objectName

- A string representation of the object name.
**Parameters:** className

- The full class name, including the package
name, of the object instance. If the MBean is a Dynamic MBean
the class name corresponds to its

getMBeanInfo()

.getClassName()

.
**Throws:** MalformedObjectNameException

- The string passed as a
parameter does not have the right format.

- ObjectInstance

```java
public ObjectInstance​(
ObjectName
objectName,

String
className)
```

Allows an object instance to be created given an object name and
the full class name, including the package name.

**Parameters:** objectName

- The object name.
**Parameters:** className

- The full class name, including the package
name, of the object instance. If the MBean is a Dynamic MBean
the class name corresponds to its

getMBeanInfo()

.getClassName()

.
If the MBean is a Dynamic MBean the class name should be retrieved
from the

MBeanInfo

it provides.

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Compares the current object instance with another object instance.

**Overrides:** equals

in class

Object
**Parameters:** object

- The object instance that the current object instance is
to be compared with.
**Returns:** True if the two object instances are equal, otherwise false.
**See Also:** Object.hashCode()

,

HashMap

- getObjectName

```java
public
ObjectName
getObjectName()
```

Returns the object name part.

**Returns:** the object name.

- getClassName

```java
public
String
getClassName()
```

Returns the class part.

**Returns:** the class name.

- toString

```java
public
String
toString()
```

Returns a string representing this ObjectInstance object. The format of this string
is not specified, but users can expect that two ObjectInstances return the same
string if and only if they are equal.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- ObjectInstance

```java
public ObjectInstance​(
String
objectName,

String
className)
throws
MalformedObjectNameException
```

Allows an object instance to be created given a string representation of
an object name and the full class name, including the package name.

**Parameters:** objectName

- A string representation of the object name.
**Parameters:** className

- The full class name, including the package
name, of the object instance. If the MBean is a Dynamic MBean
the class name corresponds to its

getMBeanInfo()

.getClassName()

.
**Throws:** MalformedObjectNameException

- The string passed as a
parameter does not have the right format.

- ObjectInstance

```java
public ObjectInstance​(
ObjectName
objectName,

String
className)
```

Allows an object instance to be created given an object name and
the full class name, including the package name.

**Parameters:** objectName

- The object name.
**Parameters:** className

- The full class name, including the package
name, of the object instance. If the MBean is a Dynamic MBean
the class name corresponds to its

getMBeanInfo()

.getClassName()

.
If the MBean is a Dynamic MBean the class name should be retrieved
from the

MBeanInfo

it provides.

---

#### Constructor Detail

ObjectInstance

```java
public ObjectInstance​(
String
objectName,

String
className)
throws
MalformedObjectNameException
```

Allows an object instance to be created given a string representation of
an object name and the full class name, including the package name.

**Parameters:** objectName

- A string representation of the object name.
**Parameters:** className

- The full class name, including the package
name, of the object instance. If the MBean is a Dynamic MBean
the class name corresponds to its

getMBeanInfo()

.getClassName()

.
**Throws:** MalformedObjectNameException

- The string passed as a
parameter does not have the right format.

---

#### ObjectInstance

public ObjectInstance​(

String

objectName,

String

className)
throws

MalformedObjectNameException

Allows an object instance to be created given a string representation of
an object name and the full class name, including the package name.

ObjectInstance

```java
public ObjectInstance​(
ObjectName
objectName,

String
className)
```

Allows an object instance to be created given an object name and
the full class name, including the package name.

**Parameters:** objectName

- The object name.
**Parameters:** className

- The full class name, including the package
name, of the object instance. If the MBean is a Dynamic MBean
the class name corresponds to its

getMBeanInfo()

.getClassName()

.
If the MBean is a Dynamic MBean the class name should be retrieved
from the

MBeanInfo

it provides.

---

#### ObjectInstance

public ObjectInstance​(

ObjectName

objectName,

String

className)

Allows an object instance to be created given an object name and
the full class name, including the package name.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Compares the current object instance with another object instance.

**Overrides:** equals

in class

Object
**Parameters:** object

- The object instance that the current object instance is
to be compared with.
**Returns:** True if the two object instances are equal, otherwise false.
**See Also:** Object.hashCode()

,

HashMap

- getObjectName

```java
public
ObjectName
getObjectName()
```

Returns the object name part.

**Returns:** the object name.

- getClassName

```java
public
String
getClassName()
```

Returns the class part.

**Returns:** the class name.

- toString

```java
public
String
toString()
```

Returns a string representing this ObjectInstance object. The format of this string
is not specified, but users can expect that two ObjectInstances return the same
string if and only if they are equal.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

equals

```java
public boolean equals​(
Object
object)
```

Compares the current object instance with another object instance.

**Overrides:** equals

in class

Object
**Parameters:** object

- The object instance that the current object instance is
to be compared with.
**Returns:** True if the two object instances are equal, otherwise false.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

object)

Compares the current object instance with another object instance.

getObjectName

```java
public
ObjectName
getObjectName()
```

Returns the object name part.

**Returns:** the object name.

---

#### getObjectName

public

ObjectName

getObjectName()

Returns the object name part.

getClassName

```java
public
String
getClassName()
```

Returns the class part.

**Returns:** the class name.

---

#### getClassName

public

String

getClassName()

Returns the class part.

toString

```java
public
String
toString()
```

Returns a string representing this ObjectInstance object. The format of this string
is not specified, but users can expect that two ObjectInstances return the same
string if and only if they are equal.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a string representing this ObjectInstance object. The format of this string
is not specified, but users can expect that two ObjectInstances return the same
string if and only if they are equal.

---

