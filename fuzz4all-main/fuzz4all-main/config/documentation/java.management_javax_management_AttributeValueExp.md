# Class AttributeValueExp

**Source:** `java.management\javax\management\AttributeValueExp.html`

### Class Description

```java
public class
AttributeValueExp

extends
Object

implements
ValueExp
```

Represents attributes used as arguments to relational constraints.
Instances of this class are usually obtained using

Query.attr

.

An

AttributeValueExp

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

#### @Deprecated

public AttributeValueExp()

An

AttributeValueExp

with a null attribute.

---

#### public AttributeValueExp​(
String
attr)

Creates a new

AttributeValueExp

representing the
specified object attribute, named attr.

**Parameters:**
- attr

- the name of the attribute whose value is the value
of this

ValueExp

.

---

### Method Details

#### public
String
getAttributeName()

Returns a string representation of the name of the attribute.

**Returns:**
- the attribute name.

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

Applies the

AttributeValueExp

on an MBean.
This method calls

getAttribute(name)

and wraps
the result as a

ValueExp

. The value returned by

getAttribute

must be a

Number

,

String

,
or

Boolean

; otherwise this method throws a

BadAttributeValueExpException

, which will cause
the containing query to be false for this

name

.

**Specified by:**
- apply

in interface

ValueExp

**Parameters:**
- name

- The name of the MBean on which the

AttributeValueExp

will be applied.

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

#### public
String
toString()

Returns the string representing its value.

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

#### protected
Object
getAttribute​(
ObjectName
name)

Return the value of the given attribute in the named MBean.
If the attempt to access the attribute generates an exception,
return null.

The MBean Server used is the one returned by

QueryEval.getMBeanServer()

.

**Parameters:**
- name

- the name of the MBean whose attribute is to be returned.

**Returns:**
- the value of the attribute, or null if it could not be
obtained.

---

### Additional Sections

#### Class AttributeValueExp

java.lang.Object

- javax.management.AttributeValueExp

javax.management.AttributeValueExp

**All Implemented Interfaces:** Serializable

,

ValueExp

```java
public class
AttributeValueExp

extends
Object

implements
ValueExp
```

Represents attributes used as arguments to relational constraints.
Instances of this class are usually obtained using

Query.attr

.

An

AttributeValueExp

may be used anywhere a

ValueExp

is required.

**Since:** 1.5
**See Also:** Serialized Form

public class

AttributeValueExp

extends

Object

implements

ValueExp

Represents attributes used as arguments to relational constraints.
Instances of this class are usually obtained using

Query.attr

.

An

AttributeValueExp

may be used anywhere a

ValueExp

is required.

Represents attributes used as arguments to relational constraints.
Instances of this class are usually obtained using

Query.attr

.

An

AttributeValueExp

may be used anywhere a

ValueExp

is required.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AttributeValueExp

()

Deprecated.

An instance created with this constructor cannot be
used in a query.

AttributeValueExp

​(

String

attr)

Creates a new

AttributeValueExp

representing the
specified object attribute, named attr.

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

Applies the

AttributeValueExp

on an MBean.

protected

Object

getAttribute

​(

ObjectName

name)

Return the value of the given attribute in the named MBean.

String

getAttributeName

()

Returns a string representation of the name of the attribute.

void

setMBeanServer

​(

MBeanServer

s)

Deprecated.

This method has no effect.

String

toString

()

Returns the string representing its value.

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

AttributeValueExp

()

Deprecated.

An instance created with this constructor cannot be
used in a query.

AttributeValueExp

​(

String

attr)

Creates a new

AttributeValueExp

representing the
specified object attribute, named attr.

---

#### Constructor Summary

Deprecated.

An instance created with this constructor cannot be
used in a query.

Creates a new

AttributeValueExp

representing the
specified object attribute, named attr.

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

Applies the

AttributeValueExp

on an MBean.

protected

Object

getAttribute

​(

ObjectName

name)

Return the value of the given attribute in the named MBean.

String

getAttributeName

()

Returns a string representation of the name of the attribute.

void

setMBeanServer

​(

MBeanServer

s)

Deprecated.

This method has no effect.

String

toString

()

Returns the string representing its value.

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

Applies the

AttributeValueExp

on an MBean.

Return the value of the given attribute in the named MBean.

Returns a string representation of the name of the attribute.

Deprecated.

This method has no effect.

Returns the string representing its value.

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

- AttributeValueExp

```java
@Deprecated

public AttributeValueExp()
```

Deprecated.

An instance created with this constructor cannot be
used in a query.

An

AttributeValueExp

with a null attribute.

- AttributeValueExp

```java
public AttributeValueExp​(
String
attr)
```

Creates a new

AttributeValueExp

representing the
specified object attribute, named attr.

**Parameters:** attr

- the name of the attribute whose value is the value
of this

ValueExp

.

============ METHOD DETAIL ==========

- Method Detail

- getAttributeName

```java
public
String
getAttributeName()
```

Returns a string representation of the name of the attribute.

**Returns:** the attribute name.

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

Applies the

AttributeValueExp

on an MBean.
This method calls

getAttribute(name)

and wraps
the result as a

ValueExp

. The value returned by

getAttribute

must be a

Number

,

String

,
or

Boolean

; otherwise this method throws a

BadAttributeValueExpException

, which will cause
the containing query to be false for this

name

.

**Specified by:** apply

in interface

ValueExp
**Parameters:** name

- The name of the MBean on which the

AttributeValueExp

will be applied.
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

- toString

```java
public
String
toString()
```

