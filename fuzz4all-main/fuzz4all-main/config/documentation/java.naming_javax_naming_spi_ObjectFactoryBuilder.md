# Interface ObjectFactoryBuilder

**Source:** `java.naming\javax\naming\spi\ObjectFactoryBuilder.html`

### Class Description

```java
public interface
ObjectFactoryBuilder
```

This interface represents a builder that creates object factories.

The JNDI framework allows for object implementations to
be loaded in dynamically via

object factories

.
For example, when looking up a printer bound in the name space,
if the print service binds printer names to References, the printer
Reference could be used to create a printer object, so that
the caller of lookup can directly operate on the printer object
after the lookup. An ObjectFactory is responsible for creating
objects of a specific type. JNDI uses a default policy for using
and loading object factories. You can override this default policy
by calling

NamingManager.setObjectFactoryBuilder()

with an ObjectFactoryBuilder,
which contains the program-defined way of creating/loading
object factories.
Any

ObjectFactoryBuilder

implementation must implement this
interface that for creating object factories.

**Since:** 1.3
**See Also:** ObjectFactory

,

NamingManager.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

,

NamingManager.setObjectFactoryBuilder(javax.naming.spi.ObjectFactoryBuilder)

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ObjectFactory
createObjectFactory​(
Object
obj,

Hashtable
<?,​?> environment)
throws
NamingException

Creates a new object factory using the environment supplied.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

**Parameters:**
- obj

- The possibly null object for which to create a factory.
- environment

- Environment to use when creating the factory.
Can be null.

**Returns:**
- A non-null new instance of an ObjectFactory.

**Throws:**
- NamingException

- If an object factory cannot be created.

---

### Additional Sections

#### Interface ObjectFactoryBuilder

```java
public interface
ObjectFactoryBuilder
```

This interface represents a builder that creates object factories.

The JNDI framework allows for object implementations to
be loaded in dynamically via

object factories

.
For example, when looking up a printer bound in the name space,
if the print service binds printer names to References, the printer
Reference could be used to create a printer object, so that
the caller of lookup can directly operate on the printer object
after the lookup. An ObjectFactory is responsible for creating
objects of a specific type. JNDI uses a default policy for using
and loading object factories. You can override this default policy
by calling

NamingManager.setObjectFactoryBuilder()

with an ObjectFactoryBuilder,
which contains the program-defined way of creating/loading
object factories.
Any

ObjectFactoryBuilder

implementation must implement this
interface that for creating object factories.

**Since:** 1.3
**See Also:** ObjectFactory

,

NamingManager.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

,

NamingManager.setObjectFactoryBuilder(javax.naming.spi.ObjectFactoryBuilder)

public interface

ObjectFactoryBuilder

This interface represents a builder that creates object factories.

The JNDI framework allows for object implementations to
be loaded in dynamically via

object factories

.
For example, when looking up a printer bound in the name space,
if the print service binds printer names to References, the printer
Reference could be used to create a printer object, so that
the caller of lookup can directly operate on the printer object
after the lookup. An ObjectFactory is responsible for creating
objects of a specific type. JNDI uses a default policy for using
and loading object factories. You can override this default policy
by calling

NamingManager.setObjectFactoryBuilder()

with an ObjectFactoryBuilder,
which contains the program-defined way of creating/loading
object factories.
Any

ObjectFactoryBuilder

implementation must implement this
interface that for creating object factories.

The JNDI framework allows for object implementations to
be loaded in dynamically via

object factories

.
For example, when looking up a printer bound in the name space,
if the print service binds printer names to References, the printer
Reference could be used to create a printer object, so that
the caller of lookup can directly operate on the printer object
after the lookup. An ObjectFactory is responsible for creating
objects of a specific type. JNDI uses a default policy for using
and loading object factories. You can override this default policy
by calling

NamingManager.setObjectFactoryBuilder()

with an ObjectFactoryBuilder,
which contains the program-defined way of creating/loading
object factories.
Any

ObjectFactoryBuilder

implementation must implement this
interface that for creating object factories.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ObjectFactory

createObjectFactory

​(

Object

obj,

Hashtable

<?,​?> environment)

Creates a new object factory using the environment supplied.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ObjectFactory

createObjectFactory

​(

Object

obj,

Hashtable

<?,​?> environment)

Creates a new object factory using the environment supplied.

---

#### Method Summary

Creates a new object factory using the environment supplied.

============ METHOD DETAIL ==========

- Method Detail

- createObjectFactory

```java
ObjectFactory
createObjectFactory​(
Object
obj,

Hashtable
<?,​?> environment)
throws
NamingException
```

Creates a new object factory using the environment supplied.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

**Parameters:** obj

- The possibly null object for which to create a factory.
**Parameters:** environment

- Environment to use when creating the factory.
Can be null.
**Returns:** A non-null new instance of an ObjectFactory.
**Throws:** NamingException

- If an object factory cannot be created.

Method Detail

- createObjectFactory

```java
ObjectFactory
createObjectFactory​(
Object
obj,

Hashtable
<?,​?> environment)
throws
NamingException
```

Creates a new object factory using the environment supplied.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

**Parameters:** obj

- The possibly null object for which to create a factory.
**Parameters:** environment

- Environment to use when creating the factory.
Can be null.
**Returns:** A non-null new instance of an ObjectFactory.
**Throws:** NamingException

- If an object factory cannot be created.

---

#### Method Detail

createObjectFactory

```java
ObjectFactory
createObjectFactory​(
Object
obj,

Hashtable
<?,​?> environment)
throws
NamingException
```

Creates a new object factory using the environment supplied.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

**Parameters:** obj

- The possibly null object for which to create a factory.
**Parameters:** environment

- Environment to use when creating the factory.
Can be null.
**Returns:** A non-null new instance of an ObjectFactory.
**Throws:** NamingException

- If an object factory cannot be created.

---

#### createObjectFactory

ObjectFactory

createObjectFactory​(

Object

obj,

Hashtable

<?,​?> environment)
throws

NamingException

Creates a new object factory using the environment supplied.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

The environment parameter is owned by the caller.
The implementation will not modify the object or keep a reference
to it, although it may keep a reference to a clone or copy.

---

