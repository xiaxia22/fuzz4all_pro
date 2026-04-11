# Class ServiceRegistry

**Source:** `java.desktop\javax\imageio\spi\ServiceRegistry.html`

### Class Description

```java
public class
ServiceRegistry

extends
Object
```

A registry for service provider instances for Image I/O service types.

Service providers are stored in one or more

categories

,
each of which is defined by a class or interface (described by a

Class

object) that all of its members must implement.

The set of categories supported by this class is limited
to the following standard Image I/O service types:

- ImageInputStreamSpi

ImageOutputStreamSpi

ImageReaderSpi

ImageTranscoderSpi

ImageWriterSpi

An attempt to load a provider that is not a subtype of one of the
above types will result in

IllegalArgumentException

.

For the general mechanism to load service providers, see

ServiceLoader

, which is
the underlying standard mechanism used by this class.

Only a single instance of a given leaf class (that is, the
actual class returned by

getClass()

, as opposed to any
inherited classes or interfaces) may be registered. That is,
suppose that the

com.mycompany.mypkg.GreenImageReaderProvider

class
is a subclass of

javax.imageio.spi.ImageReaderSpi

.
If a

GreenImageReaderProvider

instance is
registered, it will be stored in the category defined by the

ImageReaderSpi

class. If a new instance of

GreenImageReaderProvider

is registered, it will replace
the previous instance. In practice, service provider objects are
usually singletons so this behavior is appropriate.

The service provider classes should be lightweight and
quick to load. Implementations of these interfaces should avoid
complex dependencies on other classes and on native code. The usual
pattern for more complex services is to register a lightweight
proxy for the heavyweight service.

An application may customize the contents of a registry as it
sees fit, so long as it has the appropriate runtime permission.

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

**Direct Known Subclasses:** IIORegistry

---

### Field Details

*No entries found.*

### Constructor Details

#### public ServiceRegistry​(
Iterator
<
Class
<?>> categories)

Constructs a

ServiceRegistry

instance with a
set of categories taken from the

categories

argument. The categories must all be members of the set
of service types listed in the class specification.

**Parameters:**
- categories

- an

Iterator

containing

Class

objects to be used to define categories.

**Throws:**
- IllegalArgumentException

- if

categories

is

null

, or if
one of the categories is not an allowed service type.

---

### Method Details

#### public static <T>
Iterator
<T> lookupProviders​(
Class
<T> providerClass,

ClassLoader
loader)

Searches for implementations of a particular service class
using the given class loader.

The service class must be one of the service types listed
in the class specification. If it is not,

IllegalArgumentException

will be thrown.

This method transforms the name of the given service class
into a provider-configuration filename as described in the
class comment and then uses the

getResources

method of the given class loader to find all available files
with that name. These files are then read and parsed to
produce a list of provider-class names. The iterator that is
returned uses the given class loader to look up and then
instantiate each element of the list.

Because it is possible for extensions to be installed into
a running Java virtual machine, this method may return
different results each time it is invoked.

**Parameters:**
- providerClass

- a

Class

object indicating the
class or interface of the service providers being detected.
- loader

- the class loader to be used to load
provider-configuration files and instantiate provider classes,
or

null

if the system class loader (or, failing that
the bootstrap class loader) is to be used.

**Returns:**
- An

Iterator

that yields provider objects
for the given service, in some arbitrary order. The iterator
will throw an

Error

if a provider-configuration
file violates the specified format or if a provider class
cannot be found and instantiated.

**Throws:**
- IllegalArgumentException

- if

providerClass

is

null

, or if it is
not one of the allowed service types.

**Type Parameters:**
- T

- the type of the providerClass.

---

#### public static <T>
Iterator
<T> lookupProviders​(
Class
<T> providerClass)

Locates and incrementally instantiates the available providers
of a given service using the context class loader. This
convenience method is equivalent to:

```java
ClassLoader cl = Thread.currentThread().getContextClassLoader();
return Service.providers(service, cl);
```

The service class must be one of the service types listed
in the class specification. If it is not,

IllegalArgumentException

will be thrown.

**Parameters:**
- providerClass

- a

Class

object indicating the
class or interface of the service providers being detected.

**Returns:**
- An

Iterator

that yields provider objects
for the given service, in some arbitrary order. The iterator
will throw an

Error

if a provider-configuration
file violates the specified format or if a provider class
cannot be found and instantiated.

**Throws:**
- IllegalArgumentException

- if

providerClass

is

null

, or if it is
not one of the allowed service types.

**Type Parameters:**
- T

- the type of the providerClass.

---

#### public
Iterator
<
Class
<?>> getCategories()

Returns an

Iterator

of

Class

objects
indicating the current set of categories. The iterator will be
empty if no categories exist.

**Returns:**
- an

Iterator

containing

Class

objects.

---

#### public <T> boolean registerServiceProvider​(T provider,

Class
<T> category)

Adds a service provider object to the registry. The provider
is associated with the given category.

If

provider

implements the

RegisterableService

interface, its

onRegistration

method will be called. Its

onDeregistration

method will be called each time
it is deregistered from a category, for example if a
category is removed or the registry is garbage collected.

**Parameters:**
- provider

- the service provide object to be registered.
- category

- the category under which to register the
provider.

**Returns:**
- true if no provider of the same class was previously
registered in the same category category.

**Throws:**
- IllegalArgumentException

- if

provider

is

null

.
- IllegalArgumentException

- if there is no category
corresponding to

category

.
- ClassCastException

- if provider does not implement
the

Class

defined by

category

.

**Type Parameters:**
- T

- the type of the provider.

---

#### public void registerServiceProvider​(
Object
provider)

Adds a service provider object to the registry. The provider
is associated within each category present in the registry
whose

Class

it implements.

If

provider

implements the

RegisterableService

interface, its

onRegistration

method will be called once for each
category it is registered under. Its

onDeregistration

method will be called each time
it is deregistered from a category or when the registry is
finalized.

**Parameters:**
- provider

- the service provider object to be registered.

**Throws:**
- IllegalArgumentException

- if

provider

is

null

.

---

#### public void registerServiceProviders​(
Iterator
<?> providers)

Adds a set of service provider objects, taken from an

Iterator

to the registry. Each provider is
associated within each category present in the registry whose

Class

it implements.

For each entry of

providers

that implements
the

RegisterableService

interface, its

onRegistration

method will be called once for each
category it is registered under. Its

onDeregistration

method will be called each time
it is deregistered from a category or when the registry is
finalized.

**Parameters:**
- providers

- an Iterator containing service provider
objects to be registered.

**Throws:**
- IllegalArgumentException

- if

providers

is

null

or contains a

null

entry.

---

#### public <T> boolean deregisterServiceProvider​(T provider,

Class
<T> category)

Removes a service provider object from the given category. If
the provider was not previously registered, nothing happens and

false

is returned. Otherwise,

true

is returned. If an object of the same class as

provider

but not equal (using

==

) to

provider

is registered, it will not be
deregistered.

If

provider

implements the

RegisterableService

interface, its

onDeregistration

method will be called.

**Parameters:**
- provider

- the service provider object to be deregistered.
- category

- the category from which to deregister the
provider.

**Returns:**
- true

if the provider was previously
registered in the same category category,

false

otherwise.

**Throws:**
- IllegalArgumentException

- if

provider

is

null

.
- IllegalArgumentException

- if there is no category
corresponding to

category

.
- ClassCastException

- if provider does not implement
the class defined by

category

.

**Type Parameters:**
- T

- the type of the provider.

---

#### public void deregisterServiceProvider​(
Object
provider)

Removes a service provider object from all categories that
contain it.

**Parameters:**
- provider

- the service provider object to be deregistered.

**Throws:**
- IllegalArgumentException

- if

provider

is

null

.

---

#### public boolean contains​(
Object
provider)

Returns

true

if

provider

is currently
registered.

**Parameters:**
- provider

- the service provider object to be queried.

**Returns:**
- true

if the given provider has been
registered.

**Throws:**
- IllegalArgumentException

- if

provider

is

null

.

---

#### public <T>
Iterator
<T> getServiceProviders​(
Class
<T> category,
boolean useOrdering)

Returns an

Iterator

containing all registered
service providers in the given category. If

useOrdering

is

false

, the iterator
will return all of the server provider objects in an arbitrary
order. Otherwise, the ordering will respect any pairwise
orderings that have been set. If the graph of pairwise
orderings contains cycles, any providers that belong to a cycle
will not be returned.

**Parameters:**
- category

- the category to be retrieved from.
- useOrdering

-

true

if pairwise orderings
should be taken account in ordering the returned objects.

**Returns:**
- an

Iterator

containing service provider
objects from the given category, possibly in order.

**Throws:**
- IllegalArgumentException

- if there is no category
corresponding to

category

.

**Type Parameters:**
- T

- the type of the category.

---

