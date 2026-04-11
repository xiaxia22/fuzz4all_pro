# Class RMIClassLoaderSpi

**Source:** `java.rmi\java\rmi\server\RMIClassLoaderSpi.html`

### Class Description

```java
public abstract class
RMIClassLoaderSpi

extends
Object
```

RMIClassLoaderSpi

is the service provider interface for

RMIClassLoader

.

In particular, an

RMIClassLoaderSpi

instance provides an
implementation of the following static methods of

RMIClassLoader

:

- RMIClassLoader.loadClass(URL,String)

RMIClassLoader.loadClass(String,String)

RMIClassLoader.loadClass(String,String,ClassLoader)

RMIClassLoader.loadProxyClass(String,String[],ClassLoader)

RMIClassLoader.getClassLoader(String)

RMIClassLoader.getClassAnnotation(Class)

When one of those methods is invoked, its behavior is to delegate
to a corresponding method on an instance of this class.
The details of how each method delegates to the provider instance is
described in the documentation for each particular method.
See the documentation for

RMIClassLoader

for a description
of how a provider instance is chosen.

**Since:** 1.4
**See Also:** RMIClassLoader

---

### Field Details

*No entries found.*

### Constructor Details

#### public RMIClassLoaderSpi()

*No description found.*

---

### Method Details

#### public abstract
Class
<?> loadClass​(
String
codebase,

String
name,

ClassLoader
defaultLoader)
throws
MalformedURLException
,

ClassNotFoundException

Provides the implementation for

RMIClassLoader.loadClass(URL,String)

,

RMIClassLoader.loadClass(String,String)

, and

RMIClassLoader.loadClass(String,String,ClassLoader)

.

Loads a class from a codebase URL path, optionally using the
supplied loader.

Typically, a provider implementation will attempt to
resolve the named class using the given

defaultLoader

,
if specified, before attempting to resolve the class from the
codebase URL path.

An implementation of this method must either return a class
with the given name or throw an exception.

**Parameters:**
- codebase

- the list of URLs (separated by spaces) to load
the class from, or

null
- name

- the name of the class to load
- defaultLoader

- additional contextual class loader
to use, or

null

**Returns:**
- the

Class

object representing the loaded class

**Throws:**
- MalformedURLException

- if

codebase

is
non-

null

and contains an invalid URL, or
if

codebase

is

null

and a provider-specific
URL used to load classes is invalid
- ClassNotFoundException

- if a definition for the class
could not be found at the specified location

---

#### public abstract
Class
<?> loadProxyClass​(
String
codebase,

String
[] interfaces,

ClassLoader
defaultLoader)
throws
MalformedURLException
,

ClassNotFoundException

Provides the implementation for

RMIClassLoader.loadProxyClass(String,String[],ClassLoader)

.

