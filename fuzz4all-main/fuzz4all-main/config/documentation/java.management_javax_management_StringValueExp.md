# Class StringValueExp

**Source:** `java.management\javax\management\StringValueExp.html`

### Class Description

```java
public class
StringValueExp

extends
Object

implements
ValueExp
```

Represents strings that are arguments to relational constraints.
A

StringValueExp

may be used anywhere a

ValueExp

is required.

**All Implemented Interfaces:** Serializable

,

ValueExp

---

### Field Details

*No entries found.*

### Constructor Details

#### public StringValueExp()

Basic constructor.

---

#### public StringValueExp​(
String
val)

Creates a new

StringValueExp

representing the
given string.

**Parameters:**
- val

- the string that will be the value of this expression

---

### Method Details

#### public
String
getValue()

Returns the string represented by the

StringValueExp

instance.

**Returns:**
- the string.

---

#### public
String
toString()

Returns the string representing the object.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

#### @Deprecated

public void setMBeanServer​(
MBeanServer
s)

Sets the MBean server on which the query is to be performed.

**Specified by:**
- setMBeanServer

in interface

ValueExp

**Parameters:**
- s

- The MBean server on which the query is to be performed.

---

#### public
ValueExp
apply​(
ObjectName
name)
throws
BadStringOperationException
,

BadBinaryOpValueExpException
,

BadAttributeValueExpException
,

InvalidApplicationException

Applies the ValueExp on a MBean.

**Specified by:**
- apply

in interface

ValueExp

**Parameters:**
- name

- The name of the MBean on which the ValueExp will be applied.

**Returns:**
- The

ValueExp

.

**Throws:**
- BadStringOperationException

- when an invalid string
operation is passed to a method for constructing a query
- BadBinaryOpValueExpException

- when an invalid expression
is passed to a method for constructing a query
- BadAttributeValueExpException

- when an invalid MBean
attribute is passed to a query constructing method
- InvalidApplicationException

- when an invalid apply is attempted

---

### Additional Sections

#### Class StringValueExp

java.lang.Object

- javax.management.StringValueExp

javax.management.StringValueExp

**All Implemented Interfaces:** Serializable

,

ValueExp

```java
public class
StringValueExp

extends
Object

implements
ValueExp
```

Represents strings that are arguments to relational constraints.
A

StringValueExp

may be used anywhere a

ValueExp

is required.

**Since:** 1.5
**See Also:** Serialized Form

public class

StringValueExp

extends

Object

implements

ValueExp

Represents strings that are arguments to relational constraints.
A

StringValueExp

may be used anywhere a

ValueExp

is required.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StringValueExp

()

Basic constructor.

StringValueExp

​(

String

val)

Creates a new

StringValueExp

representing the
given string.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

ValueExp

apply

​(

ObjectName

name)

Applies the ValueExp on a MBean.

String

getValue

()

Returns the string represented by the

StringValueExp

instance.

void

setMBeanServer

​(

MBeanServer

s)

Deprecated.

String

toString

()

Returns the string representing the object.

- Methods declared in class java.lang.

Object

clone

,

equals

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

StringValueExp

()

Basic constructor.

StringValueExp

​(

String

val)

Creates a new

StringValueExp

representing the
given string.

---

#### Constructor Summary

Basic constructor.

Creates a new

StringValueExp

representing the
given string.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

ValueExp

apply

​(

ObjectName

name)

Applies the ValueExp on a MBean.

String

getValue

()

Returns the string represented by the

StringValueExp

instance.

void

setMBeanServer

​(

MBeanServer

s)

Deprecated.

String

toString

()

Returns the string representing the object.

- Methods declared in class java.lang.

Object

clone

,

equals

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

Applies the ValueExp on a MBean.

Returns the string represented by the

StringValueExp

instance.

Deprecated.

Returns the string representing the object.

Methods declared in class java.lang.

Object

clone

,

equals

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

- StringValueExp

```java
public StringValueExp()
```

Basic constructor.

- StringValueExp

```java
public StringValueExp​(
String
val)
```

Creates a new

StringValueExp

representing the
given string.

**Parameters:** val

- the string that will be the value of this expression

============ METHOD DETAIL ==========

- Method Detail

- getValue

```java
public
String
getValue()
```

Returns the string represented by the

StringValueExp

instance.

**Returns:** the string.

- toString

```java
public
String
toString()
```

Returns the string representing the object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- setMBeanServer

```java
@Deprecated

public void setMBeanServer​(
MBeanServer
s)
```

Deprecated.

Sets the MBean server on which the query is to be performed.

**Specified by:** setMBeanServer

in interface

ValueExp
**Parameters:** s

- The MBean server on which the query is to be performed.