#### public <T>
Iterator
<T> getServiceProviders​(
Class
<T> category,

ServiceRegistry.Filter
filter,
boolean useOrdering)

Returns an

Iterator

containing service provider
objects within a given category that satisfy a criterion
imposed by the supplied

ServiceRegistry.Filter

object's

filter

method.

The

useOrdering

argument controls the
ordering of the results using the same rules as

getServiceProviders(Class, boolean)

.

**Parameters:**
- category

- the category to be retrieved from.
- filter

- an instance of

ServiceRegistry.Filter

whose

filter

method will be invoked.
- useOrdering

-

true

if pairwise orderings
should be taken account in ordering the returned objects.

**Returns:**
- an

Iterator

containing service provider
objects from the given category, possibly in order.

**Throws:**
- IllegalArgumentException

- if there is no category
corresponding to

category

.

**Type Parameters:**
- T

- the type of the category.

---

#### public <T> T getServiceProviderByClass​(
Class
<T> providerClass)

Returns the currently registered service provider object that
is of the given class type. At most one object of a given
class is allowed to be registered at any given time. If no
registered object has the desired class type,

null

is returned.

**Parameters:**
- providerClass

- the

Class

of the desired
service provider object.

**Returns:**
- a currently registered service provider object with the
desired

Class

type, or

null

is none is
present.

**Throws:**
- IllegalArgumentException

- if

providerClass

is

null

.

**Type Parameters:**
- T

- the type of the provider.

---

#### public <T> boolean setOrdering​(
Class
<T> category,
T firstProvider,
T secondProvider)

Sets a pairwise ordering between two service provider objects
within a given category. If one or both objects are not
currently registered within the given category, or if the
desired ordering is already set, nothing happens and

false

is returned. If the providers previously
were ordered in the reverse direction, that ordering is
removed.

The ordering will be used by the

getServiceProviders

methods when their

useOrdering

argument is

true

.

**Parameters:**
- category

- a

Class

object indicating the
category under which the preference is to be established.
- firstProvider

- the preferred provider.
- secondProvider

- the provider to which

firstProvider

is preferred.

**Returns:**
- true

if a previously unset ordering
was established.

**Throws:**
- IllegalArgumentException

- if either provider is

null

or they are the same object.
- IllegalArgumentException

- if there is no category
corresponding to

category

.

**Type Parameters:**
- T

- the type of the category.

---

#### public <T> boolean unsetOrdering​(
Class
<T> category,
T firstProvider,
T secondProvider)

Sets a pairwise ordering between two service provider objects
within a given category. If one or both objects are not
currently registered within the given category, or if no
ordering is currently set between them, nothing happens
and

false

is returned.

The ordering will be used by the

getServiceProviders

methods when their

useOrdering

argument is

true

.

**Parameters:**
- category

- a

Class

object indicating the
category under which the preference is to be disestablished.
- firstProvider

- the formerly preferred provider.
- secondProvider

- the provider to which

firstProvider

was formerly preferred.

**Returns:**
- true

if a previously set ordering was
disestablished.

**Throws:**
- IllegalArgumentException

- if either provider is

null

or they are the same object.
- IllegalArgumentException

- if there is no category
corresponding to

category

.

**Type Parameters:**
- T

- the type of the category.

---

#### public void deregisterAll​(
Class
<?> category)

Deregisters all service provider object currently registered
under the given category.

**Parameters:**
- category

- the category to be emptied.

**Throws:**
- IllegalArgumentException

- if there is no category
corresponding to

category

.

---

#### public void deregisterAll()

Deregisters all currently registered service providers from all
categories.

---

#### @Deprecated
(
since
="9")
public void finalize()
throws
Throwable

Finalizes this object prior to garbage collection. The

deregisterAll

method is called to deregister all
currently registered service providers. This method should not
be called from application code.

**Overrides:**
- finalize

in class

Object

**Throws:**
- Throwable

- if an error occurs during superclass
finalization.

**See Also:**
- WeakReference

,

PhantomReference

---

### Additional Sections

#### Class ServiceRegistry

java.lang.Object

- javax.imageio.spi.ServiceRegistry

javax.imageio.spi.ServiceRegistry

**Direct Known Subclasses:** IIORegistry

```java
public class
ServiceRegistry

extends
Object
```

A registry for service provider instances for Image I/O service types.

Service providers are stored in one or more

categories

,
each of which is defined by a class or interface (described by a

Class

object) that all of its members must implement.

The set of categories supported by this class is limited
to the following standard Image I/O service types:

- ImageInputStreamSpi

ImageOutputStreamSpi

ImageReaderSpi

ImageTranscoderSpi

ImageWriterSpi

An attempt to load a provider that is not a subtype of one of the
above types will result in

IllegalArgumentException

.

For the general mechanism to load service providers, see

ServiceLoader

, which is
the underlying standard mechanism used by this class.

Only a single instance of a given leaf class (that is, the
actual class returned by

getClass()

, as opposed to any
inherited classes or interfaces) may be registered. That is,
suppose that the

com.mycompany.mypkg.GreenImageReaderProvider

class
is a subclass of

javax.imageio.spi.ImageReaderSpi

.
If a

GreenImageReaderProvider

instance is
registered, it will be stored in the category defined by the

ImageReaderSpi

class. If a new instance of

GreenImageReaderProvider

is registered, it will replace
the previous instance. In practice, service provider objects are
usually singletons so this behavior is appropriate.

The service provider classes should be lightweight and
quick to load. Implementations of these interfaces should avoid
complex dependencies on other classes and on native code. The usual
pattern for more complex services is to register a lightweight
proxy for the heavyweight service.

An application may customize the contents of a registry as it
sees fit, so long as it has the appropriate runtime permission.

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

**See Also:** RegisterableService

,

ServiceLoader

public class

ServiceRegistry

extends

Object

A registry for service provider instances for Image I/O service types.

Service providers are stored in one or more

categories

,
each of which is defined by a class or interface (described by a

Class

object) that all of its members must implement.

The set of categories supported by this class is limited
to the following standard Image I/O service types:

- ImageInputStreamSpi

ImageOutputStreamSpi

ImageReaderSpi

ImageTranscoderSpi

ImageWriterSpi

An attempt to load a provider that is not a subtype of one of the
above types will result in

IllegalArgumentException

.

For the general mechanism to load service providers, see

ServiceLoader

, which is
the underlying standard mechanism used by this class.

Only a single instance of a given leaf class (that is, the
actual class returned by

getClass()

, as opposed to any
inherited classes or interfaces) may be registered. That is,
suppose that the

com.mycompany.mypkg.GreenImageReaderProvider

class
is a subclass of

javax.imageio.spi.ImageReaderSpi

.
If a

GreenImageReaderProvider

instance is
registered, it will be stored in the category defined by the

ImageReaderSpi

class. If a new instance of

GreenImageReaderProvider

is registered, it will replace
the previous instance. In practice, service provider objects are
usually singletons so this behavior is appropriate.

The service provider classes should be lightweight and
quick to load. Implementations of these interfaces should avoid
complex dependencies on other classes and on native code. The usual
pattern for more complex services is to register a lightweight
proxy for the heavyweight service.

An application may customize the contents of a registry as it
sees fit, so long as it has the appropriate runtime permission.

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

Service providers are stored in one or more

categories

,
each of which is defined by a class or interface (described by a

Class

object) that all of its members must implement.

The set of categories supported by this class is limited
to the following standard Image I/O service types:

- ImageInputStreamSpi

ImageOutputStreamSpi

ImageReaderSpi

ImageTranscoderSpi

ImageWriterSpi

An attempt to load a provider that is not a subtype of one of the
above types will result in

IllegalArgumentException

.

For the general mechanism to load service providers, see

ServiceLoader

, which is
the underlying standard mechanism used by this class.

Only a single instance of a given leaf class (that is, the
actual class returned by

getClass()

, as opposed to any
inherited classes or interfaces) may be registered. That is,
suppose that the

com.mycompany.mypkg.GreenImageReaderProvider

class
is a subclass of

javax.imageio.spi.ImageReaderSpi

.
If a

GreenImageReaderProvider

instance is
registered, it will be stored in the category defined by the

ImageReaderSpi

class. If a new instance of

GreenImageReaderProvider

is registered, it will replace
the previous instance. In practice, service provider objects are
usually singletons so this behavior is appropriate.

The service provider classes should be lightweight and
quick to load. Implementations of these interfaces should avoid
complex dependencies on other classes and on native code. The usual
pattern for more complex services is to register a lightweight
proxy for the heavyweight service.

An application may customize the contents of a registry as it
sees fit, so long as it has the appropriate runtime permission.

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

The set of categories supported by this class is limited
to the following standard Image I/O service types:

- ImageInputStreamSpi

ImageOutputStreamSpi

ImageReaderSpi

ImageTranscoderSpi