Returns the string representing its value.

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

This method has no effect. The MBean Server used to
obtain an attribute value is

QueryEval.getMBeanServer()

.

Sets the MBean server on which the query is to be performed.

**Specified by:** setMBeanServer

in interface

ValueExp
**Parameters:** s

- The MBean server on which the query is to be performed.

- getAttribute

```java
protected
Object
getAttribute​(
ObjectName
name)
```

Return the value of the given attribute in the named MBean.
If the attempt to access the attribute generates an exception,
return null.

The MBean Server used is the one returned by

QueryEval.getMBeanServer()

.

**Parameters:** name

- the name of the MBean whose attribute is to be returned.
**Returns:** the value of the attribute, or null if it could not be
obtained.

Constructor Detail

- AttributeValueExp

```java
@Deprecated

public AttributeValueExp()
```

Deprecated.

An instance created with this constructor cannot be
used in a query.

An

AttributeValueExp

with a null attribute.

- AttributeValueExp

```java
public AttributeValueExp​(
String
attr)
```

Creates a new

AttributeValueExp

representing the
specified object attribute, named attr.

**Parameters:** attr

- the name of the attribute whose value is the value
of this

ValueExp

.

---

#### Constructor Detail

AttributeValueExp

```java
@Deprecated

public AttributeValueExp()
```

Deprecated.

An instance created with this constructor cannot be
used in a query.

An

AttributeValueExp

with a null attribute.

---

#### AttributeValueExp

@Deprecated

public AttributeValueExp()

An

AttributeValueExp

with a null attribute.

AttributeValueExp

```java
public AttributeValueExp​(
String
attr)
```

Creates a new

AttributeValueExp

representing the
specified object attribute, named attr.

**Parameters:** attr

- the name of the attribute whose value is the value
of this

ValueExp

.

---

#### AttributeValueExp

public AttributeValueExp​(

String

attr)

Creates a new

AttributeValueExp

representing the
specified object attribute, named attr.

Method Detail

- getAttributeName

```java
public
String
getAttributeName()
```

Returns a string representation of the name of the attribute.

**Returns:** the attribute name.

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

Applies the

AttributeValueExp

on an MBean.
This method calls

getAttribute(name)

and wraps
the result as a

ValueExp

. The value returned by

getAttribute

must be a

Number

,

String

,
or

Boolean

; otherwise this method throws a

BadAttributeValueExpException

, which will cause
the containing query to be false for this

name

.

**Specified by:** apply

in interface

ValueExp
**Parameters:** name

- The name of the MBean on which the

AttributeValueExp

will be applied.
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

- toString

```java
public
String
toString()
```

Returns the string representing its value.

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

This method has no effect. The MBean Server used to
obtain an attribute value is

QueryEval.getMBeanServer()

.

Sets the MBean server on which the query is to be performed.

**Specified by:** setMBeanServer

in interface

ValueExp
**Parameters:** s

- The MBean server on which the query is to be performed.

- getAttribute

```java
protected
Object
getAttribute​(
ObjectName
name)
```

Return the value of the given attribute in the named MBean.
If the attempt to access the attribute generates an exception,
return null.

The MBean Server used is the one returned by

QueryEval.getMBeanServer()

.

**Parameters:** name

- the name of the MBean whose attribute is to be returned.
**Returns:** the value of the attribute, or null if it could not be
obtained.

---

#### Method Detail

getAttributeName

```java
public
String
getAttributeName()
```

Returns a string representation of the name of the attribute.

**Returns:** the attribute name.

---

#### getAttributeName

public

String

getAttributeName()

Returns a string representation of the name of the attribute.

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

Applies the

AttributeValueExp

on an MBean.
This method calls

getAttribute(name)

and wraps
the result as a

ValueExp

. The value returned by

getAttribute

must be a

Number

,

String

,
or

Boolean

; otherwise this method throws a

BadAttributeValueExpException

, which will cause
the containing query to be false for this

name

.

**Specified by:** apply

in interface

ValueExp
**Parameters:** name

- The name of the MBean on which the

AttributeValueExp

will be applied.
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

Applies the

AttributeValueExp

on an MBean.
This method calls

getAttribute(name)

and wraps
the result as a

ValueExp

. The value returned by

getAttribute

must be a

Number

,

String

,
or

Boolean

; otherwise this method throws a

BadAttributeValueExpException

, which will cause
the containing query to be false for this

name

.

toString

```java
public
String
toString()
```

Returns the string representing its value.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns the string representing its value.

setMBeanServer

```java
@Deprecated

public void setMBeanServer​(
MBeanServer
s)
```

Deprecated.

This method has no effect. The MBean Server used to
obtain an attribute value is

QueryEval.getMBeanServer()

.

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

getAttribute

```java
protected
Object
getAttribute​(
ObjectName
name)
```

Return the value of the given attribute in the named MBean.
If the attempt to access the attribute generates an exception,
return null.

The MBean Server used is the one returned by

QueryEval.getMBeanServer()

.

**Parameters:** name

- the name of the MBean whose attribute is to be returned.
**Returns:** the value of the attribute, or null if it could not be
obtained.

---

#### getAttribute

protected

Object

getAttribute​(

ObjectName

name)

Return the value of the given attribute in the named MBean.
If the attempt to access the attribute generates an exception,
return null.

The MBean Server used is the one returned by

QueryEval.getMBeanServer()

.

Return the value of the given attribute in the named MBean.
If the attempt to access the attribute generates an exception,
return null.

The MBean Server used is the one returned by

QueryEval.getMBeanServer()

.

---

