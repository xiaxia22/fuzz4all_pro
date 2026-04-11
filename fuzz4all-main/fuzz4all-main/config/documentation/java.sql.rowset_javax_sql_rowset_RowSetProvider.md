# Class RowSetProvider

**Source:** `java.sql.rowset\javax\sql\rowset\RowSetProvider.html`

### Class Description

```java
public class
RowSetProvider

extends
Object
```

A factory API that enables applications to obtain a

RowSetFactory

implementation that can be used to create different
types of

RowSet

implementations.

Example:

```java
RowSetFactory aFactory = RowSetProvider.newFactory();
CachedRowSet crs = aFactory.createCachedRowSet();
...
RowSetFactory rsf = RowSetProvider.newFactory("com.sun.rowset.RowSetFactoryImpl", null);
WebRowSet wrs = rsf.createWebRowSet();
```

Tracing of this class may be enabled by setting the System property

javax.sql.rowset.RowSetFactory.debug

to any value but

false

.

**Since:** 1.7

---

### Field Details

*No entries found.*

### Constructor Details

#### protected RowSetProvider()

RowSetProvider constructor

---

### Method Details

#### public static
RowSetFactory
newFactory()
throws
SQLException

Creates a new instance of a

RowSetFactory

implementation. This method uses the following
look up order to determine
the

RowSetFactory

implementation class to load:

- The System property

javax.sql.rowset.RowSetFactory

. For example:

- -Djavax.sql.rowset.RowSetFactory=com.sun.rowset.RowSetFactoryImpl

The

ServiceLoader

API. The

ServiceLoader

API will look
for a class name in the file

META-INF/services/javax.sql.rowset.RowSetFactory

in jars available to the runtime. For example, to have the RowSetFactory
implementation

com.sun.rowset.RowSetFactoryImpl

loaded, the
entry in

META-INF/services/javax.sql.rowset.RowSetFactory

would be:

- com.sun.rowset.RowSetFactoryImpl

Platform default

RowSetFactory

instance.

Once an application has obtained a reference to a

RowSetFactory

,
it can use the factory to obtain RowSet instances.

**Returns:**
- New instance of a

RowSetFactory

**Throws:**
- SQLException

- if the default factory class cannot be loaded,
instantiated. The cause will be set to actual Exception

**See Also:**
- ServiceLoader

**Since:**
- 1.7

---

#### public static
RowSetFactory
newFactory​(
String
factoryClassName,

ClassLoader
cl)
throws
SQLException

Creates a new instance of a

RowSetFactory

from the
specified factory class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

RowSetFactory

it can use the factory to obtain RowSet instances.

**Parameters:**
- factoryClassName

- fully qualified factory class name that
provides an implementation of

javax.sql.rowset.RowSetFactory

.
- cl

-

ClassLoader

used to load the factory
class. If

null

current

Thread

's context
classLoader is used to load the factory class.

**Returns:**
- New instance of a

RowSetFactory

**Throws:**
- SQLException

- if

factoryClassName

is

null

, or the factory class cannot be loaded, instantiated.

**See Also:**
- newFactory()

**Since:**
- 1.7

---

### Additional Sections

#### Class RowSetProvider

java.lang.Object

- javax.sql.rowset.RowSetProvider

javax.sql.rowset.RowSetProvider

```java
public class
RowSetProvider

extends
Object
```

A factory API that enables applications to obtain a

RowSetFactory

implementation that can be used to create different
types of

RowSet

implementations.

Example:

```java
RowSetFactory aFactory = RowSetProvider.newFactory();
CachedRowSet crs = aFactory.createCachedRowSet();
...
RowSetFactory rsf = RowSetProvider.newFactory("com.sun.rowset.RowSetFactoryImpl", null);
WebRowSet wrs = rsf.createWebRowSet();
```

Tracing of this class may be enabled by setting the System property

javax.sql.rowset.RowSetFactory.debug

to any value but

false

.

**Since:** 1.7

public class

RowSetProvider

extends

Object

A factory API that enables applications to obtain a

RowSetFactory

implementation that can be used to create different
types of

RowSet

implementations.

Example:

```java
RowSetFactory aFactory = RowSetProvider.newFactory();
CachedRowSet crs = aFactory.createCachedRowSet();
...
RowSetFactory rsf = RowSetProvider.newFactory("com.sun.rowset.RowSetFactoryImpl", null);
WebRowSet wrs = rsf.createWebRowSet();
```

Tracing of this class may be enabled by setting the System property

javax.sql.rowset.RowSetFactory.debug

to any value but

false

.

Example:

RowSetFactory aFactory = RowSetProvider.newFactory();
CachedRowSet crs = aFactory.createCachedRowSet();
...
RowSetFactory rsf = RowSetProvider.newFactory("com.sun.rowset.RowSetFactoryImpl", null);
WebRowSet wrs = rsf.createWebRowSet();

Tracing of this class may be enabled by setting the System property