ImageWriterSpi

An attempt to load a provider that is not a subtype of one of the
above types will result in

IllegalArgumentException

.

For the general mechanism to load service providers, see

ServiceLoader

, which is
the underlying standard mechanism used by this class.

Only a single instance of a given leaf class (that is, the
actual class returned by

getClass()

, as opposed to any
inherited classes or interfaces) may be registered. That is,
suppose that the

com.mycompany.mypkg.GreenImageReaderProvider

class
is a subclass of

javax.imageio.spi.ImageReaderSpi

.
If a

GreenImageReaderProvider

instance is
registered, it will be stored in the category defined by the

ImageReaderSpi

class. If a new instance of

GreenImageReaderProvider

is registered, it will replace
the previous instance. In practice, service provider objects are
usually singletons so this behavior is appropriate.

The service provider classes should be lightweight and
quick to load. Implementations of these interfaces should avoid
complex dependencies on other classes and on native code. The usual
pattern for more complex services is to register a lightweight
proxy for the heavyweight service.

An application may customize the contents of a registry as it
sees fit, so long as it has the appropriate runtime permission.

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

ImageInputStreamSpi

ImageOutputStreamSpi

ImageReaderSpi

ImageTranscoderSpi

ImageWriterSpi

An attempt to load a provider that is not a subtype of one of the
above types will result in

IllegalArgumentException

.

For the general mechanism to load service providers, see

ServiceLoader

, which is
the underlying standard mechanism used by this class.

Only a single instance of a given leaf class (that is, the
actual class returned by

getClass()

, as opposed to any
inherited classes or interfaces) may be registered. That is,
suppose that the

com.mycompany.mypkg.GreenImageReaderProvider

class
is a subclass of

javax.imageio.spi.ImageReaderSpi

.
If a

GreenImageReaderProvider

instance is
registered, it will be stored in the category defined by the

ImageReaderSpi

class. If a new instance of

GreenImageReaderProvider

is registered, it will replace
the previous instance. In practice, service provider objects are
usually singletons so this behavior is appropriate.

The service provider classes should be lightweight and
quick to load. Implementations of these interfaces should avoid
complex dependencies on other classes and on native code. The usual
pattern for more complex services is to register a lightweight
proxy for the heavyweight service.

An application may customize the contents of a registry as it
sees fit, so long as it has the appropriate runtime permission.

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

For the general mechanism to load service providers, see

ServiceLoader

, which is
the underlying standard mechanism used by this class.

Only a single instance of a given leaf class (that is, the
actual class returned by

getClass()

, as opposed to any
inherited classes or interfaces) may be registered. That is,
suppose that the

com.mycompany.mypkg.GreenImageReaderProvider

class
is a subclass of

javax.imageio.spi.ImageReaderSpi

.
If a

GreenImageReaderProvider

instance is
registered, it will be stored in the category defined by the

ImageReaderSpi

class. If a new instance of

GreenImageReaderProvider

is registered, it will replace
the previous instance. In practice, service provider objects are
usually singletons so this behavior is appropriate.

The service provider classes should be lightweight and
quick to load. Implementations of these interfaces should avoid
complex dependencies on other classes and on native code. The usual
pattern for more complex services is to register a lightweight
proxy for the heavyweight service.

An application may customize the contents of a registry as it
sees fit, so long as it has the appropriate runtime permission.

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

Only a single instance of a given leaf class (that is, the
actual class returned by

getClass()

, as opposed to any
inherited classes or interfaces) may be registered. That is,
suppose that the

com.mycompany.mypkg.GreenImageReaderProvider

class
is a subclass of

javax.imageio.spi.ImageReaderSpi

.
If a

GreenImageReaderProvider

instance is
registered, it will be stored in the category defined by the

ImageReaderSpi

class. If a new instance of

GreenImageReaderProvider

is registered, it will replace
the previous instance. In practice, service provider objects are
usually singletons so this behavior is appropriate.

The service provider classes should be lightweight and
quick to load. Implementations of these interfaces should avoid
complex dependencies on other classes and on native code. The usual
pattern for more complex services is to register a lightweight
proxy for the heavyweight service.

An application may customize the contents of a registry as it
sees fit, so long as it has the appropriate runtime permission.

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

The service provider classes should be lightweight and
quick to load. Implementations of these interfaces should avoid
complex dependencies on other classes and on native code. The usual
pattern for more complex services is to register a lightweight
proxy for the heavyweight service.

An application may customize the contents of a registry as it
sees fit, so long as it has the appropriate runtime permission.

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

An application may customize the contents of a registry as it
sees fit, so long as it has the appropriate runtime permission.

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

For information on how to create and deploy service providers,
refer to the documentation on

ServiceLoader

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static interface

ServiceRegistry.Filter

A simple filter interface used by

ServiceRegistry.getServiceProviders

to select
providers matching an arbitrary criterion.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ServiceRegistry

​(

Iterator

<

Class

<?>> categories)

Constructs a

ServiceRegistry

instance with a
set of categories taken from the

categories

argument.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

contains

​(

Object

provider)

Returns

true

if

provider

is currently
registered.

void

deregisterAll

()

Deregisters all currently registered service providers from all
categories.

void

deregisterAll

​(

Class

<?> category)

Deregisters all service provider object currently registered
under the given category.

void

deregisterServiceProvider

​(

Object

provider)

Removes a service provider object from all categories that
contain it.

<T> boolean

deregisterServiceProvider

​(T provider,

Class

<T> category)

Removes a service provider object from the given category.

void

finalize

()

Deprecated.

The

finalize

method has been deprecated.

Iterator

<

Class

<?>>

getCategories

()

Returns an

Iterator

of

Class

objects
indicating the current set of categories.

<T> T

getServiceProviderByClass

​(

Class

<T> providerClass)

Returns the currently registered service provider object that
is of the given class type.

<T>

Iterator

<T>

getServiceProviders

​(

Class

<T> category,
boolean useOrdering)

Returns an

Iterator

containing all registered
service providers in the given category.

<T>

Iterator

<T>

getServiceProviders

​(

Class

<T> category,

ServiceRegistry.Filter

filter,
boolean useOrdering)

Returns an

Iterator

containing service provider
objects within a given category that satisfy a criterion
imposed by the supplied

ServiceRegistry.Filter

object's

filter

method.

static <T>

Iterator

<T>

lookupProviders

​(

Class

<T> providerClass)

Locates and incrementally instantiates the available providers
of a given service using the context class loader.

static <T>

Iterator

<T>

lookupProviders

​(

Class

<T> providerClass,

ClassLoader

loader)

Searches for implementations of a particular service class
using the given class loader.

void

registerServiceProvider

​(

Object

provider)

Adds a service provider object to the registry.

<T> boolean

registerServiceProvider

​(T provider,

Class

<T> category)

Adds a service provider object to the registry.

void

registerServiceProviders

​(

Iterator

<?> providers)

Adds a set of service provider objects, taken from an

Iterator

to the registry.

<T> boolean

setOrdering

​(

Class

<T> category,
T firstProvider,
T secondProvider)

Sets a pairwise ordering between two service provider objects
within a given category.

<T> boolean

unsetOrdering

​(

Class

<T> category,
T firstProvider,
T secondProvider)

Sets a pairwise ordering between two service provider objects
within a given category.

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

Nested Classes

Modifier and Type

Class

Description

static interface

ServiceRegistry.Filter

A simple filter interface used by

ServiceRegistry.getServiceProviders

to select
providers matching an arbitrary criterion.

---

#### Nested Class Summary

A simple filter interface used by

ServiceRegistry.getServiceProviders

to select
providers matching an arbitrary criterion.

Constructor Summary

Constructors

Constructor

Description

ServiceRegistry

​(

Iterator

<

Class

<?>> categories)

Constructs a

ServiceRegistry

instance with a
set of categories taken from the

categories

argument.

---

#### Constructor Summary

Constructs a

ServiceRegistry

instance with a
set of categories taken from the

categories

argument.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

contains

​(

Object

provider)

Returns

true

if

provider

is currently
registered.

void

deregisterAll

()

Deregisters all currently registered service providers from all
categories.

void

deregisterAll

​(

Class

<?> category)

Deregisters all service provider object currently registered
under the given category.

void

deregisterServiceProvider

​(

Object

provider)

Removes a service provider object from all categories that
contain it.

<T> boolean

deregisterServiceProvider

​(T provider,

Class

<T> category)

Removes a service provider object from the given category.

void

finalize

()

Deprecated.

The

finalize

method has been deprecated.

Iterator

<

Class

<?>>

getCategories

()

Returns an

Iterator

of

Class

objects
indicating the current set of categories.

<T> T

getServiceProviderByClass

​(

Class

<T> providerClass)

Returns the currently registered service provider object that
is of the given class type.

<T>

Iterator

<T>

getServiceProviders