- apply

```java
public
ValueExp
apply​(
ObjectName
name)
throws
BadStringOperationException
,

BadBinaryOpValueExpException
,

BadAttributeValueExpException
,

InvalidApplicationException
```

Applies the ValueExp on a MBean.

**Specified by:** apply

in interface

ValueExp
**Parameters:** name

- The name of the MBean on which the ValueExp will be applied.
**Returns:** The

ValueExp

.
**Throws:** BadStringOperationException

- when an invalid string
operation is passed to a method for constructing a query
**Throws:** BadBinaryOpValueExpException

- when an invalid expression
is passed to a method for constructing a query
**Throws:** BadAttributeValueExpException

- when an invalid MBean
attribute is passed to a query constructing method
**Throws:** InvalidApplicationException

- when an invalid apply is attempted

Constructor Detail

- StringValueExp

```java
public StringValueExp()
```

Basic constructor.

- StringValueExp

```java
public StringValueExp​(
String
val)
```

Creates a new

StringValueExp

representing the
given string.

**Parameters:** val

- the string that will be the value of this expression

---

#### Constructor Detail

StringValueExp

```java
public StringValueExp()
```

Basic constructor.

---

#### StringValueExp

public StringValueExp()

Basic constructor.

StringValueExp

```java
public StringValueExp​(
String
val)
```

Creates a new

StringValueExp

representing the
given string.

**Parameters:** val

- the string that will be the value of this expression

---

#### StringValueExp

public StringValueExp​(

String

val)

Creates a new

StringValueExp

representing the
given string.

Method Detail

- getValue

```java
public
String
getValue()
```

Returns the string represented by the

StringValueExp

instance.

**Returns:** the string.

- toString

```java
public
String
toString()
```

Returns the string representing the object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- setMBeanServer

```java
@Deprecated

public void setMBeanServer​(
MBeanServer
s)
```

Deprecated.

Sets the MBean server on which the query is to be performed.

**Specified by:** setMBeanServer

in interface

ValueExp
**Parameters:** s

- The MBean server on which the query is to be performed.

- apply

```java
public
ValueExp
apply​(
ObjectName
name)
throws
BadStringOperationException
,

BadBinaryOpValueExpException
,

BadAttributeValueExpException
,

InvalidApplicationException
```

Applies the ValueExp on a MBean.

**Specified by:** apply

in interface

ValueExp
**Parameters:** name

- The name of the MBean on which the ValueExp will be applied.
**Returns:** The

ValueExp

.
**Throws:** BadStringOperationException

- when an invalid string
operation is passed to a method for constructing a query
**Throws:** BadBinaryOpValueExpException

- when an invalid expression
is passed to a method for constructing a query
**Throws:** BadAttributeValueExpException

- when an invalid MBean
attribute is passed to a query constructing method
**Throws:** InvalidApplicationException

- when an invalid apply is attempted

---

#### Method Detail

getValue

```java
public
String
getValue()
```

Returns the string represented by the

StringValueExp

instance.

**Returns:** the string.

---

#### getValue

public

String

getValue()

Returns the string represented by the

StringValueExp

instance.

toString

```java
public
String
toString()
```

Returns the string representing the object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns the string representing the object.

setMBeanServer

```java
@Deprecated

public void setMBeanServer​(
MBeanServer
s)
```

Deprecated.

Sets the MBean server on which the query is to be performed.

**Specified by:** setMBeanServer

in interface

ValueExp
**Parameters:** s

- The MBean server on which the query is to be performed.

---

#### setMBeanServer

@Deprecated

public void setMBeanServer​(

MBeanServer

s)

Sets the MBean server on which the query is to be performed.

apply

```java
public
ValueExp
apply​(
ObjectName
name)
throws
BadStringOperationException
,

BadBinaryOpValueExpException
,

BadAttributeValueExpException
,

InvalidApplicationException
```

Applies the ValueExp on a MBean.

**Specified by:** apply

in interface

ValueExp
**Parameters:** name

- The name of the MBean on which the ValueExp will be applied.
**Returns:** The

ValueExp

.
**Throws:** BadStringOperationException

- when an invalid string
operation is passed to a method for constructing a query
**Throws:** BadBinaryOpValueExpException

- when an invalid expression
is passed to a method for constructing a query
**Throws:** BadAttributeValueExpException

- when an invalid MBean
attribute is passed to a query constructing method
**Throws:** InvalidApplicationException

- when an invalid apply is attempted

---

#### apply

public

ValueExp

apply​(

ObjectName

name)
throws

BadStringOperationException

,

BadBinaryOpValueExpException

,

BadAttributeValueExpException

,

InvalidApplicationException

Applies the ValueExp on a MBean.

---

