# Interface InitialContextFactoryBuilder

**Source:** `java.naming\javax\naming\spi\InitialContextFactoryBuilder.html`

### Class Description

```java
public interface
InitialContextFactoryBuilder
```

This interface represents a builder that creates initial context factories.

The JNDI framework allows for different initial context implementations
to be specified at runtime. An initial context is created using
an initial context factory. A program can install its own builder
that creates initial context factories, thereby overriding the
default policies used by the framework, by calling
NamingManager.setInitialContextFactoryBuilder().
The InitialContextFactoryBuilder interface must be implemented by
such a builder.

**Since:** 1.3
**See Also:** InitialContextFactory

,

NamingManager.getInitialContext(java.util.Hashtable<?, ?>)

,

NamingManager.setInitialContextFactoryBuilder(javax.naming.spi.InitialContextFactoryBuilder)

,

NamingManager.hasInitialContextFactoryBuilder()

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

#### InitialContextFactory
createInitialContextFactory​(
Hashtable
<?,​?> environment)
throws
NamingException

Creates an initial context factory using the specified
environment.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

**Parameters:**
- environment

- Environment used in creating an initial
context implementation. Can be null.

**Returns:**
- A non-null initial context factory.

**Throws:**
- NamingException

- If an initial context factory could not be created.

---

### Additional Sections

#### Interface InitialContextFactoryBuilder

```java
public interface
InitialContextFactoryBuilder
```

This interface represents a builder that creates initial context factories.

The JNDI framework allows for different initial context implementations
to be specified at runtime. An initial context is created using
an initial context factory. A program can install its own builder
that creates initial context factories, thereby overriding the
default policies used by the framework, by calling
NamingManager.setInitialContextFactoryBuilder().
The InitialContextFactoryBuilder interface must be implemented by
such a builder.

**Since:** 1.3
**See Also:** InitialContextFactory

,

NamingManager.getInitialContext(java.util.Hashtable<?, ?>)

,

NamingManager.setInitialContextFactoryBuilder(javax.naming.spi.InitialContextFactoryBuilder)

,

NamingManager.hasInitialContextFactoryBuilder()

,

InitialContext

,

InitialDirContext

public interface

InitialContextFactoryBuilder

This interface represents a builder that creates initial context factories.

The JNDI framework allows for different initial context implementations
to be specified at runtime. An initial context is created using
an initial context factory. A program can install its own builder
that creates initial context factories, thereby overriding the
default policies used by the framework, by calling
NamingManager.setInitialContextFactoryBuilder().
The InitialContextFactoryBuilder interface must be implemented by
such a builder.

The JNDI framework allows for different initial context implementations
to be specified at runtime. An initial context is created using
an initial context factory. A program can install its own builder
that creates initial context factories, thereby overriding the
default policies used by the framework, by calling
NamingManager.setInitialContextFactoryBuilder().
The InitialContextFactoryBuilder interface must be implemented by
such a builder.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

InitialContextFactory

createInitialContextFactory

​(

Hashtable

<?,​?> environment)

Creates an initial context factory using the specified
environment.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

InitialContextFactory

createInitialContextFactory

​(

Hashtable

<?,​?> environment)

Creates an initial context factory using the specified
environment.

---

#### Method Summary

Creates an initial context factory using the specified
environment.

============ METHOD DETAIL ==========

- Method Detail

- createInitialContextFactory

```java
InitialContextFactory
createInitialContextFactory​(
Hashtable
<?,​?> environment)
throws
NamingException
```

Creates an initial context factory using the specified
environment.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

**Parameters:** environment

- Environment used in creating an initial
context implementation. Can be null.
**Returns:** A non-null initial context factory.
**Throws:** NamingException

- If an initial context factory could not be created.

Method Detail

- createInitialContextFactory

```java
InitialContextFactory
createInitialContextFactory​(
Hashtable
<?,​?> environment)
throws
NamingException
```

Creates an initial context factory using the specified
environment.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

**Parameters:** environment

- Environment used in creating an initial
context implementation. Can be null.
**Returns:** A non-null initial context factory.
**Throws:** NamingException

- If an initial context factory could not be created.

---

#### Method Detail

createInitialContextFactory

```java
InitialContextFactory
createInitialContextFactory​(
Hashtable
<?,​?> environment)
throws
NamingException
```

Creates an initial context factory using the specified
environment.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

**Parameters:** environment

- Environment used in creating an initial
context implementation. Can be null.
**Returns:** A non-null initial context factory.
**Throws:** NamingException

- If an initial context factory could not be created.

---

#### createInitialContextFactory

InitialContextFactory

createInitialContextFactory​(

Hashtable

<?,​?> environment)
throws

NamingException

Creates an initial context factory using the specified
environment.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

---