​(

Class

<T> category,
boolean useOrdering)

Returns an

Iterator

containing all registered
service providers in the given category.

<T>

Iterator

<T>

getServiceProviders

​(

Class

<T> category,

ServiceRegistry.Filter

filter,
boolean useOrdering)

Returns an

Iterator

containing service provider
objects within a given category that satisfy a criterion
imposed by the supplied

ServiceRegistry.Filter

object's

filter

method.

static <T>

Iterator

<T>

lookupProviders

​(

Class

<T> providerClass)

Locates and incrementally instantiates the available providers
of a given service using the context class loader.

static <T>

Iterator

<T>

lookupProviders

​(

Class

<T> providerClass,

ClassLoader

loader)

Searches for implementations of a particular service class
using the given class loader.

void

registerServiceProvider

​(

Object

provider)

Adds a service provider object to the registry.

<T> boolean

registerServiceProvider

​(T provider,

Class

<T> category)

Adds a service provider object to the registry.

void

registerServiceProviders

​(

Iterator

<?> providers)

Adds a set of service provider objects, taken from an

Iterator

to the registry.

<T> boolean

setOrdering

​(

Class

<T> category,
T firstProvider,
T secondProvider)

Sets a pairwise ordering between two service provider objects
within a given category.

<T> boolean

unsetOrdering

​(

Class

<T> category,
T firstProvider,
T secondProvider)

Sets a pairwise ordering between two service provider objects
within a given category.

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

Returns

true

if

provider

is currently
registered.

Deregisters all currently registered service providers from all
categories.

Deregisters all service provider object currently registered
under the given category.

Removes a service provider object from all categories that
contain it.

Removes a service provider object from the given category.

Deprecated.

The

finalize

method has been deprecated.

Returns an

Iterator

of

Class

objects
indicating the current set of categories.

Returns the currently registered service provider object that
is of the given class type.

Returns an

Iterator

containing all registered
service providers in the given category.

Returns an

Iterator

containing service provider
objects within a given category that satisfy a criterion
imposed by the supplied

ServiceRegistry.Filter

object's

filter

method.

Locates and incrementally instantiates the available providers
of a given service using the context class loader.

Searches for implementations of a particular service class
using the given class loader.

Adds a service provider object to the registry.

Adds a set of service provider objects, taken from an

Iterator

to the registry.

Sets a pairwise ordering between two service provider objects
within a given category.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ServiceRegistry

```java
public ServiceRegistry​(
Iterator
<
Class
<?>> categories)
```

Constructs a

ServiceRegistry

instance with a
set of categories taken from the

categories

argument. The categories must all be members of the set
of service types listed in the class specification.

**Parameters:** categories

- an

Iterator

containing

Class

objects to be used to define categories.
**Throws:** IllegalArgumentException

- if

categories

is

null

, or if
one of the categories is not an allowed service type.

============ METHOD DETAIL ==========

- Method Detail

- lookupProviders

```java
public static <T>
Iterator
<T> lookupProviders​(
Class
<T> providerClass,

ClassLoader
loader)
```

Searches for implementations of a particular service class
using the given class loader.

The service class must be one of the service types listed
in the class specification. If it is not,

IllegalArgumentException

will be thrown.

This method transforms the name of the given service class
into a provider-configuration filename as described in the
class comment and then uses the

getResources

method of the given class loader to find all available files
with that name. These files are then read and parsed to
produce a list of provider-class names. The iterator that is
returned uses the given class loader to look up and then
instantiate each element of the list.

Because it is possible for extensions to be installed into
a running Java virtual machine, this method may return
different results each time it is invoked.

**Type Parameters:** T

- the type of the providerClass.
**Parameters:** providerClass

- a

Class

object indicating the
class or interface of the service providers being detected.
**Parameters:** loader

- the class loader to be used to load
provider-configuration files and instantiate provider classes,
or

null

if the system class loader (or, failing that
the bootstrap class loader) is to be used.
**Returns:** An

Iterator

that yields provider objects
for the given service, in some arbitrary order. The iterator
will throw an

Error

if a provider-configuration
file violates the specified format or if a provider class
cannot be found and instantiated.
**Throws:** IllegalArgumentException

- if

providerClass

is

null

, or if it is
not one of the allowed service types.

- lookupProviders

```java
public static <T>
Iterator
<T> lookupProviders​(
Class
<T> providerClass)
```

Locates and incrementally instantiates the available providers
of a given service using the context class loader. This
convenience method is equivalent to:

```java
ClassLoader cl = Thread.currentThread().getContextClassLoader();
return Service.providers(service, cl);
```

The service class must be one of the service types listed
in the class specification. If it is not,

IllegalArgumentException

will be thrown.

**Type Parameters:** T

- the type of the providerClass.
**Parameters:** providerClass

- a

Class

object indicating the
class or interface of the service providers being detected.
**Returns:** An

Iterator

that yields provider objects
for the given service, in some arbitrary order. The iterator
will throw an

Error

if a provider-configuration
file violates the specified format or if a provider class
cannot be found and instantiated.
**Throws:** IllegalArgumentException

- if

providerClass

is

null

, or if it is
not one of the allowed service types.

- getCategories

```java
public
Iterator
<
Class
<?>> getCategories()
```

Returns an

Iterator

of

Class

objects
indicating the current set of categories. The iterator will be
empty if no categories exist.

**Returns:** an

Iterator

containing

Class

objects.

- registerServiceProvider

```java
public <T> boolean registerServiceProvider​(T provider,

Class
<T> category)
```

Adds a service provider object to the registry. The provider
is associated with the given category.

If

provider

implements the

RegisterableService

interface, its

onRegistration

method will be called. Its

onDeregistration

method will be called each time
it is deregistered from a category, for example if a
category is removed or the registry is garbage collected.

**Type Parameters:** T

- the type of the provider.
**Parameters:** provider

- the service provide object to be registered.
**Parameters:** category

- the category under which to register the
provider.
**Returns:** true if no provider of the same class was previously
registered in the same category category.
**Throws:** IllegalArgumentException

- if

provider

is

null

.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.
**Throws:** ClassCastException

- if provider does not implement
the

Class

defined by

category

.

- registerServiceProvider

```java
public void registerServiceProvider​(
Object
provider)
```

Adds a service provider object to the registry. The provider
is associated within each category present in the registry
whose

Class

it implements.

If

provider

implements the

RegisterableService

interface, its

onRegistration

method will be called once for each
category it is registered under. Its

onDeregistration

method will be called each time
it is deregistered from a category or when the registry is
finalized.

**Parameters:** provider

- the service provider object to be registered.
**Throws:** IllegalArgumentException

- if

provider

is

null

.

- registerServiceProviders

```java
public void registerServiceProviders​(
Iterator
<?> providers)
```

Adds a set of service provider objects, taken from an

Iterator

to the registry. Each provider is
associated within each category present in the registry whose

Class

it implements.

For each entry of

providers

that implements
the

RegisterableService

interface, its

onRegistration

method will be called once for each
category it is registered under. Its

onDeregistration

method will be called each time
it is deregistered from a category or when the registry is
finalized.

**Parameters:** providers

- an Iterator containing service provider
objects to be registered.
**Throws:** IllegalArgumentException

- if

providers

is

null

or contains a

null

entry.

- deregisterServiceProvider

```java
public <T> boolean deregisterServiceProvider​(T provider,

Class
<T> category)
```

Removes a service provider object from the given category. If
the provider was not previously registered, nothing happens and

false

is returned. Otherwise,

true

is returned. If an object of the same class as

provider

but not equal (using

==

) to

provider

is registered, it will not be
deregistered.

If

provider

implements the

RegisterableService

interface, its

onDeregistration

method will be called.

**Type Parameters:** T

- the type of the provider.
**Parameters:** provider

- the service provider object to be deregistered.
**Parameters:** category

- the category from which to deregister the
provider.
**Returns:** true

if the provider was previously
registered in the same category category,

false

otherwise.
**Throws:** IllegalArgumentException

- if

provider

is

null

.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.
**Throws:** ClassCastException

- if provider does not implement
the class defined by

category

.

- deregisterServiceProvider

```java
public void deregisterServiceProvider​(
Object
provider)
```

Removes a service provider object from all categories that
contain it.

**Parameters:** provider

- the service provider object to be deregistered.
**Throws:** IllegalArgumentException

- if

provider

is

null

.

- contains

```java
public boolean contains​(
Object
provider)
```

Returns

true

if

provider

is currently
registered.

**Parameters:** provider

- the service provider object to be queried.
**Returns:** true

if the given provider has been
registered.
**Throws:** IllegalArgumentException

- if

provider

is

null

.

- getServiceProviders

```java
public <T>
Iterator
<T> getServiceProviders​(
Class
<T> category,
boolean useOrdering)
```

Returns an

Iterator

containing all registered
service providers in the given category. If

