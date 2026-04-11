# Class IIORegistry

**Source:** `java.desktop\javax\imageio\spi\IIORegistry.html`

### Class Description

```java
public final class
IIORegistry

extends
ServiceRegistry
```

A registry for Image I/O service provider instances. Service provider
classes may be discovered at runtime by the mechanisms documented in

ServiceLoader

.

The intent is that it be relatively inexpensive to load and inspect
all available Image I/O service provider classes.
These classes may then be used to locate and instantiate
more heavyweight classes that will perform actual work, in this
case instances of

ImageReader

,

ImageWriter

,

ImageTranscoder

,

ImageInputStream

, and

ImageOutputStream

.

Service providers included in the Java runtime are automatically
loaded as soon as this class is instantiated.

When the

registerApplicationClasspathSpis

method
is called, additional service provider instances will be discovered
using

ServiceLoader

.

It is also possible to manually add service providers not found
automatically, as well as to remove those that are using the
interfaces of the

ServiceRegistry

class. Thus
the application may customize the contents of the registry as it
sees fit.

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
IIORegistry
getDefaultInstance()

Returns the default

IIORegistry

instance used by
the Image I/O API. This instance should be used for all
registry functions.

Each

ThreadGroup

will receive its own
instance; this allows different

Applet

s in the
same browser (for example) to each have their own registry.

**Returns:**
- the default registry for the current

ThreadGroup

.

---

#### public void registerApplicationClasspathSpis()

Registers all available service providers found on the
application class path, using the default

ClassLoader

. This method is typically invoked by
the

ImageIO.scanForPlugins

method.

**See Also:**
- ImageIO.scanForPlugins()

,

ClassLoader.getResources(java.lang.String)

---

### Additional Sections

#### Class IIORegistry

java.lang.Object

- javax.imageio.spi.ServiceRegistry
- - javax.imageio.spi.IIORegistry

javax.imageio.spi.ServiceRegistry

- javax.imageio.spi.IIORegistry

javax.imageio.spi.IIORegistry

```java
public final class
IIORegistry

extends
ServiceRegistry
```

A registry for Image I/O service provider instances. Service provider
classes may be discovered at runtime by the mechanisms documented in

ServiceLoader

.

The intent is that it be relatively inexpensive to load and inspect
all available Image I/O service provider classes.
These classes may then be used to locate and instantiate
more heavyweight classes that will perform actual work, in this
case instances of

ImageReader

,

ImageWriter

,

ImageTranscoder

,

ImageInputStream

, and

ImageOutputStream

.

Service providers included in the Java runtime are automatically
loaded as soon as this class is instantiated.

When the

registerApplicationClasspathSpis

method
is called, additional service provider instances will be discovered
using

ServiceLoader

.

It is also possible to manually add service providers not found
automatically, as well as to remove those that are using the
interfaces of the

ServiceRegistry

class. Thus
the application may customize the contents of the registry as it
sees fit.

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

public final class

IIORegistry

extends

ServiceRegistry

A registry for Image I/O service provider instances. Service provider
classes may be discovered at runtime by the mechanisms documented in

ServiceLoader

.

The intent is that it be relatively inexpensive to load and inspect
all available Image I/O service provider classes.
These classes may then be used to locate and instantiate
more heavyweight classes that will perform actual work, in this
case instances of

ImageReader

,

ImageWriter

,

ImageTranscoder

,

ImageInputStream

, and

ImageOutputStream

.

Service providers included in the Java runtime are automatically
loaded as soon as this class is instantiated.

When the

registerApplicationClasspathSpis

method
is called, additional service provider instances will be discovered
using

ServiceLoader

.

It is also possible to manually add service providers not found
automatically, as well as to remove those that are using the
interfaces of the

ServiceRegistry

class. Thus
the application may customize the contents of the registry as it
sees fit.

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

When the

registerApplicationClasspathSpis

method
is called, additional service provider instances will be discovered
using

ServiceLoader

.

It is also possible to manually add service providers not found
automatically, as well as to remove those that are using the
interfaces of the

ServiceRegistry

class. Thus
the application may customize the contents of the registry as it
sees fit.

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

It is also possible to manually add service providers not found
automatically, as well as to remove those that are using the
interfaces of the

ServiceRegistry

class. Thus
the application may customize the contents of the registry as it
sees fit.

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.imageio.spi.

ServiceRegistry

ServiceRegistry.Filter

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

IIORegistry

getDefaultInstance

()

Returns the default

IIORegistry

instance used by
the Image I/O API.

void

registerApplicationClasspathSpis

()

Registers all available service providers found on the
application class path, using the default

ClassLoader

.

- Methods declared in class javax.imageio.spi.

ServiceRegistry

contains

,

deregisterAll

,

deregisterAll

,

deregisterServiceProvider

,

deregisterServiceProvider

,

finalize

,

getCategories

,

getServiceProviderByClass

,

getServiceProviders

,

getServiceProviders

,

lookupProviders

,

lookupProviders

