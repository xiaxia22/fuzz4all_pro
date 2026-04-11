# Class PrivateMLet

**Source:** `java.management\javax\management\loading\PrivateMLet.html`

### Class Description

```java
public class
PrivateMLet

extends
MLet

implements
PrivateClassLoader
```

An MLet that is not added to the

ClassLoaderRepository

.
This class acts exactly like its parent class,

MLet

, with
one exception. When a PrivateMLet is registered in an MBean
server, it is not added to that MBean server's

ClassLoaderRepository

. This is true because this class implements
the interface

PrivateClassLoader

.

**All Implemented Interfaces:** Closeable

,

Externalizable

,

Serializable

,

AutoCloseable

,

MLetMBean

,

PrivateClassLoader

,

MBeanRegistration

---

### Field Details

*No entries found.*

### Constructor Details

#### public PrivateMLet​(
URL
[] urls,
boolean delegateToCLR)

Constructs a new PrivateMLet for the specified URLs using the
default delegation parent ClassLoader. The URLs will be
searched in the order specified for classes and resources
after first searching in the parent class loader.

**Parameters:**
- urls

- The URLs from which to load classes and resources.
- delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

---

#### public PrivateMLet​(
URL
[] urls,

ClassLoader
parent,
boolean delegateToCLR)

Constructs a new PrivateMLet for the given URLs. The URLs will
be searched in the order specified for classes and resources
after first searching in the specified parent class loader.
The parent argument will be used as the parent class loader
for delegation.

**Parameters:**
- urls

- The URLs from which to load classes and resources.
- parent

- The parent class loader for delegation.
- delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

---

#### public PrivateMLet​(
URL
[] urls,

ClassLoader
parent,

URLStreamHandlerFactory
factory,
boolean delegateToCLR)

Constructs a new PrivateMLet for the specified URLs, parent
class loader, and URLStreamHandlerFactory. The parent argument
will be used as the parent class loader for delegation. The
factory argument will be used as the stream handler factory to
obtain protocol handlers when creating new URLs.

**Parameters:**
- urls

- The URLs from which to load classes and resources.
- parent

- The parent class loader for delegation.
- factory

- The URLStreamHandlerFactory to use when creating URLs.
- delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class PrivateMLet

java.lang.Object

- java.lang.ClassLoader
- - java.security.SecureClassLoader
- - java.net.URLClassLoader
- - javax.management.loading.MLet
- - javax.management.loading.PrivateMLet

java.lang.ClassLoader

- java.security.SecureClassLoader
- - java.net.URLClassLoader
- - javax.management.loading.MLet
- - javax.management.loading.PrivateMLet

java.security.SecureClassLoader

- java.net.URLClassLoader
- - javax.management.loading.MLet
- - javax.management.loading.PrivateMLet

java.net.URLClassLoader

- javax.management.loading.MLet
- - javax.management.loading.PrivateMLet

javax.management.loading.MLet

- javax.management.loading.PrivateMLet

javax.management.loading.PrivateMLet

**All Implemented Interfaces:** Closeable

,

Externalizable

,

Serializable

,

AutoCloseable

,

MLetMBean

,

PrivateClassLoader

,

MBeanRegistration

```java
public class
PrivateMLet

extends
MLet

implements
PrivateClassLoader
```

An MLet that is not added to the

ClassLoaderRepository

.
This class acts exactly like its parent class,

MLet

, with
one exception. When a PrivateMLet is registered in an MBean
server, it is not added to that MBean server's

ClassLoaderRepository

. This is true because this class implements
the interface

PrivateClassLoader

.

**Since:** 1.5
**See Also:** Serialized Form

public class

PrivateMLet

extends

MLet

implements

PrivateClassLoader

An MLet that is not added to the

ClassLoaderRepository

.
This class acts exactly like its parent class,

MLet

, with
one exception. When a PrivateMLet is registered in an MBean
server, it is not added to that MBean server's

ClassLoaderRepository

. This is true because this class implements
the interface

PrivateClassLoader

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PrivateMLet

​(

URL

[] urls,
boolean delegateToCLR)

Constructs a new PrivateMLet for the specified URLs using the
default delegation parent ClassLoader.

PrivateMLet

​(

URL

[] urls,

ClassLoader

parent,
boolean delegateToCLR)

Constructs a new PrivateMLet for the given URLs.

PrivateMLet

​(

URL

[] urls,

ClassLoader

parent,

URLStreamHandlerFactory

factory,
boolean delegateToCLR)

Constructs a new PrivateMLet for the specified URLs, parent
class loader, and URLStreamHandlerFactory.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.management.loading.

MLet

addURL

,

addURL

,

check

,

findClass

,

findLibrary

,

getLibraryDirectory

,

getMBeansFromURL

,

getMBeansFromURL

,

getURLs

,

loadClass

,

postDeregister

,

postRegister

,

preDeregister

,

preRegister

,

readExternal

,

setLibraryDirectory

,

writeExternal

- Methods declared in class java.net.

URLClassLoader

close

,

definePackage

,

findResource

,

findResources

,

getPermissions

,

getResourceAsStream

,

newInstance

