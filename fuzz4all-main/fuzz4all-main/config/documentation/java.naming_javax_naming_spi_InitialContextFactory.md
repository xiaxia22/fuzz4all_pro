# Interface InitialContextFactory

**Source:** `java.naming\javax\naming\spi\InitialContextFactory.html`

### Class Description

```java
public interface
InitialContextFactory
```

This interface represents a factory that creates an initial context.

The JNDI framework allows for different initial context implementations
to be specified at runtime. The initial context is created using
an

initial context factory

.
An initial context factory must implement the InitialContextFactory
interface, which provides a method for creating instances of initial
context that implement the Context interface.
In addition, the factory class must be public and must have a public
constructor that accepts no arguments.

**Since:** 1.3
**See Also:** InitialContextFactoryBuilder

,

NamingManager.getInitialContext(java.util.Hashtable<?, ?>)

,

InitialContext

,

InitialDirContext

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Context
getInitialContext​(
Hashtable
<?,​?> environment)
throws
NamingException

Creates an Initial Context for beginning name resolution.
Special requirements of this context are supplied
using

environment

.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

**Parameters:**
- environment

- The possibly null environment
specifying information to be used in the creation
of the initial context.

**Returns:**
- A non-null initial context object that implements the Context
interface.

**Throws:**
- NamingException

- If cannot create an initial context.

---

### Additional Sections

#### Interface InitialContextFactory

```java
public interface
InitialContextFactory
```

This interface represents a factory that creates an initial context.

The JNDI framework allows for different initial context implementations
to be specified at runtime. The initial context is created using
an

initial context factory

.
An initial context factory must implement the InitialContextFactory
interface, which provides a method for creating instances of initial
context that implement the Context interface.
In addition, the factory class must be public and must have a public
constructor that accepts no arguments.

**Since:** 1.3
**See Also:** InitialContextFactoryBuilder

,

NamingManager.getInitialContext(java.util.Hashtable<?, ?>)

,

InitialContext

,

InitialDirContext

public interface

InitialContextFactory

This interface represents a factory that creates an initial context.

The JNDI framework allows for different initial context implementations
to be specified at runtime. The initial context is created using
an

initial context factory

.
An initial context factory must implement the InitialContextFactory
interface, which provides a method for creating instances of initial
context that implement the Context interface.
In addition, the factory class must be public and must have a public
constructor that accepts no arguments.

The JNDI framework allows for different initial context implementations
to be specified at runtime. The initial context is created using
an

initial context factory

.
An initial context factory must implement the InitialContextFactory
interface, which provides a method for creating instances of initial
context that implement the Context interface.
In addition, the factory class must be public and must have a public
constructor that accepts no arguments.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Context

getInitialContext

​(

Hashtable

<?,​?> environment)

Creates an Initial Context for beginning name resolution.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Context

getInitialContext

​(

Hashtable

<?,​?> environment)

Creates an Initial Context for beginning name resolution.

---

#### Method Summary

Creates an Initial Context for beginning name resolution.

============ METHOD DETAIL ==========

- Method Detail

- getInitialContext

```java
Context
getInitialContext​(
Hashtable
<?,​?> environment)
throws
NamingException
```

Creates an Initial Context for beginning name resolution.
Special requirements of this context are supplied
using

environment

.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

**Parameters:** environment

- The possibly null environment
specifying information to be used in the creation
of the initial context.
**Returns:** A non-null initial context object that implements the Context
interface.
**Throws:** NamingException

- If cannot create an initial context.

Method Detail

- getInitialContext

```java
Context
getInitialContext​(
Hashtable
<?,​?> environment)
throws
NamingException
```

Creates an Initial Context for beginning name resolution.
Special requirements of this context are supplied
using

environment

.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

**Parameters:** environment

- The possibly null environment
specifying information to be used in the creation
of the initial context.
**Returns:** A non-null initial context object that implements the Context
interface.
**Throws:** NamingException

- If cannot create an initial context.

---

#### Method Detail

getInitialContext

```java
Context
getInitialContext​(
Hashtable
<?,​?> environment)
throws
NamingException
```

Creates an Initial Context for beginning name resolution.
Special requirements of this context are supplied
using

environment

.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

**Parameters:** environment

- The possibly null environment
specifying information to be used in the creation
of the initial context.
**Returns:** A non-null initial context object that implements the Context
interface.
**Throws:** NamingException

- If cannot create an initial context.

---

#### getInitialContext

Context

getInitialContext​(

Hashtable

<?,​?> environment)
throws

NamingException

Creates an Initial Context for beginning name resolution.
Special requirements of this context are supplied
using

environment

.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

---