javax.sql.rowset.RowSetFactory.debug

to any value but

false

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

RowSetProvider

()

RowSetProvider constructor

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

RowSetFactory

newFactory

()

Creates a new instance of a

RowSetFactory

implementation.

static

RowSetFactory

newFactory

​(

String

factoryClassName,

ClassLoader

cl)

Creates a new instance of a

RowSetFactory

from the
specified factory class name.

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

Modifier

Constructor

Description

protected

RowSetProvider

()

RowSetProvider constructor

---

#### Constructor Summary

RowSetProvider constructor

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

RowSetFactory

newFactory

()

Creates a new instance of a

RowSetFactory

implementation.

static

RowSetFactory

newFactory

​(

String

factoryClassName,

ClassLoader

cl)

Creates a new instance of a

RowSetFactory

from the
specified factory class name.

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

Creates a new instance of a

RowSetFactory

implementation.

Creates a new instance of a

RowSetFactory

from the
specified factory class name.

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

- RowSetProvider

```java
protected RowSetProvider()
```

RowSetProvider constructor

============ METHOD DETAIL ==========

- Method Detail

- newFactory

```java
public static
RowSetFactory
newFactory()
throws
SQLException
```

Creates a new instance of a

RowSetFactory

implementation. This method uses the following
look up order to determine
the

RowSetFactory

implementation class to load:

- The System property

javax.sql.rowset.RowSetFactory

. For example:

- -Djavax.sql.rowset.RowSetFactory=com.sun.rowset.RowSetFactoryImpl

The

ServiceLoader

API. The

ServiceLoader

API will look
for a class name in the file

META-INF/services/javax.sql.rowset.RowSetFactory

in jars available to the runtime. For example, to have the RowSetFactory
implementation

com.sun.rowset.RowSetFactoryImpl

loaded, the
entry in

META-INF/services/javax.sql.rowset.RowSetFactory

would be:

- com.sun.rowset.RowSetFactoryImpl

Platform default

RowSetFactory

instance.

Once an application has obtained a reference to a

RowSetFactory

,
it can use the factory to obtain RowSet instances.

**Returns:** New instance of a

RowSetFactory
**Throws:** SQLException

- if the default factory class cannot be loaded,
instantiated. The cause will be set to actual Exception
**Since:** 1.7
**See Also:** ServiceLoader

- newFactory

```java
public static
RowSetFactory
newFactory​(
String
factoryClassName,

ClassLoader
cl)
throws
SQLException
```

Creates a new instance of a

RowSetFactory

from the
specified factory class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

RowSetFactory

it can use the factory to obtain RowSet instances.

**Parameters:** factoryClassName

- fully qualified factory class name that
provides an implementation of

javax.sql.rowset.RowSetFactory

.
**Parameters:** cl

-

ClassLoader

used to load the factory
class. If

null

current

Thread

's context
classLoader is used to load the factory class.
**Returns:** New instance of a

RowSetFactory
**Throws:** SQLException

- if

factoryClassName

is

null

, or the factory class cannot be loaded, instantiated.
**Since:** 1.7
**See Also:** newFactory()

Constructor Detail

- RowSetProvider

```java
protected RowSetProvider()
```

RowSetProvider constructor

---

#### Constructor Detail

RowSetProvider

```java
protected RowSetProvider()
```

RowSetProvider constructor

---

#### RowSetProvider

protected RowSetProvider()

RowSetProvider constructor

Method Detail

- newFactory

```java
public static
RowSetFactory
newFactory()
throws
SQLException
```

Creates a new instance of a

RowSetFactory

implementation. This method uses the following
look up order to determine
the

RowSetFactory

implementation class to load:

- The System property

javax.sql.rowset.RowSetFactory

. For example:

- -Djavax.sql.rowset.RowSetFactory=com.sun.rowset.RowSetFactoryImpl

The

ServiceLoader

API. The

ServiceLoader

API will look
for a class name in the file

META-INF/services/javax.sql.rowset.RowSetFactory

in jars available to the runtime. For example, to have the RowSetFactory
implementation

com.sun.rowset.RowSetFactoryImpl

loaded, the
entry in

META-INF/services/javax.sql.rowset.RowSetFactory

would be:

- com.sun.rowset.RowSetFactoryImpl

Platform default

RowSetFactory

instance.

Once an application has obtained a reference to a

RowSetFactory

,
it can use the factory to obtain RowSet instances.

**Returns:** New instance of a

RowSetFactory
**Throws:** SQLException

- if the default factory class cannot be loaded,
instantiated. The cause will be set to actual Exception
**Since:** 1.7
**See Also:** ServiceLoader

- newFactory

```java
public static
RowSetFactory
newFactory​(
String
factoryClassName,

ClassLoader
cl)
throws
SQLException
```

Creates a new instance of a

RowSetFactory

from the
specified factory class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

RowSetFactory

it can use the factory to obtain RowSet instances.