useOrdering

is

false

, the iterator
will return all of the server provider objects in an arbitrary
order. Otherwise, the ordering will respect any pairwise
orderings that have been set. If the graph of pairwise
orderings contains cycles, any providers that belong to a cycle
will not be returned.

**Type Parameters:** T

- the type of the category.
**Parameters:** category

- the category to be retrieved from.
**Parameters:** useOrdering

-

true

if pairwise orderings
should be taken account in ordering the returned objects.
**Returns:** an

Iterator

containing service provider
objects from the given category, possibly in order.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.

- getServiceProviders

```java
public <T>
Iterator
<T> getServiceProviders​(
Class
<T> category,

ServiceRegistry.Filter
filter,
boolean useOrdering)
```

Returns an

Iterator

containing service provider
objects within a given category that satisfy a criterion
imposed by the supplied

ServiceRegistry.Filter

object's

filter

method.

The

useOrdering

argument controls the
ordering of the results using the same rules as

getServiceProviders(Class, boolean)

.

**Type Parameters:** T

- the type of the category.
**Parameters:** category

- the category to be retrieved from.
**Parameters:** filter

- an instance of

ServiceRegistry.Filter

whose

filter

method will be invoked.
**Parameters:** useOrdering

-

true

if pairwise orderings
should be taken account in ordering the returned objects.
**Returns:** an

Iterator

containing service provider
objects from the given category, possibly in order.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.

- getServiceProviderByClass

```java
public <T> T getServiceProviderByClass​(
Class
<T> providerClass)
```

Returns the currently registered service provider object that
is of the given class type. At most one object of a given
class is allowed to be registered at any given time. If no
registered object has the desired class type,

null

is returned.

**Type Parameters:** T

- the type of the provider.
**Parameters:** providerClass

- the

Class

of the desired
service provider object.
**Returns:** a currently registered service provider object with the
desired

Class

type, or

null

is none is
present.
**Throws:** IllegalArgumentException

- if

providerClass

is

null

.

- setOrdering

```java
public <T> boolean setOrdering​(
Class
<T> category,
T firstProvider,
T secondProvider)
```

Sets a pairwise ordering between two service provider objects
within a given category. If one or both objects are not
currently registered within the given category, or if the
desired ordering is already set, nothing happens and

false

is returned. If the providers previously
were ordered in the reverse direction, that ordering is
removed.

The ordering will be used by the

getServiceProviders

methods when their

useOrdering

argument is

true

.

**Type Parameters:** T

- the type of the category.
**Parameters:** category

- a

Class

object indicating the
category under which the preference is to be established.
**Parameters:** firstProvider

- the preferred provider.
**Parameters:** secondProvider

- the provider to which

firstProvider

is preferred.
**Returns:** true

if a previously unset ordering
was established.
**Throws:** IllegalArgumentException

- if either provider is

null

or they are the same object.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.

- unsetOrdering

```java
public <T> boolean unsetOrdering​(
Class
<T> category,
T firstProvider,
T secondProvider)
```

Sets a pairwise ordering between two service provider objects
within a given category. If one or both objects are not
currently registered within the given category, or if no
ordering is currently set between them, nothing happens
and

false

is returned.

The ordering will be used by the

getServiceProviders

methods when their

useOrdering

argument is

true

.

**Type Parameters:** T

- the type of the category.
**Parameters:** category

- a

Class

object indicating the
category under which the preference is to be disestablished.
**Parameters:** firstProvider

- the formerly preferred provider.
**Parameters:** secondProvider

- the provider to which

firstProvider

was formerly preferred.
**Returns:** true

if a previously set ordering was
disestablished.
**Throws:** IllegalArgumentException

- if either provider is

null

or they are the same object.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.

- deregisterAll

```java
public void deregisterAll​(
Class
<?> category)
```

Deregisters all service provider object currently registered
under the given category.

**Parameters:** category

- the category to be emptied.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.

- deregisterAll

```java
public void deregisterAll()
```

Deregisters all currently registered service providers from all
categories.

- finalize

```java
@Deprecated
(
since
="9")
public void finalize()
throws
Throwable
```

Deprecated.

The

finalize

method has been deprecated.
Subclasses that override

finalize

in order to perform cleanup
should be modified to use alternative cleanup mechanisms and
to remove the overriding

finalize

method.
When overriding the

finalize

method, its implementation must explicitly
ensure that

super.finalize()

is invoked as described in

Object.finalize()

.
See the specification for

Object.finalize()

for further
information about migration options.

Finalizes this object prior to garbage collection. The

deregisterAll

method is called to deregister all
currently registered service providers. This method should not
be called from application code.

**Overrides:** finalize

in class

Object
**Throws:** Throwable

- if an error occurs during superclass
finalization.
**See Also:** WeakReference

,

PhantomReference

Constructor Detail

- ServiceRegistry

```java
public ServiceRegistry​(
Iterator
<
Class
<?>> categories)
```

Constructs a

ServiceRegistry

instance with a
set of categories taken from the

categories

argument. The categories must all be members of the set
of service types listed in the class specification.

**Parameters:** categories

- an

Iterator

containing

Class

objects to be used to define categories.
**Throws:** IllegalArgumentException

- if

categories

is

null

, or if
one of the categories is not an allowed service type.

---

#### Constructor Detail

ServiceRegistry

```java
public ServiceRegistry​(
Iterator
<
Class
<?>> categories)
```

Constructs a

ServiceRegistry

instance with a
set of categories taken from the

categories

argument. The categories must all be members of the set
of service types listed in the class specification.

**Parameters:** categories

- an

Iterator

containing

Class

objects to be used to define categories.
**Throws:** IllegalArgumentException

- if

categories

is

null

, or if
one of the categories is not an allowed service type.

---

#### ServiceRegistry

public ServiceRegistry​(

Iterator

<

Class

<?>> categories)

Constructs a

ServiceRegistry

instance with a
set of categories taken from the

categories

argument. The categories must all be members of the set
of service types listed in the class specification.

Method Detail

- lookupProviders

```java
public static <T>
Iterator
<T> lookupProviders​(
Class
<T> providerClass,

ClassLoader
loader)
```

Searches for implementations of a particular service class
using the given class loader.

The service class must be one of the service types listed
in the class specification. If it is not,

IllegalArgumentException

will be thrown.

This method transforms the name of the given service class
into a provider-configuration filename as described in the
class comment and then uses the

getResources

method of the given class loader to find all available files
with that name. These files are then read and parsed to
produce a list of provider-class names. The iterator that is
returned uses the given class loader to look up and then
instantiate each element of the list.

Because it is possible for extensions to be installed into
a running Java virtual machine, this method may return
different results each time it is invoked.

**Type Parameters:** T

- the type of the providerClass.
**Parameters:** providerClass

- a

Class

object indicating the
class or interface of the service providers being detected.
**Parameters:** loader

- the class loader to be used to load
provider-configuration files and instantiate provider classes,
or

null

if the system class loader (or, failing that
the bootstrap class loader) is to be used.
**Returns:** An

Iterator

that yields provider objects
for the given service, in some arbitrary order. The iterator
will throw an

Error

if a provider-configuration
file violates the specified format or if a provider class
cannot be found and instantiated.
**Throws:** IllegalArgumentException

- if

providerClass

is

null

, or if it is
not one of the allowed service types.

- lookupProviders

```java
public static <T>
Iterator
<T> lookupProviders​(
Class
<T> providerClass)
```

Locates and incrementally instantiates the available providers
of a given service using the context class loader. This
convenience method is equivalent to:

```java
ClassLoader cl = Thread.currentThread().getContextClassLoader();
return Service.providers(service, cl);
```

The service class must be one of the service types listed
in the class specification. If it is not,

IllegalArgumentException

will be thrown.

**Type Parameters:** T

- the type of the providerClass.
**Parameters:** providerClass

- a

Class

object indicating the
class or interface of the service providers being detected.
**Returns:** An

Iterator

that yields provider objects
for the given service, in some arbitrary order. The iterator
will throw an

Error

if a provider-configuration
file violates the specified format or if a provider class
cannot be found and instantiated.
**Throws:** IllegalArgumentException

- if

providerClass

is

null

, or if it is
not one of the allowed service types.

- getCategories

```java
public
Iterator
<
Class
<?>> getCategories()
```

Returns an

Iterator

of

Class

objects
indicating the current set of categories. The iterator will be
empty if no categories exist.

**Returns:** an

Iterator

containing

Class

objects.

- registerServiceProvider

```java
public <T> boolean registerServiceProvider​(T provider,

Class
<T> category)
```

Adds a service provider object to the registry. The provider
is associated with the given category.

If

provider

implements the

RegisterableService

interface, its

onRegistration

method will be called. Its

onDeregistration

method will be called each time
it is deregistered from a category, for example if a
category is removed or the registry is garbage collected.