Loads a dynamic proxy class (see

Proxy

that implements a set of interfaces with the given names
from a codebase URL path, optionally using the supplied loader.

An implementation of this method must either return a proxy
class that implements the named interfaces or throw an exception.

**Parameters:**
- codebase

- the list of URLs (space-separated) to load
classes from, or

null
- interfaces

- the names of the interfaces for the proxy class
to implement
- defaultLoader

- additional contextual class loader
to use, or

null

**Returns:**
- a dynamic proxy class that implements the named interfaces

**Throws:**
- MalformedURLException

- if

codebase

is
non-

null

and contains an invalid URL, or
if

codebase

is

null

and a provider-specific
URL used to load classes is invalid
- ClassNotFoundException

- if a definition for one of
the named interfaces could not be found at the specified location,
or if creation of the dynamic proxy class failed (such as if

Proxy.getProxyClass(ClassLoader,Class[])

would throw an

IllegalArgumentException

for the given
interface list)

---

#### public abstract
ClassLoader
getClassLoader​(
String
codebase)
throws
MalformedURLException

Provides the implementation for

RMIClassLoader.getClassLoader(String)

.

Returns a class loader that loads classes from the given codebase
URL path.

If there is a security manger, its

checkPermission

method will be invoked with a

RuntimePermission("getClassLoader")

permission;
this could result in a

SecurityException

.
The implementation of this method may also perform further security
checks to verify that the calling context has permission to connect
to all of the URLs in the codebase URL path.

**Parameters:**
- codebase

- the list of URLs (space-separated) from which
the returned class loader will load classes from, or

null

**Returns:**
- a class loader that loads classes from the given codebase URL
path

**Throws:**
- MalformedURLException

- if

codebase

is
non-

null

and contains an invalid URL, or
if

codebase

is

null

and a provider-specific
URL used to identify the class loader is invalid
- SecurityException

- if there is a security manager and the
invocation of its

checkPermission

method fails, or
if the caller does not have permission to connect to all of the
URLs in the codebase URL path

---

#### public abstract
String
getClassAnnotation​(
Class
<?> cl)

Provides the implementation for

RMIClassLoader.getClassAnnotation(Class)

.

Returns the annotation string (representing a location for
the class definition) that RMI will use to annotate the class
descriptor when marshalling objects of the given class.

**Parameters:**
- cl

- the class to obtain the annotation for

**Returns:**
- a string to be used to annotate the given class when
it gets marshalled, or

null

**Throws:**
- NullPointerException

- if

cl

is

null

---

### Additional Sections

#### Class RMIClassLoaderSpi

java.lang.Object

- java.rmi.server.RMIClassLoaderSpi

java.rmi.server.RMIClassLoaderSpi

```java
public abstract class
RMIClassLoaderSpi

extends
Object
```

RMIClassLoaderSpi

is the service provider interface for

RMIClassLoader

.

In particular, an

RMIClassLoaderSpi

instance provides an
implementation of the following static methods of

RMIClassLoader

:

- RMIClassLoader.loadClass(URL,String)

RMIClassLoader.loadClass(String,String)

RMIClassLoader.loadClass(String,String,ClassLoader)

RMIClassLoader.loadProxyClass(String,String[],ClassLoader)

RMIClassLoader.getClassLoader(String)

RMIClassLoader.getClassAnnotation(Class)

When one of those methods is invoked, its behavior is to delegate
to a corresponding method on an instance of this class.
The details of how each method delegates to the provider instance is
described in the documentation for each particular method.
See the documentation for

RMIClassLoader

for a description
of how a provider instance is chosen.

**Since:** 1.4
**See Also:** RMIClassLoader

public abstract class

RMIClassLoaderSpi

extends

Object

RMIClassLoaderSpi

is the service provider interface for

RMIClassLoader

.

In particular, an

RMIClassLoaderSpi

instance provides an
implementation of the following static methods of

RMIClassLoader

:

- RMIClassLoader.loadClass(URL,String)

RMIClassLoader.loadClass(String,String)

RMIClassLoader.loadClass(String,String,ClassLoader)

RMIClassLoader.loadProxyClass(String,String[],ClassLoader)

RMIClassLoader.getClassLoader(String)

RMIClassLoader.getClassAnnotation(Class)

When one of those methods is invoked, its behavior is to delegate
to a corresponding method on an instance of this class.
The details of how each method delegates to the provider instance is
described in the documentation for each particular method.
See the documentation for

RMIClassLoader

for a description
of how a provider instance is chosen.

RMIClassLoader.loadClass(URL,String)

RMIClassLoader.loadClass(String,String)

RMIClassLoader.loadClass(String,String,ClassLoader)

RMIClassLoader.loadProxyClass(String,String[],ClassLoader)

RMIClassLoader.getClassLoader(String)

RMIClassLoader.getClassAnnotation(Class)

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RMIClassLoaderSpi

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

String

getClassAnnotation

​(

Class

<?> cl)

Provides the implementation for

RMIClassLoader.getClassAnnotation(Class)

.

abstract

ClassLoader

getClassLoader

​(

String

codebase)

Provides the implementation for

RMIClassLoader.getClassLoader(String)

.

abstract

Class

<?>

loadClass

​(

String

codebase,

String

name,

ClassLoader

defaultLoader)

Provides the implementation for

RMIClassLoader.loadClass(URL,String)

,

RMIClassLoader.loadClass(String,String)

, and

RMIClassLoader.loadClass(String,String,ClassLoader)

.

abstract

Class

<?>

loadProxyClass

​(

String

codebase,

String

[] interfaces,

ClassLoader

defaultLoader)

Provides the implementation for

RMIClassLoader.loadProxyClass(String,String[],ClassLoader)

.

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

RMIClassLoaderSpi

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

String

getClassAnnotation

​(

Class

<?> cl)

Provides the implementation for

RMIClassLoader.getClassAnnotation(Class)

.

abstract

ClassLoader

getClassLoader

​(

String

codebase)

Provides the implementation for

RMIClassLoader.getClassLoader(String)

.

abstract

Class

<?>

loadClass

​(

String

codebase,

String

name,

ClassLoader

defaultLoader)

Provides the implementation for

RMIClassLoader.loadClass(URL,String)

,

RMIClassLoader.loadClass(String,String)

, and

RMIClassLoader.loadClass(String,String,ClassLoader)

.

abstract

Class

<?>

loadProxyClass

​(

String

codebase,

String

[] interfaces,

ClassLoader

defaultLoader)

Provides the implementation for

RMIClassLoader.loadProxyClass(String,String[],ClassLoader)

.

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

Provides the implementation for

RMIClassLoader.getClassAnnotation(Class)

.

Provides the implementation for

RMIClassLoader.getClassLoader(String)

.

Provides the implementation for

RMIClassLoader.loadClass(URL,String)

,

RMIClassLoader.loadClass(String,String)

, and

RMIClassLoader.loadClass(String,String,ClassLoader)

.

Provides the implementation for

RMIClassLoader.loadProxyClass(String,String[],ClassLoader)

.

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

- RMIClassLoaderSpi

```java
public RMIClassLoaderSpi()
```

============ METHOD DETAIL ==========

- Method Detail

- loadClass

```java
public abstract
Class
<?> loadClass​(
String
codebase,

String
name,

ClassLoader
defaultLoader)
throws
MalformedURLException
,

ClassNotFoundException
```

Provides the implementation for

RMIClassLoader.loadClass(URL,String)

,

RMIClassLoader.loadClass(String,String)

, and

RMIClassLoader.loadClass(String,String,ClassLoader)

.

Loads a class from a codebase URL path, optionally using the
supplied loader.

Typically, a provider implementation will attempt to
resolve the named class using the given

defaultLoader

,
if specified, before attempting to resolve the class from the
codebase URL path.

An implementation of this method must either return a class
with the given name or throw an exception.

**Parameters:** codebase

- the list of URLs (separated by spaces) to load
the class from, or

null
**Parameters:** name

- the name of the class to load
**Parameters:** defaultLoader

- additional contextual class loader
to use, or

null
**Returns:** the

Class

object representing the loaded class
**Throws:** MalformedURLException

- if

codebase

is
non-

null

and contains an invalid URL, or
if

codebase

is

null

and a provider-specific
URL used to load classes is invalid
**Throws:** ClassNotFoundException

- if a definition for the class
could not be found at the specified location

- loadProxyClass

```java
public abstract
Class
<?> loadProxyClass​(
String
codebase,

String
[] interfaces,

ClassLoader
defaultLoader)
throws
MalformedURLException
,

ClassNotFoundException
```

Provides the implementation for

RMIClassLoader.loadProxyClass(String,String[],ClassLoader)

.

Loads a dynamic proxy class (see

Proxy

that implements a set of interfaces with the given names
from a codebase URL path, optionally using the supplied loader.

An implementation of this method must either return a proxy
class that implements the named interfaces or throw an exception.

**Parameters:** codebase

- the list of URLs (space-separated) to load
classes from, or

null
**Parameters:** interfaces

- the names of the interfaces for the proxy class
to implement
**Parameters:** defaultLoader

- additional contextual class loader
to use, or

null
**Returns:** a dynamic proxy class that implements the named interfaces
**Throws:** MalformedURLException

- if

codebase

is
non-

null

and contains an invalid URL, or
if

codebase

is

null

and a provider-specific
URL used to load classes is invalid
**Throws:** ClassNotFoundException

- if a definition for one of
the named interfaces could not be found at the specified location,
or if creation of the dynamic proxy class failed (such as if

Proxy.getProxyClass(ClassLoader,Class[])

would throw an

IllegalArgumentException

for the given
interface list)

- getClassLoader

```java
public abstract
ClassLoader
getClassLoader​(
String
codebase)
throws
MalformedURLException
```

Provides the implementation for

RMIClassLoader.getClassLoader(String)

.

Returns a class loader that loads classes from the given codebase
URL path.

If there is a security manger, its

checkPermission

method will be invoked with a

RuntimePermission("getClassLoader")

permission;
this could result in a

SecurityException

.
The implementation of this method may also perform further security
checks to verify that the calling context has permission to connect
to all of the URLs in the codebase URL path.

**Parameters:** codebase

- the list of URLs (space-separated) from which
the returned class loader will load classes from, or

null
**Returns:** a class loader that loads classes from the given codebase URL
path
**Throws:** MalformedURLException

- if

codebase

is
non-

null

and contains an invalid URL, or
if

codebase

is

null

and a provider-specific
URL used to identify the class loader is invalid
**Throws:** SecurityException

- if there is a security manager and the
invocation of its

checkPermission

method fails, or
if the caller does not have permission to connect to all of the
URLs in the codebase URL path

- getClassAnnotation

```java
public abstract
String
getClassAnnotation​(
Class
<?> cl)
```

Provides the implementation for

RMIClassLoader.getClassAnnotation(Class)

.

Returns the annotation string (representing a location for
the class definition) that RMI will use to annotate the class
descriptor when marshalling objects of the given class.

**Parameters:** cl

- the class to obtain the annotation for
**Returns:** a string to be used to annotate the given class when
it gets marshalled, or

null
**Throws:** NullPointerException

- if

cl

is

null

Constructor Detail

- RMIClassLoaderSpi

```java
public RMIClassLoaderSpi()
```

---

#### Constructor Detail

RMIClassLoaderSpi

```java
public RMIClassLoaderSpi()
```

---

#### RMIClassLoaderSpi

public RMIClassLoaderSpi()

Method Detail

- loadClass

```java
public abstract
Class
<?> loadClass​(
String
codebase,

String
name,

ClassLoader
defaultLoader)
throws
MalformedURLException
,

ClassNotFoundException
```

Provides the implementation for

RMIClassLoader.loadClass(URL,String)

,

RMIClassLoader.loadClass(String,String)

, and

RMIClassLoader.loadClass(String,String,ClassLoader)

.

Loads a class from a codebase URL path, optionally using the
supplied loader.

Typically, a provider implementation will attempt to
resolve the named class using the given

defaultLoader

,
if specified, before attempting to resolve the class from the
codebase URL path.

An implementation of this method must either return a class
with the given name or throw an exception.

**Parameters:** codebase

- the list of URLs (separated by spaces) to load
the class from, or

null
**Parameters:** name

- the name of the class to load
**Parameters:** defaultLoader

- additional contextual class loader
to use, or

null
**Returns:** the

Class

object representing the loaded class
**Throws:** MalformedURLException

- if

codebase

is
non-

null

and contains an invalid URL, or
if

codebase

is

null

and a provider-specific
URL used to load classes is invalid
**Throws:** ClassNotFoundException

- if a definition for the class
could not be found at the specified location

- loadProxyClass

```java
public abstract
Class
<?> loadProxyClass​(
String
codebase,

String
[] interfaces,

ClassLoader
defaultLoader)
throws
MalformedURLException
,

ClassNotFoundException
```

Provides the implementation for

RMIClassLoader.loadProxyClass(String,String[],ClassLoader)

.

Loads a dynamic proxy class (see

Proxy

that implements a set of interfaces with the given names
from a codebase URL path, optionally using the supplied loader.

An implementation of this method must either return a proxy
class that implements the named interfaces or throw an exception.

**Parameters:** codebase

- the list of URLs (space-separated) to load
classes from, or

null
**Parameters:** interfaces

- the names of the interfaces for the proxy class
to implement
**Parameters:** defaultLoader

- additional contextual class loader
to use, or

null
**Returns:** a dynamic proxy class that implements the named interfaces
**Throws:** MalformedURLException

- if

codebase

is
non-

null

and contains an invalid URL, or
if

codebase

is

null

and a provider-specific
URL used to load classes is invalid
**Throws:** ClassNotFoundException

- if a definition for one of
the named interfaces could not be found at the specified location,
or if creation of the dynamic proxy class failed (such as if

Proxy.getProxyClass(ClassLoader,Class[])

would throw an

IllegalArgumentException

for the given
interface list)

- getClassLoader

```java
public abstract
ClassLoader
getClassLoader​(
String
codebase)
throws
MalformedURLException
```

Provides the implementation for

RMIClassLoader.getClassLoader(String)

.

Returns a class loader that loads classes from the given codebase
URL path.

If there is a security manger, its

checkPermission

method will be invoked with a

RuntimePermission("getClassLoader")

permission;
this could result in a

SecurityException

.
The implementation of this method may also perform further security
checks to verify that the calling context has permission to connect
to all of the URLs in the codebase URL path.

**Parameters:** codebase

- the list of URLs (space-separated) from which
the returned class loader will load classes from, or

null
**Returns:** a class loader that loads classes from the given codebase URL
path
**Throws:** MalformedURLException

- if

codebase

is
non-

null

and contains an invalid URL, or
if

codebase

is

null

and a provider-specific
URL used to identify the class loader is invalid
**Throws:** SecurityException

- if there is a security manager and the
invocation of its

checkPermission

method fails, or
if the caller does not have permission to connect to all of the
URLs in the codebase URL path

- getClassAnnotation

```java
public abstract
String
getClassAnnotation​(
Class
<?> cl)
```

Provides the implementation for

RMIClassLoader.getClassAnnotation(Class)

.

Returns the annotation string (representing a location for
the class definition) that RMI will use to annotate the class
descriptor when marshalling objects of the given class.

**Parameters:** cl

- the class to obtain the annotation for
**Returns:** a string to be used to annotate the given class when
it gets marshalled, or

null
**Throws:** NullPointerException

- if

cl

is

null

---

#### Method Detail

loadClass

```java
public abstract
Class
<?> loadClass​(
String
codebase,

String
name,

ClassLoader
defaultLoader)
throws
MalformedURLException
,

ClassNotFoundException
```

Provides the implementation for

RMIClassLoader.loadClass(URL,String)

,

RMIClassLoader.loadClass(String,String)

, and

RMIClassLoader.loadClass(String,String,ClassLoader)

.

Loads a class from a codebase URL path, optionally using the
supplied loader.

Typically, a provider implementation will attempt to
resolve the named class using the given

defaultLoader

,
if specified, before attempting to resolve the class from the
codebase URL path.

An implementation of this method must either return a class
with the given name or throw an exception.

**Parameters:** codebase

- the list of URLs (separated by spaces) to load
the class from, or

null
**Parameters:** name

- the name of the class to load
**Parameters:** defaultLoader

- additional contextual class loader
to use, or

null
**Returns:** the

Class

object representing the loaded class
**Throws:** MalformedURLException

- if

codebase

is
non-

null

and contains an invalid URL, or
if

codebase

is

null

and a provider-specific
URL used to load classes is invalid
**Throws:** ClassNotFoundException

- if a definition for the class
could not be found at the specified location

---

#### loadClass

public abstract

Class

<?> loadClass​(

String

codebase,

String

name,

ClassLoader

defaultLoader)
throws

MalformedURLException

,

ClassNotFoundException

Provides the implementation for

RMIClassLoader.loadClass(URL,String)

,

RMIClassLoader.loadClass(String,String)

, and

RMIClassLoader.loadClass(String,String,ClassLoader)

.

Loads a class from a codebase URL path, optionally using the
supplied loader.

Typically, a provider implementation will attempt to
resolve the named class using the given

defaultLoader

,
if specified, before attempting to resolve the class from the
codebase URL path.

An implementation of this method must either return a class
with the given name or throw an exception.

An implementation of this method must either return a class
with the given name or throw an exception.

loadProxyClass

```java
public abstract
Class
<?> loadProxyClass​(
String
codebase,

String
[] interfaces,

ClassLoader
defaultLoader)
throws
MalformedURLException
,

ClassNotFoundException
```

Provides the implementation for

RMIClassLoader.loadProxyClass(String,String[],ClassLoader)

.

Loads a dynamic proxy class (see

Proxy

that implements a set of interfaces with the given names
from a codebase URL path, optionally using the supplied loader.

An implementation of this method must either return a proxy
class that implements the named interfaces or throw an exception.

**Parameters:** codebase

- the list of URLs (space-separated) to load
classes from, or

null
**Parameters:** interfaces

- the names of the interfaces for the proxy class
to implement
**Parameters:** defaultLoader

- additional contextual class loader
to use, or

null
**Returns:** a dynamic proxy class that implements the named interfaces
**Throws:** MalformedURLException

- if

codebase

is
non-

null

and contains an invalid URL, or
if

codebase

is

null

and a provider-specific
URL used to load classes is invalid
**Throws:** ClassNotFoundException

- if a definition for one of
the named interfaces could not be found at the specified location,
or if creation of the dynamic proxy class failed (such as if

Proxy.getProxyClass(ClassLoader,Class[])

would throw an

IllegalArgumentException

for the given
interface list)

---

#### loadProxyClass

public abstract

Class

<?> loadProxyClass​(

String

codebase,

String

[] interfaces,

ClassLoader

defaultLoader)
throws

MalformedURLException

,

ClassNotFoundException

Provides the implementation for

RMIClassLoader.loadProxyClass(String,String[],ClassLoader)

.

Loads a dynamic proxy class (see

Proxy

that implements a set of interfaces with the given names
from a codebase URL path, optionally using the supplied loader.

An implementation of this method must either return a proxy
class that implements the named interfaces or throw an exception.

An implementation of this method must either return a proxy
class that implements the named interfaces or throw an exception.

getClassLoader

```java
public abstract
ClassLoader
getClassLoader​(
String
codebase)
throws
MalformedURLException
```

Provides the implementation for

RMIClassLoader.getClassLoader(String)

.

Returns a class loader that loads classes from the given codebase
URL path.

If there is a security manger, its

checkPermission

method will be invoked with a

RuntimePermission("getClassLoader")

permission;
this could result in a

SecurityException

.
The implementation of this method may also perform further security
checks to verify that the calling context has permission to connect
to all of the URLs in the codebase URL path.

**Parameters:** codebase

- the list of URLs (space-separated) from which
the returned class loader will load classes from, or

null
**Returns:** a class loader that loads classes from the given codebase URL
path
**Throws:** MalformedURLException

- if

codebase

is
non-

null

and contains an invalid URL, or
if

codebase

is

null

and a provider-specific
URL used to identify the class loader is invalid
**Throws:** SecurityException

- if there is a security manager and the
invocation of its

checkPermission

method fails, or
if the caller does not have permission to connect to all of the
URLs in the codebase URL path

---

#### getClassLoader

public abstract

ClassLoader

getClassLoader​(

String

codebase)
throws

MalformedURLException

Provides the implementation for

RMIClassLoader.getClassLoader(String)

.

Returns a class loader that loads classes from the given codebase
URL path.

If there is a security manger, its

checkPermission

method will be invoked with a

RuntimePermission("getClassLoader")

permission;
this could result in a

SecurityException

.
The implementation of this method may also perform further security
checks to verify that the calling context has permission to connect
to all of the URLs in the codebase URL path.

If there is a security manger, its

checkPermission

method will be invoked with a

RuntimePermission("getClassLoader")

permission;
this could result in a

SecurityException

.
The implementation of this method may also perform further security
checks to verify that the calling context has permission to connect
to all of the URLs in the codebase URL path.

getClassAnnotation

```java
public abstract
String
getClassAnnotation​(
Class
<?> cl)
```

Provides the implementation for

RMIClassLoader.getClassAnnotation(Class)

.

Returns the annotation string (representing a location for
the class definition) that RMI will use to annotate the class
descriptor when marshalling objects of the given class.

**Parameters:** cl

- the class to obtain the annotation for
**Returns:** a string to be used to annotate the given class when
it gets marshalled, or

null
**Throws:** NullPointerException

- if

cl

is

null

---

#### getClassAnnotation

public abstract

String

getClassAnnotation​(

Class

<?> cl)

Provides the implementation for

RMIClassLoader.getClassAnnotation(Class)

.

Returns the annotation string (representing a location for
the class definition) that RMI will use to annotate the class
descriptor when marshalling objects of the given class.

---

