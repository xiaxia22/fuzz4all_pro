# Interface ClassLoaderRepository

**Source:** `java.management\javax\management\loading\ClassLoaderRepository.html`

### Class Description

```java
public interface
ClassLoaderRepository
```

Instances of this interface are used to keep the list of ClassLoaders
registered in an MBean Server.
They provide the necessary methods to load classes using the registered
ClassLoaders.

The first ClassLoader in a

ClassLoaderRepository

is
always the MBean Server's own ClassLoader.

When an MBean is registered in an MBean Server, if it is of a
subclass of

ClassLoader

and if it does not
implement the interface

PrivateClassLoader

, it is added to
the end of the MBean Server's

ClassLoaderRepository

.
If it is subsequently unregistered from the MBean Server, it is
removed from the

ClassLoaderRepository

.

The order of MBeans in the

ClassLoaderRepository

is
significant. For any two MBeans

X

and

Y

in the

ClassLoaderRepository

,

X

must appear before

Y

if the registration of

X

was completed before
the registration of

Y

started. If

X

and

Y

were registered concurrently, their order is
indeterminate. The registration of an MBean corresponds to the
call to

MBeanServer.registerMBean(java.lang.Object, javax.management.ObjectName)

or one of the

MBeanServer

.createMBean

methods.

**Since:** 1.5
**See Also:** MBeanServerFactory

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Class
<?> loadClass​(
String
className)
throws
ClassNotFoundException

Load the given class name through the list of class loaders.
Each ClassLoader in turn from the ClassLoaderRepository is
asked to load the class via its

ClassLoader.loadClass(String)

method. If it successfully
returns a

Class

object, that is the result of this
method. If it throws a

ClassNotFoundException

, the
search continues with the next ClassLoader. If it throws
another exception, the exception is propagated from this
method. If the end of the list is reached, a

ClassNotFoundException

is thrown.

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

#### Class
<?> loadClassWithout​(
ClassLoader
exclude,

String
className)
throws
ClassNotFoundException

Load the given class name through the list of class loaders,
excluding the given one. Each ClassLoader in turn from the
ClassLoaderRepository, except

exclude

, is asked to
load the class via its

ClassLoader.loadClass(String)

method. If it successfully returns a

Class

object,
that is the result of this method. If it throws a

ClassNotFoundException

, the search continues with the next
ClassLoader. If it throws another exception, the exception is
propagated from this method. If the end of the list is
reached, a

ClassNotFoundException

is thrown.

Be aware that if a ClassLoader in the ClassLoaderRepository
calls this method from its

loadClass

method, it exposes itself to a deadlock if another
ClassLoader in the ClassLoaderRepository does the same thing at
the same time. The

loadClassBefore(java.lang.ClassLoader, java.lang.String)

method is
recommended to avoid the risk of deadlock.

**Parameters:**
- className

- The name of the class to be loaded.
- exclude

- The class loader to be excluded. May be null,
in which case this method is equivalent to

loadClass(className)

.

**Returns:**
- the loaded class.

**Throws:**
- ClassNotFoundException

- The specified class could not
be found.

---

#### Class
<?> loadClassBefore​(
ClassLoader
stop,

String
className)
throws
ClassNotFoundException

Load the given class name through the list of class loaders,
stopping at the given one. Each ClassLoader in turn from the
ClassLoaderRepository is asked to load the class via its

ClassLoader.loadClass(String)

method. If it successfully
returns a

Class

object, that is the result of this
method. If it throws a

ClassNotFoundException

, the
search continues with the next ClassLoader. If it throws
another exception, the exception is propagated from this
method. If the search reaches

stop

or the end of
the list, a

ClassNotFoundException

is thrown.

Typically this method is called from the

loadClass

method of

stop

, to consult loaders that appear before it
in the

ClassLoaderRepository

. By stopping the
search as soon as

stop

is reached, a potential
deadlock with concurrent class loading is avoided.

**Parameters:**
- className

- The name of the class to be loaded.
- stop

- The class loader at which to stop. May be null, in
which case this method is equivalent to

loadClass(className)

.

**Returns:**
- the loaded class.

**Throws:**
- ClassNotFoundException

- The specified class could not
be found.

---

### Additional Sections

#### Interface ClassLoaderRepository

```java
public interface
ClassLoaderRepository
```

