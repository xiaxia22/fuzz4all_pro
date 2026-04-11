# Class DefaultLoaderRepository

**Source:** `java.management\javax\management\loading\DefaultLoaderRepository.html`

### Class Description

```java
@Deprecated

public class
DefaultLoaderRepository

extends
Object
```

Keeps the list of Class Loaders registered in the MBean Server.
It provides the necessary methods to load classes using the registered
Class Loaders.

This deprecated class is maintained for compatibility. In
previous versions of JMX, there was one

DefaultLoaderRepository

shared by all MBean servers.
As of JMX 1.2, that functionality is approximated by using

MBeanServerFactory.findMBeanServer(java.lang.String)

to find all known MBean
servers, and consulting the

ClassLoaderRepository

of each
one. It is strongly recommended that code referencing

DefaultLoaderRepository

be rewritten.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

#### public DefaultLoaderRepository()

*No description found.*

---

### Method Details

#### public static
Class
<?> loadClass​(
String
className)
throws
ClassNotFoundException

Go through the list of class loaders and try to load the requested
class.
The method will stop as soon as the class is found. If the class
is not found the method will throw a

ClassNotFoundException

exception.

**Parameters:**
- className

- The name of the class to be loaded.

**Returns:**
- the loaded class.

**Throws:**
- ClassNotFoundException

- The specified class could not be
found.

---

#### public static
Class
<?> loadClassWithout​(
ClassLoader
loader,

String
className)
throws
ClassNotFoundException

Go through the list of class loaders but exclude the given
class loader, then try to load
the requested class.
The method will stop as soon as the class is found. If the class
is not found the method will throw a

ClassNotFoundException

exception.

**Parameters:**
- className

- The name of the class to be loaded.
- loader

- The class loader to be excluded.

**Returns:**
- the loaded class.

**Throws:**
- ClassNotFoundException

- The specified class could not be
found.

---

### Additional Sections

#### Class DefaultLoaderRepository

java.lang.Object

- javax.management.loading.DefaultLoaderRepository

javax.management.loading.DefaultLoaderRepository

```java
@Deprecated

public class
DefaultLoaderRepository

extends
Object
```

Deprecated.

Use

MBeanServer.getClassLoaderRepository()

instead.

Keeps the list of Class Loaders registered in the MBean Server.
It provides the necessary methods to load classes using the registered
Class Loaders.

This deprecated class is maintained for compatibility. In
previous versions of JMX, there was one

DefaultLoaderRepository

shared by all MBean servers.
As of JMX 1.2, that functionality is approximated by using

MBeanServerFactory.findMBeanServer(java.lang.String)

to find all known MBean
servers, and consulting the

ClassLoaderRepository

of each
one. It is strongly recommended that code referencing

DefaultLoaderRepository

be rewritten.

**Since:** 1.5

@Deprecated

public class

DefaultLoaderRepository

extends

Object

Keeps the list of Class Loaders registered in the MBean Server.
It provides the necessary methods to load classes using the registered
Class Loaders.

This deprecated class is maintained for compatibility. In
previous versions of JMX, there was one

DefaultLoaderRepository

shared by all MBean servers.
As of JMX 1.2, that functionality is approximated by using

MBeanServerFactory.findMBeanServer(java.lang.String)

to find all known MBean
servers, and consulting the

ClassLoaderRepository

of each
one. It is strongly recommended that code referencing

DefaultLoaderRepository

be rewritten.

Keeps the list of Class Loaders registered in the MBean Server.
It provides the necessary methods to load classes using the registered
Class Loaders.

This deprecated class is maintained for compatibility. In
previous versions of JMX, there was one

DefaultLoaderRepository

shared by all MBean servers.
As of JMX 1.2, that functionality is approximated by using

MBeanServerFactory.findMBeanServer(java.lang.String)

to find all known MBean
servers, and consulting the

ClassLoaderRepository

of each
one. It is strongly recommended that code referencing

DefaultLoaderRepository

be rewritten.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultLoaderRepository

()

Deprecated.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

Class

<?>

loadClass

​(

String

className)

Deprecated.

Go through the list of class loaders and try to load the requested
class.

static

Class

<?>

loadClassWithout

​(

ClassLoader

loader,

String

className)

Deprecated.

Go through the list of class loaders but exclude the given
class loader, then try to load
the requested class.

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

DefaultLoaderRepository

()

Deprecated.

---

#### Constructor Summary

Deprecated.

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

Class

<?>

loadClass

​(

String

className)

Deprecated.

Go through the list of class loaders and try to load the requested
class.

