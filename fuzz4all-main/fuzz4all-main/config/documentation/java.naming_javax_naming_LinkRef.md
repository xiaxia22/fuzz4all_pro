# Class LinkRef

**Source:** `java.naming\javax\naming\LinkRef.html`

### Class Description

```java
public class
LinkRef

extends
Reference
```

This class represents a Reference whose contents is a name, called the link name,
that is bound to an atomic name in a context.

The name is a URL, or a name to be resolved relative to the initial
context, or if the first character of the name is ".", the name
is relative to the context in which the link is bound.

Normal resolution of names in context operations always follow links.
Resolution of the link name itself may cause resolution to pass through
other links. This gives rise to the possibility of a cycle of links whose
resolution could not terminate normally. As a simple means to avoid such
non-terminating resolutions, service providers may define limits on the
number of links that may be involved in any single operation invoked
by the caller.

A LinkRef contains a single StringRefAddr, whose type is "LinkAddress",
and whose contents is the link name. The class name field of the
Reference is that of this (LinkRef) class.

LinkRef is bound to a name using the normal Context.bind()/rebind(), and
DirContext.bind()/rebind(). Context.lookupLink() is used to retrieve the link
itself if the terminal atomic name is bound to a link.

Many naming systems support a native notion of link that may be used
within the naming system itself. JNDI does not specify whether
there is any relationship between such native links and JNDI links.

A LinkRef instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a LinkRef instance concurrently should
synchronize amongst themselves and provide the necessary locking.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public LinkRef​(
Name
linkName)

Constructs a LinkRef for a name.

**Parameters:**
- linkName

- The non-null name for which to create this link.

---

#### public LinkRef​(
String
linkName)

Constructs a LinkRef for a string name.

**Parameters:**
- linkName

- The non-null name for which to create this link.

---

### Method Details

#### public
String
getLinkName()
throws
NamingException

Retrieves the name of this link.

**Returns:**
- The non-null name of this link.

**Throws:**
- MalformedLinkException

- If a link name could not be extracted
- NamingException

- If a naming exception was encountered.

---

### Additional Sections

#### Class LinkRef

java.lang.Object

- javax.naming.Reference
- - javax.naming.LinkRef

javax.naming.Reference

- javax.naming.LinkRef

javax.naming.LinkRef

**All Implemented Interfaces:** Serializable

,

Cloneable

```java
public class
LinkRef

extends
Reference
```

This class represents a Reference whose contents is a name, called the link name,
that is bound to an atomic name in a context.

The name is a URL, or a name to be resolved relative to the initial
context, or if the first character of the name is ".", the name
is relative to the context in which the link is bound.

Normal resolution of names in context operations always follow links.
Resolution of the link name itself may cause resolution to pass through
other links. This gives rise to the possibility of a cycle of links whose
resolution could not terminate normally. As a simple means to avoid such
non-terminating resolutions, service providers may define limits on the
number of links that may be involved in any single operation invoked
by the caller.

A LinkRef contains a single StringRefAddr, whose type is "LinkAddress",
and whose contents is the link name. The class name field of the
Reference is that of this (LinkRef) class.

LinkRef is bound to a name using the normal Context.bind()/rebind(), and
DirContext.bind()/rebind(). Context.lookupLink() is used to retrieve the link
itself if the terminal atomic name is bound to a link.

Many naming systems support a native notion of link that may be used
within the naming system itself. JNDI does not specify whether
there is any relationship between such native links and JNDI links.

A LinkRef instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a LinkRef instance concurrently should
synchronize amongst themselves and provide the necessary locking.

**Since:** 1.3
**See Also:** LinkException

,

LinkLoopException

,

MalformedLinkException

,

Context.lookupLink(javax.naming.Name)

,

Serialized Form

public class

LinkRef

extends

Reference

This class represents a Reference whose contents is a name, called the link name,
that is bound to an atomic name in a context.

The name is a URL, or a name to be resolved relative to the initial
context, or if the first character of the name is ".", the name
is relative to the context in which the link is bound.

Normal resolution of names in context operations always follow links.
Resolution of the link name itself may cause resolution to pass through
other links. This gives rise to the possibility of a cycle of links whose
resolution could not terminate normally. As a simple means to avoid such
non-terminating resolutions, service providers may define limits on the
number of links that may be involved in any single operation invoked
by the caller.