,

newInstance

- Methods declared in class java.security.

SecureClassLoader

defineClass

,

defineClass

- Methods declared in class java.lang.

ClassLoader

clearAssertionStatus

,

defineClass

,

defineClass

,

defineClass

,

defineClass

,

definePackage

,

findClass

,

findLoadedClass

,

findResource

,

findSystemClass

,

getClassLoadingLock

,

getDefinedPackage

,

getDefinedPackages

,

getName

,

getPackage

,

getPackages

,

getParent

,

getPlatformClassLoader

,

getResource

,

getResources

,

getSystemClassLoader

,

getSystemResource

,

getSystemResourceAsStream

,

getSystemResources

,

getUnnamedModule

,

isRegisteredAsParallelCapable

,

loadClass

,

loadClass

,

registerAsParallelCapable

,

resolveClass

,

resources

,

setClassAssertionStatus

,

setDefaultAssertionStatus

,

setPackageAssertionStatus

,

setSigners

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

- Methods declared in interface javax.management.loading.

MLetMBean

getResource

,

getResourceAsStream

,

getResources

Constructor Summary

Constructors

Constructor

Description

PrivateMLet

​(

URL

[] urls,
boolean delegateToCLR)

Constructs a new PrivateMLet for the specified URLs using the
default delegation parent ClassLoader.

PrivateMLet

​(

URL

[] urls,

ClassLoader

parent,
boolean delegateToCLR)

Constructs a new PrivateMLet for the given URLs.

PrivateMLet

​(

URL

[] urls,

ClassLoader

parent,

URLStreamHandlerFactory

factory,
boolean delegateToCLR)

Constructs a new PrivateMLet for the specified URLs, parent
class loader, and URLStreamHandlerFactory.

---

#### Constructor Summary

Constructs a new PrivateMLet for the specified URLs using the
default delegation parent ClassLoader.

Constructs a new PrivateMLet for the given URLs.

Constructs a new PrivateMLet for the specified URLs, parent
class loader, and URLStreamHandlerFactory.

Method Summary

- Methods declared in class javax.management.loading.

MLet

addURL

,

addURL

,

check

,

findClass

,

findLibrary

,

getLibraryDirectory

,

getMBeansFromURL

,

getMBeansFromURL

,

getURLs

,

loadClass

,

postDeregister

,

postRegister

,

preDeregister

,

preRegister

,

readExternal

,

setLibraryDirectory

,

writeExternal

- Methods declared in class java.net.

URLClassLoader

close

,

definePackage

,

findResource

,

findResources

,

getPermissions

,

getResourceAsStream

,

newInstance

,

newInstance

- Methods declared in class java.security.

SecureClassLoader

defineClass

,

defineClass

- Methods declared in class java.lang.

ClassLoader

clearAssertionStatus

,

defineClass

,

defineClass

,

defineClass

,

defineClass

,

definePackage

,

findClass

,

findLoadedClass

,

findResource

,

findSystemClass

,

getClassLoadingLock

,

getDefinedPackage

,

getDefinedPackages

,

getName

,

getPackage

,

getPackages

,

getParent

,

getPlatformClassLoader

,

getResource

,

getResources

,

getSystemClassLoader

,

getSystemResource

,

getSystemResourceAsStream

,

getSystemResources

,

getUnnamedModule

,

isRegisteredAsParallelCapable

,

loadClass

,

loadClass

,

registerAsParallelCapable

,

resolveClass

,

resources

,

setClassAssertionStatus

,

setDefaultAssertionStatus

,

setPackageAssertionStatus

,

setSigners

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

- Methods declared in interface javax.management.loading.

MLetMBean

getResource

,

getResourceAsStream

,

getResources

---

#### Method Summary

Methods declared in class javax.management.loading.

MLet

addURL

,

addURL

,

check

,

findClass

,

findLibrary

,

getLibraryDirectory

,

getMBeansFromURL

,

getMBeansFromURL

,

getURLs

,

loadClass

,

postDeregister

,

postRegister

,

preDeregister

,

preRegister

,

readExternal

,

setLibraryDirectory

,

writeExternal

---

#### Methods declared in class javax.management.loading. MLet

Methods declared in class java.net.

URLClassLoader

close

,

definePackage

,

findResource

,

findResources

,

getPermissions

,

getResourceAsStream

,

newInstance

,

newInstance

---

#### Methods declared in class java.net. URLClassLoader

Methods declared in class java.security.

SecureClassLoader

defineClass

,

defineClass

---

#### Methods declared in class java.security. SecureClassLoader

Methods declared in class java.lang.

ClassLoader

clearAssertionStatus

,

defineClass

,

defineClass

,

defineClass

,

defineClass

,

definePackage

,

findClass

,

findLoadedClass

,

findResource

,

findSystemClass

,

getClassLoadingLock

,

getDefinedPackage

,

getDefinedPackages

,

getName

,

getPackage

,

getPackages

,

getParent

,

getPlatformClassLoader

,

getResource

,

getResources

,

getSystemClassLoader

,

getSystemResource

,

getSystemResourceAsStream

,

getSystemResources

,

getUnnamedModule