**Type Parameters:** T

- the type of the provider.
**Parameters:** provider

- the service provide object to be registered.
**Parameters:** category

- the category under which to register the
provider.
**Returns:** true if no provider of the same class was previously
registered in the same category category.
**Throws:** IllegalArgumentException

- if

provider

is

null

.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.
**Throws:** ClassCastException

- if provider does not implement
the

Class

defined by

category

.

- registerServiceProvider

```java
public void registerServiceProvider​(
Object
provider)
```

Adds a service provider object to the registry. The provider
is associated within each category present in the registry
whose

Class

it implements.

If

provider

implements the

RegisterableService

interface, its

onRegistration

method will be called once for each
category it is registered under. Its

onDeregistration

method will be called each time
it is deregistered from a category or when the registry is
finalized.

**Parameters:** provider

- the service provider object to be registered.
**Throws:** IllegalArgumentException

- if

provider

is

null

.

- registerServiceProviders

```java
public void registerServiceProviders​(
Iterator
<?> providers)
```

Adds a set of service provider objects, taken from an

Iterator

to the registry. Each provider is
associated within each category present in the registry whose

Class

it implements.

For each entry of

providers

that implements
the

RegisterableService

interface, its

onRegistration

method will be called once for each
category it is registered under. Its

onDeregistration

method will be called each time
it is deregistered from a category or when the registry is
finalized.

**Parameters:** providers

- an Iterator containing service provider
objects to be registered.
**Throws:** IllegalArgumentException

- if

providers

is

null

or contains a

null

entry.

- deregisterServiceProvider

```java
public <T> boolean deregisterServiceProvider​(T provider,

Class
<T> category)
```

Removes a service provider object from the given category. If
the provider was not previously registered, nothing happens and

false

is returned. Otherwise,

true

is returned. If an object of the same class as

provider

but not equal (using

==

) to

provider

is registered, it will not be
deregistered.

If

provider

implements the

RegisterableService

interface, its

onDeregistration

method will be called.

**Type Parameters:** T

- the type of the provider.
**Parameters:** provider

- the service provider object to be deregistered.
**Parameters:** category

- the category from which to deregister the
provider.
**Returns:** true

if the provider was previously
registered in the same category category,

false

otherwise.
**Throws:** IllegalArgumentException

- if

provider

is

null

.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.
**Throws:** ClassCastException

- if provider does not implement
the class defined by

category

.

- deregisterServiceProvider

```java
public void deregisterServiceProvider​(
Object
provider)
```

Removes a service provider object from all categories that
contain it.

**Parameters:** provider

- the service provider object to be deregistered.
**Throws:** IllegalArgumentException

- if

provider

is

null

.

- contains

```java
public boolean contains​(
Object
provider)
```

Returns

true

if

provider

is currently
registered.

**Parameters:** provider

- the service provider object to be queried.
**Returns:** true

if the given provider has been
registered.
**Throws:** IllegalArgumentException

- if

provider

is

null

.

- getServiceProviders

```java
public <T>
Iterator
<T> getServiceProviders​(
Class
<T> category,
boolean useOrdering)
```

Returns an

Iterator

containing all registered
service providers in the given category. If

useOrdering

is

false

, the iterator
will return all of the server provider objects in an arbitrary
order. Otherwise, the ordering will respect any pairwise
orderings that have been set. If the graph of pairwise
orderings contains cycles, any providers that belong to a cycle
will not be returned.

**Type Parameters:** T

- the type of the category.
**Parameters:** category

- the category to be retrieved from.
**Parameters:** useOrdering

-

true

if pairwise orderings
should be taken account in ordering the returned objects.
**Returns:** an

Iterator

containing service provider
objects from the given category, possibly in order.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.

- getServiceProviders

```java
public <T>
Iterator
<T> getServiceProviders​(
Class
<T> category,

ServiceRegistry.Filter
filter,
boolean useOrdering)
```

Returns an

Iterator

containing service provider
objects within a given category that satisfy a criterion
imposed by the supplied

ServiceRegistry.Filter

object's

filter

method.

The

useOrdering

argument controls the
ordering of the results using the same rules as

getServiceProviders(Class, boolean)

.

**Type Parameters:** T

- the type of the category.
**Parameters:** category

- the category to be retrieved from.
**Parameters:** filter

- an instance of

ServiceRegistry.Filter

whose

filter

method will be invoked.
**Parameters:** useOrdering

-

true

if pairwise orderings
should be taken account in ordering the returned objects.
**Returns:** an

Iterator

containing service provider
objects from the given category, possibly in order.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.

- getServiceProviderByClass

```java
public <T> T getServiceProviderByClass​(
Class
<T> providerClass)
```

Returns the currently registered service provider object that
is of the given class type. At most one object of a given
class is allowed to be registered at any given time. If no
registered object has the desired class type,

null

is returned.

**Type Parameters:** T

- the type of the provider.
**Parameters:** providerClass

- the

Class

of the desired
service provider object.
**Returns:** a currently registered service provider object with the
desired

Class

type, or

null

is none is
present.
**Throws:** IllegalArgumentException

- if

providerClass

is

null

.

- setOrdering

```java
public <T> boolean setOrdering​(
Class
<T> category,
T firstProvider,
T secondProvider)
```

Sets a pairwise ordering between two service provider objects
within a given category. If one or both objects are not
currently registered within the given category, or if the
desired ordering is already set, nothing happens and

false

is returned. If the providers previously
were ordered in the reverse direction, that ordering is
removed.

The ordering will be used by the

getServiceProviders

methods when their

useOrdering

argument is

true

.

**Type Parameters:** T

- the type of the category.
**Parameters:** category

- a

Class

object indicating the
category under which the preference is to be established.
**Parameters:** firstProvider

- the preferred provider.
**Parameters:** secondProvider

- the provider to which

firstProvider

is preferred.
**Returns:** true

if a previously unset ordering
was established.
**Throws:** IllegalArgumentException

- if either provider is

null

or they are the same object.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.

- unsetOrdering

```java
public <T> boolean unsetOrdering​(
Class
<T> category,
T firstProvider,
T secondProvider)
```

Sets a pairwise ordering between two service provider objects
within a given category. If one or both objects are not
currently registered within the given category, or if no
ordering is currently set between them, nothing happens
and

false

is returned.

The ordering will be used by the

getServiceProviders

methods when their

useOrdering

argument is

true

.

**Type Parameters:** T

- the type of the category.
**Parameters:** category

- a

Class

object indicating the
category under which the preference is to be disestablished.
**Parameters:** firstProvider

- the formerly preferred provider.
**Parameters:** secondProvider

- the provider to which

firstProvider

was formerly preferred.
**Returns:** true

if a previously set ordering was
disestablished.
**Throws:** IllegalArgumentException

- if either provider is

null

or they are the same object.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.

- deregisterAll

```java
public void deregisterAll​(
Class
<?> category)
```

Deregisters all service provider object currently registered
under the given category.

**Parameters:** category

- the category to be emptied.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.

- deregisterAll

```java
public void deregisterAll()
```

Deregisters all currently registered service providers from all
categories.

- finalize

```java
@Deprecated
(
since
="9")
public void finalize()
throws
Throwable
```

Deprecated.

The

finalize

method has been deprecated.
Subclasses that override

finalize

in order to perform cleanup
should be modified to use alternative cleanup mechanisms and
to remove the overriding

finalize

method.
When overriding the

finalize

method, its implementation must explicitly
ensure that

super.finalize()

is invoked as described in

Object.finalize()

.
See the specification for

Object.finalize()

for further
information about migration options.

Finalizes this object prior to garbage collection. The

deregisterAll

method is called to deregister all
currently registered service providers. This method should not
be called from application code.

**Overrides:** finalize

in class

Object
**Throws:** Throwable

- if an error occurs during superclass
finalization.
**See Also:** WeakReference

,

PhantomReference

---

#### Method Detail

lookupProviders

```java
public static <T>
Iterator
<T> lookupProviders​(
Class
<T> providerClass,

ClassLoader
loader)
```

Searches for implementations of a particular service class
using the given class loader.

The service class must be one of the service types listed
in the class specification. If it is not,

IllegalArgumentException

will be thrown.

This method transforms the name of the given service class
into a provider-configuration filename as described in the
class comment and then uses the

getResources

method of the given class loader to find all available files
with that name. These files are then read and parsed to
produce a list of provider-class names. The iterator that is
returned uses the given class loader to look up and then
instantiate each element of the list.

Because it is possible for extensions to be installed into
a running Java virtual machine, this method may return
different results each time it is invoked.

**Type Parameters:** T

- the type of the providerClass.
**Parameters:** providerClass

- a

Class

object indicating the
class or interface of the service providers being detected.
**Parameters:** loader

- the class loader to be used to load
provider-configuration files and instantiate provider classes,
or

null

