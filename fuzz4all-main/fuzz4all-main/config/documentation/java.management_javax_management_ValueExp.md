# Interface ValueExp

**Source:** `java.management\javax\management\ValueExp.html`

### Class Description

```java
public interface
ValueExp

extends
Serializable
```

Represents values that can be passed as arguments to
relational expressions. Strings, numbers, attributes are valid values
and should be represented by implementations of

ValueExp

.

**All Superinterfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ValueExp
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

#### @Deprecated

void setMBeanServer​(
MBeanServer
s)

Sets the MBean server on which the query is to be performed.

**Parameters:**
- s

- The MBean server on which the query is to be performed.

---

### Additional Sections

#### Interface ValueExp

**All Superinterfaces:** Serializable

**All Known Implementing Classes:** AttributeValueExp

,

StringValueExp

```java
public interface
ValueExp

extends
Serializable
```

Represents values that can be passed as arguments to
relational expressions. Strings, numbers, attributes are valid values
and should be represented by implementations of

ValueExp

.

**Since:** 1.5

public interface

ValueExp

extends

Serializable

Represents values that can be passed as arguments to
relational expressions. Strings, numbers, attributes are valid values
and should be represented by implementations of

ValueExp

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

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

void

setMBeanServer

​(

MBeanServer

s)

Deprecated.

This method is not needed because a

ValueExp

can access the MBean server in which it
is being evaluated by using

QueryEval.getMBeanServer()

.

Method Summary

All Methods

Instance Methods

Abstract Methods

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

void

setMBeanServer

​(

MBeanServer

s)

Deprecated.

This method is not needed because a

ValueExp

can access the MBean server in which it
is being evaluated by using

QueryEval.getMBeanServer()

.

---

#### Method Summary

Applies the ValueExp on a MBean.

Deprecated.

This method is not needed because a

ValueExp

can access the MBean server in which it
is being evaluated by using

QueryEval.getMBeanServer()

.

============ METHOD DETAIL ==========

- Method Detail

- apply

```java
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

- setMBeanServer

```java
@Deprecated

void setMBeanServer​(
MBeanServer
s)
```

Deprecated.

This method is not needed because a

ValueExp

can access the MBean server in which it
is being evaluated by using

QueryEval.getMBeanServer()

.

Sets the MBean server on which the query is to be performed.

**Parameters:** s

- The MBean server on which the query is to be performed.

Method Detail

- apply

```java
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

- setMBeanServer

```java
@Deprecated

void setMBeanServer​(
MBeanServer
s)
```

Deprecated.

This method is not needed because a

ValueExp

can access the MBean server in which it
is being evaluated by using

QueryEval.getMBeanServer()

.

Sets the MBean server on which the query is to be performed.

**Parameters:** s

- The MBean server on which the query is to be performed.

---

#### Method Detail

apply

```java
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

setMBeanServer

```java
@Deprecated

void setMBeanServer​(
MBeanServer
s)
```

Deprecated.

This method is not needed because a

ValueExp

can access the MBean server in which it
is being evaluated by using

QueryEval.getMBeanServer()

.

Sets the MBean server on which the query is to be performed.

**Parameters:** s

- The MBean server on which the query is to be performed.

---

#### setMBeanServer

@Deprecated

void setMBeanServer​(

MBeanServer

s)

Sets the MBean server on which the query is to be performed.

---