static

Class

<?>

loadClassWithout

​(

ClassLoader

loader,

String

className)

Deprecated.

Go through the list of class loaders but exclude the given
class loader, then try to load
the requested class.

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

Deprecated.

Go through the list of class loaders and try to load the requested
class.

Go through the list of class loaders but exclude the given
class loader, then try to load
the requested class.

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

- DefaultLoaderRepository

```java
public DefaultLoaderRepository()
```

Deprecated.

============ METHOD DETAIL ==========

- Method Detail

- loadClass

```java
public static
Class
<?> loadClass​(
String
className)
throws
ClassNotFoundException
```

Deprecated.

Go through the list of class loaders and try to load the requested
class.
The method will stop as soon as the class is found. If the class
is not found the method will throw a

ClassNotFoundException

exception.

**Parameters:** className

- The name of the class to be loaded.
**Returns:** the loaded class.
**Throws:** ClassNotFoundException

- The specified class could not be
found.

- loadClassWithout

```java
public static
Class
<?> loadClassWithout​(
ClassLoader
loader,

String
className)
throws
ClassNotFoundException
```

Deprecated.

Go through the list of class loaders but exclude the given
class loader, then try to load
the requested class.
The method will stop as soon as the class is found. If the class
is not found the method will throw a

ClassNotFoundException

exception.

**Parameters:** className

- The name of the class to be loaded.
**Parameters:** loader

- The class loader to be excluded.
**Returns:** the loaded class.
**Throws:** ClassNotFoundException

- The specified class could not be
found.

Constructor Detail

- DefaultLoaderRepository

```java
public DefaultLoaderRepository()
```

Deprecated.

---

#### Constructor Detail

DefaultLoaderRepository

```java
public DefaultLoaderRepository()
```

Deprecated.

---

#### DefaultLoaderRepository

public DefaultLoaderRepository()

Method Detail

- loadClass

```java
public static
Class
<?> loadClass​(
String
className)
throws
ClassNotFoundException
```

Deprecated.

Go through the list of class loaders and try to load the requested
class.
The method will stop as soon as the class is found. If the class
is not found the method will throw a

ClassNotFoundException

exception.

**Parameters:** className

- The name of the class to be loaded.
**Returns:** the loaded class.
**Throws:** ClassNotFoundException

- The specified class could not be
found.

- loadClassWithout

```java
public static
Class
<?> loadClassWithout​(
ClassLoader
loader,

String
className)
throws
ClassNotFoundException
```

Deprecated.

Go through the list of class loaders but exclude the given
class loader, then try to load
the requested class.
The method will stop as soon as the class is found. If the class
is not found the method will throw a

ClassNotFoundException

exception.

**Parameters:** className

- The name of the class to be loaded.
**Parameters:** loader

- The class loader to be excluded.
**Returns:** the loaded class.
**Throws:** ClassNotFoundException

- The specified class could not be
found.

---

#### Method Detail

loadClass

```java
public static
Class
<?> loadClass​(
String
className)
throws
ClassNotFoundException
```

Deprecated.

Go through the list of class loaders and try to load the requested
class.
The method will stop as soon as the class is found. If the class
is not found the method will throw a

ClassNotFoundException

exception.

**Parameters:** className

- The name of the class to be loaded.
**Returns:** the loaded class.
**Throws:** ClassNotFoundException

- The specified class could not be
found.

---

#### loadClass

public static

Class

<?> loadClass​(

String

className)
throws

ClassNotFoundException

Go through the list of class loaders and try to load the requested
class.
The method will stop as soon as the class is found. If the class
is not found the method will throw a

ClassNotFoundException

exception.

loadClassWithout

```java
public static
Class
<?> loadClassWithout​(
ClassLoader
loader,

String
className)
throws
ClassNotFoundException
```

Deprecated.

Go through the list of class loaders but exclude the given
class loader, then try to load
the requested class.
The method will stop as soon as the class is found. If the class
is not found the method will throw a

ClassNotFoundException

exception.

**Parameters:** className

- The name of the class to be loaded.
**Parameters:** loader

- The class loader to be excluded.
**Returns:** the loaded class.
**Throws:** ClassNotFoundException

- The specified class could not be
found.

---

#### loadClassWithout

public static

Class

<?> loadClassWithout​(

ClassLoader

loader,

String

className)
throws

ClassNotFoundException

Go through the list of class loaders but exclude the given
class loader, then try to load
the requested class.
The method will stop as soon as the class is found. If the class
is not found the method will throw a

ClassNotFoundException

exception.

---