A LinkRef contains a single StringRefAddr, whose type is "LinkAddress",
and whose contents is the link name. The class name field of the
Reference is that of this (LinkRef) class.

LinkRef is bound to a name using the normal Context.bind()/rebind(), and
DirContext.bind()/rebind(). Context.lookupLink() is used to retrieve the link
itself if the terminal atomic name is bound to a link.

Many naming systems support a native notion of link that may be used
within the naming system itself. JNDI does not specify whether
there is any relationship between such native links and JNDI links.

A LinkRef instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a LinkRef instance concurrently should
synchronize amongst themselves and provide the necessary locking.

The name is a URL, or a name to be resolved relative to the initial
context, or if the first character of the name is ".", the name
is relative to the context in which the link is bound.

Normal resolution of names in context operations always follow links.
Resolution of the link name itself may cause resolution to pass through
other links. This gives rise to the possibility of a cycle of links whose
resolution could not terminate normally. As a simple means to avoid such
non-terminating resolutions, service providers may define limits on the
number of links that may be involved in any single operation invoked
by the caller.

A LinkRef contains a single StringRefAddr, whose type is "LinkAddress",
and whose contents is the link name. The class name field of the
Reference is that of this (LinkRef) class.

LinkRef is bound to a name using the normal Context.bind()/rebind(), and
DirContext.bind()/rebind(). Context.lookupLink() is used to retrieve the link
itself if the terminal atomic name is bound to a link.

Many naming systems support a native notion of link that may be used
within the naming system itself. JNDI does not specify whether
there is any relationship between such native links and JNDI links.

A LinkRef instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a LinkRef instance concurrently should
synchronize amongst themselves and provide the necessary locking.

Normal resolution of names in context operations always follow links.
Resolution of the link name itself may cause resolution to pass through
other links. This gives rise to the possibility of a cycle of links whose
resolution could not terminate normally. As a simple means to avoid such
non-terminating resolutions, service providers may define limits on the
number of links that may be involved in any single operation invoked
by the caller.

A LinkRef contains a single StringRefAddr, whose type is "LinkAddress",
and whose contents is the link name. The class name field of the
Reference is that of this (LinkRef) class.

LinkRef is bound to a name using the normal Context.bind()/rebind(), and
DirContext.bind()/rebind(). Context.lookupLink() is used to retrieve the link
itself if the terminal atomic name is bound to a link.

Many naming systems support a native notion of link that may be used
within the naming system itself. JNDI does not specify whether
there is any relationship between such native links and JNDI links.

A LinkRef instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a LinkRef instance concurrently should
synchronize amongst themselves and provide the necessary locking.

A LinkRef contains a single StringRefAddr, whose type is "LinkAddress",
and whose contents is the link name. The class name field of the
Reference is that of this (LinkRef) class.

LinkRef is bound to a name using the normal Context.bind()/rebind(), and
DirContext.bind()/rebind(). Context.lookupLink() is used to retrieve the link
itself if the terminal atomic name is bound to a link.

Many naming systems support a native notion of link that may be used
within the naming system itself. JNDI does not specify whether
there is any relationship between such native links and JNDI links.

A LinkRef instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a LinkRef instance concurrently should
synchronize amongst themselves and provide the necessary locking.

LinkRef is bound to a name using the normal Context.bind()/rebind(), and
DirContext.bind()/rebind(). Context.lookupLink() is used to retrieve the link
itself if the terminal atomic name is bound to a link.

Many naming systems support a native notion of link that may be used
within the naming system itself. JNDI does not specify whether
there is any relationship between such native links and JNDI links.

A LinkRef instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a LinkRef instance concurrently should
synchronize amongst themselves and provide the necessary locking.

Many naming systems support a native notion of link that may be used
within the naming system itself. JNDI does not specify whether
there is any relationship between such native links and JNDI links.

A LinkRef instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a LinkRef instance concurrently should
synchronize amongst themselves and provide the necessary locking.

A LinkRef instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a LinkRef instance concurrently should
synchronize amongst themselves and provide the necessary locking.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.naming.

Reference

addrs

,

classFactory

,