Instances of this interface are used to keep the list of ClassLoaders
registered in an MBean Server.
They provide the necessary methods to load classes using the registered
ClassLoaders.

The first ClassLoader in a

ClassLoaderRepository

is
always the MBean Server's own ClassLoader.

When an MBean is registered in an MBean Server, if it is of a
subclass of

ClassLoader

and if it does not
implement the interface

PrivateClassLoader

, it is added to
the end of the MBean Server's

ClassLoaderRepository

.
If it is subsequently unregistered from the MBean Server, it is
removed from the

ClassLoaderRepository

.

The order of MBeans in the

ClassLoaderRepository

is
significant. For any two MBeans

X

and

Y

in the

ClassLoaderRepository

,

X

must appear before

Y

if the registration of

X

was completed before
the registration of

Y

started. If

X

and

Y

were registered concurrently, their order is
indeterminate. The registration of an MBean corresponds to the
call to

MBeanServer.registerMBean(java.lang.Object, javax.management.ObjectName)

or one of the

MBeanServer

.createMBean

methods.

**Since:** 1.5
**See Also:** MBeanServerFactory

public interface

ClassLoaderRepository

Instances of this interface are used to keep the list of ClassLoaders
registered in an MBean Server.
They provide the necessary methods to load classes using the registered
ClassLoaders.

The first ClassLoader in a

ClassLoaderRepository

is
always the MBean Server's own ClassLoader.

When an MBean is registered in an MBean Server, if it is of a
subclass of

ClassLoader

and if it does not
implement the interface

PrivateClassLoader

, it is added to
the end of the MBean Server's

ClassLoaderRepository

.
If it is subsequently unregistered from the MBean Server, it is
removed from the

ClassLoaderRepository

.

The order of MBeans in the

ClassLoaderRepository

is
significant. For any two MBeans

X

and

Y

in the

ClassLoaderRepository

,

X

must appear before

Y

if the registration of

X

was completed before
the registration of

Y

started. If

X

and

Y

were registered concurrently, their order is
indeterminate. The registration of an MBean corresponds to the
call to

MBeanServer.registerMBean(java.lang.Object, javax.management.ObjectName)

or one of the

MBeanServer

.createMBean

methods.

Instances of this interface are used to keep the list of ClassLoaders
registered in an MBean Server.
They provide the necessary methods to load classes using the registered
ClassLoaders.

The first ClassLoader in a

ClassLoaderRepository

is
always the MBean Server's own ClassLoader.

When an MBean is registered in an MBean Server, if it is of a
subclass of

ClassLoader

and if it does not
implement the interface

PrivateClassLoader

, it is added to
the end of the MBean Server's

ClassLoaderRepository

.
If it is subsequently unregistered from the MBean Server, it is
removed from the

ClassLoaderRepository

.

The order of MBeans in the

ClassLoaderRepository

is
significant. For any two MBeans

X

and

Y

in the

ClassLoaderRepository

,

X

must appear before

Y

if the registration of

X

was completed before
the registration of

Y

started. If

X

and

Y

were registered concurrently, their order is
indeterminate. The registration of an MBean corresponds to the
call to

MBeanServer.registerMBean(java.lang.Object, javax.management.ObjectName)

or one of the

MBeanServer

.createMBean

methods.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Class

<?>

loadClass

​(

String

className)

Load the given class name through the list of class loaders.

Class

<?>

loadClassBefore

​(

ClassLoader

stop,

String

className)

Load the given class name through the list of class loaders,
stopping at the given one.

Class

<?>

loadClassWithout

​(

ClassLoader

exclude,

String

className)

Load the given class name through the list of class loaders,
excluding the given one.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Class

<?>

loadClass

​(

String

className)

Load the given class name through the list of class loaders.

Class

<?>

loadClassBefore

​(

ClassLoader

stop,

String

className)

Load the given class name through the list of class loaders,
stopping at the given one.

Class

<?>

loadClassWithout

​(

ClassLoader

exclude,

String

className)

Load the given class name through the list of class loaders,
excluding the given one.

---

#### Method Summary

Load the given class name through the list of class loaders.

Load the given class name through the list of class loaders,
stopping at the given one.

Load the given class name through the list of class loaders,
excluding the given one.

============ METHOD DETAIL ==========

- Method Detail

- loadClass

```java
Class
<?> loadClass​(
String
className)
throws
ClassNotFoundException
```