**Parameters:** factoryClassName

- fully qualified factory class name that
provides an implementation of

javax.sql.rowset.RowSetFactory

.
**Parameters:** cl

-

ClassLoader

used to load the factory
class. If

null

current

Thread

's context
classLoader is used to load the factory class.
**Returns:** New instance of a

RowSetFactory
**Throws:** SQLException

- if

factoryClassName

is

null

, or the factory class cannot be loaded, instantiated.
**Since:** 1.7
**See Also:** newFactory()

---

#### Method Detail

newFactory

```java
public static
RowSetFactory
newFactory()
throws
SQLException
```

Creates a new instance of a

RowSetFactory

implementation. This method uses the following
look up order to determine
the

RowSetFactory

implementation class to load:

- The System property

javax.sql.rowset.RowSetFactory

. For example:

- -Djavax.sql.rowset.RowSetFactory=com.sun.rowset.RowSetFactoryImpl

The

ServiceLoader

API. The

ServiceLoader

API will look
for a class name in the file

META-INF/services/javax.sql.rowset.RowSetFactory

in jars available to the runtime. For example, to have the RowSetFactory
implementation

com.sun.rowset.RowSetFactoryImpl

loaded, the
entry in

META-INF/services/javax.sql.rowset.RowSetFactory

would be:

- com.sun.rowset.RowSetFactoryImpl

Platform default

RowSetFactory

instance.

Once an application has obtained a reference to a

RowSetFactory

,
it can use the factory to obtain RowSet instances.

**Returns:** New instance of a

RowSetFactory
**Throws:** SQLException

- if the default factory class cannot be loaded,
instantiated. The cause will be set to actual Exception
**Since:** 1.7
**See Also:** ServiceLoader

---

#### newFactory

public static

RowSetFactory

newFactory()
throws

SQLException

Creates a new instance of a

RowSetFactory

implementation. This method uses the following
look up order to determine
the

RowSetFactory

implementation class to load:

- The System property

javax.sql.rowset.RowSetFactory

. For example:

- -Djavax.sql.rowset.RowSetFactory=com.sun.rowset.RowSetFactoryImpl

The

ServiceLoader

API. The

ServiceLoader

API will look
for a class name in the file

META-INF/services/javax.sql.rowset.RowSetFactory

in jars available to the runtime. For example, to have the RowSetFactory
implementation

com.sun.rowset.RowSetFactoryImpl

loaded, the
entry in

META-INF/services/javax.sql.rowset.RowSetFactory

would be:

- com.sun.rowset.RowSetFactoryImpl

Platform default

RowSetFactory

instance.

Once an application has obtained a reference to a

RowSetFactory

,
it can use the factory to obtain RowSet instances.

Creates a new instance of a

RowSetFactory

implementation. This method uses the following
look up order to determine
the

RowSetFactory

implementation class to load:

The System property

javax.sql.rowset.RowSetFactory

. For example:

- -Djavax.sql.rowset.RowSetFactory=com.sun.rowset.RowSetFactoryImpl

The

ServiceLoader

API. The

ServiceLoader

API will look
for a class name in the file

META-INF/services/javax.sql.rowset.RowSetFactory

in jars available to the runtime. For example, to have the RowSetFactory
implementation

com.sun.rowset.RowSetFactoryImpl

loaded, the
entry in

META-INF/services/javax.sql.rowset.RowSetFactory

would be:

- com.sun.rowset.RowSetFactoryImpl

Platform default

RowSetFactory

instance.

-Djavax.sql.rowset.RowSetFactory=com.sun.rowset.RowSetFactoryImpl

com.sun.rowset.RowSetFactoryImpl

Once an application has obtained a reference to a

RowSetFactory

,
it can use the factory to obtain RowSet instances.

newFactory

```java
public static
RowSetFactory
newFactory​(
String
factoryClassName,

ClassLoader
cl)
throws
SQLException
```

Creates a new instance of a

RowSetFactory

from the
specified factory class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

RowSetFactory

it can use the factory to obtain RowSet instances.

**Parameters:** factoryClassName

- fully qualified factory class name that
provides an implementation of

javax.sql.rowset.RowSetFactory

.
**Parameters:** cl

-

ClassLoader

used to load the factory
class. If

null

current

Thread

's context
classLoader is used to load the factory class.
**Returns:** New instance of a

RowSetFactory
**Throws:** SQLException

- if

factoryClassName

is

null

, or the factory class cannot be loaded, instantiated.
**Since:** 1.7
**See Also:** newFactory()

---

#### newFactory

public static

RowSetFactory

newFactory​(

String

factoryClassName,

ClassLoader

cl)
throws

SQLException

Creates a new instance of a

RowSetFactory

from the
specified factory class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

RowSetFactory

it can use the factory to obtain RowSet instances.

Creates a new instance of a

RowSetFactory

from the
specified factory class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

RowSetFactory

it can use the factory to obtain RowSet instances.

---