classFactoryLocation

,

className

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LinkRef

​(

String

linkName)

Constructs a LinkRef for a string name.

LinkRef

​(

Name

linkName)

Constructs a LinkRef for a name.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getLinkName

()

Retrieves the name of this link.

- Methods declared in class javax.naming.

Reference

add

,

add

,

clear

,

clone

,

equals

,

get

,

get

,

getAll

,

getClassName

,

getFactoryClassLocation

,

getFactoryClassName

,

hashCode

,

remove

,

size

,

toString

- Methods declared in class java.lang.

Object

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

Reference

addrs

,

classFactory

,

classFactoryLocation

,

className

---

#### Field Summary

Fields declared in class javax.naming.

Reference

addrs

,

classFactory

,

classFactoryLocation

,

className

---

#### Fields declared in class javax.naming. Reference

Constructor Summary

Constructors

Constructor

Description

LinkRef

​(

String

linkName)

Constructs a LinkRef for a string name.

LinkRef

​(

Name

linkName)

Constructs a LinkRef for a name.

---

#### Constructor Summary

Constructs a LinkRef for a string name.

Constructs a LinkRef for a name.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getLinkName

()

Retrieves the name of this link.

- Methods declared in class javax.naming.

Reference

add

,

add

,

clear

,

clone

,

equals

,

get

,

get

,

getAll

,

getClassName

,

getFactoryClassLocation

,

getFactoryClassName

,

hashCode

,

remove

,

size

,

toString

- Methods declared in class java.lang.

Object

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

Retrieves the name of this link.

Methods declared in class javax.naming.

Reference

add

,

add

,

clear

,

clone

,

equals

,

get

,

get

,

getAll

,

getClassName

,

getFactoryClassLocation

,

getFactoryClassName

,

hashCode

,

remove

,

size

,

toString

---

#### Methods declared in class javax.naming. Reference

Methods declared in class java.lang.

Object

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

- LinkRef

```java
public LinkRef​(
Name
linkName)
```

Constructs a LinkRef for a name.

**Parameters:** linkName

- The non-null name for which to create this link.

- LinkRef

```java
public LinkRef​(
String
linkName)
```

Constructs a LinkRef for a string name.

**Parameters:** linkName

- The non-null name for which to create this link.

============ METHOD DETAIL ==========

- Method Detail

- getLinkName

```java
public
String
getLinkName()
throws
NamingException
```

Retrieves the name of this link.

**Returns:** The non-null name of this link.
**Throws:** MalformedLinkException

- If a link name could not be extracted
**Throws:** NamingException

- If a naming exception was encountered.

Constructor Detail

- LinkRef

```java
public LinkRef​(
Name
linkName)
```

Constructs a LinkRef for a name.

**Parameters:** linkName

- The non-null name for which to create this link.

- LinkRef

```java
public LinkRef​(
String
linkName)
```

Constructs a LinkRef for a string name.

**Parameters:** linkName

- The non-null name for which to create this link.

---

#### Constructor Detail

LinkRef

```java
public LinkRef​(
Name
linkName)
```

Constructs a LinkRef for a name.

**Parameters:** linkName

- The non-null name for which to create this link.

---

#### LinkRef

public LinkRef​(

Name

linkName)

Constructs a LinkRef for a name.

LinkRef

```java
public LinkRef​(
String
linkName)
```

Constructs a LinkRef for a string name.

**Parameters:** linkName

- The non-null name for which to create this link.

---

#### LinkRef

public LinkRef​(

String

linkName)

Constructs a LinkRef for a string name.

Method Detail

- getLinkName

```java
public
String
getLinkName()
throws
NamingException
```

Retrieves the name of this link.

**Returns:** The non-null name of this link.
**Throws:** MalformedLinkException

- If a link name could not be extracted
**Throws:** NamingException

- If a naming exception was encountered.

---

#### Method Detail

getLinkName

```java
public
String
getLinkName()
throws
NamingException
```

Retrieves the name of this link.

**Returns:** The non-null name of this link.
**Throws:** MalformedLinkException

- If a link name could not be extracted
**Throws:** NamingException

- If a naming exception was encountered.

---

#### getLinkName

public

String

getLinkName()
throws

NamingException

Retrieves the name of this link.

---