if the system class loader (or, failing that
the bootstrap class loader) is to be used.
**Returns:** An

Iterator

that yields provider objects
for the given service, in some arbitrary order. The iterator
will throw an

Error

if a provider-configuration
file violates the specified format or if a provider class
cannot be found and instantiated.
**Throws:** IllegalArgumentException

- if

providerClass

is

null

, or if it is
not one of the allowed service types.

---

#### lookupProviders

public static <T>

Iterator

<T> lookupProviders​(

Class

<T> providerClass,

ClassLoader

loader)

Searches for implementations of a particular service class
using the given class loader.

The service class must be one of the service types listed
in the class specification. If it is not,

IllegalArgumentException

will be thrown.

This method transforms the name of the given service class
into a provider-configuration filename as described in the
class comment and then uses the

getResources

method of the given class loader to find all available files
with that name. These files are then read and parsed to
produce a list of provider-class names. The iterator that is
returned uses the given class loader to look up and then
instantiate each element of the list.

Because it is possible for extensions to be installed into
a running Java virtual machine, this method may return
different results each time it is invoked.

The service class must be one of the service types listed
in the class specification. If it is not,

IllegalArgumentException

will be thrown.

This method transforms the name of the given service class
into a provider-configuration filename as described in the
class comment and then uses the

getResources

method of the given class loader to find all available files
with that name. These files are then read and parsed to
produce a list of provider-class names. The iterator that is
returned uses the given class loader to look up and then
instantiate each element of the list.

Because it is possible for extensions to be installed into
a running Java virtual machine, this method may return
different results each time it is invoked.

This method transforms the name of the given service class
into a provider-configuration filename as described in the
class comment and then uses the

getResources

method of the given class loader to find all available files
with that name. These files are then read and parsed to
produce a list of provider-class names. The iterator that is
returned uses the given class loader to look up and then
instantiate each element of the list.

Because it is possible for extensions to be installed into
a running Java virtual machine, this method may return
different results each time it is invoked.

Because it is possible for extensions to be installed into
a running Java virtual machine, this method may return
different results each time it is invoked.

lookupProviders

```java
public static <T>
Iterator
<T> lookupProviders​(
Class
<T> providerClass)
```

Locates and incrementally instantiates the available providers
of a given service using the context class loader. This
convenience method is equivalent to:

```java
ClassLoader cl = Thread.currentThread().getContextClassLoader();
return Service.providers(service, cl);
```

The service class must be one of the service types listed
in the class specification. If it is not,

IllegalArgumentException

will be thrown.

**Type Parameters:** T

- the type of the providerClass.
**Parameters:** providerClass

- a

Class

object indicating the
class or interface of the service providers being detected.
**Returns:** An

Iterator

that yields provider objects
for the given service, in some arbitrary order. The iterator
will throw an

Error

if a provider-configuration
file violates the specified format or if a provider class
cannot be found and instantiated.
**Throws:** IllegalArgumentException

- if

providerClass

is

null

, or if it is
not one of the allowed service types.

---

#### lookupProviders

public static <T>

Iterator

<T> lookupProviders​(

Class

<T> providerClass)

Locates and incrementally instantiates the available providers
of a given service using the context class loader. This
convenience method is equivalent to:

```java
ClassLoader cl = Thread.currentThread().getContextClassLoader();
return Service.providers(service, cl);
```

The service class must be one of the service types listed
in the class specification. If it is not,

IllegalArgumentException

will be thrown.

ClassLoader cl = Thread.currentThread().getContextClassLoader();
return Service.providers(service, cl);

The service class must be one of the service types listed
in the class specification. If it is not,

IllegalArgumentException

will be thrown.

getCategories

```java
public
Iterator
<
Class
<?>> getCategories()
```

Returns an

Iterator

of

Class

objects
indicating the current set of categories. The iterator will be
empty if no categories exist.

**Returns:** an

Iterator

containing

Class

objects.

---

#### getCategories

public

Iterator

<

Class

<?>> getCategories()

Returns an

Iterator

of

Class

objects
indicating the current set of categories. The iterator will be
empty if no categories exist.

registerServiceProvider

```java
public <T> boolean registerServiceProvider​(T provider,

Class
<T> category)
```

Adds a service provider object to the registry. The provider
is associated with the given category.

If

provider

implements the

RegisterableService

interface, its

onRegistration

method will be called. Its

onDeregistration

method will be called each time
it is deregistered from a category, for example if a
category is removed or the registry is garbage collected.

**Type Parameters:** T

- the type of the provider.
**Parameters:** provider

- the service provide object to be registered.
**Parameters:** category

- the category under which to register the
provider.
**Returns:** true if no provider of the same class was previously
registered in the same category category.
**Throws:** IllegalArgumentException

- if

provider

is

null

.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.
**Throws:** ClassCastException

- if provider does not implement
the

Class

defined by

category

.

---

#### registerServiceProvider

public <T> boolean registerServiceProvider​(T provider,

Class

<T> category)

Adds a service provider object to the registry. The provider
is associated with the given category.

If

provider

implements the

RegisterableService

interface, its

onRegistration

method will be called. Its

onDeregistration

method will be called each time
it is deregistered from a category, for example if a
category is removed or the registry is garbage collected.

If

provider

implements the

RegisterableService

interface, its

onRegistration

method will be called. Its

onDeregistration

method will be called each time
it is deregistered from a category, for example if a
category is removed or the registry is garbage collected.

registerServiceProvider

```java
public void registerServiceProvider​(
Object
provider)
```

Adds a service provider object to the registry. The provider
is associated within each category present in the registry
whose

Class

it implements.

If

provider

implements the

RegisterableService

interface, its

onRegistration

method will be called once for each
category it is registered under. Its

onDeregistration

method will be called each time
it is deregistered from a category or when the registry is
finalized.

**Parameters:** provider

- the service provider object to be registered.
**Throws:** IllegalArgumentException

- if

provider

is

null

.

---

#### registerServiceProvider

public void registerServiceProvider​(

Object

provider)

Adds a service provider object to the registry. The provider
is associated within each category present in the registry
whose

Class

it implements.

If

provider

implements the

RegisterableService

interface, its

onRegistration

method will be called once for each
category it is registered under. Its

onDeregistration

method will be called each time
it is deregistered from a category or when the registry is
finalized.

If

provider

implements the

RegisterableService

interface, its

onRegistration

method will be called once for each
category it is registered under. Its

onDeregistration

method will be called each time
it is deregistered from a category or when the registry is
finalized.

registerServiceProviders

```java
public void registerServiceProviders​(
Iterator
<?> providers)
```

Adds a set of service provider objects, taken from an

Iterator

to the registry. Each provider is
associated within each category present in the registry whose

Class

it implements.

For each entry of

providers

that implements
the

RegisterableService

interface, its

onRegistration

method will be called once for each
category it is registered under. Its

onDeregistration

method will be called each time
it is deregistered from a category or when the registry is
finalized.

**Parameters:** providers

- an Iterator containing service provider
objects to be registered.
**Throws:** IllegalArgumentException

- if

providers

is

null

or contains a

null

entry.

---

#### registerServiceProviders

public void registerServiceProviders​(

Iterator

<?> providers)

Adds a set of service provider objects, taken from an

Iterator

to the registry. Each provider is
associated within each category present in the registry whose

Class

it implements.

For each entry of

providers

that implements
the

RegisterableService

interface, its

onRegistration

method will be called once for each
category it is registered under. Its

onDeregistration

method will be called each time
it is deregistered from a category or when the registry is
finalized.

For each entry of

providers

that implements
the

RegisterableService

interface, its

onRegistration

method will be called once for each
category it is registered under. Its

onDeregistration

method will be called each time
it is deregistered from a category or when the registry is
finalized.

deregisterServiceProvider

```java
public <T> boolean deregisterServiceProvider​(T provider,

Class
<T> category)
```

Removes a service provider object from the given category. If
the provider was not previously registered, nothing happens and

false

is returned. Otherwise,

true

is returned. If an object of the same class as

provider

but not equal (using

==

) to

provider

is registered, it will not be
deregistered.

If

provider

implements the

RegisterableService

interface, its

onDeregistration

method will be called.

**Type Parameters:** T

- the type of the provider.
**Parameters:** provider

- the service provider object to be deregistered.
**Parameters:** category

- the category from which to deregister the
provider.
**Returns:** true

if the provider was previously
registered in the same category category,

false

otherwise.
**Throws:** IllegalArgumentException

- if

provider

is

null

.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.
**Throws:** ClassCastException

- if provider does not implement
the class defined by

category

.

---

#### deregisterServiceProvider

public <T> boolean deregisterServiceProvider​(T provider,

Class

<T> category)

Removes a service provider object from the given category. If
the provider was not previously registered, nothing happens and

false

is returned. Otherwise,

true

is returned. If an object of the same class as