Load the given class name through the list of class loaders.
Each ClassLoader in turn from the ClassLoaderRepository is
asked to load the class via its

ClassLoader.loadClass(String)

method. If it successfully
returns a

Class

object, that is the result of this
method. If it throws a

ClassNotFoundException

, the
search continues with the next ClassLoader. If it throws
another exception, the exception is propagated from this
method. If the end of the list is reached, a

ClassNotFoundException

is thrown.

**Parameters:** className

- The name of the class to be loaded.
**Returns:** the loaded class.
**Throws:** ClassNotFoundException

- The specified class could not be
found.

- loadClassWithout

```java
Class
<?> loadClassWithout​(
ClassLoader
exclude,

String
className)
throws
ClassNotFoundException
```

Load the given class name through the list of class loaders,
excluding the given one. Each ClassLoader in turn from the
ClassLoaderRepository, except

exclude

, is asked to
load the class via its

ClassLoader.loadClass(String)

method. If it successfully returns a

Class

object,
that is the result of this method. If it throws a

ClassNotFoundException

, the search continues with the next
ClassLoader. If it throws another exception, the exception is
propagated from this method. If the end of the list is
reached, a

ClassNotFoundException

is thrown.

Be aware that if a ClassLoader in the ClassLoaderRepository
calls this method from its

loadClass

method, it exposes itself to a deadlock if another
ClassLoader in the ClassLoaderRepository does the same thing at
the same time. The

loadClassBefore(java.lang.ClassLoader, java.lang.String)

method is
recommended to avoid the risk of deadlock.

**Parameters:** className

- The name of the class to be loaded.
**Parameters:** exclude

- The class loader to be excluded. May be null,
in which case this method is equivalent to

loadClass(className)

.
**Returns:** the loaded class.
**Throws:** ClassNotFoundException

- The specified class could not
be found.

- loadClassBefore

```java
Class
<?> loadClassBefore​(
ClassLoader
stop,

String
className)
throws
ClassNotFoundException
```

Load the given class name through the list of class loaders,
stopping at the given one. Each ClassLoader in turn from the
ClassLoaderRepository is asked to load the class via its

ClassLoader.loadClass(String)

method. If it successfully
returns a

Class

object, that is the result of this
method. If it throws a

ClassNotFoundException

, the
search continues with the next ClassLoader. If it throws
another exception, the exception is propagated from this
method. If the search reaches

stop

or the end of
the list, a

ClassNotFoundException

is thrown.

Typically this method is called from the

loadClass

method of

stop

, to consult loaders that appear before it
in the

ClassLoaderRepository

. By stopping the
search as soon as

stop

is reached, a potential
deadlock with concurrent class loading is avoided.

**Parameters:** className

- The name of the class to be loaded.
**Parameters:** stop

- The class loader at which to stop. May be null, in
which case this method is equivalent to

loadClass(className)

.
**Returns:** the loaded class.
**Throws:** ClassNotFoundException

- The specified class could not
be found.

Method Detail

- loadClass

```java
Class
<?> loadClass​(
String
className)
throws
ClassNotFoundException
```

Load the given class name through the list of class loaders.
Each ClassLoader in turn from the ClassLoaderRepository is
asked to load the class via its

ClassLoader.loadClass(String)

method. If it successfully
returns a

Class

object, that is the result of this
method. If it throws a

ClassNotFoundException

, the
search continues with the next ClassLoader. If it throws
another exception, the exception is propagated from this
method. If the end of the list is reached, a

ClassNotFoundException

is thrown.

**Parameters:** className

- The name of the class to be loaded.
**Returns:** the loaded class.
**Throws:** ClassNotFoundException

- The specified class could not be
found.

- loadClassWithout

```java
Class
<?> loadClassWithout​(
ClassLoader
exclude,

String
className)
throws
ClassNotFoundException
```

Load the given class name through the list of class loaders,
excluding the given one. Each ClassLoader in turn from the
ClassLoaderRepository, except

exclude

, is asked to
load the class via its

ClassLoader.loadClass(String)

method. If it successfully returns a

Class

object,
that is the result of this method. If it throws a

ClassNotFoundException

, the search continues with the next
ClassLoader. If it throws another exception, the exception is
propagated from this method. If the end of the list is
reached, a

ClassNotFoundException

is thrown.