,

registerServiceProvider

,

registerServiceProvider

,

registerServiceProviders

,

setOrdering

,

unsetOrdering

- Methods declared in class java.lang.

Object

clone

,

equals

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

Nested Class Summary

- Nested classes/interfaces declared in class javax.imageio.spi.

ServiceRegistry

ServiceRegistry.Filter

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.imageio.spi.

ServiceRegistry

ServiceRegistry.Filter

---

#### Nested classes/interfaces declared in class javax.imageio.spi. ServiceRegistry

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

IIORegistry

getDefaultInstance

()

Returns the default

IIORegistry

instance used by
the Image I/O API.

void

registerApplicationClasspathSpis

()

Registers all available service providers found on the
application class path, using the default

ClassLoader

.

- Methods declared in class javax.imageio.spi.

ServiceRegistry

contains

,

deregisterAll

,

deregisterAll

,

deregisterServiceProvider

,

deregisterServiceProvider

,

finalize

,

getCategories

,

getServiceProviderByClass

,

getServiceProviders

,

getServiceProviders

,

lookupProviders

,

lookupProviders

,

registerServiceProvider

,

registerServiceProvider

,

registerServiceProviders

,

setOrdering

,

unsetOrdering

- Methods declared in class java.lang.

Object

clone

,

equals

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

Returns the default

IIORegistry

instance used by
the Image I/O API.

Registers all available service providers found on the
application class path, using the default

ClassLoader

.

Methods declared in class javax.imageio.spi.

ServiceRegistry

contains

,

deregisterAll

,

deregisterAll

,

deregisterServiceProvider

,

deregisterServiceProvider

,

finalize

,

getCategories

,

getServiceProviderByClass

,

getServiceProviders

,

getServiceProviders

,

lookupProviders

,

lookupProviders

,

registerServiceProvider

,

registerServiceProvider

,

registerServiceProviders

,

setOrdering

,

unsetOrdering

---

#### Methods declared in class javax.imageio.spi. ServiceRegistry

Methods declared in class java.lang.

Object

clone

,

equals

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

============ METHOD DETAIL ==========

- Method Detail

- getDefaultInstance

```java
public static
IIORegistry
getDefaultInstance()
```

Returns the default

IIORegistry

instance used by
the Image I/O API. This instance should be used for all
registry functions.

Each

ThreadGroup

will receive its own
instance; this allows different

Applet

s in the
same browser (for example) to each have their own registry.

**Returns:** the default registry for the current

ThreadGroup

.

- registerApplicationClasspathSpis

```java
public void registerApplicationClasspathSpis()
```

Registers all available service providers found on the
application class path, using the default

ClassLoader

. This method is typically invoked by
the

ImageIO.scanForPlugins

method.

**See Also:** ImageIO.scanForPlugins()

,

ClassLoader.getResources(java.lang.String)

Method Detail

- getDefaultInstance

```java
public static
IIORegistry
getDefaultInstance()
```

Returns the default

IIORegistry

instance used by
the Image I/O API. This instance should be used for all
registry functions.

Each

ThreadGroup

will receive its own
instance; this allows different

Applet

s in the
same browser (for example) to each have their own registry.

**Returns:** the default registry for the current

ThreadGroup

.

- registerApplicationClasspathSpis

```java
public void registerApplicationClasspathSpis()
```

Registers all available service providers found on the
application class path, using the default

ClassLoader

. This method is typically invoked by
the

ImageIO.scanForPlugins

method.

**See Also:** ImageIO.scanForPlugins()

,

ClassLoader.getResources(java.lang.String)

---

#### Method Detail

getDefaultInstance

```java
public static
IIORegistry
getDefaultInstance()
```

Returns the default

IIORegistry

instance used by
the Image I/O API. This instance should be used for all
registry functions.

Each

ThreadGroup

will receive its own
instance; this allows different

Applet

s in the
same browser (for example) to each have their own registry.

**Returns:** the default registry for the current

ThreadGroup

.

---

#### getDefaultInstance

public static

IIORegistry

getDefaultInstance()

Returns the default

IIORegistry

instance used by
the Image I/O API. This instance should be used for all
registry functions.

Each

ThreadGroup

will receive its own
instance; this allows different

Applet

s in the
same browser (for example) to each have their own registry.

Each

ThreadGroup

will receive its own
instance; this allows different

Applet

s in the
same browser (for example) to each have their own registry.

registerApplicationClasspathSpis

```java
public void registerApplicationClasspathSpis()
```

Registers all available service providers found on the
application class path, using the default

ClassLoader

. This method is typically invoked by
the

ImageIO.scanForPlugins

method.

**See Also:** ImageIO.scanForPlugins()

,

ClassLoader.getResources(java.lang.String)

---

#### registerApplicationClasspathSpis

public void registerApplicationClasspathSpis()

Registers all available service providers found on the
application class path, using the default

ClassLoader

. This method is typically invoked by
the

ImageIO.scanForPlugins

method.

---