,

isRegisteredAsParallelCapable

,

loadClass

,

loadClass

,

registerAsParallelCapable

,

resolveClass

,

resources

,

setClassAssertionStatus

,

setDefaultAssertionStatus

,

setPackageAssertionStatus

,

setSigners

---

#### Methods declared in class java.lang. ClassLoader

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

Methods declared in interface javax.management.loading.

MLetMBean

getResource

,

getResourceAsStream

,

getResources

---

#### Methods declared in interface javax.management.loading. MLetMBean

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PrivateMLet

```java
public PrivateMLet​(
URL
[] urls,
boolean delegateToCLR)
```

Constructs a new PrivateMLet for the specified URLs using the
default delegation parent ClassLoader. The URLs will be
searched in the order specified for classes and resources
after first searching in the parent class loader.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

- PrivateMLet

```java
public PrivateMLet​(
URL
[] urls,

ClassLoader
parent,
boolean delegateToCLR)
```

Constructs a new PrivateMLet for the given URLs. The URLs will
be searched in the order specified for classes and resources
after first searching in the specified parent class loader.
The parent argument will be used as the parent class loader
for delegation.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

- PrivateMLet

```java
public PrivateMLet​(
URL
[] urls,

ClassLoader
parent,

URLStreamHandlerFactory
factory,
boolean delegateToCLR)
```

Constructs a new PrivateMLet for the specified URLs, parent
class loader, and URLStreamHandlerFactory. The parent argument
will be used as the parent class loader for delegation. The
factory argument will be used as the stream handler factory to
obtain protocol handlers when creating new URLs.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.
**Parameters:** factory

- The URLStreamHandlerFactory to use when creating URLs.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

Constructor Detail

- PrivateMLet

```java
public PrivateMLet​(
URL
[] urls,
boolean delegateToCLR)
```

Constructs a new PrivateMLet for the specified URLs using the
default delegation parent ClassLoader. The URLs will be
searched in the order specified for classes and resources
after first searching in the parent class loader.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

- PrivateMLet

```java
public PrivateMLet​(
URL
[] urls,

ClassLoader
parent,
boolean delegateToCLR)
```

Constructs a new PrivateMLet for the given URLs. The URLs will
be searched in the order specified for classes and resources
after first searching in the specified parent class loader.
The parent argument will be used as the parent class loader
for delegation.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

- PrivateMLet

```java
public PrivateMLet​(
URL
[] urls,

ClassLoader
parent,

URLStreamHandlerFactory
factory,
boolean delegateToCLR)
```

Constructs a new PrivateMLet for the specified URLs, parent
class loader, and URLStreamHandlerFactory. The parent argument
will be used as the parent class loader for delegation. The
factory argument will be used as the stream handler factory to
obtain protocol handlers when creating new URLs.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.
**Parameters:** factory

- The URLStreamHandlerFactory to use when creating URLs.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

---

#### Constructor Detail

PrivateMLet

```java
public PrivateMLet​(
URL
[] urls,
boolean delegateToCLR)
```

Constructs a new PrivateMLet for the specified URLs using the
default delegation parent ClassLoader. The URLs will be
searched in the order specified for classes and resources
after first searching in the parent class loader.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

---

#### PrivateMLet

public PrivateMLet​(

URL

[] urls,
boolean delegateToCLR)

Constructs a new PrivateMLet for the specified URLs using the
default delegation parent ClassLoader. The URLs will be
searched in the order specified for classes and resources
after first searching in the parent class loader.

PrivateMLet

```java
public PrivateMLet​(
URL
[] urls,

ClassLoader
parent,
boolean delegateToCLR)
```

Constructs a new PrivateMLet for the given URLs. The URLs will
be searched in the order specified for classes and resources
after first searching in the specified parent class loader.
The parent argument will be used as the parent class loader
for delegation.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

---

#### PrivateMLet

public PrivateMLet​(

URL

[] urls,

ClassLoader

parent,
boolean delegateToCLR)

Constructs a new PrivateMLet for the given URLs. The URLs will
be searched in the order specified for classes and resources
after first searching in the specified parent class loader.
The parent argument will be used as the parent class loader
for delegation.

PrivateMLet

```java
public PrivateMLet​(
URL
[] urls,

ClassLoader
parent,

URLStreamHandlerFactory
factory,
boolean delegateToCLR)
```

Constructs a new PrivateMLet for the specified URLs, parent
class loader, and URLStreamHandlerFactory. The parent argument
will be used as the parent class loader for delegation. The
factory argument will be used as the stream handler factory to
obtain protocol handlers when creating new URLs.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.
**Parameters:** factory

- The URLStreamHandlerFactory to use when creating URLs.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

---

#### PrivateMLet

public PrivateMLet​(

URL

[] urls,

ClassLoader

parent,

URLStreamHandlerFactory

factory,
boolean delegateToCLR)

Constructs a new PrivateMLet for the specified URLs, parent
class loader, and URLStreamHandlerFactory. The parent argument
will be used as the parent class loader for delegation. The
factory argument will be used as the stream handler factory to
obtain protocol handlers when creating new URLs.

---