Be aware that if a ClassLoader in the ClassLoaderRepository
calls this method from its

loadClass

method, it exposes itself to a deadlock if another
ClassLoader in the ClassLoaderRepository does the same thing at
the same time. The

loadClassBefore(java.lang.ClassLoader, java.lang.String)

method is
recommended to avoid the risk of deadlock.

**Parameters:** className

- The name of the class to be loaded.
**Parameters:** exclude

- The class loader to be excluded. May be null,
in which case this method is equivalent to

loadClass(className)

.
**Returns:** the loaded class.
**Throws:** ClassNotFoundException

- The specified class could not
be found.

- loadClassBefore

```java
Class
<?> loadClassBefore​(
ClassLoader
stop,

String
className)
throws
ClassNotFoundException
```

Load the given class name through the list of class loaders,
stopping at the given one. Each ClassLoader in turn from the
ClassLoaderRepository is asked to load the class via its

ClassLoader.loadClass(String)

method. If it successfully
returns a

Class

object, that is the result of this
method. If it throws a

ClassNotFoundException

, the
search continues with the next ClassLoader. If it throws
another exception, the exception is propagated from this
method. If the search reaches

stop

or the end of
the list, a

ClassNotFoundException

is thrown.

Typically this method is called from the

loadClass

method of

stop

, to consult loaders that appear before it
in the

ClassLoaderRepository

. By stopping the
search as soon as

stop

is reached, a potential
deadlock with concurrent class loading is avoided.

**Parameters:** className

- The name of the class to be loaded.
**Parameters:** stop

- The class loader at which to stop. May be null, in
which case this method is equivalent to

loadClass(className)

.
**Returns:** the loaded class.
**Throws:** ClassNotFoundException

- The specified class could not
be found.

---

#### Method Detail

loadClass

```java
Class
<?> loadClass​(
String
className)
throws
ClassNotFoundException
```

Load the given class name through the list of class loaders.
Each ClassLoader in turn from the ClassLoaderRepository is
asked to load the class via its

ClassLoader.loadClass(String)

method. If it successfully
returns a

Class

object, that is the result of this
method. If it throws a

ClassNotFoundException

, the
search continues with the next ClassLoader. If it throws
another exception, the exception is propagated from this
method. If the end of the list is reached, a

ClassNotFoundException

is thrown.

**Parameters:** className

- The name of the class to be loaded.
**Returns:** the loaded class.
**Throws:** ClassNotFoundException

- The specified class could not be
found.

---

#### loadClass

Class

<?> loadClass​(

String

className)
throws

ClassNotFoundException

Load the given class name through the list of class loaders.
Each ClassLoader in turn from the ClassLoaderRepository is
asked to load the class via its

ClassLoader.loadClass(String)

method. If it successfully
returns a

Class

object, that is the result of this
method. If it throws a

ClassNotFoundException

, the
search continues with the next ClassLoader. If it throws
another exception, the exception is propagated from this
method. If the end of the list is reached, a

ClassNotFoundException

is thrown.

loadClassWithout

```java
Class
<?> loadClassWithout​(
ClassLoader
exclude,

String
className)
throws
ClassNotFoundException
```

Load the given class name through the list of class loaders,
excluding the given one. Each ClassLoader in turn from the
ClassLoaderRepository, except

exclude

, is asked to
load the class via its

ClassLoader.loadClass(String)

method. If it successfully returns a

Class

object,
that is the result of this method. If it throws a

ClassNotFoundException

, the search continues with the next
ClassLoader. If it throws another exception, the exception is
propagated from this method. If the end of the list is
reached, a

ClassNotFoundException

is thrown.

Be aware that if a ClassLoader in the ClassLoaderRepository
calls this method from its

loadClass

method, it exposes itself to a deadlock if another
ClassLoader in the ClassLoaderRepository does the same thing at
the same time. The

loadClassBefore(java.lang.ClassLoader, java.lang.String)

method is
recommended to avoid the risk of deadlock.

**Parameters:** className

- The name of the class to be loaded.
**Parameters:** exclude

- The class loader to be excluded. May be null,
in which case this method is equivalent to

loadClass(className)

.
**Returns:** the loaded class.
**Throws:** ClassNotFoundException

- The specified class could not
be found.

---

#### loadClassWithout

Class

<?> loadClassWithout​(

ClassLoader

exclude,

String

className)
throws

