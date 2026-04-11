# Interface QueryExp

**Source:** `java.management\javax\management\QueryExp.html`

### Class Description

```java
public interface
QueryExp

extends
Serializable
```

Represents relational constraints similar to database query "where
clauses". Instances of QueryExp are returned by the static methods of the

Query

class.

It is possible, but not
recommended, to create custom queries by implementing this
interface. In that case, it is better to extend the

QueryEval

class than to implement the interface directly, so that
the

setMBeanServer(javax.management.MBeanServer)

method works correctly.

**All Superinterfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean apply​(
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

Applies the QueryExp on an MBean.

**Parameters:**
- name

- The name of the MBean on which the QueryExp will be applied.

**Returns:**
- True if the query was successfully applied to the MBean, false otherwise

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

#### void setMBeanServer​(
MBeanServer
s)

Sets the MBean server on which the query is to be performed.

**Parameters:**
- s

- The MBean server on which the query is to be performed.

---

### Additional Sections

#### Interface QueryExp

**All Superinterfaces:** Serializable

**All Known Implementing Classes:** ObjectName

```java
public interface
QueryExp

extends
Serializable
```

Represents relational constraints similar to database query "where
clauses". Instances of QueryExp are returned by the static methods of the

Query

class.

It is possible, but not
recommended, to create custom queries by implementing this
interface. In that case, it is better to extend the

QueryEval

class than to implement the interface directly, so that
the

setMBeanServer(javax.management.MBeanServer)

method works correctly.

**Since:** 1.5
**See Also:** MBeanServer.queryNames

public interface

QueryExp

extends

Serializable

Represents relational constraints similar to database query "where
clauses". Instances of QueryExp are returned by the static methods of the

Query

class.

It is possible, but not
recommended, to create custom queries by implementing this
interface. In that case, it is better to extend the

QueryEval

class than to implement the interface directly, so that
the

setMBeanServer(javax.management.MBeanServer)

method works correctly.

Represents relational constraints similar to database query "where
clauses". Instances of QueryExp are returned by the static methods of the

Query

class.

It is possible, but not
recommended, to create custom queries by implementing this
interface. In that case, it is better to extend the

QueryEval

class than to implement the interface directly, so that
the

setMBeanServer(javax.management.MBeanServer)

method works correctly.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

apply

​(

ObjectName

name)

Applies the QueryExp on an MBean.

void

setMBeanServer

​(

MBeanServer

s)

Sets the MBean server on which the query is to be performed.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

apply

​(

ObjectName

name)

Applies the QueryExp on an MBean.

void

setMBeanServer

​(

MBeanServer

s)

Sets the MBean server on which the query is to be performed.

---

#### Method Summary

Applies the QueryExp on an MBean.

Sets the MBean server on which the query is to be performed.

============ METHOD DETAIL ==========

- Method Detail

- apply

```java
boolean apply​(
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

Applies the QueryExp on an MBean.

**Parameters:** name

- The name of the MBean on which the QueryExp will be applied.
**Returns:** True if the query was successfully applied to the MBean, false otherwise
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
void setMBeanServer​(
MBeanServer
s)
```

Sets the MBean server on which the query is to be performed.

**Parameters:** s

- The MBean server on which the query is to be performed.

Method Detail

- apply

```java
boolean apply​(
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

Applies the QueryExp on an MBean.

**Parameters:** name

- The name of the MBean on which the QueryExp will be applied.
**Returns:** True if the query was successfully applied to the MBean, false otherwise
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
void setMBeanServer​(
MBeanServer
s)
```

Sets the MBean server on which the query is to be performed.

**Parameters:** s

- The MBean server on which the query is to be performed.

---

#### Method Detail

apply

```java
boolean apply​(
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

Applies the QueryExp on an MBean.

**Parameters:** name

- The name of the MBean on which the QueryExp will be applied.
**Returns:** True if the query was successfully applied to the MBean, false otherwise
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

boolean apply​(

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

Applies the QueryExp on an MBean.

setMBeanServer

```java
void setMBeanServer​(
MBeanServer
s)
```

Sets the MBean server on which the query is to be performed.

**Parameters:** s

- The MBean server on which the query is to be performed.

---

#### setMBeanServer

void setMBeanServer​(

MBeanServer

s)

Sets the MBean server on which the query is to be performed.

---