provider

but not equal (using

==

) to

provider

is registered, it will not be
deregistered.

If

provider

implements the

RegisterableService

interface, its

onDeregistration

method will be called.

If

provider

implements the

RegisterableService

interface, its

onDeregistration

method will be called.

deregisterServiceProvider

```java
public void deregisterServiceProvider​(
Object
provider)
```

Removes a service provider object from all categories that
contain it.

**Parameters:** provider

- the service provider object to be deregistered.
**Throws:** IllegalArgumentException

- if

provider

is

null

.

---

#### deregisterServiceProvider

public void deregisterServiceProvider​(

Object

provider)

Removes a service provider object from all categories that
contain it.

contains

```java
public boolean contains​(
Object
provider)
```

Returns

true

if

provider

is currently
registered.

**Parameters:** provider

- the service provider object to be queried.
**Returns:** true

if the given provider has been
registered.
**Throws:** IllegalArgumentException

- if

provider

is

null

.

---

#### contains

public boolean contains​(

Object

provider)

Returns

true

if

provider

is currently
registered.

getServiceProviders

```java
public <T>
Iterator
<T> getServiceProviders​(
Class
<T> category,
boolean useOrdering)
```

Returns an

Iterator

containing all registered
service providers in the given category. If

useOrdering

is

false

, the iterator
will return all of the server provider objects in an arbitrary
order. Otherwise, the ordering will respect any pairwise
orderings that have been set. If the graph of pairwise
orderings contains cycles, any providers that belong to a cycle
will not be returned.

**Type Parameters:** T

- the type of the category.
**Parameters:** category

- the category to be retrieved from.
**Parameters:** useOrdering

-

true

if pairwise orderings
should be taken account in ordering the returned objects.
**Returns:** an

Iterator

containing service provider
objects from the given category, possibly in order.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.

---

#### getServiceProviders

public <T>

Iterator

<T> getServiceProviders​(

Class

<T> category,
boolean useOrdering)

Returns an

Iterator

containing all registered
service providers in the given category. If

useOrdering

is

false

, the iterator
will return all of the server provider objects in an arbitrary
order. Otherwise, the ordering will respect any pairwise
orderings that have been set. If the graph of pairwise
orderings contains cycles, any providers that belong to a cycle
will not be returned.

getServiceProviders

```java
public <T>
Iterator
<T> getServiceProviders​(
Class
<T> category,

ServiceRegistry.Filter
filter,
boolean useOrdering)
```

Returns an

Iterator

containing service provider
objects within a given category that satisfy a criterion
imposed by the supplied

ServiceRegistry.Filter

object's

filter

method.

The

useOrdering

argument controls the
ordering of the results using the same rules as

getServiceProviders(Class, boolean)

.

**Type Parameters:** T

- the type of the category.
**Parameters:** category

- the category to be retrieved from.
**Parameters:** filter

- an instance of

ServiceRegistry.Filter

whose

filter

method will be invoked.
**Parameters:** useOrdering

-

true

if pairwise orderings
should be taken account in ordering the returned objects.
**Returns:** an

Iterator

containing service provider
objects from the given category, possibly in order.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.

---

#### getServiceProviders

public <T>

Iterator

<T> getServiceProviders​(

Class

<T> category,

ServiceRegistry.Filter

filter,
boolean useOrdering)

Returns an

Iterator

containing service provider
objects within a given category that satisfy a criterion
imposed by the supplied

ServiceRegistry.Filter

object's

filter

method.

The

useOrdering

argument controls the
ordering of the results using the same rules as

getServiceProviders(Class, boolean)

.

The

useOrdering

argument controls the
ordering of the results using the same rules as

getServiceProviders(Class, boolean)

.

getServiceProviderByClass

```java
public <T> T getServiceProviderByClass​(
Class
<T> providerClass)
```

Returns the currently registered service provider object that
is of the given class type. At most one object of a given
class is allowed to be registered at any given time. If no
registered object has the desired class type,

null

is returned.

**Type Parameters:** T

- the type of the provider.
**Parameters:** providerClass

- the

Class

of the desired
service provider object.
**Returns:** a currently registered service provider object with the
desired

Class

type, or

null

is none is
present.
**Throws:** IllegalArgumentException

- if

providerClass

is

null

.

---

#### getServiceProviderByClass

public <T> T getServiceProviderByClass​(

Class

<T> providerClass)

Returns the currently registered service provider object that
is of the given class type. At most one object of a given
class is allowed to be registered at any given time. If no
registered object has the desired class type,

null

is returned.

setOrdering

```java
public <T> boolean setOrdering​(
Class
<T> category,
T firstProvider,
T secondProvider)
```

Sets a pairwise ordering between two service provider objects
within a given category. If one or both objects are not
currently registered within the given category, or if the
desired ordering is already set, nothing happens and

false

is returned. If the providers previously
were ordered in the reverse direction, that ordering is
removed.

The ordering will be used by the

getServiceProviders

methods when their

useOrdering

argument is

true

.

**Type Parameters:** T

- the type of the category.
**Parameters:** category

- a

Class

object indicating the
category under which the preference is to be established.
**Parameters:** firstProvider

- the preferred provider.
**Parameters:** secondProvider

- the provider to which

firstProvider

is preferred.
**Returns:** true

if a previously unset ordering
was established.
**Throws:** IllegalArgumentException

- if either provider is

null

or they are the same object.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.

---

#### setOrdering

public <T> boolean setOrdering​(

Class

<T> category,
T firstProvider,
T secondProvider)

Sets a pairwise ordering between two service provider objects
within a given category. If one or both objects are not
currently registered within the given category, or if the
desired ordering is already set, nothing happens and

false

is returned. If the providers previously
were ordered in the reverse direction, that ordering is
removed.

The ordering will be used by the

getServiceProviders

methods when their

useOrdering

argument is

true

.

The ordering will be used by the

getServiceProviders

methods when their

useOrdering

argument is

true

.

unsetOrdering

```java
public <T> boolean unsetOrdering​(
Class
<T> category,
T firstProvider,
T secondProvider)
```

Sets a pairwise ordering between two service provider objects
within a given category. If one or both objects are not
currently registered within the given category, or if no
ordering is currently set between them, nothing happens
and

false

is returned.

The ordering will be used by the

getServiceProviders

methods when their

useOrdering

argument is

true

.

**Type Parameters:** T

- the type of the category.
**Parameters:** category

- a

Class

object indicating the
category under which the preference is to be disestablished.
**Parameters:** firstProvider

- the formerly preferred provider.
**Parameters:** secondProvider

- the provider to which

firstProvider

was formerly preferred.
**Returns:** true

if a previously set ordering was
disestablished.
**Throws:** IllegalArgumentException

- if either provider is

null

or they are the same object.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.

---

#### unsetOrdering

public <T> boolean unsetOrdering​(

Class

<T> category,
T firstProvider,
T secondProvider)

Sets a pairwise ordering between two service provider objects
within a given category. If one or both objects are not
currently registered within the given category, or if no
ordering is currently set between them, nothing happens
and

false

is returned.

The ordering will be used by the

getServiceProviders

methods when their

useOrdering

argument is

true

.

The ordering will be used by the

getServiceProviders

methods when their

useOrdering

argument is

true

.

deregisterAll

```java
public void deregisterAll​(
Class
<?> category)
```

Deregisters all service provider object currently registered
under the given category.

**Parameters:** category

- the category to be emptied.
**Throws:** IllegalArgumentException

- if there is no category
corresponding to

category

.

---

#### deregisterAll

public void deregisterAll​(

Class

<?> category)

Deregisters all service provider object currently registered
under the given category.

deregisterAll

```java
public void deregisterAll()
```

Deregisters all currently registered service providers from all
categories.

---

#### deregisterAll

public void deregisterAll()

Deregisters all currently registered service providers from all
categories.

finalize

```java
@Deprecated
(
since
="9")
public void finalize()
throws
Throwable
```

Deprecated.

The

finalize

method has been deprecated.
Subclasses that override

finalize

in order to perform cleanup
should be modified to use alternative cleanup mechanisms and
to remove the overriding

finalize

method.
When overriding the

finalize

method, its implementation must explicitly
ensure that

super.finalize()

is invoked as described in

Object.finalize()

.
See the specification for

Object.finalize()

for further
information about migration options.

Finalizes this object prior to garbage collection. The

deregisterAll

method is called to deregister all
currently registered service providers. This method should not
be called from application code.

**Overrides:** finalize

in class

Object
**Throws:** Throwable

- if an error occurs during superclass
finalization.
**See Also:** WeakReference

,

PhantomReference

---

#### finalize

@Deprecated

(

since

="9")
public void finalize()
throws

Throwable

Finalizes this object prior to garbage collection. The

deregisterAll

method is called to deregister all
currently registered service providers. This method should not
be called from application code.

---

