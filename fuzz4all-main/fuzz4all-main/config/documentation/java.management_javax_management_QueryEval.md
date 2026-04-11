# Class QueryEval

**Source:** `java.management\javax\management\QueryEval.html`

### Class Description

```java
public abstract class
QueryEval

extends
Object

implements
Serializable
```

Allows a query to be performed in the context of a specific MBean server.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public QueryEval()

*No description found.*

---

### Method Details

#### public void setMBeanServer​(
MBeanServer
s)

Sets the MBean server on which the query is to be performed.
The setting is valid for the thread performing the set.
It is copied to any threads created by that thread at the moment
of their creation.

For historical reasons, this method is not static, but its
behavior does not depend on the instance on which it is
called.

**Parameters:**
- s

- The MBean server on which the query is to be performed.

**See Also:**
- getMBeanServer()

---

#### public static
MBeanServer
getMBeanServer()

Return the MBean server that was most recently given to the

setMBeanServer

method by this thread.
If this thread never called that method, the result is the
value its parent thread would have obtained from

getMBeanServer

at the moment of the creation of
this thread, or null if there is no parent thread.

**Returns:**
- the MBean server.

**See Also:**
- setMBeanServer(javax.management.MBeanServer)

---

### Additional Sections

#### Class QueryEval

java.lang.Object

- javax.management.QueryEval

javax.management.QueryEval

**All Implemented Interfaces:** Serializable

```java
public abstract class
QueryEval

extends
Object

implements
Serializable
```

Allows a query to be performed in the context of a specific MBean server.

**Since:** 1.5
**See Also:** Serialized Form

public abstract class

QueryEval

extends

Object

implements

Serializable

Allows a query to be performed in the context of a specific MBean server.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

QueryEval

()

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

MBeanServer

getMBeanServer

()

Return the MBean server that was most recently given to the

setMBeanServer

method by this thread.

void

setMBeanServer

​(

MBeanServer

s)

Sets the MBean server on which the query is to be performed.

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

toString

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

QueryEval

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

MBeanServer

getMBeanServer

()

Return the MBean server that was most recently given to the

setMBeanServer

method by this thread.

void

setMBeanServer

​(

MBeanServer

s)

Sets the MBean server on which the query is to be performed.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Return the MBean server that was most recently given to the

setMBeanServer

method by this thread.

Sets the MBean server on which the query is to be performed.

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

toString

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

- QueryEval

```java
public QueryEval()
```

============ METHOD DETAIL ==========

- Method Detail

- setMBeanServer

```java
public void setMBeanServer​(
MBeanServer
s)
```

Sets the MBean server on which the query is to be performed.
The setting is valid for the thread performing the set.
It is copied to any threads created by that thread at the moment
of their creation.

For historical reasons, this method is not static, but its
behavior does not depend on the instance on which it is
called.

**Parameters:** s

- The MBean server on which the query is to be performed.
**See Also:** getMBeanServer()

- getMBeanServer

```java
public static
MBeanServer
getMBeanServer()
```

Return the MBean server that was most recently given to the

setMBeanServer

method by this thread.
If this thread never called that method, the result is the
value its parent thread would have obtained from

getMBeanServer

at the moment of the creation of
this thread, or null if there is no parent thread.

**Returns:** the MBean server.
**See Also:** setMBeanServer(javax.management.MBeanServer)

Constructor Detail

- QueryEval

```java
public QueryEval()
```

---

#### Constructor Detail

QueryEval

```java
public QueryEval()
```

---

#### QueryEval

public QueryEval()

Method Detail

- setMBeanServer

```java
public void setMBeanServer​(
MBeanServer
s)
```

Sets the MBean server on which the query is to be performed.
The setting is valid for the thread performing the set.
It is copied to any threads created by that thread at the moment
of their creation.

For historical reasons, this method is not static, but its
behavior does not depend on the instance on which it is
called.

**Parameters:** s

- The MBean server on which the query is to be performed.
**See Also:** getMBeanServer()

- getMBeanServer

```java
public static
MBeanServer
getMBeanServer()
```

Return the MBean server that was most recently given to the

setMBeanServer

method by this thread.
If this thread never called that method, the result is the
value its parent thread would have obtained from

getMBeanServer

at the moment of the creation of
this thread, or null if there is no parent thread.

**Returns:** the MBean server.
**See Also:** setMBeanServer(javax.management.MBeanServer)

---

#### Method Detail

setMBeanServer

```java
public void setMBeanServer​(
MBeanServer
s)
```

Sets the MBean server on which the query is to be performed.
The setting is valid for the thread performing the set.
It is copied to any threads created by that thread at the moment
of their creation.

For historical reasons, this method is not static, but its
behavior does not depend on the instance on which it is
called.

**Parameters:** s

- The MBean server on which the query is to be performed.
**See Also:** getMBeanServer()

---

#### setMBeanServer

public void setMBeanServer​(

MBeanServer

s)

Sets the MBean server on which the query is to be performed.
The setting is valid for the thread performing the set.
It is copied to any threads created by that thread at the moment
of their creation.

For historical reasons, this method is not static, but its
behavior does not depend on the instance on which it is
called.

Sets the MBean server on which the query is to be performed.
The setting is valid for the thread performing the set.
It is copied to any threads created by that thread at the moment
of their creation.

For historical reasons, this method is not static, but its
behavior does not depend on the instance on which it is
called.

getMBeanServer

```java
public static
MBeanServer
getMBeanServer()
```

Return the MBean server that was most recently given to the

setMBeanServer

method by this thread.
If this thread never called that method, the result is the
value its parent thread would have obtained from

getMBeanServer

at the moment of the creation of
this thread, or null if there is no parent thread.

**Returns:** the MBean server.
**See Also:** setMBeanServer(javax.management.MBeanServer)

---

#### getMBeanServer

public static

MBeanServer

getMBeanServer()

Return the MBean server that was most recently given to the

setMBeanServer

method by this thread.
If this thread never called that method, the result is the
value its parent thread would have obtained from

getMBeanServer

at the moment of the creation of
this thread, or null if there is no parent thread.

---