ClassNotFoundException

Load the given class name through the list of class loaders,
excluding the given one. Each ClassLoader in turn from the
ClassLoaderRepository, except

exclude

, is asked to
load the class via its

ClassLoader.loadClass(String)

method. If it successfully returns a

Class

object,
that is the result of this method. If it throws a

ClassNotFoundException

, the search continues with the next
ClassLoader. If it throws another exception, the exception is
propagated from this method. If the end of the list is
reached, a

ClassNotFoundException

is thrown.

Be aware that if a ClassLoader in the ClassLoaderRepository
calls this method from its

loadClass

method, it exposes itself to a deadlock if another
ClassLoader in the ClassLoaderRepository does the same thing at
the same time. The

loadClassBefore(java.lang.ClassLoader, java.lang.String)

method is
recommended to avoid the risk of deadlock.

Load the given class name through the list of class loaders,
excluding the given one. Each ClassLoader in turn from the
ClassLoaderRepository, except

exclude

, is asked to
load the class via its

ClassLoader.loadClass(String)

method. If it successfully returns a

Class

object,
that is the result of this method. If it throws a

ClassNotFoundException

, the search continues with the next
ClassLoader. If it throws another exception, the exception is
propagated from this method. If the end of the list is
reached, a

ClassNotFoundException

is thrown.

Be aware that if a ClassLoader in the ClassLoaderRepository
calls this method from its

loadClass

method, it exposes itself to a deadlock if another
ClassLoader in the ClassLoaderRepository does the same thing at
the same time. The

loadClassBefore(java.lang.ClassLoader, java.lang.String)

method is
recommended to avoid the risk of deadlock.

loadClassBefore

```java
Class
<?> loadClassBefore​(
ClassLoader
stop,

String
className)
throws
ClassNotFoundException
```

Load the given class name through the list of class loaders,
stopping at the given one. Each ClassLoader in turn from the
ClassLoaderRepository is asked to load the class via its

ClassLoader.loadClass(String)

method. If it successfully
returns a

Class

object, that is the result of this
method. If it throws a

ClassNotFoundException

, the
search continues with the next ClassLoader. If it throws
another exception, the exception is propagated from this
method. If the search reaches

stop

or the end of
the list, a

ClassNotFoundException

is thrown.

Typically this method is called from the

loadClass

method of

stop

, to consult loaders that appear before it
in the

ClassLoaderRepository

. By stopping the
search as soon as

stop

is reached, a potential
deadlock with concurrent class loading is avoided.

**Parameters:** className

- The name of the class to be loaded.
**Parameters:** stop

- The class loader at which to stop. May be null, in
which case this method is equivalent to

loadClass(className)

.
**Returns:** the loaded class.
**Throws:** ClassNotFoundException

- The specified class could not
be found.

---

#### loadClassBefore

Class

<?> loadClassBefore​(

ClassLoader

stop,

String

className)
throws

ClassNotFoundException

Load the given class name through the list of class loaders,
stopping at the given one. Each ClassLoader in turn from the
ClassLoaderRepository is asked to load the class via its

ClassLoader.loadClass(String)

method. If it successfully
returns a

Class

object, that is the result of this
method. If it throws a

ClassNotFoundException

, the
search continues with the next ClassLoader. If it throws
another exception, the exception is propagated from this
method. If the search reaches

stop

or the end of
the list, a

ClassNotFoundException

is thrown.

Typically this method is called from the

loadClass

method of

stop

, to consult loaders that appear before it
in the

ClassLoaderRepository

. By stopping the
search as soon as

stop

is reached, a potential
deadlock with concurrent class loading is avoided.

Load the given class name through the list of class loaders,
stopping at the given one. Each ClassLoader in turn from the
ClassLoaderRepository is asked to load the class via its

ClassLoader.loadClass(String)

method. If it successfully
returns a

Class

object, that is the result of this
method. If it throws a

ClassNotFoundException

, the
search continues with the next ClassLoader. If it throws
another exception, the exception is propagated from this
method. If the search reaches

stop

or the end of
the list, a

ClassNotFoundException

is thrown.

Typically this method is called from the

loadClass

method of

stop

, to consult loaders that appear before it
in the

ClassLoaderRepository

. By stopping the
search as soon as

stop

is reached, a potential
deadlock with concurrent class loading is avoided.

---

